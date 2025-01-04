import pygame 
from pygame.math import Vector2
import random
import math
import sys

pygame.init()
screen_info = pygame.display.Info()

# Set the window size to match the screen size
screen_width, screen_height = screen_info.current_w, screen_info.current_h
window_size = (screen_width, screen_height)
WIN = pygame.display.set_mode(window_size)

#Establishes the paddles 
paddle1_rect=pygame.Rect(screen_width//7,screen_height//7,screen_width//30,screen_height//3)
paddle2_rect=pygame.Rect(screen_width-paddle1_rect.x,screen_height//7,screen_width//30,screen_height//3)

paddle1_rect.center=(paddle1_rect.x,screen_height//2)
paddle2_rect.center=(paddle2_rect.x,screen_height//2)

#Establishes the ball and its movement properties 
BALL_RECT=pygame.Rect(0,0,paddle1_rect.width//2,paddle1_rect.width//2)
BALL_RECT.center=(screen_width//2,screen_height//2)
#ball_vel=Vector2(random.randint(1,3),random.randint(1,3))
random_number = random.choice([random.randint(-5, -3), random.randint(3, 5)])
random_number2 = random.choice([random.randint(-5, -3), random.randint(3, 5)])
ball_vel=Vector2(random_number,random_number2)


#Establishes the score
player1_score=0
player2_score=0

#Establishes clock and FPS
FPS=60
clock=pygame.time.Clock()


run=True

#Function to handle paddle movement through keyboard input
def paddle_handle_movement(keys_pressed,left,right):
    if keys_pressed[pygame.K_w] and left.top>0:
        left.y-=5
    if keys_pressed[pygame.K_s] and left.bottom<screen_height:
        left.y+=5

    if keys_pressed[pygame.K_UP] and right.top>0:
        right.y-=5
    if keys_pressed[pygame.K_DOWN] and right.bottom<screen_height:
        right.y+=5

#Function to deal with a goal score scenario
def scored(ball,player1_score,player2_score,screen_width,screen_height):
    global ball_vel
    #New random velocity)
    random_number = random.choice([random.randint(-5, -3), random.randint(3, 5)])
    random_number2 = random.choice([random.randint(-5, -3), random.randint(3, 5)])
    
    #If player2 scores on player 1(Right to left)
    if ball.left<=0:
        ball.center=(screen_width//2,screen_height//2)
        player2_score+=1
        ball_vel=Vector2(random_number,random_number2)
    #If player1 scores on player2(left to right)
    if ball.right>=screen_width:
        ball.center=(screen_width//2,screen_height//2)
        player1_score+=1
        ball_vel=Vector2(random_number,random_number2)

    

    

    return player1_score,player2_score

def ball_handle_movement(ball,paddle1,paddle2):
    ball.move_ip(ball_vel)
    norm=Vector2(1,0)
    passed=(ball.left<paddle1.right-abs(ball_vel.x)) or (ball.right>paddle2.left+abs(ball_vel.x))
    if (ball.colliderect(paddle1) or ball.colliderect(paddle2)):
        paddle_rect = paddle1 if ball.colliderect(paddle1) else paddle2
        if not passed:

            # Compute the collision angle
            offset = ball.centery - paddle_rect.centery
            normalized_offset = offset / (paddle_rect.height / 2)
            collision_angle = normalized_offset * (math.pi / 3)

            # Reflect the velocity vector
            norm = Vector2(1, 0)
            ball_vel.reflect_ip(norm.rotate(collision_angle))
        else:
            #A real terrible solution but it works 
            if paddle_rect==paddle1:
                if paddle_rect.bottom-6<=ball.top<=paddle_rect.bottom:
                    new_coords=list(paddle_rect.bottomright)
                    new_coords[0]+=1
                    ball.topleft=tuple(new_coords)
                elif paddle_rect.top<=ball.bottom<=paddle_rect.top+6:
                    new_coords=list(paddle_rect.topright)
                    new_coords[0]+=1
                    ball.bottomleft=tuple(new_coords)
            else:
                if paddle_rect.bottom-6<=ball.top<=paddle_rect.bottom:
                    new_coords=list(paddle_rect.bottomleft)
                    new_coords[0]-=1
                    ball.topright=tuple(new_coords)
                elif paddle_rect.top<=ball.bottom<=paddle_rect.top+6:
                    new_coords=list(paddle_rect.topleft)
                    new_coords[0]-=1
                    ball.bottomright=tuple(new_coords)
        
    
    if ball.top < 0:
        ball_vel.reflect_ip(Vector2(0, 1))
    if ball.bottom > screen_height:
        ball_vel.reflect_ip(Vector2(0, -1))
    
    
    
    

    
def draw_game_elements(win, paddle1_rect, paddle2_rect, ball_rect, score1, score2):
    font = pygame.font.SysFont("Impact", 50)
    score1_text = font.render(str(score1), True, (255, 255, 255))
    score2_text = font.render(str(score2), True, (255, 255, 255))
    
    score1_rect = score1_text.get_rect()
    score1_rect.center = (win.get_width()//4, 50)
    
    score2_rect = score2_text.get_rect()
    score2_rect.center = (win.get_width() - win.get_width()//4, 50)
    
    pygame.draw.rect(win, (255, 255, 255), paddle1_rect)
    pygame.draw.rect(win, (255, 255, 255), paddle2_rect)
    pygame.draw.rect(win, (255, 255, 255), ball_rect)
    win.blit(score1_text, score1_rect)
    win.blit(score2_text, score2_rect)
        

run=True
while run:
    clock.tick(FPS)
    black=pygame.Rect(0,0,screen_width,screen_height)
    pygame.draw.rect(WIN,(0,0,0),black)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            

    keys_pressed=pygame.key.get_pressed()

    paddle_handle_movement(keys_pressed,paddle1_rect,paddle2_rect)
    ball_handle_movement(BALL_RECT,paddle1_rect,paddle2_rect)
    player1_score,player2_score=scored(BALL_RECT,player1_score,player2_score,screen_width,screen_height)

    draw_game_elements(WIN, paddle1_rect, paddle2_rect, BALL_RECT,player1_score,player2_score)
    pygame.display.flip()

    if player1_score==10 or player2_score==10:
        pygame.quit()
        sys.exit()
                


    