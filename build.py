import os
import subprocess


def build_executable():
    """使用PyInstaller将Python脚本打包为exe"""
    script_name = "img2ico.py"
    icon_file = "logo.ico"  # 注意：PyInstaller需要ICO格式的图标
    output_dir = "dist"

    # 确保图标文件存在（需要先将logo.svg转换为logo.ico）
    if not os.path.exists(icon_file):
        print(f"错误: 找不到图标文件 {icon_file}，请先将logo.svg转换为ICO格式")
        return

    # 构建命令
    cmd = [
        "pyinstaller",
        "--onefile",
        f"--icon={icon_file}",
        f"--distpath={output_dir}",
        script_name,
    ]

    try:
        # 执行打包命令
        print("开始打包...")
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print("打包成功!")
        print(
            f"可执行文件位于: {os.path.join(output_dir, os.path.splitext(script_name)[0] + '.exe')}"
        )
    except subprocess.CalledProcessError as e:
        print(f"打包失败: {e.stderr}")


if __name__ == "__main__":
    build_executable()
