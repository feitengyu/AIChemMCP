# llm_client.py
import os
import json
from openai import OpenAI
import time


API_KEY_FILE = "./static/OPENAI_KEY"
with open(API_KEY_FILE, 'r') as f:
    api_key = f.read().strip()
os.environ["OPENAI_API_KEY"] = api_key

class OpenAI_LLM:
    def __init__(self, model="qwen-plus-2025-09-11"):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY 环境变量未设置！")

        self.client = OpenAI(api_key=api_key,base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",)
        self.model = model

    def _format_tools_for_openai(self, mcp_tools: dict) -> list:
        """将MCP的工具格式转换为OpenAI API要求的格式"""
        openai_tools = []
        for tool_name, tool_data in mcp_tools.items():
            openai_tools.append({
                "type": "function",
                "function": {
                    "name": tool_name,
                    "description": tool_data.get("description", ""),
                    "parameters": tool_data.get("parameters", {"type": "object", "properties": {}})
                }
            })
        return openai_tools

    def get_decision(self, system_prompt: str, history: list, mcp_tools: dict) -> dict:
        """
        调用OpenAI API获取LLM的决策（说话或调用工具）。
        """
        # 1. 格式化OpenAI需要的工具列表
        openai_tools = self._format_tools_for_openai(mcp_tools)

        # 2. 格式化对话历史
        messages = [{"role": "system", "content": system_prompt}]
        for turn in history:
            role = turn['role']
            content = turn['content']

            if role == "user":
                messages.append({"role": "user", "content": content})
            elif role == "assistant" and "tool_call" in content:
                # 将我们的tool_call格式转换回OpenAI的格式
                tool_call = content['tool_call']
                messages.append({
                    "role": "assistant",
                    "tool_calls": [{
                        "id": f"call_{tool_call['method']}_{int(time.time())}",  # 创造一个临时的ID
                        "type": "function",
                        "function": {
                            "name": tool_call['method'],
                            "arguments": json.dumps(tool_call['params'])
                        }
                    }]
                })
            elif role == "tool_result":
                # OpenAI期望工具结果的角色是 'tool'
                # 我们需要找到对应的工具调用ID，这里为了简化，我们只传递内容
                messages.append({
                    "role": "tool",
                    "tool_call_id": messages[-1]['tool_calls'][0]['id'],  # 使用上一条消息的ID
                    "name": messages[-1]['tool_calls'][0]['function']['name'],
                    "content": json.dumps(content)
                })

        # 3. 发起API调用
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=openai_tools,
                tool_choice="auto"
            )

            response_message = response.choices[0].message

            # 4. 解析API的响应
            if response_message.tool_calls:
                # LLM决定调用一个工具
                tool_call = response_message.tool_calls[0].function
                return {
                    "thought": response_message.content or "I should use a tool to proceed.",
                    "tool_call": {
                        "method": tool_call.name,
                        "params": json.loads(tool_call.arguments)
                    }
                }
            else:
                # LLM决定直接与用户对话
                return {
                    "thought": "I will respond directly to the user.",
                    "speak": response_message.content
                }
        except Exception as e:
            print(f"[LLM_CLIENT_ERROR] API call failed: {e}")
            return {"speak": "I'm sorry, I encountered an error while processing your request."}

    def generate_plan(self, system_prompt: str, user_goal: str, mcp_tools: dict):
        """
        调用OpenAI API直接生成plan。
        """
        # 1. 格式化OpenAI需要的工具列表
        openai_tools = self._format_tools_for_openai(mcp_tools)

        # 2. 创建一个“容器”工具，强制LLM输出一个计划列表
        plan_schema = {
            "type": "object",
            "properties": {
                "plan": {
                    "type": "array",
                    "description": "一个包含所有计划步骤的有序列表。",
                    "items": {
                        "type": "object",
                        "properties": {
                            "method": {
                                "type": "string",
                                "description": "要调用的工具名称。",
                                # 使用enum来确保LLM只能选择真实存在的工具
                                "enum": list(mcp_tools.keys())
                            },
                            "params": {"type": "object", "description": "传递给工具的参数。"}
                        },
                        "required": ["method", "params"]
                    }
                }
            },
            "required": ["plan"]
        }

        planner_tool = {
            "type": "function",
            "function": {
                "name": "submit_workflow_plan",
                "description": "提交最终生成的、包含多个步骤的工作流计划。",
                "parameters": plan_schema
            }
        }

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_goal}
        ]

        try:
            # 3. 发起API调用，强制使用我们的“容器”工具
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=openai_tools + [planner_tool],  # 只给它这个容器工具
                tool_choice={"type": "function", "function": {"name": "submit_workflow_plan"}}
            )

            # 4. 从响应中提取出计划列表
            tool_call_args = response.choices[0].message.tool_calls[0].function.arguments
            plan_data = json.loads(tool_call_args)
            return plan_data.get("plan", [])

        except Exception as e:
            print(f"[LLM_CLIENT_ERROR] Plan generation failed: {e}")
            return [{"method": "error", "params": {"message": str(e)}}]
