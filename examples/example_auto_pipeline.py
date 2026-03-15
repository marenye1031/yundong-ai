#!/usr/bin/env python3
"""全自动流水线生成示例"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from yundong_ai import AutoPipeline, ConfigManager

def main():
    """主函数"""
    print("=== 全自动视频生成流水线示例 ===")
    
    # 初始化配置
    config = ConfigManager()
    if not config.api_key:
        print("请先配置API密钥在.env文件中")
        sys.exit(1)
    
    # 初始化全自动流水线
    auto_pipeline = AutoPipeline(config)
    
    # 示例主题
    topic = "人工智能的未来发展趋势"
    
    print(f"\n主题: {topic}")
    print(f"行业: {config.default_industry}")
    print(f"目标受众: {config.default_target_audience}")
    print(f"默认视频时长: {config.default_duration}秒")
    print(f"默认宽高比: {config.default_aspect_ratio}")
    
    # 执行完整流水线
    print("\n--- 开始执行全自动流水线 ---")
    result = auto_pipeline.full_pipeline(topic)
    
    print("\n--- 流水线结果 ---")
    if result.get('error'):
        print(f"流水线执行失败: {result['error']}")
        sys.exit(1)
    
    # 显示结果
    print(f"\n标题: {result['title']}")
    print(f"文案长度: {len(result['copy_content'])}字")
    
    video_result = result['video_result']
    print("\n视频生成结果:")
    if video_result.get('error'):
        print(f"视频生成失败: {video_result['error']}")
    else:
        if video_result.get('task_id'):
            print(f"任务ID: {video_result['task_id']}")
            print("视频正在生成中，请稍后查看")
        elif video_result.get('data') and video_result['data'].get('video_url'):
            print(f"视频链接: {video_result['data']['video_url']}")
            print("视频已生成完成!")
    
    print("\n=== 示例结束 ===")
    print("\n下一个主题建议：")
    print("- AI在教育领域的应用")
    print("- 元宇宙的发展前景")
    print("- 企业数字化转型")
    print("- AI绘画的创作技巧")

if __name__ == '__main__':
    main()