import os

import pygame

import Text
from button import Button
from functions import *
from menus import *
from building import Building
from shared_resources import *

#Maybe abusing import * here. Learn better solution.


#Establishes basic information like FPS and screen size
FPS=30

pygame.init
pygame.font.init()


WIDTH, HEIGHT = 900,500

WIN= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Amongst the Stars")

pygame_icon = LOG_ICON=pygame.image.load(os.path.join('Assets', 'logo.png'))
pygame.display.set_icon(pygame_icon)

BIG_FONT=init_sys_font('cascadiamonoregular',24)
#Text box constraints
textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

#Sets clock
clock=pygame.time.Clock()

#Loads fonts




#Loads images
UI_BASE=pygame.image.load(os.path.join('Assets', 'basebars.png'))
BUILD_ICON=pygame.image.load(os.path.join('Assets', 'buildicon.png'))
DESTROY_ICON=pygame.image.load(os.path.join('Assets', 'destroyicon.png'))
STATS_ICON=pygame.image.load(os.path.join('Assets', 'statsicon.png'))
LOG_ICON=pygame.image.load(os.path.join('Assets', 'logicon.png'))
NEXT_ICON=pygame.image.load(os.path.join('Assets', 'endday.png'))



MERCURY_SURFACE=pygame.image.load(os.path.join('Assets', 'mercurysurface.png'))
VENUS_SURFACE=pygame.image.load(os.path.join('Assets', 'venussurface.png'))
MOON_SURFACE=pygame.image.load(os.path.join('Assets', 'moonsurface.png'))
MARS_SURFACE=pygame.image.load(os.path.join('Assets', 'marssurface.png'))
EUROPA_SURFACE=pygame.image.load(os.path.join('Assets', 'europasurface.png'))
IO_SURFACE=pygame.image.load(os.path.join('Assets', 'iosurface.png'))
TITAN_SURFACE=pygame.image.load(os.path.join('Assets', 'titansurface.png'))


#Establishes buttons in class
BUILD_BUTTON=Button(815,113,BUILD_ICON)
DESTROY_BUTTON=Button(815,206,DESTROY_ICON)
STATS_BUTTON=Button(815,292,STATS_ICON)
END_BUTTON=Button(815,365,NEXT_ICON)



#Function to draw the main screen
def draw_screen(planet_surface,day,critical_list,non_critical_list):
    WIN.blit(planet_surface,(0,0))
    WIN.blit(UI_BASE,(0,0))
    
    MENU_FONT=init_sys_font('cascadiamonoregular',30)
    RESOURCE_FONT=init_sys_font('cascadiamonoregular',16)

    WIN.blit(MENU_FONT.render(f"Day:{day}",1,(0,0,0)),(400,17))
    WIN.blit(RESOURCE_FONT.render(f"Food:{critical_list[0]}   Water:{critical_list[1]}   O2:{critical_list[2]}", True, (0,0,0)), (3, 27))
    WIN.blit(RESOURCE_FONT.render(f"$:{non_critical_list[0]}  Mats:{non_critical_list[1]}  Power:{non_critical_list[2]}", True, (0,0,0)), (537, 27))



    


def loss_check(critical_list,population,loss_timer,run_var,day,past_day):
    
    if day!=past_day:
        if 0 in critical_list:
            loss_timer+=1
            
            
        else:
            loss_timer=0

        if loss_timer==5 or population==0:
            run_var=False

        past_day=day
    return loss_timer,run_var,past_day

#Contains actions for if main buttons pressed
def buttons(build_menu,destroy_menu,day,past_day,stats_menu):
    next=False

    if BUILD_BUTTON.draw(WIN):
        build_menu.visible=not build_menu.visible

    if DESTROY_BUTTON.draw(WIN):
        print("Good")
        destroy_menu.visible=not destroy_menu.visible
    
    if STATS_BUTTON.draw(WIN):
        stats_menu.visible=not stats_menu.visible
    

    if END_BUTTON.draw(WIN):
        next=True

    return next
        


#bonus_factors
'''List contains bonuses that will be applied to resource gain. 1 is a multiplier of 1
Bonuses are in order of food, water, oxygen,building materials,money,population,power'''




def intro(planet_surface,bonus_factors):
    
    #Loads intro-specific images
    #Faction logos
    INTRO_BACKGROUND=pygame.image.load(os.path.join('Assets', 'intro_background.png'))
    UTC_LOGO=pygame.image.load(os.path.join('Assets', 'Utopialogo.png'))
    AT_LOGO=pygame.image.load(os.path.join('Assets', 'ATlogo.png'))
    RF_LOGO=pygame.image.load(os.path.join('Assets', 'RFlogo.png'))
    NF_LOGO=pygame.image.load(os.path.join('Assets', 'NFlogo.png'))


    #Planet logos
    MERCURY_LOGO=pygame.image.load(os.path.join('Assets','mercury_logo.png'))
    VENUS_LOGO=pygame.image.load(os.path.join('Assets','Venus logo.png'))
    MARS_LOGO=pygame.image.load(os.path.join('Assets','mars_logo.png'))
    MOON_LOGO=pygame.image.load(os.path.join('Assets','moon_logo.png'))
    TITAN_LOGO=pygame.image.load(os.path.join('Assets','titan_logo.png'))
    EUROPA_LOGO=pygame.image.load(os.path.join('Assets','europa_logo.png'))

    #Buttons and things 
    #Faction buttons
    UTC_BUTTON=Button(125,200,UTC_LOGO)
    AT_BUTTON=Button(300,200,AT_LOGO)
    RF_BUTTON=Button(475,200,RF_LOGO)
    NF_BUTTON=Button(650,200,NF_LOGO)

    #Planet buttons

    MERCURY_BUTTON=Button(125,50,MERCURY_LOGO)
    VENUS_BUTTON=Button(300,50,VENUS_LOGO)
    MARS_BUTTON=Button(475,50,MARS_LOGO)
    MOON_BUTTON=Button(650,50,MOON_LOGO)
    TITAN_BUTTON=Button(125,300,TITAN_LOGO)
    EUROPA_BUTTON=Button(300,300,EUROPA_LOGO)
    

    BACK_ICON=pygame.image.load(os.path.join('Assets', 'back.png'))
    BACK_BUTTON=Button(5,4,BACK_ICON)

    CONFIRM_ICON=pygame.image.load(os.path.join('Assets', 'confirm.png'))
    CONFIRM_BUTTON=Button(WIDTH-5-(CONFIRM_ICON.get_width()),4,CONFIRM_ICON)

    WIN.blit(INTRO_BACKGROUND,(0,0))
    pygame.display.update()

    
    

    #Loads text_box area constraint
    intro_text_box=pygame.Rect(89,45,776,418)


    #Draws text within text box. Text is intro lore
    drawText(WIN, Text.INTRO_LORE, (255,255,255), intro_text_box, BIG_FONT, align=textAlignCenter, aa=False, bkg=None)
    pygame.display.update()

    #Faction select screen.
    
    intro_desc_font=init_sys_font('cascadiamonoregular',20)
    intro_select_font=init_sys_font('cascadiamonoregular',16)

    WIN.blit(INTRO_BACKGROUND,(0,0))
    pygame.display.update()


    #Text constraint boxes
    lore_box=pygame.Rect(51,188,500,301)
    bonuses_box=pygame.Rect(553,188,250,300)


    
    
    
    
    #Will keep bringing up factions until one is selected
    selected=False
    while selected==False:
        WIN.blit(INTRO_BACKGROUND,(0,0))
        WIN.blit(intro_select_font.render(Text.UTC_NAME,1,(255,255,255)),(140,150))
        WIN.blit(intro_select_font.render(Text.AT_NAME,1,(255,255,255)),(315,150))
        WIN.blit(intro_select_font.render(Text.RF_NAME,1,(255,255,255)),(450,150))
        WIN.blit(intro_select_font.render(Text.NF_NAME,1,(255,255,255)),(665,150))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.QUIT

        #Checks if the faction icons are clicked. 
        if UTC_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(UTC_LOGO,(WIDTH//2-(UTC_LOGO.get_width()//2),50))
            drawText(WIN, Text.UTC_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.UTC_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonus_factors[:]=[1,1,1,1,1.15,0.9,1.05]
                    back=True
                    selected=True

                pygame.display.update()
                
            

            
        

        if AT_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(AT_LOGO,(WIDTH//2-(AT_LOGO.get_width()//2),50))
            drawText(WIN, Text.AT_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.AT_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    back=True
                    selected=True
                

                pygame.display.update()
                
        

        if RF_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(RF_LOGO,(WIDTH//2-(RF_LOGO.get_width()//2),50))
            drawText(WIN, Text.RF_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.RF_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonus_factors[:]=[1,1.15,1,1,0.9,1.05,1]
                    back=True
                    selected=True
                    

                pygame.display.update()
        

        if NF_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(NF_LOGO,(WIDTH//2-(AT_LOGO.get_width()//2),50))
            drawText(WIN, Text.NF_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.NF_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonus_factors[:]=[1,1,1,1.05,1,1.15,0.9]
                    back=True
                    selected=True
          

                pygame.display.update()
    
        pygame.display.update()

    selected=False 
  
    while selected==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.QUIT

        WIN.blit(INTRO_BACKGROUND,(0,0))
        WIN.blit(intro_select_font.render(Text.MERCURY_NAME,1,(255,255,255)),(160,30))
        WIN.blit(intro_select_font.render(Text.VENUS_NAME,1,(255,255,255)),(345,30))
        WIN.blit(intro_select_font.render(Text.MARS_NAME,1,(255,255,255)),(525,30))
        WIN.blit(intro_select_font.render(Text.MOON_NAME,1,(255,255,255)),(700,30))
        WIN.blit(intro_select_font.render(Text.TITAN_NAME,1,(255,255,255)),(160,280))
        WIN.blit(intro_select_font.render(Text.EUROPA_NAME,1,(255,255,255)),(345,280))

        if MERCURY_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(MERCURY_LOGO,(WIDTH//2-(MERCURY_LOGO.get_width()//2),50))
            drawText(WIN, Text.MERCURY_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.MERCURY_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonuses=[0,0,0,0,0,-0.1,0.1]
                    bonus_factors[:]=add_lists(bonus_factors,bonuses)
                    planet_surface=MERCURY_SURFACE
                    back=True
                    selected=True
                    

                pygame.display.update()

        if VENUS_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(VENUS_LOGO,(WIDTH//2-(VENUS_LOGO.get_width()//2),50))
            drawText(WIN, Text.VENUS_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.VENUS_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonuses=[0,-0.1,0.1,0,0,0,0]
                    bonus_factors[:]=add_lists(bonus_factors,bonuses)
                    planet_surface=VENUS_SURFACE
                    back=True
                    selected=True
                    

                pygame.display.update()
        
        if MARS_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(MARS_LOGO,(WIDTH//2-(MARS_LOGO.get_width()//2),50))
            drawText(WIN, Text.MARS_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.MARS_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonuses=[0,0,0,0,0,0.1,-0.1]
                    bonus_factors[:]=add_lists(bonus_factors,bonuses)
                    planet_surface=MARS_SURFACE
                    back=True
                    selected=True
                    

                pygame.display.update()

        if MOON_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(MOON_LOGO,(WIDTH//2-(MOON_LOGO.get_width()//2),50))
            drawText(WIN, Text.MOON_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.MOON_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonuses=[-0.1,0,0,0,0.1,0,0]
                    bonus_factors[:]=add_lists(bonus_factors,bonuses)
                    planet_surface=MOON_SURFACE
                    back=True
                    selected=True
                    

                pygame.display.update()

        if TITAN_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(TITAN_LOGO,(WIDTH//2-(MOON_LOGO.get_width()//2),50))
            drawText(WIN, Text.TITAN_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.TITAN_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonuses=[0,0,-0.1,+0.1,0,0,0]
                    bonus_factors[:]=add_lists(bonus_factors,bonuses)
                    planet_surface=TITAN_SURFACE
                    back=True
                    selected=True
                    

                pygame.display.update()
        if EUROPA_BUTTON.draw(WIN):
            WIN.blit(INTRO_BACKGROUND,(0,0))
            WIN.blit(EUROPA_LOGO,(WIDTH//2-(EUROPA_LOGO.get_width()//2),50))
            drawText(WIN, Text.EUROPA_LORE, (255,255,255), lore_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            drawText(WIN, Text.EUROPA_BONUSES, (255,255,255), bonuses_box, intro_desc_font, align=textAlignLeft, aa=False, bkg=None)
            pygame.display.update()
            back=False

            #Will hold this screen until back is selected or faction is confirmed
            while back==False:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.QUIT

                if BACK_BUTTON.draw(WIN):
                    back=True

                if CONFIRM_BUTTON.draw(WIN):
                    bonuses=[0,+0.1,0,-0.1,0,0,0]
                    bonus_factors[:]=add_lists(bonus_factors,bonuses)
                    planet_surface=EUROPA_SURFACE
                    back=True
                    selected=True
                    

                pygame.display.update()

        pygame.display.update()

    pygame.display.update()

    return planet_surface
    
    
#Establishes menus for construction, deconstruction, stats, and the log  







#The main loop


def main(production_queue,buildings_list,bonus_factors,day,critical_list,non_critical_list,population):
    run=True
    clock=pygame.time.Clock()
    
    #Time until game over
    loss_timer=0
    
    past_day=None
    
    planet_surface=None

    build_menu=BuildMenu()
    destroy_menu=DestroyMenu()
    stats_menu=Stats_Menu()
    

    
    planet_surface=intro(planet_surface,bonus_factors)

    while run:
        clock.tick(FPS)
        mouse_pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.QUIT

        

        
        draw_screen(planet_surface,day,critical_list,non_critical_list)
        build_menu.draw(WIN)
        destroy_menu.draw(WIN)
        stats_menu.draw(WIN,buildings_list,production_queue)
        next=buttons(build_menu,destroy_menu,day,past_day,stats_menu)
        
        if next:
            day,population,buildings_list=next_day(production_queue,buildings_list,bonus_factors,day,critical_list,non_critical_list,population)
            print(day,non_critical_list,critical_list,non_critical_list,population)
            print("time",loss_timer)
            print(buildings_list)

        loss_timer,run,past_day=loss_check(critical_list,population,loss_timer,run,day,past_day)
        

    
        pygame.display.update()
        
if __name__ == "__main__":
    main(production_queue,buildings_list,bonus_factors,1,critical_list,non_critical_list,population)
