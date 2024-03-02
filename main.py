#Підключення бібліотек
import pygame 


import random
#активування  бібліотеки
pygame.init()

#Встановлення рамок гри
window = pygame.display.set_mode((600,600))

#window.fill(back)
clock=pygame.time.Clock()

# Кольори
FON = (200, 255, 255)     
RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)

#window.fill((FON))

# Клас для створеня прямокутників
class Area():
    def __init__(self,x=0,y=0,width=200,height=100,rect_color=FON):
        self.rect= pygame.Rect(x,y,width,height)
        self.color= rect_color

    def set_color(self,new_color):
        self.color = new_color

    def fill (self):
        pygame.draw.rect(window,self.color,self.rect)

    def outline(self,frame_color,thickness):
        pygame.draw.rect(window,frame_color,self.rect,thickness)

    def collidepoint(self,x,y):
       return self.rect.collidepoint(x,y)

    def colliderect(self,rect):
        return self.rect.colliderect(rect)
#Під-клас для малюваня прямокутника з текстом і без тексту 
class Label(Area):
#Функція для заносиння таксту в прямокутника 
    def set_text(self,text,fsize =12,text_color=(0,0,0)):
        self.text = text
        self.image= pygame.font.Font(None, fsize).render(text,True, text_color)
    
    def draw(self,shift_x,shift_y):
        self.fill()
        window.blit(self.image,(self.rect.x + shift_x, self.rect.y + shift_y))
#Під-клас для малювання прямокутника з картинкою
class Picture(Area):
    def __init__(self,filename,x=0,y=0,width=200,height=100,color=FON):
        super().__init__(x,y,width,height,color)
        self.image=pygame.image.load(filename)

    def draw(self):
        #self.fill()
        window.blit(self.image,(self.rect.x , self.rect.y))




walls = []

appls = []

cords = []

for i in range(0, 500, 70):
    for j in range(0,500,70):
        cords.append([i,j])

cords_now = random.choice(cords)
snakee = Picture('head_right.png',cords_now[0],cords_now[1] ,25,25)
cords.remove(cords_now)

for i in range(6):
    cords_now = random.choice(cords)
    appls.append(Picture('apple1.png', cords_now[0],cords_now[1],30,25))
    cords.remove(cords_now)

for i in range(6):
    cords_now = random.choice(cords)
    walls.append(Picture('wall.png',cords_now[0],cords_now[1],30,30))
    cords.remove(cords_now)

snake_size = 1 

snake_img=['head_right.png','body_horizontal.png','tail_left.png',]
snake_img.reverse()
#print(snake_img)
snake=[]



#створення мняча 
#ball= Picture("ball.png",160,200,70,50,FON)

#створення платформи 
#platforma_x=200
#platforma_y=330
#platforma= Picture("platform.png",platforma_x,platforma_y,100,25,FON)

#Зміні для полекшеня роботи 
#start_x=5
#start_y=5
#count=9
#monsters=[]
#speed=25
#SIZE=25
dx, dy = 0 , 0

#move_right=False
#move_left=False
#створеня 24 монстрів добавляння їх в список і ростановка їх по місьцях 
#for j in range (0,3):
#    x= start_x + (27.5*j)
#    y=start_y + (55*j)
#    for i in range(0,count):
#        enemy=Picture("enemy.png",x,y,50,50,FON)
#        monsters.append(enemy)
#        x=x+55
#    count=count-1



#Ігровий цикл

game_over = False
while not game_over:

    window.fill((FON))

    #Замальовівання фону в мняча і платформи
    #    ball.fill()
    #    platforma.fill()
    #    window.fill(back)

    #snakee.rect.x += dx * SIZE 
    #snakee.rect.y += dy * SIZE 

    
    if len(snake) > snake_size:
        del snake [0]
        
    for i in range(len(snake)):
        snake[i].image = pygame.image.load(snake_img[i])
        snake[i].draw()

    for apple in appls:
        apple.fill()
        apple.draw()
        if apple.colliderect(snakee.rect):
            apple.fill()
            snake_size += 1
            appls.remove(apple)
        

    for stina in walls :
        stina.fill()
        stina.draw()
        if stina.colliderect(snakee.rect):
            time_text = Label(150,150,0,0,FON)
            time_text.set_text('YOU LOSE',60,(255,0,0))
            time_text.draw(10,10)
            game_over = True
    
    
        
    #Привязуваня платформи до клавіші вправо і ліво, вверх і вниз
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True 

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        dx,dy = 0 , -1

    if key[pygame.K_s]:
        dx , dy = 0 , 1

    if key[pygame.K_a]:
        dx , dy = -1 , 0

    if key[pygame.K_d]:
        dx , dy = 1 , 0 
        
    

    #            if event.key ==pygame.K_RIGHT:
    #                move_right=True
    #
    #            if event.key == pygame.K_LEFT:
    #                move_left=True

    #        if event.type == pygame.KEYUP:
    #            if event.key == pygame.K_RIGHT:
    #                move_right=False
    #
    #            if event.key == pygame.K_LEFT:
    #                move_left=False
    # Руханя платформи вправо здопогою клавіші право
    #    if move_right :
    #        platforma.rect.x += 3
    # Руханя платформи вліво здопогою клавіші ліво
    #    if move_left:
    #        platforma.rect.x -=3
    #Руханя м'яча по траєкторії
    #    ball.rect.x +=dx

    #    ball.rect.y +=dy
    #Відбивання м'яча від платформи і змінення траєкторіЇ м'яча
    #    if ball.rect.colliderect(platforma.rect):
    #        dy *= -1  #dy = dy * -1
    #Відбивання м'яча від потолку і боків екрану  гри 
    #if ball.rect.x > 450 or ball.rect.x < 0:
        #    dx *= 0

        #if ball.rect.y < 0:
        #    dy *= 0
        

    #Малювання монстрів
    #    for enemy in monsters:
    #        enemy.draw()
    #Видалення монстрів коли м'яч їх доторкнувся
    #        if enemy.rect.colliderect(ball.rect):
    #            monsters.remove(enemy)
    #            enemy.fill()
    #            dy *= -1

    #Екран виграшу
    if len(appls) == 0:
        time_text=Label(150,150,50,50,FON)
        time_text.set_text("YOU WIN",60,(0,200,0))
        time_text.draw(10,10)
        game_over = True

    #Малювання  м'яча
    #    ball.draw()
    #Малювання платформи
    #    platforma.draw()
    #Екран програшу
    #    if ball.rect.y > 400 or ball.rect.y == 400:
    #        window_end=Label(0,0,0,0,FON)
    #        window_end.set_text("YOU LOSE",60,(200,0,0))
    #        window_end.draw(160,200)
    #        break

    #Обновлення екрану
    
    pygame.display.update()
    #Частота кадрів
    clock.tick(1)
    