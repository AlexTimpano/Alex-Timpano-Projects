#This list contains criticial non-population resources for the game. order is food, water, oxygen
critical_list=[1000,1000,1000]
#This list contains less-critical resources. Order is building materials,MONEY and POWER
non_critical_list=[1000,500,1000]
#The population
population=250
#The production queue. The list of things to be constructed
production_queue=[]

#bonus_factors
'''List contains bonuses that will be applied to resource gain. 1 is a multiplier of 1
Bonuses are in order of food, water, oxygen,building materials,money,population,power'''
bonus_factors=[1,1,1,1,1,1,1]

planet_surface=None
faction=None

#Buildings


buildings_list = {
    "FARM": [],
    "ICE MINE": [],
    "MOLECULE SPLITTER": [],
    "FACTORY": [],
    "BANK": [],
    "POWER PLANT": [],
    "HABITAT": []
}

#The production queue. The list of things to be constructed
production_queue=[]

