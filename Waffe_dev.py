import os

from PIL import Image

from dev import waffe_main
from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))
WAFFE_WINDOW = waffe_main.WAFFE_MAIN(
    width=1280,
    height=720,
    fullscreen=False,
    title="WAFFE-DEV",
    monitor=None,
    share=None,
    icon=Image.open(global_path.get_proj_abs_path("assets/dev_icon.png")),
)
WAFFE_WINDOW.close()
