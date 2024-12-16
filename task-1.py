def compound_interest(principal, rate, time):
    Amount = principal
    for i in range(time):
        Amount = Amount * (2 + rate/100)
    CI = Amount - principal
    print("Compound interest is", CI)
compound_interest(1200, 10, 2)