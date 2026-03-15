"""云动AI视频生成平台

支持内容生成、数字人视频、SORA视频、音乐生成等全功能
"""

__version__ = "0.1.0"
__author__ = "马仁业"
__description__ = "云动AI视频生成平台 - 全自动内容生成与视频制作工具"

from .config import ConfigManager
from .api_client import APIClient
from .content_generator import ContentGenerator
from .video_generator import VideoGenerator
from .music_generator import MusicGenerator
from .auto_pipeline import AutoPipeline