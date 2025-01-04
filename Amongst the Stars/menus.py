import pygame
pygame.init
pygame.font.init()

from building import *
import os
from button import Button
from functions import init_sys_font,to_sublists,str_object_list
from shared_resources import *

MENU_BACKGROUND=pygame.image.load(os.path.join('Assets', 'Infobox.png'))
MENU_FONT=init_sys_font('cascadiamonoregular',16)
CONFIRM_ICON=pygame.image.load(os.path.join('Assets', 'confirm.png'))
CONFIRM_ICON=pygame.transform.scale(CONFIRM_ICON,(25,25))

BACK_ICON=pygame.image.load(os.path.join('Assets', 'back.png'))
BACK_ICON=pygame.transform.scale(BACK_ICON,(25,25))




class BuildMenu():
    
    def __init__(self):
        self.image = MENU_BACKGROUND
        self.visible = False

        self.buttons = [
            Button(607, 138, CONFIRM_ICON),
            Button(607, 182, CONFIRM_ICON),
            Button(607, 215, CONFIRM_ICON),
            Button(607,250,CONFIRM_ICON),
            Button(607,292,CONFIRM_ICON),
            Button(607,333,CONFIRM_ICON),
            Button(607,368,CONFIRM_ICON)
            # add more buttons here as needed
        ]

    def draw(self, surface):
        if not self.visible:
            return
    
        surface.blit(self.image, (0,0))
        surface.blit(MENU_FONT.render(f"Building   Production   Cost   Build time   Maintenance   Power",1,(0,0,0)),(41,99))
        surface.blit(MENU_FONT.render(f"Farm        {round(100*bonus_factors[0],2)}       100     5 days         10         50",1,(0,0,0)),(59,148))
        surface.blit(MENU_FONT.render(f"Ice Mine    {round(100*bonus_factors[1],2)}        100     5 days         10         50",1,(0,0,0)),(42,188))
        surface.blit(MENU_FONT.render(f"Molecule splitter {round(100*bonus_factors[2],2)}        100     5 days         10         50",1,(0,0,0)),(6,221))
        surface.blit(MENU_FONT.render(f"Factory       {round(100*bonus_factors[3],2)}         100     5 days         10         50",1,(0,0,0)),(43,261))
        surface.blit(MENU_FONT.render(f"Bank        {round(100*bonus_factors[4],2)}        100     5 days         10         50",1,(0,0,0)),(57,302))
        surface.blit(MENU_FONT.render(f"Power Plant    {round(100*bonus_factors[5],2)}        100     5 days         10         50",1,(0,0,0)),(30,342))
        surface.blit(MENU_FONT.render(f"Habitat      {round(10*bonus_factors[6],2)}        100     5              10         50 ",1,(0,0,0)),(45,375))

        for button in self.buttons:
            if button.draw(surface):
                # update the state of the game based on which button was clicked
                if button == self.buttons[0]:
                    constructing=construct(production_queue,non_critical_list,"FARM",bonus_factors)
                elif button == self.buttons[1]:
                    constructing=construct(production_queue,non_critical_list,"ICE MINE",bonus_factors)
                elif button==self.buttons[2]:
                    constructing=construct(production_queue,non_critical_list,"MOLECULE SPLITTER",bonus_factors)
                elif button==self.buttons[3]:
                    constructing=construct(production_queue,non_critical_list,"FACTORY",bonus_factors)
                elif button==self.buttons[4]:
                    constructing=construct(production_queue,non_critical_list,"BANK",bonus_factors)
                elif button==self.buttons[5]:
                    constructing=construct(production_queue,non_critical_list,"POWER PLANT",bonus_factors)
                elif button==self.buttons[6]:
                    constructing=construct(production_queue,non_critical_list,"HABITAT",bonus_factors)
                # add more conditions here as needed


class DestroyMenu():
    
    def __init__(self):
        self.image = MENU_BACKGROUND
        self.visible = False

        self.buttons = [
            Button(607, 138, CONFIRM_ICON),
            Button(607, 182, CONFIRM_ICON),
            Button(607, 215, CONFIRM_ICON),
            Button(607,250,CONFIRM_ICON),
            Button(607,292,CONFIRM_ICON),
            Button(607,333,CONFIRM_ICON),
            Button(607,368,CONFIRM_ICON)
            # add more buttons here as needed
        ]

    def draw(self, surface):
        if not self.visible:
            return
        
        """TODO: Implement special refund pricing"""
    
        surface.blit(self.image, (0,0))
        surface.blit(MENU_FONT.render(f"Building   Mats refund   Cost   Build time   Maintenance   Power",1,(0,0,0)),(41,99))
        surface.blit(MENU_FONT.render(f"Farm        {round(50*bonus_factors[0],2)}       100     5 days         10         50",1,(0,0,0)),(59,148))
        surface.blit(MENU_FONT.render(f"Ice Mine    {round(50*bonus_factors[1],2)}        100     5 days         10         50",1,(0,0,0)),(42,188))
        surface.blit(MENU_FONT.render(f"Molecule splitter {round(50*bonus_factors[2],2)}        100     5 days         10         50",1,(0,0,0)),(6,221))
        surface.blit(MENU_FONT.render(f"Factory       {round(50*bonus_factors[3],2)}         100     5 days         10         50",1,(0,0,0)),(43,261))
        surface.blit(MENU_FONT.render(f"Bank        {round(50*bonus_factors[4],2)}        100     5 days         10         50",1,(0,0,0)),(57,302))
        surface.blit(MENU_FONT.render(f"Power Plant    {round(50*bonus_factors[5],2)}        100     5 days         10         50",1,(0,0,0)),(30,342))
        surface.blit(MENU_FONT.render(f"Habitat      {round(5*bonus_factors[6],2)}        100     5              10         50 ",1,(0,0,0)),(45,375))

        for button in self.buttons:
            if button.draw(surface):
                # update the state of the game based on which button was clicked
                if button == self.buttons[0]:
                    destroyed=deconstruct(buildings_list,non_critical_list,"FARM")
                elif button == self.buttons[1]:
                    destroyed=deconstruct(buildings_list,non_critical_list,"ICE MINE")
                elif button==self.buttons[2]:
                    destroyed=deconstruct(buildings_list,non_critical_list,"MOLECULE SPLITTER")
                elif button==self.buttons[3]:
                    destroyed=deconstruct(buildings_list,non_critical_list,"FACTORY")
                elif button==self.buttons[4]:
                    destroyed=deconstruct(buildings_list,non_critical_list,"BANK")
                elif button==self.buttons[5]:
                    destroyed=deconstruct(buildings_list,non_critical_list,"POWER PLANT")
                elif button==self.buttons[6]:
                    destroyed=deconstruct(buildings_list,non_critical_list,"HABITAT")
                # add more conditions here as needed


class Stats_Menu():
    
    def __init__(self):
        self.image = MENU_BACKGROUND
        self.visible = False
        self.next=Button(495,374,CONFIRM_ICON)
        self.back=Button(281,376,BACK_ICON)
        self.production_display=0

    def draw(self, surface,buildings_list,production_queue):
        if not self.visible:
            return
        
        """TODO: Implement special refund pricing"""
    
        surface.blit(self.image, (0,0))
        surface.blit(MENU_FONT.render(f"Building     Amount     Total Production",1,(0,0,0)),(222,99))
        surface.blit(MENU_FONT.render(f"Farm        {len(buildings_list['FARM'])}             {len(buildings_list['FARM'])*(round(100*bonus_factors[0],2))}",1,(0,0,0)),(240,131))
        surface.blit(MENU_FONT.render(f"Ice Mine      {len(buildings_list['ICE MINE'])}             {float(len(buildings_list['ICE MINE'])*(round(100*bonus_factors[1],2)))}",1,(0,0,0)),(221,162))
        surface.blit(MENU_FONT.render(f"Molecule Splitter   {len(buildings_list['MOLECULE SPLITTER'])}             {float(len(buildings_list['MOLECULE SPLITTER'])*(round(100*bonus_factors[2],2)))}",1,(0,0,0)),(167,204))
        surface.blit(MENU_FONT.render(f"Factory       {len(buildings_list['FACTORY'])}             {len(buildings_list['FACTORY'])*(round(100*bonus_factors[3],2))}",1,(0,0,0)),(223,243))
        surface.blit(MENU_FONT.render(f"Bank        {len(buildings_list['BANK'])}             {len(buildings_list['BANK'])*(round(100*bonus_factors[4],2))}",1,(0,0,0)),(240,277))
        surface.blit(MENU_FONT.render(f"Power plant    {len(buildings_list['POWER PLANT'])}             {len(buildings_list['POWER PLANT'])*(round(100*bonus_factors[5],2))}",1,(0,0,0)),(210,313))
        surface.blit(MENU_FONT.render(f"Under construction ",1,(0,0,0)),(321,381))
        surface.blit(MENU_FONT.render(f"Habitat      {len(buildings_list['HABITAT'])}             {len(buildings_list['HABITAT'])*(round(100*bonus_factors[6],2))}",1,(0,0,0)),(225,345))

        sublist=to_sublists(production_queue,5)

        if self.next.draw(surface):
            if len(sublist) != 0 and self.production_display < len(sublist)-1:
                self.production_display += 1

        if self.back.draw(surface):
            if len(sublist) != 0 and self.production_display > 0:
                self.production_display -= 1

        if len(sublist)!=0:
            surface.blit(MENU_FONT.render(f"{str_object_list(sublist[self.production_display])}",1,(0,0,0)),(60,422))
        
        