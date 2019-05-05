import pygame
import random as rd
from pygame.locals import *
from sys import exit
from testingmusic21_2 import *
#input_text= ''
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
notesize = 10
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
    #pygame.draw.lines(screen,white,False,make_geo(x,y,width,height), 5)
    pygame.draw.ellipse(screen, white,(x, y, height/2, width/2), 5)
    pygame.draw.line(screen, white, [x+120, y+50], [x+120, y-150], 5)

def make_shapes(screen):
    #draw_geo(50,900,200,250,screen)
    #draw_geo(s_width-250,900,200,250,screen)
    draw_geo(50,250,200,250,screen)
    draw_geo(s_width-250,250,200,250,screen)
    draw_geo(50,600,200,250,screen)
    draw_geo(s_width-250,600,200,250,screen)

def music_note(screen):
    pygame.draw.ellipse(screen, white,[5, 5, 5, 5], 5)

def make_piano(screen):
    key_w = 75
    key_l = 200
    xi = 275
    key_y = s_height/2.5
    for x in range(xi,xi+(key_w*14),key_w):
        pygame.draw.rect(screen,white,[x, key_y,key_w,key_l],0)
        pygame.draw.rect(screen,grey,[x, key_y,key_w,key_l],2)

    for x in range(int(xi+(key_w/1.5)),int(xi+(key_w*3)-(key_w/2)),key_w):
        pygame.draw.rect(screen,black,[x,key_y,key_w/1.5, key_l/1.5])

    for x in range(int(xi+(key_w*7)+(key_w/1.5)),int(xi+(key_w*10)-(key_w/1.5)),key_w):
        pygame.draw.rect(screen,black,[x,key_y,key_w/1.5, key_l/1.5])

    for x in range(int(xi+(key_w*3)+(key_w/1.5)),int(xi+(key_w*7)-(key_w/1.5)),key_w):
        pygame.draw.rect(screen,black,[x,key_y,key_w/1.5, key_l/1.5])

    for x in range(int(xi+(key_w*10)+(key_w/1.5)),int(xi+(key_w*14)-(key_w/1.5)),key_w):
        pygame.draw.rect(screen,black,[x,key_y,key_w/1.5, key_l/1.5])

def title_desc(screen):
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

def step1(screen, input_box):
    input_box.update()
    input_box.draw(screen)
    step1 = smallfont.render('S T E P  1 : i n p u t  a  l y r i c', True, white)
    screen.blit(step1,(300,s_height/2.8))

def step2(a,b,screen):
    ran = list(range(300, s_width-300, 212))

    for x in range(0,len(g_list)):
        genre = medfont.render(g_list[x], True, white)
        genre_rect = genre.get_rect(center=(ran[x]+75, s_height/1.64))
        screen.blit(genre,genre_rect)

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

def step3(a,b,screen):
        #step 3
    if a > 650 and a < 950 and b > (s_height/1.3) and b < (s_height/1.3)+60:
        pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],0)
        step3 = smallfont.render('G E N E R A T E   M Y   S O N G !', True, darkblue)
    else:
        pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],3)
        step3 = smallfont.render('G E N E R A T E   M Y   S O N G !', True, white)
    s3_rect = step3.get_rect(center=(s_width/2, s_height/1.24))
    screen.blit(step3,s3_rect)

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

class Note:
    '''
    Class to keep track of a note's location + vector
    '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

def make_note():
    '''
    function to make moving notes for background
    '''
    note = Note()
    note.x = rd.randrange(notesize, s_width-notesize)
    note.y = rd.randrange(notesize, s_height-notesize)
    note.dx = rd.choice([0.5, -0.5])
    note.dy = rd.choice([0.5, -0.5])
    note.color = white

    return note

class Scene():
    """
    initiating generic Scene class
    """
    def __init__(self):
        self.next = self
        self.Buttons= []
        self.generate_music = False
        #self.lyric = glyrics

    def render(self, screen):
        """
        The Scene renders its background and all the Buttons in it.
        """
        # print("Drawing scene {}".format(self.imgname))
        screen.fill(self.color)

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
        jazz.check_clicked(events)
        rb.check_clicked(events)
        pop.check_clicked(events)
        rock.check_clicked(events)
        random.check_clicked(events)
        generate.check_clicked(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (a, b) = pygame.mouse.get_pos()
                if a>650 and b>610 and a<950 and b<680:
                # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(Output())

    def Render(self, screen, input_box):

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

        step1(screen, input_box)
        step2(a,b,screen)
        step3(a,b,screen)
        #geometric points
        make_shapes(screen)


class Output(Scene):
    '''
    Creating Scene subclass for output scene
    '''
    def __init__(self):
        Scene.__init__(self)
        self.generate_music = True

    def Update(self):
        if self.generate_music == True:
            self.new_song = generate_song(input_text, genre_buttons)
            play_song(self.new_song)
            self.generate_music = False

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (a, b) = pygame.mouse.get_pos()
                if a>650 and b>610 and a<950 and b<680:
                # Move to the next scene when the user pressed Enter
                    # Resets all the buttons and the input text
                    global input_text
                    input_text = ''
                    for button in genre_buttons.values():
                        button.clicked = False
                    self.SwitchToScene(Title())
                elif a>650 and a<950 and b>80 and b<150:
                    show_song(self.new_song)

            back.check_clicked(events)


    def Render(self, screen, input_box=None):
        note_list = []

        for i in range(rd.randrange(2,10)):
            note = make_note()
            note_list.append(note)

        for note in note_list:
            note.x += note.dx
            note.y += note.dy

            if note.y > s_height-notesize or note.y < notesize:
                note.dy *= -0.5

            if note.x < s_width-notesize or note.x < notesize:
                note.dx *= -0.5

        #create black screen
        screen.fill(darkgreen)

        #ncreate moving notes
        for note in note_list:
            pygame.draw.ellipse(screen, note.color,[note.x, note.y, 25, 25], 0)
            pygame.draw.line(screen, note.color,(note.x+20,note.y+10),(note.x+20,note.y-50),5)

        #creating title

        title = smallfont.render(input_text, True, white)
        text_rect = title.get_rect(center=(s_width/2, s_height/4))
        screen.blit(title,text_rect)

        (a, b) = pygame.mouse.get_pos()
        if a > 650 and a < 950 and b > (s_height/1.3) and b < (s_height/1.3)+60:
            pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],0)
            step3 = smallfont.render('B A C K  T O  M E N U !', True, darkgreen)
        else:
            pygame.draw.rect(screen,white,[650, s_height/1.3,300,60],3)
            step3 = smallfont.render('B A C K  T O  M E N U !', True, white)
        s3_rect = step3.get_rect(center=(s_width/2, s_height/1.24))
        screen.blit(step3,s3_rect)

        if a>650 and a<950 and b > (s_height/9) and b < (s_height/9)+60:
            pygame.draw.rect(screen,white,[650, s_height/9,300,60],0)
            step4 = smallfont.render('C L I C K  F O R  S H E E T  M U S I C !', True, darkgreen)
        else:
            pygame.draw.rect(screen,white,[650, s_height/9,300,60],3)
            step4 = smallfont.render('C L I C K  F O R  S H E E T  M U S I C !', True, white)
        s4_rect = step4.get_rect(center=(s_width/2, s_height/6.9))
        screen.blit(step4,s4_rect)

        make_piano(screen)
        make_shapes(screen)


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
        self.clicked = False

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
                    self.clickedAction(events)
                    self.clicked = True
        return self.clicked

    def render(self, screen):
        """TODO: RENDER ITEMS"""

    def clickedAction(self, events):
        """This is a default click action so we know that the method works"""
        print("The {} button was clicked!".format(self.imgname))



class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = white
        self.text = text
        self.txt_surface = medfont.render(text, True, white)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = grey if self.active else white
        if event.type == pygame.KEYDOWN:
            if self.active:
                #if event.key == pygame.K_RETURN:
                #    global input_text
                #    input_text = self.text
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = medfont.render(self.text, True, white)

    def update(self):
        # Resize the box if the text is too long.
        global input_text
        input_text = self.text

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

"""Create buttons for each genre, and to generate the song."""
   #TODO: Change the clicked action according to button.
jazz = Button('Jazz', (150, 70), coords=(300,450))
rb = Button('R&B', (150, 70), coords=(512,450))
pop = Button('Pop', (150, 70), coords=(724,450))
rock = Button('Rock', (150, 70), coords=(936,450))
random = Button('Random Genre', (150, 70), coords=(1148,450))
generate = Button('Generate Music', (300, 70), coords=(650,610))
back = Button('Go Back', (300, 70), coords=(650,610))
sheetmusic = Button('Sheet Music', (300, 70), coords=(650, 80))
genre_buttons = {'jazz':jazz, 'rb':rb, 'pop':pop, 'rock':rock, 'random':random}
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
    input_box = InputBox(300, s_height/2.5,1000,60)
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

            input_box.handle_event(event)

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Render(screen, input_box)
        active_scene.Update()

        active_scene = active_scene.next
        pygame.display.flip()
        clock.tick(fps)



if __name__ == '__main__':
    main(60, Title())
