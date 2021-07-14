#Artifact simulation program 1.0
import random

#resources
substatchance = range(1,100)
substat4= 0
artifacttype = ["Circlet", "Goblet", "Timepiece", "Feather", "Flower"]
mainstatTP = ["ATK%", "DEF%", "Elemental Mastery", "Energy Recharge", "HP%"]
mainstatG = ["Anemo Damage", "Cryo Damage", "Dendro Damage", "Electro Damage", "Geo Damage", "Hydro Damage", "Physical Damage", "Pyro Damage", "ATK%", "DEF%", "HP%", "Elemental Mastery"]
mainstatC = ["ATK%", "Critical Damage", "Critical Rate", "DEF%", "Elemental Mastery", "HP%", "Healing Bonus"]
substat = ["ATK%", "ATK", "DEF%", "DEF", "Critical Rate", "Critical Damage", "Elemental Mastery", "Energy Recharge", "HP", "HP%"]

#order : HP%, ATK%, DEF%, EM, Crate, Cdamage, Hbonus
#mainstatvaluesC = [7, 8.7, 28, 4.7, 9.3, 5.4]
hpsubstat = [209, 239, 270, 300]
atksubstat = [14, 16, 17, 19]
defsubstat = [16, 19, 21, 23]
hpercentsubstat = [4.1, 4.7, 5.2, 5.9]
atkpercentsubstat = [4.1, 4.7, 5.2, 5.9]
defpercentsubstat = [5.1, 5.8, 6.6, 7.3]
elemasterysubstat = [16, 19, 21, 23]
energyrechargesubstat = [4.5, 5.2, 5.8, 6.5]
critratesubstat = [2.7, 3.1, 3.5, 3.9]
critdamagesubstat = [5.4, 6.2, 7, 7.8]

#code
artitype = random.choice(artifacttype)
if artitype == "Circlet" :
    print("Artifact : Circlet")
    MainStat = random.choice(mainstatC)
    if MainStat in substat :
        substat.remove(MainStat)
    if MainStat in ["ATK%", "HP%"] :
        MainStat = [MainStat, 7]
    elif MainStat == "DEF%" :
        MainStat = ["DEF%", 8.7]
    elif MainStat == "Elemental Mastery" :
        MainStat = ["Elemental Mastery", 28]
    elif MainStat == "Critical Rate" :
        MainStat = ["Critical Rate", 4.7]
    elif MainStat == "Critical Damage" :
        MainStat = ["Critical Damage", 9.3]
    elif MainStat == "Healing Bonus" :
        MainStat = ["Healing Bonus", 5.4]
    ####SubStat 1####
    substat1 = random.choice(substat)
    substat.remove(substat1)
    if substat1 == "ATK%" :
        substatV1 = random.choice(atkpercentsubstat)
        substat1 = ["ATK", substatV1]
    elif substat1 == "ATK" :
        substatV1 = random.choice(atksubstat)
        substat1 = ["ATK", substatV1]
    elif substat1 == "DEF%" :
        substatV1 = random.choice(defpercentsubstat)
        substat1 = ["DEF%", substatV1]
    elif substat1 == "DEF" :
        substatV1 = random.choice(defsubstat)
        substat1 = ["DEF", substatV1]
    elif substat1 == "Critical Rate" :
        substatV1 = random.choice(critratesubstat)
        substat1 = ["Critical Rate", substatV1]
    elif substat1 == "Critical Damage" :
        substatV1 = random.choice(critdamagesubstat)
        substat1 = ["Critical Damage", substatV1]
    elif substat1 == "Elemental Mastery" :
        substatV1 = random.choice(elemasterysubstat)
        substat1 = ["Elemental Mastery", substatV1]
    elif substat1 == "Energy Recharge" :
        substatV1 = random.choice(energyrechargesubstat)
        substat1 = ["Energy Recharge", substatV1]
    elif substat1 == "HP%" :
        substatV1 = random.choice(hpercentsubstat)
        substat1 = ["HP%", substatV1]
    elif substat1 == "HP" :
        substatV1 = random.choice(hpsubstat)
        substat1 = ["HP", substatV1]
    #### SubStat 2 ####
    substat2 = random.choice(substat)
    substat.remove(substat2)
    if substat2 == "ATK%" :
        substatV2 = random.choice(atkpercentsubstat)
        substat2 = ["ATK", substatV2]
    elif substat2 == "ATK" :
        substatV2 = random.choice(atksubstat)
        substat2 = ["ATK", substatV2]
    elif substat2 == "DEF%" :
        substatV2 = random.choice(defpercentsubstat)
        substat2 = ["DEF%", substatV2]
    elif substat2 == "DEF" :
        substatV2 = random.choice(defsubstat)
        substat2 = ["DEF", substatV2]
    elif substat2 == "Critical Rate" :
        substatV2 = random.choice(critratesubstat)
        substat2 = ["Critical Rate", substatV2]
    elif substat2 == "Critical Damage" :
        substatV2 = random.choice(critdamagesubstat)
        substat2 = ["Critical Damage", substatV2]
    elif substat2 == "Elemental Mastery" :
        substatV2 = random.choice(elemasterysubstat)
        substat2 = ["Elemental Mastery", substatV2]
    elif substat2 == "Energy Recharge" :
        substatV2 = random.choice(energyrechargesubstat)
        substat2 = ["Energy Recharge", substatV2]
    elif substat2 == "HP%" :
        substatV2 = random.choice(hpercentsubstat)
        substat2 = ["HP%", substatV2]
    elif substat2 == "HP" :
        substatV2 = random.choice(hpsubstat)
        substat2 = ["HP", substatV2]
    #### SubStat 3 ####
    substat3 = random.choice(substat)
    substat.remove(substat3)
    if substat3 == "ATK%" :
        substatV3 = random.choice(atkpercentsubstat)
        substat3 = ["ATK", substatV3]
    elif substat3 == "ATK" :
        substatV3 = random.choice(atksubstat)
        substat3 = ["ATK", substatV3]
    elif substat3 == "DEF%" :
        substatV3 = random.choice(defpercentsubstat)
        substat3 = ["DEF%", substatV3]
    elif substat3 == "DEF" :
        substatV3 = random.choice(defsubstat)
        substat3 = ["DEF", substatV3]
    elif substat3 == "Critical Rate" :
        substatV3 = random.choice(critratesubstat)
        substat3 = ["Critical Rate", substatV3]
    elif substat3 == "Critical Damage" :
        substatV3 = random.choice(critdamagesubstat)
        substat3 = ["Critical Damage", substatV3]
    elif substat3 == "Elemental Mastery" :
        substatV3 = random.choice(elemasterysubstat)
        substat3 = ["Elemental Mastery", substatV3]
    elif substat3 == "Energy Recharge" :
        substatV3 = random.choice(energyrechargesubstat)
        substat3 = ["Energy Recharge", substatV3]
    elif substat3 == "HP%" :
        substatV3 = random.choice(hpercentsubstat)
        substat3 = ["HP%", substatV3]
    elif substat3 == "HP" :
        substatV3 = random.choice(hpsubstat)
        substat3 = ["HP", substatV3]
    chance = random.choice(substatchance)
    if chance >= 80 :
            substat4 = random.choice(substat)
            if substat4 == "ATK%":
                substatV4 = random.choice(atkpercentsubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "ATK":
                substatV4 = random.choice(atksubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "DEF%":
                substatV4 = random.choice(defpercentsubstat)
                substat4 = ["DEF%", substatV4]
            elif substat4 == "DEF":
                substatV4 = random.choice(defsubstat)
                substat4 = ["DEF", substatV4]
            elif substat4 == "Critical Rate":
                substatV4 = random.choice(critratesubstat)
                substat4 = ["Critical Rate", substatV4]
            elif substat4 == "Critical Damage":
                substatV4 = random.choice(critdamagesubstat)
                substat4 = ["Critical Damage", substatV4]
            elif substat4 == "Elemental Mastery":
                substatV4 = random.choice(elemasterysubstat)
                substat4 = ["Elemental Mastery", substatV4]
            elif substat4 == "Energy Recharge":
                substatV4 = random.choice(energyrechargesubstat)
                substat4 = ["Energy Recharge", substatV4]
            elif substat4 == "HP%":
                substatV4 = random.choice(hpercentsubstat)
                substat4 = ["HP%", substatV4]
            elif substat4 == "HP":
                substatV4 = random.choice(hpsubstat)
                substat4 = ["HP", substatV4]
if artitype == "Goblet" :
    print("Artifact : Goblet")
    MainStat = random.choice(mainstatG)
    if MainStat in substat :
        substat.remove(MainStat)
    if MainStat in ["ATK%", "HP%"] :
        MainStat = [MainStat, 7]
    elif MainStat == "DEF%" :
        MainStat = ["DEF%", 8.7]
    elif MainStat == "Elemental Mastery" :
        MainStat = ["Elemental Mastery", 28]
    elif MainStat == "Critical Rate" :
        MainStat = ["Critical Rate", 4.7]
    elif MainStat == "Critical Damage" :
        MainStat = ["Critical Damage", 9.3]
    elif MainStat == "Healing Bonus" :
        MainStat = ["Healing Bonus", 5.4]
    ####SubStat 1####
    substat1 = random.choice(substat)
    substat.remove(substat1)
    if substat1 == "ATK%" :
        substatV1 = random.choice(atkpercentsubstat)
        substat1 = ["ATK", substatV1]
    elif substat1 == "ATK" :
        substatV1 = random.choice(atksubstat)
        substat1 = ["ATK", substatV1]
    elif substat1 == "DEF%" :
        substatV1 = random.choice(defpercentsubstat)
        substat1 = ["DEF%", substatV1]
    elif substat1 == "DEF" :
        substatV1 = random.choice(defsubstat)
        substat1 = ["DEF", substatV1]
    elif substat1 == "Critical Rate" :
        substatV1 = random.choice(critratesubstat)
        substat1 = ["Critical Rate", substatV1]
    elif substat1 == "Critical Damage" :
        substatV1 = random.choice(critdamagesubstat)
        substat1 = ["Critical Damage", substatV1]
    elif substat1 == "Elemental Mastery" :
        substatV1 = random.choice(elemasterysubstat)
        substat1 = ["Elemental Mastery", substatV1]
    elif substat1 == "Energy Recharge" :
        substatV1 = random.choice(energyrechargesubstat)
        substat1 = ["Energy Recharge", substatV1]
    elif substat1 == "HP%" :
        substatV1 = random.choice(hpercentsubstat)
        substat1 = ["HP%", substatV1]
    elif substat1 == "HP" :
        substatV1 = random.choice(hpsubstat)
        substat1 = ["HP", substatV1]
    #### SubStat 2 ####
    substat2 = random.choice(substat)
    substat.remove(substat2)
    if substat2 == "ATK%" :
        substatV2 = random.choice(atkpercentsubstat)
        substat2 = ["ATK", substatV2]
    elif substat2 == "ATK" :
        substatV2 = random.choice(atksubstat)
        substat2 = ["ATK", substatV2]
    elif substat2 == "DEF%" :
        substatV2 = random.choice(defpercentsubstat)
        substat2 = ["DEF%", substatV2]
    elif substat2 == "DEF" :
        substatV2 = random.choice(defsubstat)
        substat2 = ["DEF", substatV2]
    elif substat2 == "Critical Rate" :
        substatV2 = random.choice(critratesubstat)
        substat2 = ["Critical Rate", substatV2]
    elif substat2 == "Critical Damage" :
        substatV2 = random.choice(critdamagesubstat)
        substat2 = ["Critical Damage", substatV2]
    elif substat2 == "Elemental Mastery" :
        substatV2 = random.choice(elemasterysubstat)
        substat2 = ["Elemental Mastery", substatV2]
    elif substat2 == "Energy Recharge" :
        substatV2 = random.choice(energyrechargesubstat)
        substat2 = ["Energy Recharge", substatV2]
    elif substat2 == "HP%" :
        substatV2 = random.choice(hpercentsubstat)
        substat2 = ["HP%", substatV2]
    elif substat2 == "HP" :
        substatV2 = random.choice(hpsubstat)
        substat2 = ["HP", substatV2]
    #### SubStat 3 ####
    substat3 = random.choice(substat)
    substat.remove(substat3)
    if substat3 == "ATK%" :
        substatV3 = random.choice(atkpercentsubstat)
        substat3 = ["ATK", substatV3]
    elif substat3 == "ATK" :
        substatV3 = random.choice(atksubstat)
        substat3 = ["ATK", substatV3]
    elif substat3 == "DEF%" :
        substatV3 = random.choice(defpercentsubstat)
        substat3 = ["DEF%", substatV3]
    elif substat3 == "DEF" :
        substatV3 = random.choice(defsubstat)
        substat3 = ["DEF", substatV3]
    elif substat3 == "Critical Rate" :
        substatV3 = random.choice(critratesubstat)
        substat3 = ["Critical Rate", substatV3]
    elif substat3 == "Critical Damage" :
        substatV3 = random.choice(critdamagesubstat)
        substat3 = ["Critical Damage", substatV3]
    elif substat3 == "Elemental Mastery" :
        substatV3 = random.choice(elemasterysubstat)
        substat3 = ["Elemental Mastery", substatV3]
    elif substat3 == "Energy Recharge" :
        substatV3 = random.choice(energyrechargesubstat)
        substat3 = ["Energy Recharge", substatV3]
    elif substat3 == "HP%" :
        substatV3 = random.choice(hpercentsubstat)
        substat3 = ["HP%", substatV3]
    elif substat3 == "HP" :
        substatV3 = random.choice(hpsubstat)
        substat3 = ["HP", substatV3]
    chance = random.choice(substatchance)
    if chance >= 80 :
            substat4 = random.choice(substat)
            if substat4 == "ATK%":
                substatV4 = random.choice(atkpercentsubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "ATK":
                substatV4 = random.choice(atksubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "DEF%":
                substatV4 = random.choice(defpercentsubstat)
                substat4 = ["DEF%", substatV4]
            elif substat4 == "DEF":
                substatV4 = random.choice(defsubstat)
                substat4 = ["DEF", substatV4]
            elif substat4 == "Critical Rate":
                substatV4 = random.choice(critratesubstat)
                substat4 = ["Critical Rate", substatV4]
            elif substat4 == "Critical Damage":
                substatV4 = random.choice(critdamagesubstat)
                substat4 = ["Critical Damage", substatV4]
            elif substat4 == "Elemental Mastery":
                substatV4 = random.choice(elemasterysubstat)
                substat4 = ["Elemental Mastery", substatV4]
            elif substat4 == "Energy Recharge":
                substatV4 = random.choice(energyrechargesubstat)
                substat4 = ["Energy Recharge", substatV4]
            elif substat4 == "HP%":
                substatV4 = random.choice(hpercentsubstat)
                substat4 = ["HP%", substatV4]
            elif substat4 == "HP":
                substatV4 = random.choice(hpsubstat)
                substat4 = ["HP", substatV4]
if artitype ==  "Timepiece" :
    print("Artifact : Timepiece")
    MainStat = random.choice(mainstatTP)
    if MainStat in substat :
        if MainStat in substat:
            substat.remove(MainStat)
        if MainStat in ["ATK%", "HP%"]:
            MainStat = [MainStat, 7]
        elif MainStat == "DEF%":
            MainStat = ["DEF%", 8.7]
        elif MainStat == "Elemental Mastery":
            MainStat = ["Elemental Mastery", 28]
        elif MainStat == "Critical Rate":
            MainStat = ["Critical Rate", 4.7]
        elif MainStat == "Critical Damage":
            MainStat = ["Critical Damage", 9.3]
        elif MainStat == "Healing Bonus":
            MainStat = ["Healing Bonus", 5.4]
        ####SubStat 1####
        substat1 = random.choice(substat)
        substat.remove(substat1)
        if substat1 == "ATK%":
            substatV1 = random.choice(atkpercentsubstat)
            substat1 = ["ATK", substatV1]
        elif substat1 == "ATK":
            substatV1 = random.choice(atksubstat)
            substat1 = ["ATK", substatV1]
        elif substat1 == "DEF%":
            substatV1 = random.choice(defpercentsubstat)
            substat1 = ["DEF%", substatV1]
        elif substat1 == "DEF":
            substatV1 = random.choice(defsubstat)
            substat1 = ["DEF", substatV1]
        elif substat1 == "Critical Rate":
            substatV1 = random.choice(critratesubstat)
            substat1 = ["Critical Rate", substatV1]
        elif substat1 == "Critical Damage":
            substatV1 = random.choice(critdamagesubstat)
            substat1 = ["Critical Damage", substatV1]
        elif substat1 == "Elemental Mastery":
            substatV1 = random.choice(elemasterysubstat)
            substat1 = ["Elemental Mastery", substatV1]
        elif substat1 == "Energy Recharge":
            substatV1 = random.choice(energyrechargesubstat)
            substat1 = ["Energy Recharge", substatV1]
        elif substat1 == "HP%":
            substatV1 = random.choice(hpercentsubstat)
            substat1 = ["HP%", substatV1]
        elif substat1 == "HP":
            substatV1 = random.choice(hpsubstat)
            substat1 = ["HP", substatV1]
        #### SubStat 2 ####
        substat2 = random.choice(substat)
        substat.remove(substat2)
        if substat2 == "ATK%":
            substatV2 = random.choice(atkpercentsubstat)
            substat2 = ["ATK", substatV2]
        elif substat2 == "ATK":
            substatV2 = random.choice(atksubstat)
            substat2 = ["ATK", substatV2]
        elif substat2 == "DEF%":
            substatV2 = random.choice(defpercentsubstat)
            substat2 = ["DEF%", substatV2]
        elif substat2 == "DEF":
            substatV2 = random.choice(defsubstat)
            substat2 = ["DEF", substatV2]
        elif substat2 == "Critical Rate":
            substatV2 = random.choice(critratesubstat)
            substat2 = ["Critical Rate", substatV2]
        elif substat2 == "Critical Damage":
            substatV2 = random.choice(critdamagesubstat)
            substat2 = ["Critical Damage", substatV2]
        elif substat2 == "Elemental Mastery":
            substatV2 = random.choice(elemasterysubstat)
            substat2 = ["Elemental Mastery", substatV2]
        elif substat2 == "Energy Recharge":
            substatV2 = random.choice(energyrechargesubstat)
            substat2 = ["Energy Recharge", substatV2]
        elif substat2 == "HP%":
            substatV2 = random.choice(hpercentsubstat)
            substat2 = ["HP%", substatV2]
        elif substat2 == "HP":
            substatV2 = random.choice(hpsubstat)
            substat2 = ["HP", substatV2]
        #### SubStat 3 ####
        substat3 = random.choice(substat)
        substat.remove(substat3)
        if substat3 == "ATK%":
            substatV3 = random.choice(atkpercentsubstat)
            substat3 = ["ATK", substatV3]
        elif substat3 == "ATK":
            substatV3 = random.choice(atksubstat)
            substat3 = ["ATK", substatV3]
        elif substat3 == "DEF%":
            substatV3 = random.choice(defpercentsubstat)
            substat3 = ["DEF%", substatV3]
        elif substat3 == "DEF":
            substatV3 = random.choice(defsubstat)
            substat3 = ["DEF", substatV3]
        elif substat3 == "Critical Rate":
            substatV3 = random.choice(critratesubstat)
            substat3 = ["Critical Rate", substatV3]
        elif substat3 == "Critical Damage":
            substatV3 = random.choice(critdamagesubstat)
            substat3 = ["Critical Damage", substatV3]
        elif substat3 == "Elemental Mastery":
            substatV3 = random.choice(elemasterysubstat)
            substat3 = ["Elemental Mastery", substatV3]
        elif substat3 == "Energy Recharge":
            substatV3 = random.choice(energyrechargesubstat)
            substat3 = ["Energy Recharge", substatV3]
        elif substat3 == "HP%":
            substatV3 = random.choice(hpercentsubstat)
            substat3 = ["HP%", substatV3]
        elif substat3 == "HP":
            substatV3 = random.choice(hpsubstat)
            substat3 = ["HP", substatV3]
        chance = random.choice(substatchance)
        if chance >= 80:
            substat4 = random.choice(substat)
            if substat4 == "ATK%":
                substatV4 = random.choice(atkpercentsubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "ATK":
                substatV4 = random.choice(atksubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "DEF%":
                substatV4 = random.choice(defpercentsubstat)
                substat4 = ["DEF%", substatV4]
            elif substat4 == "DEF":
                substatV4 = random.choice(defsubstat)
                substat4 = ["DEF", substatV4]
            elif substat4 == "Critical Rate":
                substatV4 = random.choice(critratesubstat)
                substat4 = ["Critical Rate", substatV4]
            elif substat4 == "Critical Damage":
                substatV4 = random.choice(critdamagesubstat)
                substat4 = ["Critical Damage", substatV4]
            elif substat4 == "Elemental Mastery":
                substatV4 = random.choice(elemasterysubstat)
                substat4 = ["Elemental Mastery", substatV4]
            elif substat4 == "Energy Recharge":
                substatV4 = random.choice(energyrechargesubstat)
                substat4 = ["Energy Recharge", substatV4]
            elif substat4 == "HP%":
                substatV4 = random.choice(hpercentsubstat)
                substat4 = ["HP%", substatV4]
            elif substat4 == "HP":
                substatV4 = random.choice(hpsubstat)
                substat4 = ["HP", substatV4]
if artitype ==  "Feather" :
    print("Artifact : Feather")
    MainStat = "ATK"
    if MainStat in substat :
        substat.remove(MainStat)
        ####SubStat 1####
        substat1 = random.choice(substat)
        substat.remove(substat1)
        if substat1 == "ATK%":
            substatV1 = random.choice(atkpercentsubstat)
            substat1 = ["ATK", substatV1]
        elif substat1 == "ATK":
            substatV1 = random.choice(atksubstat)
            substat1 = ["ATK", substatV1]
        elif substat1 == "DEF%":
            substatV1 = random.choice(defpercentsubstat)
            substat1 = ["DEF%", substatV1]
        elif substat1 == "DEF":
            substatV1 = random.choice(defsubstat)
            substat1 = ["DEF", substatV1]
        elif substat1 == "Critical Rate":
            substatV1 = random.choice(critratesubstat)
            substat1 = ["Critical Rate", substatV1]
        elif substat1 == "Critical Damage":
            substatV1 = random.choice(critdamagesubstat)
            substat1 = ["Critical Damage", substatV1]
        elif substat1 == "Elemental Mastery":
            substatV1 = random.choice(elemasterysubstat)
            substat1 = ["Elemental Mastery", substatV1]
        elif substat1 == "Energy Recharge":
            substatV1 = random.choice(energyrechargesubstat)
            substat1 = ["Energy Recharge", substatV1]
        elif substat1 == "HP%":
            substatV1 = random.choice(hpercentsubstat)
            substat1 = ["HP%", substatV1]
        elif substat1 == "HP":
            substatV1 = random.choice(hpsubstat)
            substat1 = ["HP", substatV1]
        #### SubStat 2 ####
        substat2 = random.choice(substat)
        substat.remove(substat2)
        if substat2 == "ATK%":
            substatV2 = random.choice(atkpercentsubstat)
            substat2 = ["ATK", substatV2]
        elif substat2 == "ATK":
            substatV2 = random.choice(atksubstat)
            substat2 = ["ATK", substatV2]
        elif substat2 == "DEF%":
            substatV2 = random.choice(defpercentsubstat)
            substat2 = ["DEF%", substatV2]
        elif substat2 == "DEF":
            substatV2 = random.choice(defsubstat)
            substat2 = ["DEF", substatV2]
        elif substat2 == "Critical Rate":
            substatV2 = random.choice(critratesubstat)
            substat2 = ["Critical Rate", substatV2]
        elif substat2 == "Critical Damage":
            substatV2 = random.choice(critdamagesubstat)
            substat2 = ["Critical Damage", substatV2]
        elif substat2 == "Elemental Mastery":
            substatV2 = random.choice(elemasterysubstat)
            substat2 = ["Elemental Mastery", substatV2]
        elif substat2 == "Energy Recharge":
            substatV2 = random.choice(energyrechargesubstat)
            substat2 = ["Energy Recharge", substatV2]
        elif substat2 == "HP%":
            substatV2 = random.choice(hpercentsubstat)
            substat2 = ["HP%", substatV2]
        elif substat2 == "HP":
            substatV2 = random.choice(hpsubstat)
            substat2 = ["HP", substatV2]
        #### SubStat 3 ####
        substat3 = random.choice(substat)
        substat.remove(substat3)
        if substat3 == "ATK%":
            substatV3 = random.choice(atkpercentsubstat)
            substat3 = ["ATK", substatV3]
        elif substat3 == "ATK":
            substatV3 = random.choice(atksubstat)
            substat3 = ["ATK", substatV3]
        elif substat3 == "DEF%":
            substatV3 = random.choice(defpercentsubstat)
            substat3 = ["DEF%", substatV3]
        elif substat3 == "DEF":
            substatV3 = random.choice(defsubstat)
            substat3 = ["DEF", substatV3]
        elif substat3 == "Critical Rate":
            substatV3 = random.choice(critratesubstat)
            substat3 = ["Critical Rate", substatV3]
        elif substat3 == "Critical Damage":
            substatV3 = random.choice(critdamagesubstat)
            substat3 = ["Critical Damage", substatV3]
        elif substat3 == "Elemental Mastery":
            substatV3 = random.choice(elemasterysubstat)
            substat3 = ["Elemental Mastery", substatV3]
        elif substat3 == "Energy Recharge":
            substatV3 = random.choice(energyrechargesubstat)
            substat3 = ["Energy Recharge", substatV3]
        elif substat3 == "HP%":
            substatV3 = random.choice(hpercentsubstat)
            substat3 = ["HP%", substatV3]
        elif substat3 == "HP":
            substatV3 = random.choice(hpsubstat)
            substat3 = ["HP", substatV3]
        chance = random.choice(substatchance)
        if chance >= 80:
            substat4 = random.choice(substat)
            if substat4 == "ATK%":
                substatV4 = random.choice(atkpercentsubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "ATK":
                substatV4 = random.choice(atksubstat)
                substat4 = ["ATK", substatV4]
            elif substat4 == "DEF%":
                substatV4 = random.choice(defpercentsubstat)
                substat4 = ["DEF%", substatV4]
            elif substat4 == "DEF":
                substatV4 = random.choice(defsubstat)
                substat4 = ["DEF", substatV4]
            elif substat4 == "Critical Rate":
                substatV4 = random.choice(critratesubstat)
                substat4 = ["Critical Rate", substatV4]
            elif substat4 == "Critical Damage":
                substatV4 = random.choice(critdamagesubstat)
                substat4 = ["Critical Damage", substatV4]
            elif substat4 == "Elemental Mastery":
                substatV4 = random.choice(elemasterysubstat)
                substat4 = ["Elemental Mastery", substatV4]
            elif substat4 == "Energy Recharge":
                substatV4 = random.choice(energyrechargesubstat)
                substat4 = ["Energy Recharge", substatV4]
            elif substat4 == "HP%":
                substatV4 = random.choice(hpercentsubstat)
                substat4 = ["HP%", substatV4]
            elif substat4 == "HP":
                substatV4 = random.choice(hpsubstat)
                substat4 = ["HP", substatV4]
if artitype ==  "Flower" :
    print("Artifact : Flower")
    MainStat = "HP"
    substat.remove(MainStat)
    ####SubStat 1####
    substat1 = random.choice(substat)
    substat.remove(substat1)
    if substat1 == "ATK%":
        substatV1 = random.choice(atkpercentsubstat)
        substat1 = ["ATK", substatV1]
    elif substat1 == "ATK":
        substatV1 = random.choice(atksubstat)
        substat1 = ["ATK", substatV1]
    elif substat1 == "DEF%":
        substatV1 = random.choice(defpercentsubstat)
        substat1 = ["DEF%", substatV1]
    elif substat1 == "DEF":
        substatV1 = random.choice(defsubstat)
        substat1 = ["DEF", substatV1]
    elif substat1 == "Critical Rate":
        substatV1 = random.choice(critratesubstat)
        substat1 = ["Critical Rate", substatV1]
    elif substat1 == "Critical Damage":
        substatV1 = random.choice(critdamagesubstat)
        substat1 = ["Critical Damage", substatV1]
    elif substat1 == "Elemental Mastery":
        substatV1 = random.choice(elemasterysubstat)
        substat1 = ["Elemental Mastery", substatV1]
    elif substat1 == "Energy Recharge":
        substatV1 = random.choice(energyrechargesubstat)
        substat1 = ["Energy Recharge", substatV1]
    elif substat1 == "HP%":
        substatV1 = random.choice(hpercentsubstat)
        substat1 = ["HP%", substatV1]
    elif substat1 == "HP":
        substatV1 = random.choice(hpsubstat)
        substat1 = ["HP", substatV1]
    #### SubStat 2 ####
    substat2 = random.choice(substat)
    substat.remove(substat2)
    if substat2 == "ATK%":
        substatV2 = random.choice(atkpercentsubstat)
        substat2 = ["ATK", substatV2]
    elif substat2 == "ATK":
        substatV2 = random.choice(atksubstat)
        substat2 = ["ATK", substatV2]
    elif substat2 == "DEF%":
        substatV2 = random.choice(defpercentsubstat)
        substat2 = ["DEF%", substatV2]
    elif substat2 == "DEF":
        substatV2 = random.choice(defsubstat)
        substat2 = ["DEF", substatV2]
    elif substat2 == "Critical Rate":
        substatV2 = random.choice(critratesubstat)
        substat2 = ["Critical Rate", substatV2]
    elif substat2 == "Critical Damage":
        substatV2 = random.choice(critdamagesubstat)
        substat2 = ["Critical Damage", substatV2]
    elif substat2 == "Elemental Mastery":
        substatV2 = random.choice(elemasterysubstat)
        substat2 = ["Elemental Mastery", substatV2]
    elif substat2 == "Energy Recharge":
        substatV2 = random.choice(energyrechargesubstat)
        substat2 = ["Energy Recharge", substatV2]
    elif substat2 == "HP%":
        substatV2 = random.choice(hpercentsubstat)
        substat2 = ["HP%", substatV2]
    elif substat2 == "HP":
        substatV2 = random.choice(hpsubstat)
        substat2 = ["HP", substatV2]
    #### SubStat 3 ####
    substat3 = random.choice(substat)
    substat.remove(substat3)
    if substat3 == "ATK%":
        substatV3 = random.choice(atkpercentsubstat)
        substat3 = ["ATK", substatV3]
    elif substat3 == "ATK":
        substatV3 = random.choice(atksubstat)
        substat3 = ["ATK", substatV3]
    elif substat3 == "DEF%":
        substatV3 = random.choice(defpercentsubstat)
        substat3 = ["DEF%", substatV3]
    elif substat3 == "DEF":
        substatV3 = random.choice(defsubstat)
        substat3 = ["DEF", substatV3]
    elif substat3 == "Critical Rate":
        substatV3 = random.choice(critratesubstat)
        substat3 = ["Critical Rate", substatV3]
    elif substat3 == "Critical Damage":
        substatV3 = random.choice(critdamagesubstat)
        substat3 = ["Critical Damage", substatV3]
    elif substat3 == "Elemental Mastery":
        substatV3 = random.choice(elemasterysubstat)
        substat3 = ["Elemental Mastery", substatV3]
    elif substat3 == "Energy Recharge":
        substatV3 = random.choice(energyrechargesubstat)
        substat3 = ["Energy Recharge", substatV3]
    elif substat3 == "HP%":
        substatV3 = random.choice(hpercentsubstat)
        substat3 = ["HP%", substatV3]
    elif substat3 == "HP":
        substatV3 = random.choice(hpsubstat)
        substat3 = ["HP", substatV3]
    chance = random.choice(substatchance)
    if chance >= 80:
        substat4 = random.choice(substat)
        if substat4 == "ATK%":
            substatV4 = random.choice(atkpercentsubstat)
            substat4 = ["ATK", substatV4]
        elif substat4 == "ATK":
            substatV4 = random.choice(atksubstat)
            substat4 = ["ATK", substatV4]
        elif substat4 == "DEF%":
            substatV4 = random.choice(defpercentsubstat)
            substat4 = ["DEF%", substatV4]
        elif substat4 == "DEF":
            substatV4 = random.choice(defsubstat)
            substat4 = ["DEF", substatV4]
        elif substat4 == "Critical Rate":
            substatV4 = random.choice(critratesubstat)
            substat4 = ["Critical Rate", substatV4]
        elif substat4 == "Critical Damage":
            substatV4 = random.choice(critdamagesubstat)
            substat4 = ["Critical Damage", substatV4]
        elif substat4 == "Elemental Mastery":
            substatV4 = random.choice(elemasterysubstat)
            substat4 = ["Elemental Mastery", substatV4]
        elif substat4 == "Energy Recharge":
            substatV4 = random.choice(energyrechargesubstat)
            substat4 = ["Energy Recharge", substatV4]
        elif substat4 == "HP%":
            substatV4 = random.choice(hpercentsubstat)
            substat4 = ["HP%", substatV4]
        elif substat4 == "HP":
            substatV4 = random.choice(hpsubstat)
            substat4 = ["HP", substatV4]


print(" Mains stat:", MainStat)
print("Substats:    ")
print(" ", substat1)
print(" ", substat2)
print(" ", substat3)
if substat4 != 0:
    print(" ", substat4)