# host_controller.py
import subprocess
import json
import sys
import time
from threading import Thread
from queue import Queue
from servers import *
import os

class HostController:
    """
    一个用于启动、管理和与多个MCP服务器子进程通信的控制器。
    """

    def __init__(self, server_configs):
        self.server_configs = server_configs
        self.servers = {}  # 存储服务器进程和管道
        self.message_queue = Queue()  # 用于从所有服务器接收消息的线程安全队列

    def start_all_servers(self):
        """根据配置启动所有服务器"""
        print("[HOST] Starting all servers...")
        for name, config in self.server_configs.items():
            command = ["python", config["script"]] + config.get("args", [])

            try:
                process = subprocess.Popen(
                    command,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    encoding="utf-8",
                    text=True,  # 使用文本模式进行IO
                    bufsize=1,  # 行缓冲
                    universal_newlines=True
                )
                self.servers[name] = {"process": process, "stdin": process.stdin}

                # 为每个服务器的 stdout 和 stderr 启动监听线程
                Thread(target=self._listen_pipe, args=(name, process.stdout, "STDOUT"), daemon=True).start()
                Thread(target=self._listen_pipe, args=(name, process.stderr, "STDERR"), daemon=True).start()

                print(f"[HOST] Server '{name}' process started.")
            except FileNotFoundError:
                print(f"[HOST] Error: Script not found for '{name}': {config['script']}", file=sys.stderr)
                sys.exit(1)

    def _listen_pipe(self, server_name, pipe, pipe_type):
        """
        线程目标函数：持续读取一个管道（stdout/stderr）并将内容放入队列。
        """
        for line in iter(pipe.readline, ''):
            message = {
                "server_name": server_name,
                "type": pipe_type,
                "content": line.strip()
            }
            self.message_queue.put(message)
        pipe.close()
        print(f"[{server_name} {pipe_type} READER] Pipe closed.", file=sys.stderr)

    def send_to_server(self, server_name: str, request: dict):
        """向指定的服务器发送一个JSON-RPC请求"""
        if server_name in self.servers:
            server = self.servers[server_name]
            message_str = json.dumps(request)
            print(f"[HOST] -> [{server_name}] {message_str}")
            server["stdin"].write(message_str + '\n')
            server["stdin"].flush()
        else:
            print(f"[HOST] Error: No server named '{server_name}'.", file=sys.stderr)

    def process_messages_forever(self):
        """
        主消息处理循环：从队列中取出并处理消息。
        在真实的Agent中，这里会包含复杂的逻辑（如处理advertise，更新工具列表等）。
        """
        print("\n[HOST] Now listening for messages from all servers...")
        while True:
            try:
                message = self.message_queue.get(timeout=1)  # 等待1秒

                server = message['server_name']
                msg_type = message['type']
                content = message['content']

                if msg_type == "STDOUT":
                    # 正常的消息，通常是JSON-RPC响应或advertise
                    print(f"[FROM {server}] {content}")
                elif msg_type == "STDERR":
                    # 错误日志
                    print(f"[LOG {server}] {content}", file=sys.stderr)

            except Exception:
                # 队列为空时，可以执行一些其他的心跳或检查任务
                # print("[HOST] Queue is empty. Checking server status...")
                """
                all_processes_running = all(
                    info["process"].poll() is None for info in self.servers.values()
                )
                if not all_processes_running:
                    print("[HOST] One or more servers have stopped. Exiting.", file=sys.stderr)
                    break
                """
                pass

    def shutdown_all_servers(self):
        """优雅地关闭所有服务器子进程"""
        print("\n[HOST] Shutting down all servers...")
        for name, server in self.servers.items():
            if server["process"].poll() is None:  # 如果进程还在运行
                server["process"].terminate()  # 发送终止信号
                try:
                    server["process"].wait(timeout=5)  # 等待最多5秒
                    print(f"[HOST] Server '{name}' terminated.")
                except subprocess.TimeoutExpired:
                    server["process"].kill()  # 如果无法终止，则强制杀死
                    print(f"[HOST] Server '{name}' forcefully killed.")


if __name__ == "__main__":
    # 定义您要启动的五个服务器
    # 我们使用同一个dummy_server.py脚本，但传递不同的参数来模拟五个不同的服务器
    # 服务器文件夹路径
    SERVERS_DIR = "servers"


    # 函数：将文件名转换为服务器类名（如prediction_server.py -> PredictionServer）
    def filename_to_server_name(filename):
        # 去掉.py后缀
        base_name = os.path.splitext(filename)[0]
        # 按下划线分割并转换为驼峰式
        parts = base_name.split("_")
        return "".join(part.capitalize() for part in parts)


    # 自动生成SERVER_DEFINITIONS
    SERVER_DEFINITIONS = {}
    # 遍历servers文件夹下的所有文件
    for filename in os.listdir(SERVERS_DIR):
        # 只处理.py文件
        if filename.endswith(".py"):
            # 生成服务器名称
            server_name = filename_to_server_name(filename)
            # 构建脚本路径
            script_path = os.path.join(SERVERS_DIR, filename)
            # 添加到字典
            SERVER_DEFINITIONS[server_name] = {
                "script": script_path,
                "args": []
            }

    controller = HostController(SERVER_DEFINITIONS)
    controller.start_all_servers()

    # 等待服务器初始化并发送advertise消息
    print("\n[HOST] Waiting for servers to initialize...")
    time.sleep(2)

    # 主动发送一个测试指令
    test_request = {
        "jsonrpc": "2.0",
        "method": "tool_from_prediction",
        "params": "What is the weather like?",
        "id": 1001
    }
    controller.send_to_server("PredictionServer", test_request)

    print("\n[HOST] Press Ctrl+C to shut down.")
    try:
        # 启动主消息循环
        controller.process_messages_forever()
    except KeyboardInterrupt:
        # 用户按下Ctrl+C时，优雅地退出
        pass
    except Exception as e:
        # 捕获其他所有异常，打印失效信息后不做额外处理
        print(f"功能失效: {str(e)}")
    finally:
        # 无论是否发生异常，最终都关闭所有服务器
        controller.shutdown_all_servers()