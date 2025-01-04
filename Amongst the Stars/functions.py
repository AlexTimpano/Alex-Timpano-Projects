import pygame
import math 

#Generic functions for use within the game

#init_sys_font and init_custom_font are quick ways to make fonts
def init_sys_font(font_name,size):
    font=pygame.font.SysFont(font_name,size)
    return font

def init_custom_font(path,size):
    font=pygame.font.Font(path,size)
    return font


font = pygame.font.SysFont(None, 40)

textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

'''drawText function borrowed from stackoverflow. Fits text to a rect without having
to manually measure and draw a bunch of lines. Can align text in various ways based on
values above. Default is left alignment. 

Code by: Rabbid76

Code link: https://stackoverflow.com/a/64598520/20506239'''

def drawText(surface, text, color, rect, font, align=textAlignLeft, aa=False, bkg=None):
    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList: image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, aa, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i*spaceWidth, lineBottom
            surface.blit(image, (round(x), y))
            lineLeft += image.get_width() 
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]: remainingText += text + " "
        return remainingText
    return ""

def add_lists(bonus_factors, bonuses):
    for i in range(len(bonus_factors)):
        bonus_factors[i] += bonuses[i]
    return bonus_factors

def to_sublists(main_list,sublist_size):
    if len(main_list)==0:
        sublists=[]
    else:
        sublists=[main_list[i:i+sublist_size] for i in range(0,len(main_list),sublist_size)]
    return sublists

def str_object_list(object_list):
    neo_list=", ".join((item.name + ": " + str(item.build_time)+"d") for item in object_list)

    return neo_list


def next_day(production_queue,buildings_list,bonus_factors,day,crit_list,non_crit_list,population):

    if day<=50:
        day+=1


        #Checks buildings under construction. Removes them from production queue and addes them to
        #Relevent buildings list.
        for item in production_queue:
            if item.build_time==1:
               
                buildings_list[item.name.upper()].append(item)
            item.build_time-=1
                

        production_queue[:]=[item for item in production_queue if item.build_time!=0]


        #Consts for population growth and production
        POP_CONSUMPTION=0.35
        POP_GROWTH=5
        POP_BONUS=(population//500)*0.1

        #Handles production, power use, and maintenance 
        for building in buildings_list["FARM"]:
            produce=True 

            if building.power<=non_crit_list[2]:
                non_crit_list[2]-=building.power
            else:
                produce=False
                print("lack of power")

            if building.maintenance<=non_crit_list[0]:
                non_crit_list[0]-=building.maintenance
            else:
                produce=False
                print("lack of mats",building.maintenance,non_crit_list[0])

            
            
            if produce:
                crit_list[0]+=building.production*(bonus_factors[0]+POP_BONUS)


        for building in buildings_list["ICE MINE"]:
            produce=True 

            if building.power<=non_crit_list[2]:
                non_crit_list[2]-=building.power
            else:
                produce=False

            if building.maintenance<=non_crit_list[0]:
                non_crit_list[0]-=building.maintenance
            else:
                produce=False
            
            if produce:
                crit_list[1]+=building.production*(bonus_factors[1]+POP_BONUS)

        for building in buildings_list["MOLECULE SPLITTER"]:
            produce=True 

            if building.power<=non_crit_list[2]:
                non_crit_list[2]-=building.power
            else:
                produce=False

            if building.maintenance<=non_crit_list[0]:
                non_crit_list[0]-=building.maintenance
            else:
                produce=False
            
            if produce:
                crit_list[2]+=building.production*(bonus_factors[2]+POP_BONUS)


        for building in buildings_list["MOLECULE SPLITTER"]:
            produce=True 

            if building.power<=non_crit_list[2]:
                non_crit_list[2]-=building.power
            else:
                produce=False

            if building.maintenance<=non_crit_list[0]:
                non_crit_list[0]-=building.maintenance
            else:
                produce=False
            
            if produce:
                non_crit_list[0]+=building.production*(bonus_factors[3]+POP_BONUS)

        for building in buildings_list["BANK"]:
            produce=True 

            if building.power<=non_crit_list[2]:
                non_crit_list[2]-=building.power
            else:
                produce=False

            if building.maintenance<=non_crit_list[0]:
                non_crit_list[0]-=building.maintenance
            else:
                produce=False
            
            if produce:
                non_crit_list[1]+=building.production*(bonus_factors[4]+POP_BONUS)

        for building in buildings_list["POWER PLANT"]:
            produce=True 


            if building.maintenance<=non_crit_list[0]:
                non_crit_list[0]-=building.maintenance
            else:
                produce=False
            
            if produce:
                non_crit_list[2]+=building.production*(bonus_factors[5]+POP_BONUS)

        for building in buildings_list["HABITAT"]:
            produce=True 

            if building.power<=non_crit_list[2]:
                non_crit_list[2]-=building.power
            else:
                produce=False

            if building.maintenance<=non_crit_list[0]:
                non_crit_list[0]-=building.maintenance
            else:
                produce=False
            
            if produce:
                population+=building.production*(bonus_factors[4]+POP_BONUS)

        crit_list[0]-=int((population*POP_CONSUMPTION))
        crit_list[1]-=int((population*POP_CONSUMPTION))
        crit_list[2]-=int((population*POP_CONSUMPTION))


        if crit_list[0]<0:
            crit_list[0]=0
        if crit_list[1]<0:
            crit_list[1]=0
        if crit_list[2]<0:
            crit_list[2]=0

        population+=POP_GROWTH
        

        return day,population,buildings_list
    else:
        pygame.quit()
            
    
            


            