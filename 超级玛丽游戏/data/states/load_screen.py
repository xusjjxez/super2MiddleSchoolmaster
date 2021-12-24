__author__ = 'justinarmstrong'

from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..components import info
import pygame as pg


class LoadScreen(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)


    def set_next_state(self):
        """Sets the next state"""
        return c.LEVEL1

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.LOAD_SCREEN


    def update(self, surface, keys, current_time):
        """Updates the loading screen"""
        if (current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(c.BLACK)

        elif (current_time - self.start_time) < 2635:
            surface.fill((106, 150, 252))

        else:
            self.done = True




class GameOver(LoadScreen):
    """A loading screen with Game Over"""
    def __init__(self):
        super(GameOver, self).__init__()

    # 绘制文字
    def print_text(self, screen, x, y, text, fcolor=(255, 0, 0)):
        self.font = pg.font.SysFont('SimHei', 130)  # 得分字体
        self.imgtext = self.font.render(text, True, fcolor)  # 字体渲染
        screen.blit(self.imgtext, (x, y))

    def set_next_state(self):
        """Sets next state"""
        return c.MAIN_MENU

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.GAME_OVER

    def update(self, surface, keys, current_time):
        size = width, height = 1216,760
        self.current_time = current_time
        self.sound_manager.update(self.persist, None)

        endBg = setup.GFX['middle2']
        if (self.current_time - self.start_time) < 7000:
            surface = pg.display.set_mode(size)#新加载一个窗口，适应背景图片大小
            surface.blit(pg.transform.scale(endBg,size),(0,0)) #将背景图片scale重置下大小，画到screen上，从左上角开始画
            self.print_text(surface, 360, 350, '二中必胜！')
            # surface.fill(c.RED)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface) #画出画布来
        # elif (self.current_time - self.start_time) < 7200:
        #     surface.fill(c.BLUE)
        # elif (self.current_time - self.start_time) < 7235:
        #     surface.fill((106, 150, 252))
        else:
            self.done = True


class TimeOut(LoadScreen):
    """Loading Screen with Time Out"""
    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):
        """Sets next state"""
        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_info_state(self):
        """Sets the state to send to the overhead info object"""
        return c.TIME_OUT

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.GRAY)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        else:
            self.done = True









