"""云动AI视频生成平台安装脚本"""

from setuptools import setup, find_packages
import os
import sys

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 直接读取版本信息
version = "0.1.0"
author = "马仁业"

setup(
    name="yundong-ai",
    version=version,
    author=author,
    author_email="your_email@example.com",
    description="云动AI视频生成平台 - 全自动内容生成与视频制作工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marenye1031/yundong-ai",
    project_urls={
        "Bug Reports": "https://github.com/marenye1031/yundong-ai/issues",
        "Source": "https://github.com/marenye1031/yundong-ai",
        "API Key": "https://ai.zhiaii.cn/pc/user/access_token",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "pycryptodome>=3.20.0"
    ],
    entry_points={
        'console_scripts': [
            'yundong-ai = yundong_ai.cli:main'
        ],
        'openclaw_skills': [
            'yundong_ai = yundong_ai'
        ]
    },
    include_package_data=True,
    license="MIT"
)