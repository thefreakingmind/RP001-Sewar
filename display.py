import cv2 
import numpy as np
import sdl2.ext
import sdl2

# For 3D Picture.Fixed the Blue Effect
class Display(object):
    def __init__(self, W, H):
        sdl2.ext.init()
        self.W = W
        self.H = H
        self.window = sdl2.ext.Window("test", size=(W,H))
        self.window.show()       
        
    # Draw The Image
    def draw(self,img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)

        
        surf = sdl2.ext.pixels3d(self.window.get_surface())
        surf[:, :, 0:3] = img.swapaxes(0,1)
        self.window.refresh()



class Display2d(object):
    def __init__(self, W, H):
        sdl2.ext.init()
        self.W = W
        self.H = H
        self.window = sdl2.ext.Window("Slam", size=(W,H))


    def paint(self, img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        surf = sdl2.ext.pixel2d(self.window.get_surface())
        surf[:] = img.swapaxes(0,1)[:, :, :0]
        self.window.refresh()

