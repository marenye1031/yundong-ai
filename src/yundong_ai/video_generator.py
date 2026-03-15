"""视频生成模块"""

from .config import ConfigManager
from .api_client import APIClient
from typing import Dict, Optional

class VideoGenerator:
    def __init__(self, config: ConfigManager = None):
        self.config = config or ConfigManager()
        self.api_client = APIClient(config)
    
    def create_digital_human_video(self, content: str, anchor_id: str = None, voice_id: str = None) -> Dict:
        """创建数字人视频"""
        return self.api_client.create_digital_human_video(content, anchor_id, voice_id)
    
    def create_sora_video(self, prompt: str, aspect_ratio: str = None) -> Dict:
        """创建SORA视频"""
        return self.api_client.create_sora_video(prompt, aspect_ratio)
    
    def create_simple_video(self, prompt: str) -> Dict:
        """创建普通AI视频"""
        return self.api_client.call_api(
            '/api/yundong/scene',
            {
                'action': 'create_video',
                'prompt': prompt,
                'aspect_ratio': self.config.default_aspect_ratio,
                'duration': self.config.default_duration,
                'name': f'普通AI视频_{self._generate_unique_id()}'
            }
        )
    
    def create_digital_human_with_auto_content(self, topic: str) -> Dict:
        """自动生成内容并创建数字人视频"""
        from .content_generator import ContentGenerator
        
        content_gen = ContentGenerator(self.config)
        copy_result = content_gen.generate_copy(topic)
        
        if copy_result.get('error'):
            return copy_result
            
        # 从返回结果中提取文案内容
        copy_content = self._extract_copy_content(copy_result)
        if not copy_content:
            return {"error": "无法生成有效文案"}
            
        return self.create_digital_human_video(copy_content)
    
    def _extract_copy_content(self, result: Dict) -> Optional[str]:
        """从结果中提取文案内容"""
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0].get('message', {}).get('content', '')
        elif 'content' in result:
            return result['content']
        elif 'data' in result:
            return result['data'].get('content', '')
        else:
            return str(result)
    
    def _generate_unique_id(self) -> str:
        """生成唯一ID"""
        import uuid
        return str(uuid.uuid4())[:8]