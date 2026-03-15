"""云动AI视频生成平台 - OpenClaw Skill"""

__version__ = "0.1.0"
__name__ = "云动AI视频生成"
__description__ = "支持数字人视频、SORA视频和全自动流水线生成"

from .api_client import APIClient
from .auto_pipeline import AutoPipeline
from .config import ConfigManager
from .content_generator import ContentGenerator
from .video_generator import VideoGenerator

__all__ = [
    'APIClient',
    'AutoPipeline',
    'ConfigManager',
    'ContentGenerator',
    'VideoGenerator'
]

def initialize_skill():
    """Initialize skill for OpenClaw"""
    return {
        'name': __name__,
        'version': __version__,
        'description': __description__,
        'modules': __all__,
        'functions': [
            {
                'name': '全自动视频',
                'function': lambda query: AutoPipeline().full_pipeline(query),
                'params': {'query': 'str'},
                'help': '全自动生成视频，用法: 全自动视频 我是做软件公司的，要找客户'
            },
            {
                'name': '数字人视频',
                'function': lambda query: VideoGenerator().create_digital_human_video(query),
                'params': {'query': 'str'},
                'help': '生成数字人视频，用法: 数字人视频 AI技术发展趋势'
            },
            {
                'name': 'SORA视频',
                'function': lambda query: VideoGenerator().create_sora_video(query),
                'params': {'query': 'str'},
                'help': '生成SORA视频，用法: SORA视频 未来科技城市景象'
            }
        ]
    }
