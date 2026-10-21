# Constants
DATA = 10

def main():
    #Inputs
    gb_used = int(input("How much data did you use?: "))
    base_cost = float(input("What is your base cost?: "))


    total_cost = base_cost
    if gb_used <= DATA: 
        print("Within data limit")
        
    elif gb_used > DATA:

        if gb_used < DATA + 5:
            print("Moderate Data Usage")
        else:
            print("High Data Usage")
        total_cost = 40 + (gb_used - DATA) * 2

    print(f"Total Cost: ${total_cost: .2f}")

main()