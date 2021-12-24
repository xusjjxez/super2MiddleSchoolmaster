__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import constants as c

class Flag(pg.sprite.Sprite):
    """Flag on top of the flag pole at the end of the level"""
    def __init__(self, x, y):
        super(Flag, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_images()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.state = c.TOP_OF_POLE

    def create_image(self, filename, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()
        self.image_yuandan = setup.GFX[filename]
        image.blit(self.image_yuandan, (0, 0), (0, 0, 500, 380))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width / 5),
                                    int(rect.height / 5)))
        return image

    def setup_images(self):
        """Sets up a list of image frames"""
        self.frames = []

        self.frames.append(
            self.create_image('flag',501,380))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self, *args):
        """Updates behavior"""
        self.handle_state()


    def handle_state(self):
        """Determines behavior based on state"""
        if self.state == c.TOP_OF_POLE:
            self.image = self.frames[0]
        elif self.state == c.SLIDE_DOWN:
            self.sliding_down()
        elif self.state == c.BOTTOM_OF_POLE:
            self.image = self.frames[0]


    def sliding_down(self):
        """State when Mario reaches flag pole"""
        self.y_vel = -5
        self.rect.y += self.y_vel

        if self.rect.top < 340:
            self.state = c.BOTTOM_OF_POLE


class Pole(pg.sprite.Sprite):
    """Pole that the flag is on top of"""
    def __init__(self, x, y):
        super(Pole, self).__init__()
        self.sprite_sheet = setup.GFX['tile_set']
        self.setup_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def setup_frames(self):
        """Create the frame list"""
        self.frames = []

        self.frames.append(
            self.get_image(263, 208, 2, 16))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self, *args):
        """Placeholder for update, since there is nothing to update"""
        pass


class Finial(pg.sprite.Sprite):
    """The top of the flag pole"""
    def __init__(self, x, y):
        super(Finial, self).__init__()
        self.sprite_sheet = setup.GFX['tile_set']
        self.setup_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y


    def setup_frames(self):
        """Creates the self.frames list"""
        self.frames = []

        self.frames.append(
            self.get_image(260, 200, 8, 8))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def update(self, *args):
        pass



