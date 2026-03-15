"""配置管理模块"""

import os
import json
from dotenv import load_dotenv
from typing import Dict, List, Optional

class DigitalHumanConfig:
    """数字人形象配置"""
    def __init__(self, config: Dict):
        self.id = config['id']
        self.name = config['name']
        self.desc = config.get('desc', '')
        self.scenes = [s.strip() for s in config.get('scenes', '').split(',') if s.strip()]
        self.style = config.get('style', '')
        self.gender = config.get('gender', '')

class VoiceConfig:
    """声音配置"""
    def __init__(self, config: Dict):
        self.id = config['id']
        self.name = config['name']
        self.desc = config.get('desc', '')
        self.scenes = [s.strip() for s in config.get('scenes', '').split(',') if s.strip()]
        self.gender = config.get('gender', '')
        self.speed = float(config.get('speed', 1.0))

class ConfigManager:
    """配置管理器"""
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('YUNDONG_API_KEY')
        self.base_url = os.getenv('YUNDONG_API_BASE_URL', 'https://ai.zhiaii.cn')
        
        # 智能体配置
        self.topic_agent_id = os.getenv('YUNDONG_TOPIC_AGENT_ID')
        self.title_agent_id = os.getenv('YUNDONG_TITLE_AGENT_ID')
        self.copy_agent_id = os.getenv('YUNDONG_COPY_AGENT_ID')
        self.video_robot_id = os.getenv('YUNDONG_VIDEO_ROBOT_ID')
        self.xhs_robot_id = os.getenv('YUNDONG_XHS_ROBOT_ID')
        self.sora_robot_id = os.getenv('YUNDONG_SORA_ROBOT_ID')
        
        # 默认参数
        self.default_industry = os.getenv('YUNDONG_DEFAULT_INDUSTRY', '互联网行业')
        self.default_target_audience = os.getenv('YUNDONG_DEFAULT_TARGET_AUDIENCE', '年轻白领')
        self.default_duration = int(os.getenv('YUNDONG_DEFAULT_DURATION', 10))
        self.default_aspect_ratio = os.getenv('YUNDONG_DEFAULT_ASPECT_RATIO', '9:16')
        self.default_music_style = os.getenv('YUNDONG_DEFAULT_MUSIC_STYLE', '轻快流行')
        self.default_line_type = os.getenv('YUNDONG_DEFAULT_LINE_TYPE', '2')
        self.video_robot_id = os.getenv('YUNDONG_VIDEO_ROBOT_ID', '0')
        self.xhs_robot_id = os.getenv('YUNDONG_XHS_ROBOT_ID', '0')
        self.sora_robot_id = os.getenv('YUNDONG_SORA_ROBOT_ID', '0')
        
        # 数字人配置
        self.digital_humans = self._load_digital_humans()
        self.voices = self._load_voices()
    
    def _load_digital_humans(self) -> List[DigitalHumanConfig]:
        """加载数字人配置"""
        humans_str = os.getenv('YUNDONG_DIGITAL_HUMANS', '[]')
        try:
            humans_data = json.loads(humans_str)
            return [DigitalHumanConfig(h) for h in humans_data]
        except Exception as e:
            print(f"加载数字人配置失败: {e}")
            return []
    
    def _load_voices(self) -> List[VoiceConfig]:
        """加载声音配置"""
        voices_str = os.getenv('YUNDONG_VOICES', '[]')
        try:
            voices_data = json.loads(voices_str)
            return [VoiceConfig(v) for v in voices_data]
        except Exception as e:
            print(f"加载声音配置失败: {e}")
            return []
    
    def select_digital_human(self, content: str) -> Optional[DigitalHumanConfig]:
        """根据内容自动选择数字人"""
        # 简单的关键词匹配算法，可扩展为AI分析
        for human in self.digital_humans:
            for scene in human.scenes:
                if scene in content:
                    return human
        return self.digital_humans[0] if self.digital_humans else None
    
    def select_voice(self, content: str) -> Optional[VoiceConfig]:
        """根据内容自动选择声音"""
        for voice in self.voices:
            for scene in voice.scenes:
                if scene in content:
                    return voice
        return self.voices[0] if self.voices else None