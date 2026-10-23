# Engineering Design

**Team members:**
Owen Wetherell
Damon Myers

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

*List each input and its Python data type. Note the input assumptions.*

gb used as a float
base cost as a float
input is assumed numeric

## Processing and decisions

*What calculations and conversions are needed? How will you organize the decisions, including the nested decision?*
Get data used (GB) from the user
Get base plan cost from the user
Set total cost to the base plan cost

Call is_over_limit with data used
[
If is_over_limit returns True:
       Calculate GB over = data used - 10
    Display how many GB over the limit
    If GB over is 5 or less:
        Display "Moderate extra usage"
    Else:
        Display "High extra usage"
    Add GB over x $2 to the total cost
Else:
    Display "You are within your data limit"

Display the total bill formatted as dollars
]
## Output

*What will the program display for each usage category?*

Within limit (10 GB or less):
    "You are within your data limit"
    "Your total bill is: $XX.XX"

Moderate (over 10 GB, up to 5 GB over):
    "You are X.X GB over your limit."
    "Moderate Extra Usage."
    "Your total bill is: $XX.XX"

High (more than 5 GB over):
    "You are X.X GB over your limit."
    "High extra usage."
    "Your total bill is: $XX.XX"

## Function design

*Give your data-allowance-checking function's name, parameters, and returned result. How will the program use that result?*

Name: is_over_limit

Parameter: True if gb_used is more than 10 GB, False if it is 10 GB or less.

How the program uses it: 
main() calls is_over_limit(gb_used) and uses the result in an if statement. 
If it returns True, the program calculates how many GB over the limit the customer went, uses a nested if to decide if the extra usage is moderate or high, 
and adds $2 per extra GB to the bill. If it returns False, the program tells the customer they are within their data limit and the bill is just the base plan cost.