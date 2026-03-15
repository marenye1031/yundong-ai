"""音乐生成模块"""

from .config import ConfigManager
from .api_client import APIClient
from typing import Dict, Optional

class MusicGenerator:
    def __init__(self, config: ConfigManager = None):
        self.config = config or ConfigManager()
        self.api_client = APIClient(config)
    
    def create_music(self, prompt: str, style: str = None) -> Dict:
        """创建音乐"""
        return self.api_client.create_music(prompt, style)
    
    def create_music_for_video(self, video_topic: str, style: str = None) -> Dict:
        """为视频主题生成配套音乐"""
        prompt = f"为'{video_topic}'主题视频生成合适的背景音乐，风格为{style or self.config.default_music_style}"
        return self.create_music(prompt, style)
    
    def create_digital_human_with_music(self, content: str) -> Dict:
        """创建带背景音乐的数字人视频"""
        video_result = self.api_client.create_digital_human_video(content)
        if video_result.get('error'):
            return video_result
            
        # 提取视频主题相关信息
        video_topic = self._extract_topic_from_content(content)
        music_result = self.create_music_for_video(video_topic)
        
        if music_result.get('error'):
            return video_result  # 至少返回视频结果
            
        return {
            'video_result': video_result,
            'music_result': music_result
        }
    
    def _extract_topic_from_content(self, content: str) -> str:
        """从内容中提取主题"""
        # 简单提取前30个字符作为主题
        return content[:30] + '...' if len(content) > 30 else content