# Constants
DATA = 10

def main():
    #Inputs
    gb_used = int(input("How much data did you use?: "))
    base_cost = float(input("wuts ur base cost?: "))


    total_cost = base_cost
    if gb_used <= DATA: 
        print("within data limit")
    elif gb_used > DATA:
        if gb_used < DATA + 5:
            print("moderate data usage")
        else:
            print("high usage")
        total_cost = 40 + (gb_used - DATA) * 2

    print(total_cost)
main()