### ホットリロード

usage: flet run [-h] [--port PORT] [--directory] [--recursive] [--hidden] [--web]
script

Runs Flet app in Python with hot reload.

positional arguments:
script path to a Python script

options:
-h, --help show this help message and exit
-v, --verbose -v for detailed output and -vv for more detailed
-p PORT, --port PORT custom TCP port to run Flet app on
-d, --directory watch script directory
-r, --recursive watch script directory and all sub-directories recursively
-n, --hidden application window is hidden on startup
-w, --web open app in a web browser

- sample

```
flet run Calc1.py -d
flet run main.py -r
```

### packaging

auto-py-to-exe

```bash
auto-py-to-exe
```

flet がインストール済の環境でないとうまくいかない？

#### 応急処置

FLET_DEBUG_MODE = False

にして flet pack する

（DEBUG 実行時は = True）

#### カスタム Icon

flet pack your_program.py --icon <your-image.png>

- これで一応成功した。assets もうまくいった
  cd Apps/Solitaire/src
  flet pack main.py --icon card_back.png --add-data "assets;assets"
