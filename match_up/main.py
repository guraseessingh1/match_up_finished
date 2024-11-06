import pygame

WIDTH = 600
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
screen.fill(WHITE)
pygame.display.update()
aresnal_image = pygame.image.load("images/arsenal.png")
aresnal_image = pygame.transform.scale(aresnal_image,(100,100))
chealsea_image  = pygame.image.load("images/chealsea.png")
chealsea_image = pygame.transform.scale(chealsea_image,(100,100))
liverpool_image = pygame.image.load("images/liverpool.png")
liverpool_image = pygame.transform.scale(liverpool_image,(100,100))
man_c_image = pygame.image.load("images/man_c.png")
man_c_image = pygame.transform.scale(man_c_image,(100,100))
man_u_image = pygame.image.load("images/man_u.png")
man_u_image = pygame.transform.scale(man_u_image,(100,100))

screen.blit(aresnal_image,(50,10))
screen.blit(chealsea_image,(50,120))
screen.blit(liverpool_image,(50,230))
screen.blit(man_c_image,(50,340))
screen.blit(man_u_image,(50,450))
pygame.display.update()

font = pygame.font.SysFont("comicsans",25)
text_1 = font.render("Liverpool",True,"black")
text_2 = font.render("Mancester united",True,"black")
text_3 = font.render("Mancester_city",True,"black")
text_4 = font.render("Chealsea",True,"black")
text_5 = font.render("Arsenal",True,"black")


screen.blit(text_1 ,(350,30))
screen.blit(text_2,(350,150))
screen.blit(text_3,(350,250))
screen.blit(text_4,(350,360))
screen.blit(text_5,(350,470))
pygame.display.update()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,"black",(pos),20,0)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.circle(screen,"black",(pos2),20,0)
        pygame.draw.line(screen,"black",(pos),(pos2),3)
        pygame.display.update()
