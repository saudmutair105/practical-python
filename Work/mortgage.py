# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
totalpaid = 0.0
months = 0
month = 0
extra_payment = 1000
extra_begin = 60
extra_end = 108

while principal > 0:

    if extra_begin <= months + 1 <= extra_end:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        totalpaid = totalpaid + payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        totalpaid = totalpaid + payment
    months = months + 1
    month = month + 1
    print(month, totalpaid, principal)
# Exercise 1.7
