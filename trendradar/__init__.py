# coding=utf-8
"""
TrendRadar - 热点新闻聚合与分析工具

使用方式:
  python -m trendradar        # 模块执行
  trendradar                  # 安装后执行
"""

from trendradar.context import AppContext

__version__ = "6.10.0"
__all__ = ["AppContext", "__version__"]

# DEBUG: 验证代码是否生效
import os
print(f"[代码验证] __init__.py 路径: {__file__}")
print(f"[代码验证] 修改标识: 2026-07-09-01")
