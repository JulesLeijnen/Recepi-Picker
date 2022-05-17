import jsonpickle


#----------------------IMPORTS----------------------------------
#----------------------MAIN-------------------------------------

def main():
    return

#----------------------MAIN-------------------------------------
#----------------------Classes----------------------------------

#//-------------------------------------------------
class Recipie:
    def __init__(self, _name, _prepTime, _ingredientsPP, _whoCanEat, _freqWeight):
        self.name = _name
        self.prepTime = _prepTime
        self.ingredientsPP = _ingredientsPP
        self.whoCanEat = _whoCanEat
        self.freqWeight = _freqWeight
    
    def calculateAmountsAndPrice(self, amountPeople):
        amountPeople = amountPeople
        Total = None
        return Total
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
