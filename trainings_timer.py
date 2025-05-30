
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
        self.count_down: bool = True
        self.time: float = 0.0
        self.pre_timer: bool = False
        self.pre_timer_time: float = 0.0
        self.pre_timer_running: bool = False
        self.fps: int = 0
        self.time_button_list: List[Btn] = []
        self.create_buttons()

        

        # fonts
        self.small_font: pg.font.Font = pg.font.SysFont("comic sans", 23)
        self.time_font: pg.font.Font = pg.font.SysFont("comic sans", 55, bold=True)

        # pre-render
        self.get_ready_text: pg.Surface = self.time_font.render("GET READY", True, "white")
        get_ready_x: int = round(self.WIDTH / 2 - self.get_ready_text.get_width() / 2)
        get_ready_y: int = round(self.HEIGHT / 3 - self.get_ready_text.get_height() / 2)
        self.get_ready_pos: tuple[int, int] = (get_ready_x, get_ready_y)
        self.plus_sign: pg.Surface = self.time_font.render("+", True, "white")
        self.pre_timer_text: pg.Surface = self.small_font.render("pre timer in s", True, "white")
        self.overtime_text: pg.Surface = self.time_font.render("OVERTIME", True, "white")
        overtime_x: int = round(self.WIDTH / 2 - self.overtime_text.get_width() / 2)
        overtime_y: int = round(self.HEIGHT / 3 - self.overtime_text.get_height() / 2)
        self.overtime_pos: tuple[int, int] = (overtime_x, overtime_y)

    def check_buttons(self) -> None:
        """ Checks if a button is clicked. """
        for idx, btn in enumerate(self.time_button_list):
            if btn.check_clicked() and not self.timer_running:
                self.time = btn.get_value() * 60
                self.count_down = True
        for idx, btn in enumerate(self.pre_timer_button_list):
            if btn.check_clicked() and not self.timer_running:
                self.pre_timer_time = float(idx * 10)
                self.pre_timer = True if idx > 0 else False
                self.count_down = True
        if self.start_button.check_clicked():
            self.timer_running = True if not self.pre_timer else False
            self.pre_timer_running = True if self.pre_timer else False
        if self.stop_button.check_clicked():
            self.timer_running = False
            self.pre_timer_running = False

    def create_buttons(self) -> None:
        """ Creates all the buttons. """
        for i in range(2, 12):
            button_value: str = ""
            if i <= 5:
                button_value = str(i)
            else:
                button_value = str(5 * (i - 4))
            self.time_button_list.append(Btn(pos=(5 + (i - 2) * 55, 10), size=(50, 50), text=(button_value), color="white"))
        self.pre_timer_button_list: List[Btn] = [Btn(pos=(5, 170 + i * 55), size=(50, 50), text=str(i * 10), color="white") for i in range(4)]
        self.start_button: Btn = Btn(pos=(175, 455), size=(100, 50), text="START", color="green")
        self.stop_button: Btn = Btn(pos=(280, 455), size=(100, 50), text="STOP", color="red")

    def event_handler(self) -> None:
        """ Handles all the events. """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.app_running = False

    def handle_time(self, time: float, dt: float) -> float:
        """ Handles the time of the timer. """
        if self.count_down:
            time -= dt
        else:
            time += dt

        return time

    def render_screen(self) -> None:
        """ Draws all the elements on the screen. """
        pg.display.set_caption(f"Trainings Timer          FPS:{self.fps}")
        self.screen.fill("black")
        if not self.timer_running and not self.pre_timer_running:
            for btn in self.time_button_list:
                btn.render(self.screen)
            for btn in self.pre_timer_button_list:
                btn.render(self.screen)
            rotated_pre_timer_text: pg.Surface = pg.transform.rotate(self.pre_timer_text, 90)
            self.screen.blit(rotated_pre_timer_text, (60, 197))
        self.start_button.render(self.screen)
        self.stop_button.render(self.screen)
        if not self.pre_timer:
            minute: int = int(self.time / 60)
            minute_zero: str = "" if minute > 9 else "0"
            second: int = int(self.time % 60)
            second_zero: str = "" if second > 9 else "0"
            time_to_blit: pg.Surface = self.time_font.render(f"{minute_zero}{str(minute)}:{second_zero}{str(second)}", True, "white")
            time_x_pos: int = round(self.WIDTH / 2 - time_to_blit.get_width() / 2)
            time_y_pos: int = round(self.HEIGHT / 2 - time_to_blit.get_height() / 2)
            self.screen.blit(time_to_blit, (time_x_pos, time_y_pos))
        else:
            pre_timer__zero: str = "" if self.pre_timer_time > 9 else "0"
            time_to_blit: pg.Surface = self.time_font.render(f"{pre_timer__zero}{str(round(self.pre_timer_time))}", True, "white")
            time_x_pos: int = round(self.WIDTH / 2 - time_to_blit.get_width() / 2)
            time_y_pos: int = round(self.HEIGHT / 2 - time_to_blit.get_height() / 2)
            self.screen.blit(time_to_blit, (time_x_pos, time_y_pos))
            self.screen.blit(self.get_ready_text, self.get_ready_pos)
        if not self.count_down:
            self.screen.blit(self.overtime_text, self.overtime_pos)
            self.screen.blit(self.plus_sign, (time_x_pos - 50, time_y_pos))

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
            if self.timer_running:
                self.time = self.handle_time(self.time, dt)
                if self.time <= 0 and self.count_down:
                    self.count_down = False
            if self.pre_timer_running:
                self.pre_timer_time = self.handle_time(self.pre_timer_time, dt)
                if self.pre_timer_time <= 0:
                    self.pre_timer = False
                    self.pre_timer_running = False
                    self.timer_running = True
            self.render_screen()
            # fps throttler
            if dt < MAX_FPS_TIME:
                pg.time.wait(int(1000 * (MAX_FPS_TIME - dt)))


        pg.quit()
        

if __name__ == "__main__":
    trainings_timer = TrainingsTimer()
    trainings_timer.run()