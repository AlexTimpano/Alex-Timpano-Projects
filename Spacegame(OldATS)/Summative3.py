##########################
##########################
##Settling the void     ##
##Alex Timpano          ##
##1/19/2022             ##
##ICS4U                 ##
##########################
##########################

#Importing modules and files
import random
from Events import events
import universalVariables

#Establishing timer that counts time until game over.
losstimer=0

#Sets the standard resource gain multipliers. 1 is 100% gain. AKA no multiplier 
bonusfactors=[1,1,1,1,1,1,1]
"""factor order is:
food:1
water:2
oxygen:3
building mat:4
money:5
population:6
power:7"""

#Function to check if game is lost and to increase loss timer if critical resources are at 0
def loss_check():
    global losstimer
    if any(0 in inner_list for inner_list in universalVariables.resourcelist)==True:
        losstimer+=1
        print(f"Critical resource(s) at 0. {5-losstimer} days remaning until mission failure")
        
        if losstimer>=5:
            print("Critical resources have depleted. Game over")
            quit()
    else:
        losstimer=0

    

    if universalVariables.population==0:
        print("The colony lies silent. Mission failure")
        quit()

#Daily income functon.
def dailygains():
    
    global resourcelist, money, population
    universalVariables.resourcelist[0][1]+= ((universalVariables.incomes[0]+(universalVariables.hydroponics[3]*universalVariables.hydroponics[0]))*bonusfactors[0])-(universalVariables.population*0.05)
    universalVariables.resourcelist[1][1]+=((universalVariables.incomes[1]+(universalVariables.iceMine[3]*universalVariables.iceMine[0]))*bonusfactors[1])-(universalVariables.population*0.1)
    universalVariables.resourcelist[2][1]+= ((universalVariables.incomes[2]+(universalVariables.moleculeSplitter[3]*universalVariables.moleculeSplitter[0]))*bonusfactors[2])-(universalVariables.population*0.02)
    universalVariables.resourcelist[3][1]+= (universalVariables.incomes[3]+(universalVariables.industrialModule[3]*universalVariables.industrialModule[0]))*bonusfactors[3]
    universalVariables.money+= (universalVariables.incomes[4]+(universalVariables.spacePort[3]*universalVariables.spacePort[0]))*bonusfactors[4]
    universalVariables.population+= (universalVariables.incomes[5]+(universalVariables.hospital[3]*universalVariables.hospital[0]))*bonusfactors[5]
    universalVariables.resourcelist[4][1]+=((universalVariables.incomes[6]+(universalVariables.solarFarm[3]*universalVariables.solarFarm[0]))*bonusfactors[6])-(universalVariables.hydroponics[2]*universalVariables.hydroponics[0]+universalVariables.iceMine[2]*universalVariables.iceMine[0]+universalVariables.moleculeSplitter[2]*universalVariables.moleculeSplitter[0]+universalVariables.industrialModule[2]*universalVariables.industrialModule[0]+universalVariables.spacePort[2]*universalVariables.spacePort[0]+universalVariables.hospital[2]*universalVariables.hospital[0]+universalVariables.solarFarm[2]*universalVariables.solarFarm[0])








#Lore. It's not my best piece of writting. But it works for this.
print("The year is 2075. Humanity is ready to make a new home on an alien world. Long-term bases already exist on planets across the solar system but this will be the first attempt at creating a permanent interplanetary colony that is self-sufficient. Your task is to manage this new colony and last for 50 days without any support from Earth to prove that your colony is truly self-sufficient")

print("\nAs the director of the United Nations Interplanetary Settlement(UNIS) effort you are given the choice to choose where in the solar system to place the first colony. Every planet has its own advantages and disadvantages")

print("""\nTerrestrial Planets(And moon)\nMars: The Red planet. Humanity has long dreamed of settling mars. Will you make that dream a reality? Mars is easier but no cake walk. It has decent water supplies and atmospheric CO2 that could be turned into oxygen
    \nThe Moon: Ever since Neil Armstrong set foot on the moon in 1969 it became inevitable that humans would one day settle on the moon. The moon has no atmosphere but is closer to the sun and has easy access to solar power.
    \nVenus: The harshest planet in the solar system. High heat, a thick crushing atmosphere and sulphiric acid rain. It'll be a challenge. Can you do it?
    \nMercury: The closest plane to the sun. High heat, easy access to solar power, no naturally occuring air or water. It's a solar engineer's paradise, and a hydro engineer's nightmare.
    \nThe Jovian Moons
    \nIo: A volcanic moon orbiting Jupiter. Slightly reduced power output due to volcanic aerosols blocking out the sun. Building materials are sure to be found.
    \nEuropa: A moon made entirely out of ice and water. Needless to say water will be extremely plentfiul. Air can also be acquired by splitting up the water. Slightly reduced power output.
    \nTitan: One of the most interesting moons in the solar system. Titan is the only moon to have an atmosphere and oceans of liquid methane which can be used for fuel. Solar power is greatly reduced by the thick atmosphere but the abundance of fuel should provide a major economic boost""")



#Player chooses their planet. Their planet provides certain bonuses or penalties. Also sets certain planet characteristics as an object
while True:
    planet=input("\n\nPlease select your planet from the aforementioned options. As a reminder those are. Mars, Moon, Venus, Mercury, Io, Europa, and Titan:").capitalize()


    #Note to self. Find better descriptive words
    if planet=="Mars":
        bonusfactors[1]+=0.15
        bonusfactors[2]+=0.25
        universalVariables.planetSpecs=events(planet, "plain", "chilly", "thin")
        
        break

    elif planet=="Moon":
        bonusfactors[2]-=0.35
        bonusfactors[6]+=0.30
        universalVariables.planetSpecs=events(planet, "rocky", "chilly", "negligible")
        break

    elif planet=="Venus":
        bonusfactors[6]-=0.10
        bonusfactors[5]-=0.20
        universalVariables.planetSpecs=events(planet, "plain", "scorching", "crushing")
        break
        
        
    elif planet=="Mercury":
        bonusfactors[1]-=0.40
        bonusfactors[6]+=0.40
        universalVariables.planetSpecs=events(planet, "relatively flat", "scorching", "negligible")
        break

    elif planet=="Io":
        bonusfactors[6]-=0.1
        bonusfactors[3]+=0.25
        universalVariables.planetSpecs=events(planet, "volcanic", "cold", "negligible")
        break

    elif planet=="Europa":
        bonusfactors[6]-=0.1
        bonusfactors[1]+=0.65
        universalVariables.planetSpecs=events(planet, "glacial", "frigid", "negligible")
        break

    elif planet=="Titan":
        bonusfactors[4]+=0.40
        bonusfactors[6]-=0.35
        universalVariables.planetSpecs=events(planet, "hilly", "frozen", "thick")
        break

    else:
        print("\nInvalid planet selection")
        

print(f"Planet {planet} selected.")


print(f"""Resource gain rates for {planet} are: \nFood: {bonusfactors[0]*100}%
    \nWater: {bonusfactors[1]*100}%
    \nOxygen: {bonusfactors[2]*100}%
    \nBuilding materials: {bonusfactors[3]*100}%
    \nMoney: {bonusfactors[4]*100}%
    \nPopulation: {bonusfactors[5]*100}%
    \nPower: {bonusfactors[6]*100}%""")

#Main for loop that counts to 50 days. 
for day in range(1,51):
    print(f"\nDay {day}")
    loss_check()
    dailygains()
    #1/5 chance of getting a random event
    if random.randint(1,5)==5:
        events.randomEvents(random.randint(1,8))
    print(f"\nFood: {universalVariables.resourcelist[0][1]}   Water: {universalVariables.resourcelist[1][1]}   Oxygen: {universalVariables.resourcelist[2][1]}   Building Materials: {universalVariables.resourcelist[3][1]}   Money: {universalVariables.money}   Population: {universalVariables.population}   Power: {universalVariables.resourcelist[4][1]}")   
    finished=False
    while finished==False:
        #Player can select their action for the day
        action=input("What would you like to do today? Build(B), Deconstruct(D), Check Buildings(CB) or end day(E)?: ")
        if action=="B":
            #Player can choose which building to build. If there are insufficient resources no will automatically be chosen
            while True:
                building=input(f"\nWhat building would you like to build? Hydroponics(Cost:{universalVariables.hydroponics[1]}), Ice Mine(Cost:{universalVariables.iceMine[1]}), Molecule Splitter(Cost:{universalVariables.moleculeSplitter[1]}), Industrial Module(Cost:{universalVariables.industrialModule[1]}), Spaceport(Cost:{universalVariables.spacePort[1]}), Hospital(Cost:{universalVariables.hospital[1]}), Solar Farm(Cost:{universalVariables.solarFarm[1]}), or NONE") 

                #Checks to see if the building entered matches one on the list. If yes, confirm build and check if resources are available.
                if building.capitalize()=="Hydroponics":
                    buildinput=input(f"Hydroponics labs grow fresh food using water and mineral solutions in place of soil. Compact and perfect for interplanetary colonization. Will produce {universalVariables.hydroponics[3]} food. Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.resourcelist[3][1]>=universalVariables.hydroponics[1]:
                            universalVariables.resourcelist[3][1]-=universalVariables.hydroponics[1]
                            universalVariables.hydroponics[0]+=1
                            print("Hydroponics built")
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue
                    
                elif building.capitalize()=="Ice mine":
                    buildinput=input(f"Simple automated mines that extract ice from the local area or comets if no ice is available. Will produce {universalVariables.iceMine[3]} water. Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.resourcelist[3][1]>=universalVariables.iceMine[1]:
                            universalVariables.resourcelist[3][1]-=universalVariables.iceMine[1]
                            universalVariables.iceMine[0]+=1
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Molecule splitter":
                    buildinput=input(f"Splits molecules like CO2 and H2O into their component elements to acquire free oxygen gas. Will produce {universalVariables.moleculeSplitter[3]} oxygen. Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.resourcelist[3][1]>=universalVariables.moleculeSplitter[1]:
                            universalVariables.resourcelist[3][1]-=universalVariables.moleculeSplitter[1]
                            universalVariables.moleculeSplitter[0]+=1
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Industrial module":
                    buildinput=input(f"General purpose industrial module to extract and refine raw materials into useful building materials. Will produce {universalVariables.industrialModule[3]} building materials. Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.resourcelist[3][1]>=universalVariables.industrialModule[1]:
                            universalVariables.resourcelist[3][1]-=universalVariables.industrialModule[1]
                            universalVariables.industrialModule+=1
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Spaceport":
                    buildinput=input(f"Dedicated takeoff and landing site for rockets. Will produce {universalVariables.spacePort[3]} money. Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.resourcelist[3][1]>=universalVariables.spacePort[1]:
                            universalVariables.resourcelist[3][1]-=universalVariables.spacePort[1]
                            universalVariables.spacePort[0]+=1
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Hospital":
                    buildinput=input(f"General purpose medical centre. Saves lives and increases birthrate. Will grow population by {universalVariables.hospital[3]} daily. Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.resourcelist[3][1]>=universalVariables.hospital[1]:
                            universalVariables.resourcelist[3][1]-=universalVariables.hospital[1]
                            universalVariables.hospital[0]+=1
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Solar farm":
                    buildinput=input(f"An array of graphene enhanced solar panels to generate electricity from sunlight. Will produce {universalVariables.solarFarm[3]} power. Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.resourcelist[3][1]>=universalVariables.solarFarm[1]:
                            universalVariables.resourcelist[3][1]-=universalVariables.solarFarm[1]
                            universalVariables.solarFarm[0]+=1
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="None":
                    break
                    
                else:
                    print("Invalid input. Please pick a building from the list")
                    break

                finished=True

        #Deconstruct menu. Players can choose buildings to destroy in exchange for a 65% refund on their building materials.
        if action=="D":
            while True:
                building=input(f"\nWhat building would you like to dismantle? Hydroponics(Refund:{universalVariables.hydroponics[1]*0.65}), Ice Mine(Refund:{universalVariables.iceMine[1]*0.65}), Molecule Splitter(Refund:{universalVariables.moleculeSplitter[1]*0.65}), Industrial Module(Refnu:{universalVariables.industrialModule[1]*0.65}), Spaceport(Refund:{universalVariables.spacePort[1]*0.65}), Hospital(Refund:{universalVariables.hospital[1]*0.65}), Solar Farm(Refund:{universalVariables.solarFarm[1]*0.65}), or NONE") 

                #Checks to see if there are more than 0 of the selected building and if the building is actually on the list.
                if building.capitalize()=="Hydroponics":
                    buildinput=input("Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.hydroponics[0]>0:
                            universalVariables.resourcelist[3][1]+=universalVariables.hydroponics[1]*0.65
                            universalVariables.hydroponics[0]-=1
                            finished=True
                            break
                        else:
                            print("You need to have buildings to dismantle them")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue
                    
                elif building.capitalize()=="Ice mine":
                    buildinput=input("Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.iceMine[0]>0:
                            universalVariables.resourcelist[3][1]+=universalVariables.iceMine[1]*0.65
                            universalVariables.iceMine[0]-=1
                            finished=True
                            break
                        else:
                            print("You need to have buildings to dismantle them")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Molecule splitter":
                    buildinput=input("Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if moleculeSplitter[0]>0:
                            universalVariables.resourcelist[3][1]+=universalVariables.moleculeSplitter[1]*0.65
                            universalVariables.moleculeSplitter[0]-=1
                            finished=True
                            break
                        else:
                            print("You need to have buildings to dismantle them")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Industrial module":
                    buildinput=input("Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.industrialModule[0]>0:
                            universalVariables.resourcelist[3][1]+=universalVariables.industrialModule[1]*0.65
                            universalVariables.industrialModule-=1
                            finished=True
                            break
                        else:
                            print("You need to have buildings to dismantle them")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Spaceport":
                    buildinput=input("Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.spacePort[0]>0:
                            universalVariables.resourcelist[3][1]+=universalVariables.spacePort[1]*0.65
                            universalVariables.spacePort[0]-=1
                            finished=True
                            break
                        else:
                            print("You need to have buildings to dismantle them")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Hospital":
                    buildinput=input("Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.hospital[0]>0:
                            universalVariables.resourcelist[3][1]+=universalVariables.hospital[1]*0.65
                            universalVariables.hospital[0]-=1
                            finished=True
                            break
                        else:
                            print("You need to have buildings to dismantle them")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="Solar farm":
                    buildinput=input("Confirm?(Y/N): ").upper()
                    if buildinput=="Y":
                        if universalVariables.solarFarm[0]>0:
                            universalVariables.resourcelist[3][1]+=universalVariables.solarFarm[1]*0.65
                            universalVariables.solarFarm[0]-=1
                            finished=True
                            break
                        else:
                            print("You don't have enough building materials to build this")
                            continue
                    elif buildinput=="N":
                        continue

                    else:
                        print("Invalid. Yes(Y) or No(N)")
                        continue

                elif building.capitalize()=="None":
                    break
                    
                else:
                    print("Invalid input. Please pick a building from the list")
                    break
                
                

                
        #Prints resource list
        if action=="CB":
            print(f"""\nHydroponics: {universalVariables.hydroponics[0]}
Ice mine: {universalVariables.iceMine[0]}
Molecule Splitter: {universalVariables.moleculeSplitter[0]}
Industrial Module: {universalVariables.industrialModule[0]}
Spaceport: {universalVariables.spacePort[0]}
Hospital: {universalVariables.hospital[0]}
Solar Farm: {universalVariables.solarFarm[0]}\n""")
        #Ends turn
        if action=="E":
            finished=True

        elif action !="B" and action !="D" and action !="CB" and action !="E":
            print("Invalid input. Please select from the list of available actions")
                
                
        
print("Message from UNIS Command: Congratulations. You have proven that your colony truly is self-sufficient. Outside communications are restored and regular resource shipments will begin shortly. Thank you for your participation in this experiment")

