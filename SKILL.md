# 云动AI视频生成Skill

## 描述
云动AI视频生成平台 - 支持数字人视频、SORA视频和全自动流水线生成

## 功能
- 📝 生成吸引人的视频标题
- 📄 生成适合口播的视频文案
- 🎬 生成高质量的数字人视频
- 🎨 生成SORA风格视频素材
- 🚀 全自动生成完整短视频

## 配置
### 环境变量
| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| YUNDONG_API_KEY | API密钥 | 必填 |
| YUNDONG_API_BASE_URL | API基础URL | https://ai.zhiaii.cn |
| YUNDONG_DEFAULT_INDUSTRY | 默认行业 | 互联网行业 |
| YUNDONG_DEFAULT_TARGET_AUDIENCE | 默认目标受众 | 年轻白领 |
| YUNDONG_DEFAULT_DURATION | 默认视频时长 | 10 |
| YUNDONG_DEFAULT_ASPECT_RATIO | 默认宽高比 | 9:16 |

### 智能体配置
| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| YUNDONG_TOPIC_AGENT_ID | 选题智能体ID | 1527 |
| YUNDONG_TITLE_AGENT_ID | 标题智能体ID | 1528 |
| YUNDONG_COPY_AGENT_ID | 文案智能体ID | 1496 |
| YUNDONG_VIDEO_ROBOT_ID | 口播文案智能体ID | 0 |
| YUNDONG_XHS_ROBOT_ID | 小红书文案智能体ID | 0 |
| YUNDONG_SORA_ROBOT_ID | SORA提示词智能体ID | 0 |

## 使用方法
```python
from yundong_ai import AutoPipeline

# 全自动生成
pipeline = AutoPipeline()
result = pipeline.full_pipeline('我是做软件公司的，要找客户')

# 数字人视频生成
from yundong_ai import VideoGenerator
video_gen = VideoGenerator()
result = video_gen.create_digital_human_video('AI技术发展趋势')

# SORA视频生成
result = video_gen.create_sora_video('未来科技城市景象')
```

## 命令行工具
```powershell
# 全自动生成
yundong-ai '我是做软件公司的，要找客户' --auto

# 数字人视频生成
yundong-ai 'AI技术发展趋势' --video

# SORA视频生成
yundong-ai '未来科技城市景象' --sora
```

## 依赖
- requests>=2.31.0
- python-dotenv>=1.0.0
- pycryptodome>=3.20.0

## 链接
- GitHub项目：https://github.com/marenye1031/yundong-ai
- 获取API密钥：https://ai.zhiaii.cn/pc/user/access_token
