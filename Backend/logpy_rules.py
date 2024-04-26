from kanren import Relation, facts, run, lall, var,lany, conde, eq, membero 
from collections.abc import Iterable


resonante = Relation()
value_within_range_rel = Relation()
categorize_measure_rel = Relation()

def value_within_range(value):
    return ((value <= 5) and (value >= -5))

def categorize_measure(dict_of_failling_frecuencies, qty):
    print(len(dict_of_failling_frecuencies))
    print(qty)
    if(len(dict_of_failling_frecuencies)!=qty): 
        return "measurementError"
    elif all(value > 5 for value in dict_of_failling_frecuencies.values()):
        return "volumeTooHigh"
    elif all(value < -5 for value in dict_of_failling_frecuencies.values()):
        return "volumeTooLow"


#All the facts. Each value to right has it's resonant to the left and viceversa
facts(resonante, (20, 40))
facts(resonante, (40, 80))
facts(resonante, (30, 60))
facts(resonante, (60, 120))
facts(resonante, (50, 100))
facts(resonante, (100, 200))
facts(resonante, (150, 300))
facts(resonante, (300, 600))
facts(resonante, (600, 1200))
facts(resonante, (200, 400))
facts(resonante, (400, 800))
facts(resonante, (500, 1000))
facts(resonante, (1000, 2000))
facts(resonante, (2000, 4000))
facts(resonante, (4000, 8000))
facts(resonante, (3000, 6000))
facts(resonante, (6000, 12000))
facts(resonante, (5000, 10000))
facts(resonante, (10000, 20000))


#This method checks iteratively the facts and produces a list with all the resonants that needs to be checked
def give_me_resonantes(value):
    resonant_values = []
    resonant_values.append(value)
    while True:
        x = var() 
        resonant = run(0, x, resonante(value, x))
        if resonant:
            resonant_values.append(resonant[0])
            value = resonant[0]
        else:
            break;
    return resonant_values


