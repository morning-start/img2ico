# img2ico

`img2ico` 是一个将PNG或JPG图像转换为ICO格式图标的命令行工具，支持多图保存模式和自定义尺寸。

## 使用

将PNG或JPG图像文件拖放到 `img2ico.exe` 图标上，即可在相同目录下生成ICO图标文件。

也可以在命令行中使用以下参数：

- `-o, --output`: 指定输出ICO文件路径。
- `-s, --sizes`: 指定ICO图标尺寸列表，例如 `-s 16 -s 32 -s 48`。默认尺寸为 `16, 32, 48, 64, 128, 256`。
- `-m, --multi`: 启用多图保存模式，为每个尺寸生成单独的ICO文件。

## 安装

确保你的Python版本 >= 3.11，然后通过以下命令安装依赖：

```bash
uv sync
```

### 基本命令
```bash
uv run main.py [输入图像文件路径]
```


### 示例

1. 转换单个图像为包含默认尺寸的单一ICO文件：
```bash
uv run main.py input.png
```

2. 转换图像并指定输出路径：
```bash
uv run main.py input.png -o output.ico
```

3. 转换图像并指定自定义尺寸：
```bash
uv run main.py input.png -s 16 -s 32 -s 48
```

4. 启用多图保存模式，为每个尺寸生成单独的ICO文件：
```bash
uv run main.py input.png -m
```

## 构建应用

如果你想构建独立的可执行文件，可以运行 `build.py` 脚本：
```bash
uv run build.py
```