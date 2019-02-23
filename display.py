import numpy as np
import sdl2.ext
import sdl2
import cv2



class Display(object):
    def __init__(self, W, H):
        sdl2.ext.init()
        self.W, self.H = W, H
        self.window = sdl2.ext.Window(title = "SLAM",size=(W,H))
        self.window.show()

    def draw(self, img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        surf = sdl2.ext.pixels2d(self.window.get_surface())
        surf[:] = img.swapaxes(0,1)[:,:, 0]
        self.window.refresh()



        



