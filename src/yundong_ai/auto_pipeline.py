"""全自动生成流水线"""

from .config import ConfigManager
from .content_generator import ContentGenerator
from .video_generator import VideoGenerator
from typing import Dict, Optional

class AutoPipeline:
    def __init__(self, config: ConfigManager = None):
        self.config = config or ConfigManager()
        self.content_gen = ContentGenerator(config)
        self.video_gen = VideoGenerator(config)
    
    def full_pipeline(self, topic: str) -> Dict:
        """完整流水线：直接使用全自动视频生成接口"""
        print("=== 全自动视频生成流水线 ===")
        print(f"主题: {topic}")
        print(f"行业: {self.config.default_industry}")
        print(f"目标受众: {self.config.default_target_audience}")
        print("\n--- 提交全自动视频任务 ---")
        
        # 直接调用全自动视频生成接口
        result = self.video_gen.api_client.add_video_task(topic)
        
        print("\n--- 完成! ---")
        return {
            'topic': topic,
            'task_result': result
        }
    
    def sora_pipeline(self, topic: str) -> Dict:
        """SORA视频流水线：选题 → SORA提示词 → SORA视频"""
        print("=== SORA视频生成流水线 ===")
        print(f"主题: {topic}")
        
        # 生成SORA提示词
        sora_result = self.content_gen.generate_sora_prompt(topic)
        if sora_result.get('error'):
            return sora_result
            
        sora_prompt = self._extract_sora_prompt(sora_result)
        if not sora_prompt:
            return {"error": "无法生成有效SORA提示词"}
        
        print(f"SORA提示词: {sora_prompt}")
        
        # 生成SORA视频
        video_result = self.video_gen.create_sora_video(sora_prompt)
        
        return {
            'topic': topic,
            'sora_prompt': sora_prompt,
            'video_result': video_result
        }
    
    def _extract_title(self, result: Dict) -> Optional[str]:
        """从结果中提取标题"""
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content'].strip()
        elif 'content' in result:
            return result['content'].strip()
        else:
            return str(result)
    
    def _extract_copy(self, result: Dict) -> Optional[str]:
        """从结果中提取文案"""
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content'].strip()
        elif 'content' in result:
            return result['content'].strip()
        else:
            return str(result)
    
    def _extract_sora_prompt(self, result: Dict) -> Optional[str]:
        """从结果中提取SORA提示词"""
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content'].strip()
        elif 'content' in result:
            return result['content'].strip()
        else:
            return str(result)