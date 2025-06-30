import os

import typer
from PIL import Image

app = typer.Typer()


def process_output_path(input_path, output_path=None, size=None, multi_mode=False):
    """处理输出文件路径，支持多图模式和尺寸后缀"""
    if output_path is None:
        base_name, _ = os.path.splitext(input_path)
    else:
        base_name, _ = os.path.splitext(output_path)

    if multi_mode and size is not None:
        return f"{base_name}_{size}x{size}.ico"
    else:
        return f"{base_name}.ico"


def save_single_ico(image, output_path, sizes):
    """保存包含多个尺寸的单一ICO文件"""
    try:
        image.save(output_path, format="ICO", sizes=[(s, s) for s in sizes])
        print(f"成功转换为ICO: {output_path}")
        return True
    except Exception as e:
        print(f"保存单一ICO失败: {e}")
        return False


def save_multi_icos(image, input_path, output_path, sizes):
    """保存多个不同尺寸的ICO文件"""
    success = True
    for size in sizes:
        size_output = process_output_path(input_path, output_path, size, True)
        try:
            # 调整图像大小并保存
            resized_img = image.resize((size, size), Image.LANCZOS)
            resized_img.save(size_output, format="ICO")
            print(f"成功保存尺寸为{size}x{size}的图标: {size_output}")
        except Exception as e:
            print(f"保存尺寸{size}x{size}的图标失败: {e}")
            success = False
    return success


def convert_to_ico(input_path, output_path=None, sizes=None, multi_mode=False):
    """将PNG或JPG图像转换为ICO格式，支持多图保存模式"""
    if sizes is None:
        sizes = [16, 32, 48, 64, 128, 256]  # ICO常见尺寸

    try:
        # 打开图像
        with Image.open(input_path) as img:
            if multi_mode:
                return save_multi_icos(img, input_path, output_path, sizes)
            else:
                final_output = process_output_path(input_path, output_path)
                return save_single_ico(img, final_output, sizes)
    except Exception as e:
        print(f"转换失败: {e}")
        return False


@app.command()
def main(
    input: str = typer.Argument(..., help="输入图像文件路径"),
    output: str = typer.Option(None, "-o", "--output", help="输出ICO文件路径"),
    sizes: list[int] = typer.Option(
        None, "-s", "--sizes", help="ICO图标尺寸列表，如: 16 32 48"
    ),
    multi: bool = typer.Option(
        False, "-m", "--multi", help="启用多图保存模式，为每个尺寸生成单独的ICO文件"
    ),
):
    """将PNG或JPG图像转换为ICO格式"""
    # 转换图像
    convert_to_ico(input, output, sizes, multi)


if __name__ == "__main__":
    app()
