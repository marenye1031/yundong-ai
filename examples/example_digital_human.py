#!/usr/bin/env python3
"""数字人视频生成示例"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from yundong_ai import VideoGenerator, ConfigManager

def main():
    """主函数"""
    print("=== 数字人视频生成示例 ===")
    
    # 初始化配置
    config = ConfigManager()
    if not config.api_key:
        print("请先配置API密钥在.env文件中")
        sys.exit(1)
    
    # 初始化视频生成器
    video_gen = VideoGenerator(config)
    
    # 示例文案
    content = "欢迎使用云动AI数字人视频生成平台！这是一个AI驱动的全自动视频制作工具。"
    
    # 生成数字人视频
    print("\n--- 开始生成数字人视频 ---")
    print(f"文案内容: {content}")
    print(f"默认行业: {config.default_industry}")
    print(f"默认目标受众: {config.default_target_audience}")
    
    # 选择数字人形象和声音
    selected_human = config.select_digital_human(content)
    selected_voice = config.select_voice(content)
    
    print(f"\n自动选择的数字人形象: {selected_human.name} (ID: {selected_human.id})")
    print(f"自动选择的声音: {selected_voice.name} (ID: {selected_voice.id})")
    
    # 生成视频
    result = video_gen.create_digital_human_video(content)
    
    print("\n--- 生成结果 ---")
    print(f"响应状态: {'成功' if not result.get('error') else '失败'}")
    if result.get('error'):
        print(f"错误信息: {result['error']}")
    else:
        if result.get('task_id'):
            print(f"任务ID: {result['task_id']}")
            print("视频正在生成中，请稍后查看")
        elif result.get('data') and result['data'].get('video_url'):
            print(f"视频链接: {result['data']['video_url']}")
            print("视频已生成完成!")
    
    print("\n=== 示例结束 ===")

if __name__ == '__main__':
    main()