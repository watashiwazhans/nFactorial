import pygame
import math

lim = False

def main():
    pygame.init()

    #Display:
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Perfect Circle")

    #Fps:
    clock = pygame.time.Clock()
    FPS = 6000

    #Color:
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    GREEN = (0,255,0)

    #Variable:
    position = (0,0)
    ls = []
    time = 0
    slow = False
    global lim


    while True:
        pressed = pygame.mouse.get_pressed()
        if pressed[0] and lim == False:
            time += 1
            if time < 1000:
                ls += position,
            else:
                slow = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEMOTION:
                position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ls = []
                slow = False
                lim = False
            if event.type == pygame.MOUSEBUTTONUP:
                time = 0


        screen.fill(BLACK)

        pygame.draw.circle(screen, WHITE, (400,400), 5)
        if len(ls) > 2:
            score = calculate_percentage("self", ls)
            show_percentage("self", screen, WHITE, score, ls[0], slow, lim)
            draw('self', screen, ls, GREEN)


        pygame.display.update()

        clock.tick(FPS)

def show_percentage(self, screen, color, score, ls_0, slow, lim):
    Font = pygame.font.SysFont('times new roman', 30)
    if slow == False and lim == False:
        percentage = Font.render(str("{:.1f}".format(score)) + '%', True, color)
    elif slow == True:
        percentage = Font.render("XX.X" + '%', True, color)
        Toslow = Font.render("Too slow", True, color)
        screen.blit(Toslow, (360, 410))
    elif lim == True:
        percentage = Font.render("XX.X" + '%', True, color)
        Lim = Font.render("Draw a full circle", True, color)
        screen.blit(Lim, (360, 410))
    screen.blit(percentage, (370,360))

def calculate_percentage(self, ls):
    sum = 0
    ls_0 = math.sqrt((ls[0][0]-400)**2 + (ls[0][1]-400)**2)
    for x in ls:
        x = math.sqrt((x[0]-400)**2 + (x[1]-400)**2)
        if x < ls_0:
            sum += (x/ls_0 * 100)
        else:
            sum += (ls_0/x * 100)
    return sum/len(ls)

def draw(self, screen, ls, color):
    ls_0 = math.sqrt((ls[0][0]-400)**2 + (ls[0][1]-400)**2)
    f = ls[0]
    for x in ls:
        g = math.sqrt((x[0]-400)**2 + (x[1]-400)**2)
        if g > ls_0:
            g = int(g/ls_0*120)
        else:
            g = int(ls_0/g*120)
        if g<250:
            pygame.draw.line(screen, (0+g,255-g,0), f, x, 10)
        else:
            global lim
            lim = True
        
        f = x

main()