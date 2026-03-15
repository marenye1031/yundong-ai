#!/usr/bin/env python3
"""SORA视频生成示例"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from yundong_ai import VideoGenerator, ContentGenerator, ConfigManager

def main():
    """主函数"""
    print("=== SORA视频生成示例 ===")
    
    # 初始化配置
    config = ConfigManager()
    if not config.api_key:
        print("请先配置API密钥在.env文件中")
        sys.exit(1)
    
    # 初始化内容生成器
    content_gen = ContentGenerator(config)
    
    # 示例主题
    topic = "未来科技城市"
    
    print("\n--- 步骤1: 生成SORA提示词 ---")
    print(f"主题: {topic}")
    
    # 生成SORA提示词
    sora_result = content_gen.generate_sora_prompt(topic)
    
    if sora_result.get('error'):
        print(f"提示词生成失败: {sora_result['error']}")
        # 使用默认提示词
        prompt = f"{topic}，未来科技感，赛博朋克风格，4K分辨率，高质量画面，动态场景"
    else:
        prompt = sora_result.get('choices', [{}])[0].get('message', {}).get('content', '')
        if not prompt:
            prompt = f"{topic}，未来科技感，赛博朋克风格，4K分辨率，高质量画面，动态场景"
    
    print(f"\n生成的提示词: {prompt}")
    
    print("\n--- 步骤2: 生成SORA视频 ---")
    
    # 初始化视频生成器
    video_gen = VideoGenerator(config)
    
    # 生成SORA视频
    result = video_gen.create_sora_video(prompt)
    
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