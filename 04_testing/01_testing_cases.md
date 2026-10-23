# Test Cases

Run each case separately. Determine the expected results by hand before running your program.

From the repository folder, run:

```text
python 03_execution/data_bill.py
```

Check the usage message, overage amount when applicable, and total bill. Paste each terminal run as evidence, then mark Pass or Fail and explain why.

## Case 1: At the data limit

- Data used (GB): 10
- Base plan cost: 40

**Expected results:**
10 GB is not over the 10 GB limit, so there's no overage charge.
Message: "You are within your data limit"
Total bill: $40.00

**Evidence (paste your terminal run):**

```text

C:\Users\zelda\Documents\GitHub\myers-wetherell-cpw102-phone-bill-calculator\03_execution> python data_bill.py
How much data did you use (GB)?: 10
What is your base cost?: 40
You are within your data limit.
Your total bill is: $40.00
```

**Pass / Fail and why:**
Pass, correct result of being exactly at customer's data limit of 10 GB, so the program only charged the base cost.

## Case 2: At 5 GB over the limit

- Data used (GB): 15
- Base plan cost: 40

**Expected results:**
15 GB is 5 over the limit of 10.
5GB is also the moderate usage cutoff so it counts as moderate, not high.
Message: "You are 5 GB over your limit" and "Moderate extra usage"
Total bill: $50.00     #$40.00 + (5 *$2) = $40.00 + $10.00 = $50.00

**Evidence (paste your terminal run):**

```text

C:\Users\zelda\Documents\GitHub\myers-wetherell-cpw102-phone-bill-calculator\03_execution> python data_bill.py
How much data did you use (GB)?: 15
What is your base cost?: 40
You are 5.0 GB over your limit.
Moderate extra usage.
Your total bill is: $50.00
```

**Pass / Fail and why:**
Pass. The program correctly showed 5.0 GB over the limit and labeled it as moderate extra usage.

## Case 3: Above 5 GB over the limit

- Data used (GB): 15.5
- Base plan cost: 50

**Expected results:**
15.5 GB is 5.5 GB over the 10 GB limit, which will be counted as high extra usage.
Message: "You are 5.5 GB over your limit." and "High extra usage."
Total bill: $61.00     # $50.00 + (5.5 * $2) = $50.00 + $11 = $61.00

**Evidence (paste your terminal run):**

```text

C:\Users\zelda\Documents\GitHub\myers-wetherell-cpw102-phone-bill-calculator\03_execution> python data_bill.py
How much data did you use (GB)?: 15.5
What is your base cost?: 50
You are 5.5 GB over your limit.
High extra usage.
Your total bill is: $61.00
```

**Pass / Fail and why:**
Pass. The program accepted the decimal input, correctly showed 5.5 GB over the limit and labeled it as high extra usage.

If a case fails, fix the program and add evidence of the rerun below that case.

