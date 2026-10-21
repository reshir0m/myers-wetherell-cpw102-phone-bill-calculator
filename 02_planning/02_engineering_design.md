# Engineering Design

**Team members:**

Plan how your code will meet the product requirements. Keep answers brief.

## Inputs

*List each input and its Python data type. Note the input assumptions.*
Data Used
Base Cost of Plan

## Processing and decisions

*What calculations and conversions are needed? How will you organize the decisions, including the nested decision?*
Check data usage
Determine if user has under, normal, moderate, or high usage
Calculate base data price + data usage = total
    [
        if our user's data usage is low
            print "within data limit"
        elif our user's data usage within limit
            print "within data limit"
        elif data usage is moderate
            print(f"moderate extra usage : {data_calc_over}")
        elif data usage is high:
            print(f"high extra usage: {data_calc_over}")
    ]
## Output

*What will the program display for each usage category?*
Low Usage : print "within data limit"
Normal Usage : print "within data limit"
Moderate Usage: print "moderate extra usage"
High Usage: print "high extra usage"

## Function design

*Give your data-allowance-checking function's name, parameters, and returned result. How will the program use that result?*

