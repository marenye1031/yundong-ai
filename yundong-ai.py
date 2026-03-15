#!/usr/bin/env python3
"""云动AI视频生成平台 - 正式版"""

import sys
import os
sys.path.insert(0, 'src')

from yundong_ai import ContentGenerator, VideoGenerator, AutoPipeline, ConfigManager

def print_help():
    """打印帮助信息"""
    print("=== 云动AI视频生成平台 ===")
    print("\n🎯 功能：")
    print("  📝 生成吸引人的视频标题")
    print("  📄 生成适合口播的视频文案")
    print("  🎬 生成高质量的数字人视频")
    print("  🎨 生成SORA风格视频素材")
    print("  🚀 全自动生成完整短视频")
    print("\n📋 使用方法：")
    print("  python yundong-ai.py '主题内容' --[options]")
    print("\n⚙️ 选项：")
    print("  --title       仅生成标题")
    print("  --copy        仅生成文案")
    print("  --video       仅生成数字人视频")
    print("  --sora        仅生成SORA视频")
    print("  --auto        全自动生成（推荐）")
    print("\n🌟 示例：")
    print("  python yundong-ai.py '我是做软件公司的，要找客户' --auto")
    print("  python yundong-ai.py 'AI技术发展趋势' --video")
    print("  python yundong-ai.py '未来科技城市' --sora")
    print("\n💡 提示：主题越具体，生成效果越好")

def main():
    """主函数"""
    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h', 'help']:
        print_help()
        sys.exit(1)
    
    topic = sys.argv[1]
    options = sys.argv[2:]
    
    if not options:
        print("⚠️ 请指定要执行的操作，例如--auto或--video")
        print("💡 执行python yundong-ai.py --help查看帮助")
        sys.exit(1)
    
    # 初始化配置
    try:
        config = ConfigManager()
        
        # 检查API密钥
        if not config.api_key or config.api_key == 'your_api_key_here':
            print("⚠️  未配置API密钥或使用默认值")
            print("🔑 请访问以下网址获取API密钥:")
            print("   https://ai.zhiaii.cn/pc/user/access_token")
            print("📋 配置方法：在.env文件中设置YUNDONG_API_KEY=your_api_key_here")
            print("\n示例：")
            print("  YUNDONG_API_KEY=abc123def456...")
            sys.exit(1)
    except Exception as e:
        print(f"❌ 配置初始化失败: {e}")
        sys.exit(1)
    
    print(f"=== 云动AI视频生成平台 ===")
    print(f"🎯 主题: {topic}")
    print(f"📊 配置: 行业={config.default_industry}, 受众={config.default_target_audience}, 时长={config.default_duration}秒")
    print()
    
    generated_title = None
    generated_copy = None
    
    # 生成标题
    if '--title' in options or '--auto' in options:
        try:
            print("📝 开始生成标题...")
            content_gen = ContentGenerator(config)
            result = content_gen.generate_title(topic)
            
            if result.get('error'):
                print(f"❌ 标题生成失败: {result['error']}")
            else:
                print("🎉 标题生成成功!")
                for i, choice in enumerate(result.get('choices', []), 1):
                    title = choice.get('message', {}).get('content', '')
                    print(f"\n{i}. {title}")
                    if i == 1:
                        generated_title = title
        except Exception as e:
            print(f"❌ 标题生成异常: {e}")
        print()
    
    # 生成文案
    if '--copy' in options or '--auto' in options:
        try:
            print("📄 开始生成文案...")
            content_gen = ContentGenerator(config)
            use_title = generated_title or topic
            result = content_gen.generate_copy(use_title)
            
            if result.get('error'):
                print(f"❌ 文案生成失败: {result['error']}")
            else:
                print("🎉 文案生成成功!")
                for i, choice in enumerate(result.get('choices', []), 1):
                    copy_content = choice.get('message', {}).get('content', '')
                    print(f"\n{i}. {copy_content}")
                    if i == 1:
                        generated_copy = copy_content
                print(f"\n字数统计: {len(copy_content)}字")
        except Exception as e:
            print(f"❌ 文案生成异常: {e}")
        print()
    
    # 生成数字人视频
    if '--video' in options or '--auto' in options:
        try:
            print("🎬 开始生成数字人视频...")
            video_gen = VideoGenerator(config)
            use_content = generated_copy or topic
            result = video_gen.create_digital_human_video(use_content)
            
            if result.get('error'):
                print(f"❌ 视频生成失败: {result['error']}")
            else:
                print("🎉 数字人视频生成成功!")
                task_id = result.get('task_id', '')
                if not task_id and result.get('data'):
                    task_id = result['data'].get('task_id', result['data'].get('id', {}).get('task_id', ''))
                if task_id:
                    print(f"📋 任务ID: {task_id}")
                print(f"⏳ 视频正在全自动生成中，请稍后查看")
                if result.get('data') and result['data'].get('video_url'):
                    print(f"📺 视频链接: {result['data']['video_url']}")
        except Exception as e:
            print(f"❌ 视频生成异常: {e}")
        print()
    
    # 生成SORA视频
    if '--sora' in options:
        try:
            print("🎨 开始生成SORA视频...")
            video_gen = VideoGenerator(config)
            result = video_gen.create_sora_video(topic)
            
            if result.get('error'):
                print(f"❌ SORA视频生成失败: {result['error']}")
            else:
                print("🎉 SORA视频生成成功!")
                task_id = result.get('task_id', '')
                if not task_id and result.get('data'):
                    task_id = result['data'].get('task_id', result['data'].get('id', {}).get('task_id', ''))
                if task_id:
                    print(f"📋 任务ID: {task_id}")
                print(f"⏳ 视频正在全自动生成中，请稍后查看")
        except Exception as e:
            print(f"❌ SORA视频生成异常: {e}")
        print()
    
    # 全自动生成
    if '--auto' in options:
        try:
            print("🚀 全自动流水线已完成以下步骤:")
            print("  ✅ 智能标题生成")
            print("  ✅ 专业文案创作")
            print("  ✅ 数字人视频合成")
            print(f"\n💡 完整短视频正在全自动生成中，稍后将可以查看最终结果")
        except Exception as e:
            print(f"❌ 全自动生成异常: {e}")
    
    print("--- 操作完成 ---\n")
    
    if not (result.get('error') if 'result' in locals() else True):
        print("🎯 下一步建议:")
        print("  1. 定期查看视频生成状态")
        print("  2. 配置参数优化效果")
        print("  3. 批量生成多个视频")

if __name__ == '__main__':
    main()