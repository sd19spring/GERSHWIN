import pygame
from pygame.locals import *
from sys import exit

"""
DEFINING SCREEN SIZE
"""
s_width = 1600
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
font = 'ubuntu'
bigfont = pygame.font.SysFont(font, 100)
myfont = pygame.font.SysFont(font, 18)
smallfont = pygame.font.SysFont(font, 18)
medfont = pygame.font.SysFont(font, 23)

'''
GENRE
'''
g_list = ["J A Z Z", "R & B", "P O P", "R O C K", "R A N D O M"]

'''
AESTHETIC EXTRAS
'''
def make_geo(x,y,width,height):
    points = []
    points.append((x,y-(2/3)*height))
    points.append((x+width,y-(2/3.0) * height))
    points.append((x + width/2.0,y-height)) # top of roof
    points.append((x,y-(2/3)*height))

    return points

def draw_geo(x,y,width,height,screen):
    pygame.draw.lines(screen,white,False,make_geo(x,y,width,height), 2)

#-----------------------------------------

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
    """
    initiating generic Scene class
    """
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

    def Terminate(self):
        self.SwitchToScene(None)

class Title(Scene):
    '''
    Creating Scene subclass for input title scene
    '''
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
        screen.fill(darkblue)

        #creating title
        title = bigfont.render('G E R S H W I N', True, white)
        text_rect = title.get_rect(center=(s_width/2, s_height/10))
        screen.blit(title,text_rect)

        #create line
        pygame.draw.line(screen,white, (300, s_height/5), (s_width-300, s_height/5), 2)

        #description text
        desc = medfont.render('r a n d o m   t u n e   g e n e r a t o r   w i t h   l y r i c a l   i n p u t', True, white)
        desc_rect = desc.get_rect(center=(s_width/2, s_height/4))
        screen.blit(desc,desc_rect)

        #step 1
        pygame.draw.rect(screen,white,[300, s_height/2.5,1000,60],3)
        step1 = smallfont.render('S T E P  1 : i n p u t  a  l y r i c', True, white)
        screen.blit(step1,(300,s_height/2.8))

        #step 2
        ran = list(range(300, s_width-300, 212))
        for i in ran:
            pygame.draw.rect(screen,white,[i, s_height/1.75, 150, 60], 3)
        for x in range(0,len(g_list)):
            genre = medfont.render(g_list[x], True, white)
            genre_rect = genre.get_rect(center=(ran[x]+75, s_height/1.64))
            screen.blit(genre,genre_rect)

        step2 = smallfont.render('S T E P  2 : c h o o s e  a  g e n r e', True, white)
        screen.blit(step2,(300, s_height/1.9))

        #step 3
        pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],3)
        step3 = smallfont.render('G E N E R A T E   M Y   S O N G !', True, white)
        s3_rect = step3.get_rect(center=(s_width/2, s_height/1.24))
        screen.blit(step3,s3_rect)

        #geometric points
        draw_geo(50,850,200,250,screen)
        draw_geo(s_width-250,850,200,250,screen)


class Output(Scene):
    '''
    Creating Scene subclass for output scene
    '''
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
        screen.fill(darkgreen)

        #creating title
        title = bigfont.render('O U T P UT  S O N G', True, white)
        text_rect = title.get_rect(center=(s_width/2, s_height/4))
        screen.blit(title,text_rect)



class Button():
    '''
    initiating Button class

    - used for genres, back button, generate button, save button
    '''
    def __init__(self, imgname, size, coords=(500,520)):
        self.coords = coords
        self.imgname = imgname
        self.size = size
        #Size from tuple to ints
        self.xsize = size[0]
        self.ysize = size[1]
        # Coords from tuple to ints
        self.x = coords[0]
        self.y = coords[1]

    def check_clicked(self, events):
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
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clickedAction()
            return True
        return False

    def render(self, screen):
        """TODO: RENDER ITEMS"""

    def clickedAction(self):
        """This is a default click action so we know that the method works"""
        print("The {} button was clicked!".format(self.imgname))


class Game:
    inventory = None
    scene = None


"""Create buttons for each genre, and to generate the song."""
   #TODO: Change the clicked action according to button.
jazz = Button('Jazz', (150, 70), coords=(300,450))
rb = Button('R&B', (150, 70), coords=(512,450))
pop = Button('Pop', (150, 70), coords=(724,450))
rock = Button('Rock', (150, 70), coords=(936,450))
random = Button('Random Genre', (150, 70), coords=(1148,450))
generate = Button('Generate Music', (300, 70), coords=(650,610))
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
        jazz.check_clicked(filtered_events)
        rb.check_clicked(filtered_events)
        pop.check_clicked(filtered_events)
        rock.check_clicked(filtered_events)
        random.check_clicked(filtered_events)
        generate.check_clicked(filtered_events)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)



if __name__ == '__main__':
    main(60, Title())
