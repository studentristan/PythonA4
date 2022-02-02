#assignment 4.7
#Tristan Werden
#Todo: None

def computegrade(score) :
    if (score > 1) or  (score < 0) :
        return("that is not a valid number please use 0-1")
        quit()
    elif score >= .9 :
        return("A")
    elif score >= .8 :
        return("B")
    elif score >= .7 :
        return("C")
    elif score >= .6 :
        return("D")
    else :
        return("F")

try :
    score = float(input("input score: "))
except :
    print("that is not a number please use numeric input")
    quit()

print(computegrade(score))
