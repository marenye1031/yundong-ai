"""内容生成模块"""

from .config import ConfigManager
from .api_client import APIClient
from typing import Dict, Optional

class ContentGenerator:
    def __init__(self, config: ConfigManager = None):
        self.config = config or ConfigManager()
        self.api_client = APIClient(config)
    
    def generate_topic(self, industry: str = None, audience: str = None) -> Dict:
        """生成选题"""
        question = f"为{industry or self.config.default_industry}行业的{audience or self.config.default_target_audience}生成适合视频制作的热门选题，包含具体角度和吸引点"
        return self.api_client.generate_content(
            self.config.topic_agent_id,
            question
        )
    
    def generate_title(self, topic: str) -> Dict:
        """生成标题"""
        question = f"为选题'{topic}'生成吸引人的视频标题，符合短视频平台风格"
        return self.api_client.generate_content(
            self.config.title_agent_id,
            question
        )
    
    def generate_copy(self, title: str) -> Dict:
        """生成视频文案"""
        question = f"标题'{title}'生成适合视频口播的文案"
        return self.api_client.generate_content(
            self.config.copy_agent_id,
            question
        )
    
    def generate_xhs_copy(self, title: str) -> Dict:
        """生成小红书风格文案"""
        prompt = f"为标题'{title}'生成小红书风格文案，符合小红书用户阅读习惯"
        return self.api_client.generate_content(
            self.config.xhs_robot_id,
            prompt
        )
    
    def generate_sora_prompt(self, topic: str) -> Dict:
        """生成SORA视频提示词"""
        prompt = f"为主题'{topic}'生成详细的SORA视频提示词，包含场景描述、画面风格、动态效果等"
        return self.api_client.generate_content(
            self.config.sora_robot_id,
            prompt
        )
    
    def generate_topic_from_text(self, topic_text: str) -> Dict:
        """根据文本生成选题"""
        question = f"为'{topic_text}'生成适合视频制作的热门选题，包含具体角度和吸引点"
        return self.api_client.generate_content(
            self.config.topic_agent_id,
            question
        )