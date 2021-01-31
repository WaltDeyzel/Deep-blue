from random import randint
import random
from numpy import random as npR

def lookIn(path, child):

    for cor in path:
        if cor not in child:
            child.append(cor)
    

def crossover(option_1, option_2):

    path_1 = option_1.getSolution()
    path_2 = option_2.getSolution()

    child_1 = path_1[:int(len(path_1)/2)]
    child_2 = path_2[:int(len(path_1)/2)]

    lookIn(path_1, child_1)
    lookIn(path_2, child_2)
    
    return(child_1)

def crossover2(option_1, option_2):

    path_1 = option_1.getSolution()
    path_2 = option_2.getSolution()

    half = int(len(path_1)/2)
    x = int(npR.uniform()*half)
    y = int(npR.uniform()*half)+half
    child_1 = path_1[x:y]
    lookIn(path_2, child_1)

    return(child_1)

def crossover3(option_1, option_2, option_3):

    path_1 = option_1.getSolution()
    path_2 = option_2.getSolution()
    path_3 = option_3.getSolution()

    third = int(len(path_1)/3)
    child = path_1[0:third]

    i = 1
    for cor in path_2:
        if cor not in child:
            child.append(cor)
            i += 1
        if i == third:
            i = 1
            break
    
    for cor in path_3:
        if cor not in child:
            child.append(cor)
            i += 1

    return(child)


if __name__ == "__main__":
       
    path_1 = [[-273, -1], [215, -65], [55, 142], [-192, -135], [-38, 133], [74, 120], [275, 299], [207, 188], [-153, 37], [82, 208], [1, 182], [-2, 99], [-190, 8], [-281, -128], [129, 36], [163, -129], [262, 242], [-299, 21], [153, 4], [210, 209], [109, -246], [179, -5], [-173, 28], [-156, -180], [268, -97], [238, 25], [-12, -174], [43, 275], [-12, -181], [-195, -217], [297, -54], [-258, 117], [275, -214], [45, 249], [-233, 154], [139, 171], [-194, -4], [295, -271], [101, 37], [-102, -163], [37, 229], [151, -297], [-148, -172], [263, -243], [-232, 230], [-253, 4], [35, 212], [267, -17], [-229, -38], [-11, 59]] 
 
    path_2 = [[82, 208], [1, 182], [-2, 99], [-190, 8], [-281, -128], [129, 36], [163, -129], [262, 242], [-299, 21], [153, 4], [210, 209], [-273, -1], [215, -65], [55, 142], [-192, -135], [-38, 133], [74, 120], [275, 299], [207, 188], [-153, 37], [109, -246], [179, -5], [-173, 28], [-156, -180], [268, -97], [238, 25], [-12, -174], [43, 275], [-12, -181], [-195, -217], [297, -54], [-258, 117], [275, -214], [45, 249], [-233, 154], [139, 171], [-194, -4], [295, -271], [101, 37], [-102, -163], [37, 229], [151, -297], [-148, -172], [263, -243], [-232, 230], [-253, 4], [35, 212], [267, -17], [-229, -38], [-11, 59]] 
 
    path_3 = [[163, -129], [262, 242], [-299, 21], [153, 4], [210, 209], [-273, -1], [215, -65], [55, 142], [-192, -135], [-38, 133], [74, 120], [275, 299], [207, 188], [-153, 37], [109, -246], [179, -5], [-173, 28], [-156, -180], [268, -97], [238, 25], [-12, -174], [43, 275], [-12, -181], [-195, -217], [297, -54], [-258, 117], [275, -214], [45, 249], [-233, 154], [139, 171], [-194, -4], [295, -271], [101, 37], [-102, -163], [37, 229], [151, -297], [-148, -172], [263, -243], [-232, 230], [-253, 4], [35, 212], [267, -17], [-229, -38], [82, 208], [1, 182], [-2, 99], [-190, 8], [-281, -128], [129, 36], [-11, 59]] 
 

    third = int(len(path_1)/3)
    child = path_1[0:third]
    print(child)
    print('len', len(path_1), len(child))
    i = 1
    for cor in path_2:
        if cor not in child:
            child.append(cor)
            i += 1
        if i == third:
            i = 1
            break
    print(child)
    print('len', len(path_1), len(child))
    for cor in path_3:
        if cor not in child:
            child.append(cor)
            i += 1

    print('len', len(path_1), len(child))