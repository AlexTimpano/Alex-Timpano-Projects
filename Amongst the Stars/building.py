
import pygame
from shared_resources import *
pygame.init
pygame.font.init()



class Building():
    def __init__(self,name,production,build_time,maintenance,power):
        self.name=name
        self.production=production
        self.build_time=build_time
        self.maintenance=maintenance
        self.power=power 

    def __str__(self):
        print(self.name,self.production,self.build_cost,self.build_time,self.maintenance,self.power)










#Function responsible for the construction of a building. Requires the amount of building materials available
#Possible building types are 



def construct(production_queue,NC_list,building_type,bonus_factors):



    if NC_list[0]<100:
        constructing=False
    else:
        constructing=True 
        NC_list[0]-=100
        if building_type == "FARM":
            production_queue.append(Building("Farm", round(100*bonus_factors[0], 2), 5, 10, 50))
        elif building_type == "ICE MINE":
            production_queue.append(Building("Ice Mine", round(100*bonus_factors[1], 2), 5, 10, 50))
        elif building_type == "MOLECULE SPLITTER":
            production_queue.append(Building("Molecule splitter", round(100*bonus_factors[2], 2), 5, 10, 50))
        elif building_type == "FACTORY":
            production_queue.append(Building("Factory", round(100*bonus_factors[3], 2), 5, 10, 50))
        elif building_type == "BANK":
            production_queue.append(Building("Bank", round(100*bonus_factors[4], 2), 5, 10, 50))
        elif building_type == "POWER PLANT":
            production_queue.append(Building("Power plant", round(100*bonus_factors[5], 2), 5, 10, 0))
        elif building_type == "HABITAT":
            production_queue.append(Building("Habitat", round(10*bonus_factors[6], 2), 5, 10, 50))

    return constructing


def deconstruct(buildings_list,NC_list,building_type):
    if len(buildings_list[building_type])<=0:
        destroyed=False
    else:
        destroyed=True
        to_destroy=buildings_list[building_type].pop()
        NC_list[0]+=50

    return destroyed

   

        



        
            


