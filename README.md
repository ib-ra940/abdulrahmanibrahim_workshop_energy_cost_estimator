# Workshop Energy Cost Estimator

## What it does
This program asks for each workshop machine's name, power (watts) and hours used per day. It then calculates the daily and monthly energy in kWh and the cost at the user's tariff in Naira per kWh.

## How to run it
Install Python 3, then run: python energy_estimator.py

## Sample output
```
=== Workshop Energy Cost Estimator ===
How many machines? 2
Enter your tariff (Naira per kWh): 209.5

--- Machine 1 ---
Name: Lathe
Power (watts): 2200
Hours used per day (max 24): 5

--- Machine 2 ---
Name: Welder
Power (watts): 4000
Hours used per day (max 24): 2

=== RESULTS ===
Machine              kWh/day   kWh/month
Lathe                  11.00      330.00
Welder                  8.00      240.00
----------------------------------------
Total daily energy:   19.00 kWh
Total monthly energy: 570.00 kWh (30 days)
Daily cost:           N3,980.50
Monthly cost:         N119,415.00

=== BIGGEST ENERGY USER ===
Lathe uses 57.9% of your energy.
Tip: this machine dominates your bill. Reduce its running hours first.
```

## My own twist
The program finds the machine that uses the most energy, shows its percentage share of the total, and gives a tip on how to cut the bill.

## What I learned
- How to check input with try/except so the program does not crash when a letter is typed instead of a number.
- How to use lists and a loop to store and process data for many machines.

## Author
Abdulrahman Ibrahim, ND2 Mechatronics Engineering, YabaTech.
