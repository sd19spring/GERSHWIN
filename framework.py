import pygame
from pygame.locals import *
from sys import exit

"""
DEFINING SCREEN SIZE
"""
s_width = 1000
s_height = 800
size = [s_width, s_height]

"""
DEFINING COLORS
"""
black = (0,0,0)
white = (255, 255, 255)
brightred = (255, 69, 0)
brightgreen = (0, 255, 0)
blue = (0,0,255)
darkred = (178, 34, 34)
darkgreen = (25, 100, 50)
darkblue = (25, 50, 150)
"""
DEFINING FONTS
"""
pygame.font.init()
font = 'tlwgtypewriter'
bigfont = pygame.font.SysFont(font, 40)
myfont = pygame.font.SysFont(font, 18)
smallfont = pygame.font.SysFont(font, 15)
medfont = pygame.font.SysFont(font, 25)

def check_quit(events):
    """Monitors events to check if an attempt to quit has been made
    Returns boolean quittin_time True if there was an attempt to quit
    """
    quittin_time=False
    for event in events:
        if event.type == pygame.QUIT:
            quittin_time = True
    return quittin_time

def check_click(scene, events):
    """
    Check for a click and when something is clicked check to see what it clicked
    on and call that items ClickedAction()
    """
    for event in events:
        #print("event")
            # Maybe this should be moved to Scene, so the game doesn't need
            # to know about this logic.
        #printline to check if this is being called
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Buttons in the Scene are drawn first-to-last, so when two Buttons
            # overlap, the last one is displayed. We want to check for clicks
            # last-to-first, so you only click on the top Button.
            Buttons = scene.list_Buttons()[::-1]
            for Button in Buttons:
                #print("Checking Button {}".format(Button.imgname))
                if Button.check_click():
                    # Only click one Button
                    break

class Scene():
    def __init__(self):
        self.next = self
        self.Buttons= []

    def list_Buttons(self):
        return self.Buttons

    def render(self, screen):
        """
        The Scene renders its background and all the Buttons in it.
        """
        # print("Drawing scene {}".format(self.imgname))
        screen.fill(self.color)

        for button in self.Buttons:
            # print("  Drawing Button {}".format(button.imgname))
            button.render(screen)

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switchToScene(None)

class Title(Scene):
    def __init__(self):
        Scene.__init__(self)

    def Update(self):
        pass

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(Output())

    def Render(self, screen):

        #create black screen
        screen.fill(black)

        #creating title
        title = bigfont.render('G E R S H W I N', True, white)
        screen.blit(title,(s_width/2-100, s_height/2))

class Output(Scene):
    def __init__(self):
        Scene.__init__(self)

    def Update(self):
        pass

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(Title())

    def Render(self, screen):

        #create black screen
        screen.fill(blue)

        #creating title
        title = bigfont.render('O U T P UT  S O N G', True, white)
        screen.blit(title,(s_width/2-100, s_height/2))

class Button():
    # To be removed from the scene, we've got to know which scene we're in
    # To blit our image, we have to know the image, size, and coords
    #   (but we can default coords to (0,0) to make it easy)
    # To give the user a message, we need to know the message
    def __init__(self, imgname, size, message=None, coords=(500,520)):
        self.coords = coords
        self.imgname = imgname
        self.size = size
        #Size from tuple to ints
        self.xsize = size[0]
        self.ysize = size[1]
        # Coords from tuple to ints
        self.x = coords[0]
        self.y = coords[1]

    def check_click(self):
        """
        Checks if the mouse was clicked on this Button, and if so, calls
        its clickedAction()
        """
        x = self.x
        y = self.y
        xsize = self.xsize
        ysize = self.ysize
        (a, b) = pygame.mouse.get_pos()
        if a>x and b>y and a<x+xsize and b<y+ysize:
            self.clickedAction()
            return True
        return False

    def render(self, screen):
        """TODO: RENDER ITEMS"""

    def clickedAction(self):
        """This is a default click action so we know that the method works"""
        print("Button {} clicked!".format(self.imgname))


class Game:
    inventory = None
    scene = None



#------------------------------------------------------------------#


def main(fps, starting_scene):
    pygame.init()

    #initializing screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GERSHWIN")

    #looping until close button is clicked
    done = False

    #managing how fast screen updates
    clock = pygame.time.Clock()

    """
    main
    """
    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)



if __name__ == '__main__':
    main(60, Title())
