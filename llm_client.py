# llm_client.py
# 使用chatGPT-4o模型的OpenAI客户端，集成工具名称翻译功能
import os
import json
import re
import time
from openai import OpenAI


API_KEY_FILE = "/opt/data/private/src/AIChemMCP/static/OPENAI_API_KEY"
with open(API_KEY_FILE, 'r') as f:
    api_key = f.read().strip()
os.environ["OPENAI_API_KEY"] = api_key


class ToolNameTranslator:
    """工具名称翻译器，使用大模型API批量翻译中文工具名称"""
    
    def __init__(self, model="gpt-4o"):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY 环境变量未设置！")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.translation_cache = {}
        self.load_cache()

    def load_cache(self, cache_file="tool_name_translations.json"):
        """加载翻译缓存"""
        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    self.translation_cache = json.load(f)
                print(f"✅ 加载了 {len(self.translation_cache)} 个缓存的工具名称翻译")
            except Exception as e:
                print(f"❌ 加载翻译缓存失败: {e}")
                self.translation_cache = {}

    def save_cache(self, cache_file="tool_name_translations.json"):
        """保存翻译缓存"""
        try:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.translation_cache, f, ensure_ascii=False, indent=2)
            print(f"✅ 保存了 {len(self.translation_cache)} 个工具名称翻译到缓存")
        except Exception as e:
            print(f"❌ 保存翻译缓存失败: {e}")

    def translate_tool_names_batch(self, tool_names, batch_size=20):
        """批量翻译工具名称"""
        print(f"🔄 开始批量翻译 {len(tool_names)} 个工具名称...")
        
        # 先检查缓存中已有的翻译
        remaining_names = []
        translations = {}
        
        for name in tool_names:
            if name in self.translation_cache:
                translations[name] = self.translation_cache[name]
            else:
                remaining_names.append(name)
        
        if not remaining_names:
            print("✅ 所有工具名称已存在缓存中")
            return translations
        
        print(f"🔄 需要翻译 {len(remaining_names)} 个新工具名称")
        
        # 分批处理剩余的名称
        for i in range(0, len(remaining_names), batch_size):
            batch = remaining_names[i:i + batch_size]
            print(f"🔄 翻译批次 {i//batch_size + 1}/{(len(remaining_names)-1)//batch_size + 1}")
            
            batch_translations = self._translate_batch(batch)
            translations.update(batch_translations)
            
            # 更新缓存
            self.translation_cache.update(batch_translations)
            self.save_cache()
            
            # 避免API限制
            time.sleep(1)
        
        print(f"✅ 完成所有工具名称翻译！")
        return translations

    def _translate_batch(self, tool_names, max_retries=3):
        """翻译单个批次的工具名称，包含重试机制"""
        # 构建提示词
        prompt = self._build_translation_prompt(tool_names)
        
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": """你是一个专业的化学实验室设备名称翻译专家。请将中文设备名称准确翻译成英文，遵循以下规则：
1. 使用标准的实验室设备命名规范
2. 保持专业性，使用准确的科技术语
3. 名称格式：只使用字母、数字、下划线和连字符
4. 避免使用空格和其他特殊字符
5. 对于复合设备，使用有意义的组合名称
6. 确保名称简洁且具有描述性"""
                        },
                        {
                            "role": "user", 
                            "content": prompt
                        }
                    ],
                    temperature=0.1  # 低温度确保一致性
                )
                
                result_text = response.choices[0].message.content
                translations = self._parse_translation_result(result_text, tool_names)
                
                # 验证所有名称都被翻译
                missing = set(tool_names) - set(translations.keys())
                if missing:
                    if attempt < max_retries - 1:
                        print(f"⚠️ 第{attempt+1}次尝试缺少翻译: {missing}，进行重试...")
                        continue
                    else:
                        raise Exception(f"重试{max_retries}次后仍缺少翻译: {missing}")
                
                return translations
                
            except Exception as e:
                print(f"❌ 第{attempt+1}次翻译失败: {e}")
                if attempt < max_retries - 1:
                    print("🔄 等待2秒后重试...")
                    time.sleep(2)
                else:
                    raise Exception(f"翻译失败，已重试{max_retries}次: {e}")

    def _build_translation_prompt(self, tool_names):
        """构建翻译提示词"""
        names_list = "\n".join([f"- {name}" for name in tool_names])
        
        return f"""
请将以下化学实验室设备名称翻译成英文。

要求返回纯JSON格式，不要包含任何其他文本：
```json
{{
  "原名称1": "english_name_1",
  "原名称2": "english_name_2",
  ...
}}

需要翻译的设备名称：
{names_list}
"""

    def _parse_translation_result(self, result_text, original_names):
        """解析翻译结果"""
        try:
            # 尝试从结果中提取JSON
            if "```json" in result_text:
                json_str = result_text.split("```json")[1].split("```")[0].strip()
            elif "```" in result_text:
                json_str = result_text.split("```")[1].strip()
            else:
                # 尝试直接解析整个文本
                json_str = result_text.strip()
            
            translations = json.loads(json_str)
            
            return translations
            
        except Exception as e:
            print(f"❌ 解析翻译结果失败: {e}")
            print(f"原始响应: {result_text}")
            raise Exception(f"解析翻译结果失败: {e}")


class OpenAI_LLM:
    def __init__(self, model="gpt-4o"):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY 环境变量未设置！")

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.translator = ToolNameTranslator()
        self.tool_name_mapping = {}  # 工具名称映射缓存
        self.sanitized_to_original_mapping = {}  # 清理后名称到原始名称的映射

    def _build_openai_tools_and_mapping(self, mcp_tools: dict):
        """构建OpenAI工具列表和名称映射（使用翻译后的名称）"""
        # 获取所有需要翻译的工具名称
        tool_names = list(mcp_tools.keys())
        
        # 批量翻译工具名称
        if not self.tool_name_mapping:
            self.tool_name_mapping = self.translator.translate_tool_names_batch(tool_names)
        
        openai_tools = []
        sanitized_to_original = {}
        used_names = set()
        
        for tool_name, tool_data in mcp_tools.items():
            # 使用翻译后的名称
            if tool_name not in self.tool_name_mapping:
                raise Exception(f"工具名称 '{tool_name}' 翻译失败，无法构建工具列表")
                
            base_sanitized_name = self.tool_name_mapping[tool_name]
            
            # 确保名称唯一
            sanitized_name = base_sanitized_name
            counter = 1
            while sanitized_name in used_names:
                sanitized_name = f"{base_sanitized_name}_{counter}"
                counter += 1
            used_names.add(sanitized_name)
            
            # 保存映射
            sanitized_to_original[sanitized_name] = tool_name
            
            # 构建OpenAI工具格式
            openai_tools.append({
                "type": "function",
                "function": {
                    "name": sanitized_name,
                    "description": tool_data.get("description", ""),
                    "parameters": tool_data.get("parameters", {"type": "object", "properties": {}})
                }
            })
        
        # 保存映射供后续使用
        self.sanitized_to_original_mapping = sanitized_to_original
        
        return openai_tools, sanitized_to_original

    def _find_original_tool_name(self, sanitized_name: str) -> str:
        """将清理后的工具名称映射回原始名称"""
        return self.sanitized_to_original_mapping.get(sanitized_name, sanitized_name)

    def debug_tool_names(self, mcp_tools: dict):
        """调试工具名称，显示原始名称和清理后的名称"""
        print("\n=== 工具名称调试信息 ===")
        for tool_name in mcp_tools.keys():
            sanitized = self.tool_name_mapping.get(tool_name, "未翻译")
            print(f"原始: '{tool_name}' -> 清理: '{sanitized}'")
        print("=======================\n")

    def get_decision(self, system_prompt: str, history: list, mcp_tools: dict) -> dict:
        """
        调用OpenAI API获取LLM的决策（说话或调用工具）。
        """
        # 1. 构建OpenAI工具列表和映射
        openai_tools, sanitized_to_original = self._build_openai_tools_and_mapping(mcp_tools)

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
                # 查找清理后的工具名称
                sanitized_method = None
                for sanitized, original in sanitized_to_original.items():
                    if original == tool_call['method']:
                        sanitized_method = sanitized
                        break
                
                if sanitized_method is None:
                    raise Exception(f"找不到工具 '{tool_call['method']}' 的翻译名称")
                
                messages.append({
                    "role": "assistant",
                    "tool_calls": [{
                        "id": f"call_{sanitized_method}_{int(time.time())}",
                        "type": "function",
                        "function": {
                            "name": sanitized_method,
                            "arguments": json.dumps(tool_call['params'])
                        }
                    }]
                })
            elif role == "tool_result":
                # 需要找到对应的工具调用ID
                if messages and 'tool_calls' in messages[-1]:
                    messages.append({
                        "role": "tool",
                        "tool_call_id": messages[-1]['tool_calls'][0]['id'],
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
                # 将清理后的工具名称映射回原始名称
                original_tool_name = self._find_original_tool_name(tool_call.name)
                
                return {
                    "thought": response_message.content or "I should use a tool to proceed.",
                    "tool_call": {
                        "method": original_tool_name,
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
        """调用OpenAI API直接生成plan。"""
        try:
            # 调试：显示工具名称转换
            self.debug_tool_names(mcp_tools)
            
            # 1. 构建OpenAI工具列表和映射
            openai_tools, sanitized_to_original = self._build_openai_tools_and_mapping(mcp_tools)
            
            # 使用映射中的键作为可用的工具名称
            available_tool_names = list(sanitized_to_original.keys())
            
            # 2. 创建一个"容器"工具，强制LLM输出一个计划列表
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
                                    "enum": available_tool_names
                                },
                                "params": {
                                    "type": "object", 
                                    "description": "传递给工具的参数。",
                                    "properties": {},
                                    "additionalProperties": True
                                }
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

            # 3. 发起API调用，强制使用我们的"容器"工具
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=[planner_tool],  # 只传递规划工具，不传递其他工具
                tool_choice={"type": "function", "function": {"name": "submit_workflow_plan"}}
            )

            # 4. 检查响应并提取计划
            response_message = response.choices[0].message
            
            if not response_message.tool_calls:
                print(f"[LLM_CLIENT_ERROR] No tool call in response: {response_message}")
                return [{"method": "error", "params": {"message": "No plan generated"}}]
                
            tool_call = response_message.tool_calls[0]
            tool_call_args = tool_call.function.arguments
            
            try:
                plan_data = json.loads(tool_call_args)
            except json.JSONDecodeError as e:
                print(f"[LLM_CLIENT_ERROR] JSON decode error: {e}, raw arguments: {tool_call_args}")
                return [{"method": "error", "params": {"message": f"JSON decode error: {e}"}}]
            
            # 5. 将清理后的工具名称映射回原始名称
            original_plan = []
            for step in plan_data.get("plan", []):
                if "method" not in step:
                    print(f"[LLM_CLIENT_ERROR] Step missing 'method': {step}")
                    continue
                    
                original_method = self._find_original_tool_name(step["method"])
                step_params = step.get("params", {})
                
                original_plan.append({
                    "method": original_method,
                    "params": step_params
                })
            
            return original_plan

        except Exception as e:
            print(f"[LLM_CLIENT_ERROR] Plan generation failed: {e}")
            import traceback
            traceback.print_exc()
            return [{"method": "error", "params": {"message": str(e)}}]


# 批量翻译工具
def batch_translate_all_tools(servers_dir="servers_and_tools"):
    """批量翻译所有工具名称"""
    import os
    
    # 从服务器文件名中提取工具名称
    tool_names = set()
    
    if not os.path.exists(servers_dir):
        print(f"错误: 目录 '{servers_dir}' 不存在")
        return
    
    # 遍历所有服务器文件
    for filename in os.listdir(servers_dir):
        if filename.endswith("_server_v2.py"):
            # 从文件名提取设备名称（去掉后缀）
            device_name = filename.replace("_server_v2.py", "")
            # 将下划线还原为原始名称（假设原始名称中没有下划线）
            original_name = device_name.replace('_', '')
            tool_names.add(original_name)
    
    tool_names = list(tool_names)
    print(f"📋 找到 {len(tool_names)} 个工具名称需要翻译")
    
    # 批量翻译
    translator = ToolNameTranslator()
    translations = translator.translate_tool_names_batch(tool_names)
    
    # 保存完整的翻译结果
    output_file = "all_tool_translations.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 翻译完成！结果已保存到 {output_file}")
    print("\n翻译结果预览:")
    for cn, en in list(translations.items())[:10]:  # 显示前10个
        print(f"  {cn} -> {en}")


if __name__ == "__main__":
    # 运行批量翻译
    batch_translate_all_tools()