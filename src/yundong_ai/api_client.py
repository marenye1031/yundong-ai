"""API通信客户端"""

import requests
import json
from typing import Dict, Optional
from .config import ConfigManager

class APIClient:
    def __init__(self, config: Optional[ConfigManager] = None):
        self.config = config or ConfigManager()
        self.headers = {
            'Authorization': self.config.api_key,
            'Content-Type': 'application/json; charset=utf-8'
        }
    
    def call_api(self, endpoint: str, data: Dict) -> Dict:
        """通用API调用方法"""
        url = f"{self.config.base_url}{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, json=data, timeout=60)
            response.encoding = 'utf-8'
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API调用失败: {e}")
            try:
                if hasattr(e, 'response') and e.response.text:
                    print(f"响应内容: {e.response.text}")
            except:
                pass
            return {"error": str(e)}
    
    def generate_content(self, agent_type: str, question: str) -> Dict:
        """生成选题/标题/文案"""
        import uuid
        data = {
            'agent_type': agent_type,
            'question': question,
            'unique_id': str(uuid.uuid4()),
            'stream': 0,
            'model': '1',
            'model_version': 2,
            'industry': self.config.default_industry,
            'target_audience': self.config.default_target_audience
        }
        return self.call_api('/api/v3/chat/agent', data)
    
    def create_digital_human_video(self, content: str, anchor_id: str = None, voice_id: str = None) -> Dict:
        """创建数字人视频"""
        data = {
            'action': 'compound_video',
            'name': f'数字人视频',
            'audio_type': 1,
            'msg': content,
            'anchor_id': anchor_id or self.config.select_digital_human(content).id,
            'voice_id': voice_id or self.config.select_voice(content).id,
            'width': 1080,
            'height': 1920,
            'duration': self.config.default_duration,
            'model_version': 2
        }
        return self.call_api('/api/yundong/scene', data)
    
    def create_sora_video(self, prompt: str, aspect_ratio: str = None) -> Dict:
        """创建SORA视频"""
        data = {
            'action': 'sora_video',
            'type': 'create_sora_video',
            'line_type': int(self.config.default_line_type) if hasattr(self.config, 'default_line_type') else 2,
            'aspectRatio': aspect_ratio or self.config.default_aspect_ratio,
            'duration': self.config.default_duration,
            'prompt': prompt,
            'image_url': '',
            'name': f'SORA视频'
        }
        return self.call_api('/api/yundong/scene', data)
    
    def create_music(self, prompt: str, style: str = None) -> Dict:
        """创建音乐"""
        data = {
            'action': 'create_music',
            'prompt': prompt,
            'style': style or self.config.default_music_style,
            'name': f'音乐_{self._generate_unique_id()}'
        }
        return self.call_api('/api/yundong/scene', data)
    
    def add_video_task(self, topic: str) -> Dict:
        """添加视频任务到自动流水线"""
        data = {
            'title': topic,
            'content': '根据主题全自动生成适合互联网行业年轻白领的短视频',
            'video_robot': self.config.video_robot_id,
            'xhs_robot': self.config.xhs_robot_id,
            'sora_robot': self.config.sora_robot_id,
            'anchor': self.config.select_digital_human(topic).id,
            'voice': self.config.select_voice(topic).id
        }
        return self.call_api('/api/sora.FlowTask/addVideoTask', data)
    
    def _generate_unique_id(self) -> str:
        """生成唯一ID"""
        import uuid
        return str(uuid.uuid4())[:8]