import os

from PIL import Image

from src import waffe_main
from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))
WAFFE_WINDOW = waffe_main.WAFFE_MAIN(
    width=1280,
    height=720,
    fullscreen=False,
    title="WAFFE",
    monitor=None,
    share=None,
    icon=Image.open(global_path.get_proj_abs_path("assets/icon.png")),
)
WAFFE_WINDOW.close()
