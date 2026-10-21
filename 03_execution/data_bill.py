# Constants
DATA = 10

def main():
    #Inputs
    gb_used = input("How much data did you use?: ")
    base_cost = input()

    total_cost = base_cost
    if gb_used < DATA:
        print("within data limit")

main()