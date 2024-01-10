import pygame

run1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("pixil-frame-0.png"),(160,70)),True,False)
run2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("pixil-frame-0(1).png"),(160,70)),True,False)
back = pygame.transform.scale(pygame.image.load("background.png"),(5000,500))
guy = run1
runcount = 0
pygame.init()
screen = pygame.display.set_mode([500, 500])
y = 305
x = 0
counter = 0
jump = False
while True:
    x -= 3
    runcount += 1
    if runcount == 80:
        runcount = 0 
        if guy == run1:
            guy = run2
        elif guy == run2:
            guy = run1
    print(jump)
    if y != 305 and jump == False:
        y += 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if jump != True:
                if event.key == pygame.K_UP:
                    jump = True
    
    if jump == True:
        counter += 1
        y -= 5
        if counter == 20:
            jump = False
            counter = 0

    screen.fill((255, 255, 255))
    screen.blit(back,(x,0))
    screen.blit(guy,(100,y))
    pygame.display.flip()
