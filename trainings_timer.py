
from button import Button as Btn

from time import perf_counter as pc
import pygame as pg

from typing import List, Final


class TrainingsTimer:
    WIDTH: Final[int] = 555
    HEIGHT: Final[int] = 555
    def __init__(self) -> None:
        pg.init()
        self.screen: pg.Surface = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.app_running: bool = True
        self.timer_running: bool = False
        self.time: float = 0.0
        self.fps: int = 0
        self.create_buttons()

        self.time_font: pg.font.Font = pg.font.SysFont("comic sans", 55, bold=True)

    def check_buttons(self) -> None:
        """ Checks if a button is clicked. """
        for idx, btn in enumerate(self.button_list):
            if btn.check_clicked() and not self.timer_running:
                self.time = float((idx + 1) * 2)

    def create_buttons(self) -> None:
        """ Creates all the buttons. """
        print("Create btn")
        self.button_list: List[Btn] = [Btn(pos=(5 + i * 55, 5), size=(50, 50), text=(str((i + 1) * 2)), color="white") for i in range(10)]

    def event_handler(self) -> None:
        """ Handles all the events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.app_running = False

    def render_screen(self) -> None:
        """ Draws all the elements on the screen. """
        pg.display.set_caption(f"Trainings Timer          FPS:{self.fps}")
        self.screen.fill("black")
        for btn in self.button_list:
            btn.render(self.screen)
        time_to_blit: pg.Surface = self.time_font.render(str(self.time), True, "white")
        time_x_pos: int = round(self.WIDTH / 2 - time_to_blit.get_width() / 2)
        time_y_pos: int = round(self.HEIGHT / 2 - time_to_blit.get_height() / 2)
        self.screen.blit(time_to_blit, (time_x_pos, time_y_pos))

        pg.display.update()

    def run(self) -> None:
        """ The run method of the timer. """
        MAX_FPS: int = 60
        MAX_FPS_TIME: float = 1 / MAX_FPS
        old_time: float = pc()
        frames: int = 0
        fps_timer: float = 0.0
        while self.app_running:
            # calculating delta time
            dt = pc() - old_time
            old_time = pc()
            # counting fps
            frames += 1
            fps_timer += dt
            if fps_timer >= 1:
                self.fps = frames
                frames = 0
                fps_timer = 0.0

            self.event_handler()
            self.check_buttons()
            self.render_screen()
            # fps throttler
            if dt < MAX_FPS_TIME:
                pg.time.wait(int(1000 * (MAX_FPS_TIME - dt)))


        pg.quit()
        

if __name__ == "__main__":
    trainings_timer = TrainingsTimer()
    trainings_timer.run()