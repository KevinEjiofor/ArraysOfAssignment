investment = 1000
rate_of_return = 7 / 100
for year in range(1, 31):
    print("year", year, 'Amount deposited =$ ', investment * ((1 + rate_of_return) ** year))