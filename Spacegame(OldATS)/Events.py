#Imports random and universal variables
import random
import universalVariables

userinput=""

#Makes and initializes class
class events:
    def __init__(self, name, terrain, temperature, atmosphere):
        self.name=name
        self.terrain=terrain
        self.temperature=temperature
        self.atmosphere=atmosphere

#Random events function. Simple events with small rewards based on actions. Most just ask if the user wants to pay or not. One just provides a free bonus
    def randomEvents(randnum):
        if randnum==1:
            print(f"""Ice deposit located
A large deposit of ice has been found deep undergound on {universalVariables.planetSpecs.name}. The ice could be mined, melted and filtered and stored but it will cost 50 dollars. Should we begin the operation?""")
            while True:
                userinput=input("Y or N?").upper()
                if userinput =="Y":
                    if universalVariables.money>=50:
                        universalVariables.resourcelist[1][1]+=random.randint(50,300)
                        break
                    else:
                        print("You lack the funds to launch this mission")
                        break
                elif userinput=="N":
                    break
                else:
                    print("Invalid input. Please select yes or no")

        elif randnum==2:
            print(f"""Gas Vent Located
A large natural vent of oxygen gas has been located in the {universalVariables.planetSpecs.terrain} terrain of {universalVariables.planetSpecs.name} but it's depleting fast. With an investment of 50 dollars we could contain the vent and extract it's oxygen before it diffuses into the {Summative3.planetSpecs.atmosphere} atmosphere of {Summative3.planet} Should we proceed?""")
            while True:
                userinput=input("Y or N?").upper()
                if userinput =="Y":
                    if universalVariables.money>=50:
                        universalVariables.resourcelist[2][1]+=random.randint(50,300)
                        break
                    else:
                        print("You lack the funds to launch this mission")
                        break
                elif userinput=="N":
                    break
                else:
                    print("Invalid input. Please select yes or no")

        elif randnum==3:
            print(f"""High quality mineral deposit located
A large deposit of high quality minerals has been located on {universalVariables.planetSpecs.name}. If mined it could yield a large amount of resources but the area is unstable and will require an investment of 50 dollars to guarantee safety. Should we proceed?""")
            while True:
                userinput=input("Y or N?").upper()
                if userinput =="Y":
                    if universalVariables.money>=50:
                        universalVariables.resourcelist[3][1]+=random.randint(50,300)
                        break
                    else:
                        print("You lack the funds to launch this mission")
                        break
                elif userinput=="N":
                    break
                else:
                    print("Invalid input. Please select yes or no")

        elif randnum==4:
            print(f"""Battery surplus
It was discovered that the colonial mission was accidentally supplied with additional electrical storage units but they were built and lost amongst the {universalVariables.planetSpecs.terrain} terrain of {universalVariables.planetSpecs.name}. For an investment of 50 dollars we can mount a mission to locate them and extract their energy. Should we proceed?""")
            while True:
                userinput=input("Y or N?").upper()
                if userinput =="Y":
                    if universalVariables.money>=50:
                        universalVariables.resourcelist[3][1]+=random.randint(50,300)
                        break
                    else:
                        print("You lack the funds to launch this mission")
                        break
                elif userinput=="N":
                    break
                else:
                    print("Invalid input. Please select yes or no")

        elif randnum==5:
            print(f"""Little rover
On the desolate {universalVariables.planetSpecs.terrain} surface of {universalVariables.planetSpecs.name} we have found an old rover from the early space age. While it couldn't be brought back online we have repurposed it into a monument that will raise morale""")
            universalVariables.incomes[5]+=5

        elif randnum==6:
            print(f"""Our batteries are low and its getting dark
Misfortune hit the {universalVariables.planetSpecs.name} colony power grid early today as it was revealed a large potion of our solar panels and batteries were defective and were losing capacity fast. We have the technology to repair them today but it will cost {Summative3.solarFarm[1]*50} dollars to get it done. Should we proceed?""")
            while True:
                userinput=input("Y or N?").upper()
                if userinput =="Y":
                    if universalVariables.money>=universalVariables.solarFarm[0]*50:
                        break
                    else:
                        print("You lack the funds to launch this mission")
                        universalVariables.incomes[6]=(universalVariables.incomes[6]*80)
                        print("Daily power income reduced to 80%")
                elif userinput=="N":
                    universalVariables.incomes[6]=(universalVariables.incomes[6]*80)
                    print("Daily power income reduced to 80%")
                    break
                else:
                    print("Invalid input. Please select yes or no")

        elif randnum==7:
            print(f"""{universalVariables.planetSpecs.name} innovation
Despite lacking the advanced research facilities of Earth, scientists on {universalVariables.planetSpecs.name} are working daily to improve our ability to survive on this hostile world. With a 200 investment our researchers believe they can improve our molecule splitting technologies allowing improved oxygen production. Should we proceed?""")
            while True:
                userinput=input("Y or N?").upper()
                if userinput =="Y":
                    if universalVariables.money>=200:
                        universalVariables.moleculeSplitter[3]+=(universalVariables.moleculeSplitter*0.20)
                        print("Oxygen production increased by 20%")
                        break
                    else:
                        print("You lack the funds to launch this mission")
                elif userinput=="N":
                    break
                else:
                    print("Invalid input. Please select yes or no")


        elif randnum==8:
            print(f"""Concrete and other wonders of material science
Some wondered if it was possible but we now have concrete evidence that local materials can be used to make a new type of concrete that's stronger than any found on Earth and is also easier to produce since it's made of easily source local materials. With an investment of 100 dollars we can roll it out soon""")
            while True:
                userinput=input("Y or N?").upper()
                if userinput =="Y":
                    if universalVariables.money>=200:
                        universalVariables.incomes[3]+=universalVariables.incomes[3]*0.1
                        print("Building materials production increased by 10%")
                        break
                    else:
                        print("You lack the funds to launch this mission")
                elif userinput=="N":
                    break
                else:
                    print("Invalid input. Please select yes or no")


            
        

        
            
            

    
