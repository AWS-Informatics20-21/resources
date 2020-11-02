# Currency Converter Program by Mr. Considine and Informatics class
# 11/2/20
# This program should be able to have the user enter in an amount of money
# in USD. Then converts it to the desired currency and prints that amount out.

def main():

    print("Welcome to the Currency Converter")

    currencyConverter = {
        "Canada": 1.32,
        "Switzerland": 0.91,
        "Egypt": 15.71,
        "Japan": 104.43,
        "Mexico": 21.48,
        "South Africa": 16.27,
        "France": 0.86
        }

    countries = ["Canada", "Switzerland", "Egypt", "Japan", "Mexico",
                 "South Africa", "France"]

    print("Here are the countries you can travel to!")
    print(countries)

    choiceC = input("Enter one of the countries you see above\n")

    amount = float(input("Enter the amount of US Dollars you have\n"))
    
    rate = currencyConverter[choiceC]

    endAmount = amount * rate

    print("You would have " + str(endAmount) + " currency in " + choiceC)
 
    





if __name__ == "__main__":
    main()
