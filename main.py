#TODO:
#   Logging
#   ErrorHandling

import pickle
import sqlite3
from sqlite3 import Error
import logging
import os

#TEMP
#TEMP
def error():
    print("temp ERROR")
    exit(1)
#TEMP
#TEMP

#----------------------IMPORTS----------------------------------
#GlobalVars
DBFileNames = ["Recipies.db", "Ingredients.db"]
DBFilePath = ".\Database"

#----------------------MAIN-------------------------------------

def main():
    return

#----------------------MAIN-------------------------------------
#----------------------INITIATE---------------------------------

def init():
    global DBFileNames, DBFilePath
    checks = init_checks() #checks all needed things before main part of program starts (Correct loading libs, needed files, etc.)
    print(checks)
    if checks == None:
        error()
        pass
    SQLiteConnect(DBFileNames, DBFilePath)
    return

def init_checks():
    global DBFileNames, DBFilePath
    checksOutput = [] #Create variable that gets passed if code fails completely somehow
    DBFilesChecked = []

    #check if needed files are there
    for filename in DBFileNames:
        if filename in os.listdir(DBFilePath):
            DBFilesChecked.append(filename)
            pass
        else:
            #Log fuckup
            #flag empty lists because of new making
            for names in DBFileNames:
                with open("{}\{}".format(DBFilePath, names), 'x') as file: #create file with filename
                    pass
                #log creation file
    #logging all db files there, with flag if needed
    checksOutput.append(DBFilesChecked) #Here the first element wil be a list of all files checked that were needed

    return checksOutput

def SQLiteConnect(Filenames, FilePath):
    
    RecepiePath = "{}\{}".format(FilePath, Filenames[0])
    IngredientsPath = "{}\{}".format(FilePath, Filenames[1])

    try:
        RecepieDB = sqlite3.connect(RecepiePath)
        IngredientDB = sqlite3.connect(IngredientsPath)
        print(sqlite3.version)
        print(type(RecepieDB))
    except Error as e:
        print(e)
    finally:
        if RecepieDB and IngredientDB:
            RecepieDB.close()
            IngredientDB.close()


    return RecepieDB, IngredientDB

#----------------------INITIATE---------------------------------

#----------------------Classes----------------------------------

#//-------------------------------------------------
class Recipie:
    def __init__(self, _name, _prepTime, _ingredientsPP, _ingredientsDosage, _whoCanEat, _freqWeight):
        self.name = _name
        self.prepTime = _prepTime
        self.ingredientsPP = _ingredientsPP
        self.ingredientsDosage = _ingredientsDosage
        self.whoCanEat = _whoCanEat
        self.freqWeight = _freqWeight
#//-------------------------------------------------
class Ingredient:
    def __init__(self, _name, _unit, _pricePerUnit, _allergens):
        self.name = _name
        self.unit = _unit
        self.pricePerUnit = _pricePerUnit
        self.allergens = _allergens
#//-------------------------------------------------

#----------------------Classes----------------------------------
#----------------------StoreInstanceInJSON----------------------

# temp1 = Recipie("test1", 60, [], [], [], 1)
# print(temp1)
# JSONString = jsonpickle.encode(temp1)
# print(JSONString)
SQLiteConnect(DBFileNames, DBFilePath)
# init_checks()