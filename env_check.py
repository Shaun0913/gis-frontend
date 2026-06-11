#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
开发环境一键自检脚本（Python版）
检测：Git / Node.js / Python / Java 版本
"""

import subprocess
import sys

def run_cmd(cmd):
    try:
        # 执行命令并捕获输出
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8"
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"❌ 检测失败：{e.output.strip()}"
    except Exception as e:
        return f"❌ 检测出错：{str(e)}"

def main():
    print("=" * 60)
    print("          开发环境一键自检脚本（Python版）")
    print("  检测项目：Git  Node.js  Python  Java")
    print("=" * 60)
    print()

    print("【1. 检测 Git 版本】")
    print(run_cmd("git --version"))
    print()

    print("【2. 检测 Node.js 与 npm 版本】")
    print("Node.js:", run_cmd("node -v"))
    print("npm:", run_cmd("npm -v"))
    print()

    print("【3. 检测 Python 版本】")
    print("Python:", sys.version.split()[0])
    print("pip:", run_cmd("pip --version"))
    print()

    print("【4. 检测 Java 版本】")
    print(run_cmd("java -version"))
    print()

    print("=" * 60)
    print("✅ 检测完成")
    print("=" * 60)

if __name__ == "__main__":
    main()
    # 防止运行后闪退
    input("\n按 Enter 键退出...")