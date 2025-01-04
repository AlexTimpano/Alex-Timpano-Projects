#Universal variables
#Sets and stores variables that are to be shared between all files in game


#Sets game resources and inital amounts. 
resourcelist=[["Food", 1000], ["Water", 1000], ["Oxygen", 1000], ["Building Material", 1000], ["Power", 1000]]
money=5000
population=500
#Base incomes of all resources in order of noney,population
incomes=[10,10,10,10,30,50,50]


"""
Contains information on buildings in this order:

1: amount of buildings
2: Cost of building
3: Power consumption
4: Resource production
"""

hydroponics=[0,250,10,15]
iceMine=[0,100,5,10]
moleculeSplitter=[0,300,20,35]
industrialModule=[0,50,15,20]
spacePort=[0,200,30,200]
hospital=[0,150,20,15]
solarFarm=[0,100,0,65]



planetSpecs=None
#universalVariables.
