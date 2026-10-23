# Constants
DATA_LIMIT = 10
OVERAGE_RATE = 2
MODERATE_LIMIT = 5

def is_over_limit(gb_used):
    return gb_used > DATA_LIMIT

def main():
    #Inputs
    gb_used = float(input("How much data did you use (GB)?: "))
    base_cost = float(input("What is your base cost?: "))


    total_cost = base_cost
    if is_over_limit(gb_used):
        gb_over = gb_used - DATA_LIMIT
        print(f"You are {gb_over:.1f} GB over your limit.")

        if gb_over <= MODERATE_LIMIT:
            print("Moderate extra usage.")
        else:
            print("High extra usage.")
    
        total_cost = base_cost + gb_over * 2
    else:
        print("You are within your data limit.")


    print(f"Your total bill is: ${total_cost:.2f}")

main()



# if gb_used <= DATA: 
#         print("Within data limit")
#     elif gb_used > DATA:
#         if gb_used < DATA + 5:
#             print("Moderate Data Usage")
#         else:
#             print("High Data Usage")