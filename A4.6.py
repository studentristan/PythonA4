#assignment 4.6
#Tristan Werden
#Todo: None

def computepay(hours, rate) :
    total = hours * rate

    if hours > 40 :
        overtime = hours - 40
        overtimePay = overtime * (rate * .5)
        total = total + overtimePay
    return (total)

try :
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except :
    print("Error, please enter numeric input")
    quit()

print("Pay " + str(computepay(hours, rate)))
