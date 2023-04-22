import glfw
from dev.Graphics import waffe_graphics
import keyboard


class WAFFE_MAIN:
    def __init__(
        self,
        width: int,
        height: int,
        fullscreen: bool,
        title: str,
        monitor,
        share,
        icon,
    ):
        # GLFW INIT
        glfw.init()

        # VAR
        self.WAFFE_WINDOW = None
        self.WAFFE_WINDOW_TITLE = title
        self.FPS_LAST_TIME = glfw.get_time()
        self.FPS_CURRENT_TIME = glfw.get_time()
        self.FPS_NUM_FRAMES = 0
        self.FPS_FRAME_TIME = 0

        self.build_glfw_window(
            width=width,
            height=height,
            fullscreen=fullscreen,
            title=title,
            monitor=monitor,
            share=share,
            icon=icon,
        )
        waffe_graphics.gl_set()
        self.render()

    def build_glfw_window(
        self,
        width: int,
        height: int,
        fullscreen: bool,
        title: str,
        monitor,
        share,
        icon,
    ):
        glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)
        if fullscreen:
            self.WAFFE_WINDOW = glfw.create_window(
                width=glfw.get_video_mode(glfw.get_primary_monitor()).size.width,
                height=glfw.get_video_mode(glfw.get_primary_monitor()).size.height,
                title=title,
                monitor=glfw.get_primary_monitor(),
                share=share,
            )
        else:
            self.WAFFE_WINDOW = glfw.create_window(
                width=width,
                height=height,
                title=title,
                monitor=monitor,
                share=share,
            )
        if icon is not None:
            glfw.set_window_icon(window=self.WAFFE_WINDOW, count=1, images=icon)
        glfw.make_context_current(window=self.WAFFE_WINDOW)

        if self.WAFFE_WINDOW is not None:
            print(f"WAFFE_WINDOW created. width={width}, height={height}")
        else:
            print("WAFFE_WINDOW failed to create.")

    def render(self):
        waffe_graphics.shaders()
        while not glfw.window_should_close(window=self.WAFFE_WINDOW):
            glfw.poll_events()
            waffe_graphics.render()

            if keyboard.is_pressed("esc"):
                self.close()

            self.calculate_framerate()
            glfw.swap_buffers(window=self.WAFFE_WINDOW)

    def calculate_framerate(self):
        self.FPS_CURRENT_TIME = glfw.get_time()
        delta = self.FPS_CURRENT_TIME - self.FPS_LAST_TIME

        if delta >= 1:
            framerate = max(1, int(self.FPS_NUM_FRAMES // delta))
            glfw.set_window_title(
                window=self.WAFFE_WINDOW,
                title=f"{self.WAFFE_WINDOW_TITLE}_____Running at {framerate} fps",
            )
            print(f"{self.WAFFE_WINDOW_TITLE}_____Running at {framerate} fps")
            self.FPS_LAST_TIME = self.FPS_CURRENT_TIME
            self.FPS_NUM_FRAMES = -1
            self.FPS_FRAME_TIME = 1000.0 / framerate

        self.FPS_NUM_FRAMES += 1

    def close(self):
        glfw.destroy_window(window=self.WAFFE_WINDOW)
        glfw.terminate()
