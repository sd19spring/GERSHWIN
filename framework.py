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
grey = (128, 128, 128)
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
    pygame.draw.lines(screen,white,False,make_geo(x,y,width,height), 5)

def make_shapes(screen):
    draw_geo(50,900,200,250,screen)
    draw_geo(s_width-250,900,200,250,screen)
    draw_geo(50,350,200,250,screen)
    draw_geo(s_width-250,350,200,250,screen)
    draw_geo(50,600,200,250,screen)
    draw_geo(s_width-250,600,200,250,screen)
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
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (a, b) = pygame.mouse.get_pos()
                        if a>650 and b>610 and a<950 and b<680:
                        # Move to the next scene when the user pressed Enter
                            self.SwitchToScene(Output())
                jazz.check_clicked(events)
                rb.check_clicked(events)
                pop.check_clicked(events)
                rock.check_clicked(events)
                random.check_clicked(events)
                generate.check_clicked(events)

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
        ran = list(range(300, s_width-300, 212))

        (a, b) = pygame.mouse.get_pos()
        #step 1
        if a > 300 and a < 1300 and b > (s_height/2.5) and b < (s_height/2.5)+60:
            pygame.draw.rect(screen,white,[300, s_height/2.5,1000,60],0)

        else:
            pygame.draw.rect(screen,white,[300, s_height/2.5,1000,60],3)

        for x in range(0,len(g_list)):
                    genre = medfont.render(g_list[x], True, white)
                    genre_rect = genre.get_rect(center=(ran[x]+75, s_height/1.64))
                    screen.blit(genre,genre_rect)
        step1 = smallfont.render('S T E P  1 : i n p u t  a  l y r i c', True, white)
        screen.blit(step1,(300,s_height/2.8))

        #step 2
        #x = 0, 1...
        #i = 300, 512...
        #212x+300=i -> (i-300)/212 = x
        for i in ran:
            if a>i and a<i+150 and b>(s_height/1.75) and b < (s_height/1.75)+60:
                pygame.draw.rect(screen,white,[i, s_height/1.75, 150, 60],0)
                x = int((i-300)/212)
                genre = medfont.render(g_list[x], True, darkblue)
                genre_rect = genre.get_rect(center=(ran[x]+75, s_height/1.64))
                screen.blit(genre,genre_rect)
            else:
                pygame.draw.rect(screen,white,[i, s_height/1.75, 150, 60], 3)

        step2 = smallfont.render('S T E P  2 : c h o o s e  a  g e n r e', True, white)
        screen.blit(step2,(300, s_height/1.9))

        #step 3
        if a > 650 and a < 950 and b > (s_height/1.3) and b < (s_height/1.3)+60:
            pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],0)
            step3 = smallfont.render('G E N E R A T E   M Y   S O N G !', True, darkblue)
        else:
            pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],3)
            step3 = smallfont.render('G E N E R A T E   M Y   S O N G !', True, white)
        s3_rect = step3.get_rect(center=(s_width/2, s_height/1.24))
        screen.blit(step3,s3_rect)

        #geometric points
        make_shapes(screen)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                (a, b) = pygame.mouse.get_pos()
                if a>650 and b>610 and a<950 and b<680:
                # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(Title())
            back.check_clicked(events)

    def Render(self, screen):

        #create black screen
        screen.fill(darkgreen)

        #creating title
        title = bigfont.render('O U T P U T  S O N G', True, white)
        text_rect = title.get_rect(center=(s_width/2, s_height/4))
        screen.blit(title,text_rect)

        (a, b) = pygame.mouse.get_pos()
        if a > 650 and a < 950 and b > (s_height/1.3) and b < (s_height/1.3)+60:
            pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],0)
        else:
            pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],3)
        step3 = smallfont.render('B A C K  T O  M E N U !', True, white)
        s3_rect = step3.get_rect(center=(s_width/2, s_height/1.24))
        screen.blit(step3,s3_rect)

        make_shapes(screen)

        pygame.draw.rect(screen,white,[300, s_height/2.5,1000,200],3)
        out = smallfont.render('v i s u a l  o u t p u t  w i l l  g o  h e r e !', True, white)
        screen.blit(out,(650,s_height/2))

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
back = Button('Go Back', (300, 70), coords=(650,610))
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
