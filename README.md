# 云动AI视频生成平台

## 🎯 简介

云动AI视频生成平台是一款功能强大的AI内容生成与视频制作工具，集成了选题、标题、文案、数字人视频、SORA视频等全功能，支持一键全自动生成短视频。

## ✨ 功能特性

### 📝 内容生成
- ✅ **智能标题生成**：基于主题生成吸引人的视频标题
- ✅ **专业文案创作**：生成适合口播的短视频文案
- ✅ **多风格优化**：支持普通视频和小红书风格
- ✅ **自动选择**：智能匹配行业和受众特点

### 🎬 视频生成
- ✅ **数字人视频**：高质量数字人口播视频
- ✅ **SORA视频**：AI生成场景和背景
- ✅ **多形象支持**：多种数字人形象可供选择
- ✅ **多音色选择**：自然流畅的语音合成
- ✅ **全自动流水线**：输入主题即可得到成品视频

### 🚀 平台优势
- **真正全自动**：无需人工干预，AI完成所有环节
- **专业优化**：每一步都经过AI优化，适合短视频传播
- **节省时间**：手动需要几小时，现在只需几分钟
- **批量生产**：可一次性生成多个不同风格的视频
- **易于使用**：简单的API调用和命令行工具

## 📦 安装方式

### 方式1：直接解压使用
```powershell
unzip yundong-ai-skill.zip -d ~/.openclaw/workspace/skills/
```

### 方式2：Python包安装
```powershell
pip install yundong-ai
```

### 方式3：源码安装
```powershell
git clone https://github.com/marenye1031/yundong-ai.git
cd yundong-ai
pip install .
```

## 🚀 快速开始

### 基本配置

1. 复制环境变量示例文件：
```powershell
cp .env.example .env
```

2. 编辑`.env`文件，填写你的API密钥和配置：
```ini
# API Credentials
YUNDONG_API_KEY=your_api_key_here
YUNDONG_API_BASE_URL=https://ai.zhiaii.cn

# Agent Configurations
YUNDONG_TOPIC_AGENT_ID=1527      # 选题智能体ID
YUNDONG_TITLE_AGENT_ID=1528      # 标题智能体ID
YUNDONG_COPY_AGENT_ID=1496       # 文案智能体ID
YUNDONG_VIDEO_ROBOT_ID=0         # 口播文案智能体ID
YUNDONG_XHS_ROBOT_ID=0           # 小红书文案智能体ID
YUNDONG_SORA_ROBOT_ID=0           # SORA提示词智能体ID

# Default Preferences
YUNDONG_DEFAULT_INDUSTRY=互联网行业
YUNDONG_DEFAULT_TARGET_AUDIENCE=年轻白领
YUNDONG_DEFAULT_DURATION=10       # 默认视频时长（秒）
YUNDONG_DEFAULT_ASPECT_RATIO=9:16 # 默认宽高比 (9:16, 16:9, 1:1)
YUNDONG_DEFAULT_MUSIC_STYLE=轻快流行 # 默认音乐风格
YUNDONG_DEFAULT_LINE_TYPE=2       # 默认线路类型
```

### Python API调用

#### 1. 数字人视频生成
```python
from yundong_ai import VideoGenerator

video_gen = VideoGenerator()
result = video_gen.create_digital_human_video("我是做软件公司的，要找客户")
print(result)
```

#### 2. SORA视频生成
```python
from yundong_ai import VideoGenerator

video_gen = VideoGenerator()
result = video_gen.create_sora_video("未来科技城市景象")
print(result)
```

#### 3. 全自动流水线
```python
from yundong_ai import AutoPipeline

pipeline = AutoPipeline()
result = pipeline.full_pipeline("AI技术发展趋势")
print(result)
```

#### 4. 内容生成
```python
from yundong_ai import ContentGenerator

content_gen = ContentGenerator()
title_result = content_gen.generate_title("AI技术发展趋势")
copy_result = content_gen.generate_copy(title_result['choices'][0]['message']['content'])
print(title_result)
print(copy_result)
```

## 🖥️ 命令行工具

### 基本用法
```powershell
python yundong-ai.py '主题内容' --[options]
```

### 选项说明
| 选项 | 功能 | 示例 |
|------|------|------|
| `--title` | 生成视频标题 | `--title` |
| `--copy` | 生成视频文案 | `--copy` |
| `--video` | 生成数字人视频 | `--video` |
| `--sora` | 生成SORA视频 | `--sora` |
| `--auto` | 全自动生成完整视频 | `--auto` |

### 使用示例

#### 全自动生成（推荐）
```powershell
python yundong-ai.py '我是做软件公司的，要找客户' --auto
```

#### 数字人视频生成
```powershell
python yundong-ai.py 'AI技术发展趋势' --video
```

#### SORA视频生成
```powershell
python yundong-ai.py '未来科技城市景象' --sora
```

#### 仅生成标题和文案
```powershell
python yundong-ai.py '我是做软件公司的，要找客户' --title --copy
```

## 🎯 生成效果示例

### 📝 标题生成示例
**主题**: 我是做软件公司的，要找客户
**生成标题**:
1. 我开软件公司前3年亏掉200万，才搞懂：找客户的底层逻辑，比技术重要100倍！
2. 别再瞎跑业务了！我用程序员的算法思维，总结出3个精准找到客户的"最优解"
3. 软件公司找客户的3个致命误区！我曾因为第2个，差点让团队解散（附避坑指南）

### 📄 文案生成示例
```

我用程序员的算法思维悟透一个反直觉真相：找客户的底层逻辑，比技术重要100倍！别再瞎跑业务，要把客户当“精准流量”，用利他思维设计业务接口，而非硬推代码。

想知道精准找客户的3个最优解？评论区留言，我教你破局！
```

## 🎨 数字人配置

### 支持的数字人形象
- **职业形象** (ID: 956xx0)：专业商务风格
- **休闲形象** (ID: 95xx16)：轻松日常风格
- **创新形象** (ID: 90xx98)：科技感风格

### 支持的音色
- **平和型声音** (ID: afdce4386dxxxxc8980e)：自然流畅
- **激情型声音** (ID: be3c8a2xxxx184935cae)：富有感染力

## 🔧 配置说明

### 获取API密钥
您可以通过以下网址获取API密钥：
🔑 [获取云动AI API Key](https://ai.zhiaii.cn/pc/user/access_token)

### 环境变量配置
| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `YUNDONG_API_KEY` | API密钥 | 必填 |
| `YUNDONG_API_BASE_URL` | API基础URL | https://ai.zhiaii.cn |
| `YUNDONG_DEFAULT_INDUSTRY` | 默认行业 | 互联网行业 |
| `YUNDONG_DEFAULT_TARGET_AUDIENCE` | 默认目标受众 | 年轻白领 |
| `YUNDONG_DEFAULT_DURATION` | 默认视频时长 | 10 |
| `YUNDONG_DEFAULT_ASPECT_RATIO` | 默认宽高比 | 9:16 |
| `YUNDONG_DEFAULT_LINE_TYPE` | 默认线路类型 | 2 |

### 智能体配置
| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `YUNDONG_TOPIC_AGENT_ID` | 选题智能体ID | 1527 |
| `YUNDONG_TITLE_AGENT_ID` | 标题智能体ID | 1528 |
| `YUNDONG_COPY_AGENT_ID` | 文案智能体ID | 1496 |
| `YUNDONG_VIDEO_ROBOT_ID` | 口播文案智能体ID | 0 |
| `YUNDONG_XHS_ROBOT_ID` | 小红书文案智能体ID | 0 |
| `YUNDONG_SORA_ROBOT_ID` | SORA提示词智能体ID | 0 |

## 🌟 应用场景

### 📱 短视频内容生产
- 抖音/快手视频批量生成
- 小红书笔记自动创作
- 视频号内容矩阵搭建

### 📞 获客与营销
- 产品介绍视频生成
- 行业解决方案视频
- 品牌故事宣传视频

### 🎓 教育与培训
- 知识科普短视频
- 技术讲解视频
- 课程片段生成

### 📺 企业宣传
- 公司介绍视频
- 团队风采视频
- 企业文化视频

## 🤝 技术支持

- **问题反馈**: 请在GitHub Issues中提交问题
- **技术文档**: 查看项目Wiki获取详细文档
- **API文档**: http://doc.7seme.com/index.php/26
- **联系方式**: 请查看项目主页

## 📜 许可证

MIT License - 详见LICENSE文件

## 📧 更新日志

### v0.1.0 (2026-03-15)
- 🎉 初始版本发布
- ✅ 支持数字人视频生成
- ✅ 支持SORA视频生成
- ✅ 支持全自动视频生产流水线
- ✅ 支持内容生成（标题/文案）
- ✅ 提供Python API和命令行工具
