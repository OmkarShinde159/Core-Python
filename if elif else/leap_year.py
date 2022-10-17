#WAP to check if the input year/ Enter year is leap year or not

# leap year is a year occure once in every four year
# century leap year is divisible by 100 and 400

year = int(input("Enter a year: ")

if year % 400==0 or year % 100!=0 and year % 4==0:
    print(year,"Year is a leap year")
else:
    print(year,"is not a leap year")
    
