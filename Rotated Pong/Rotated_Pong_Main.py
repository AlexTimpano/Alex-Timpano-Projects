import pygame 
import sys
from classes import Paddle,Ball
import time
pygame.init()

WIN=pygame.display.set_mode((1500,800))
FPS=60
clock=pygame.time.Clock()

left_paddle_keys = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_q, pygame.K_e]
right_paddle_keys=[pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_RSHIFT,pygame.K_KP1]

left_paddle_box=pygame.Rect(5,5,630,790)
right_paddle_box=pygame.Rect(865,5,620,790)

left_paddle=Paddle(250,400,left_paddle_keys,left_paddle_box)
right_paddle=Paddle(1250,400,right_paddle_keys,right_paddle_box)

ball=Ball(750,400)

paddle_sprites=pygame.sprite.Group(left_paddle,right_paddle)
ball_sprite=pygame.sprite.GroupSingle(ball)

player1_score=0
player2_score=0

font=pygame.font.SysFont("Impact",50)

def draw_game_elements(WIN,paddles,ball,player1_score,player2_score):
    score1_rect=pygame.Rect(375,200,100,100)
    score2_rect=pygame.Rect(1125,200,100,100)
    score1_rect.center=(375,200)
    score2_rect.center=(1125,200)

    

    score1=font.render(str(player1_score),True,(255,255,255))
    score2=font.render(str(player2_score),True,(255,255,255))

    WIN.blit(score1,score1_rect)
    WIN.blit(score2,score2_rect)

    paddles.draw(WIN)
    ball.draw(WIN)



def winner(WIN,player1_score,player2_score):
    winner_text=""
    if player1_score==10:
        winner_text=font.render("Player 1 wins!",True,(255,255,255))
    elif player2_score==10:
        winner_text=font.render("Player 2 wins!",True,(255,255,255))

    if winner_text!="":
        victory_rect=pygame.Rect(750,400,100,100)
        victory_rect.center=(750,400)
        WIN.blit(winner_text,victory_rect)
        pygame.display.flip()
        
        



run=True
while run:
    clock.tick(FPS)
    black=pygame.Rect(0,0,1500,800)
    pygame.draw.rect(WIN,(0,0,0),black)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            sys.exit()

    winner_text=""
    if player1_score==10:
        winner_text=font.render("Player 1 wins!",True,(255,255,255))
    elif player2_score==10:
        winner_text=font.render("Player 2 wins!",True,(255,255,255))

    if winner_text!="":
        victory_rect=pygame.Rect(750,400,100,100)
        victory_rect.center=(750,400)
        WIN.blit(winner_text,victory_rect)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()
        
            

    
        

    left_paddle.update()
    right_paddle.update()
    player1_score,player2_score=ball.update(paddle_sprites,player1_score,player2_score)

    
    draw_game_elements(WIN,paddle_sprites,ball_sprite,player1_score,player2_score)
    
    pygame.display.flip()
    
