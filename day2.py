#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line 
bill = float(input("What is the bill :\n$"))
people = int(input("How many people are gonna split the bill?\n"))
percentage = int(input("How much percentage tip you want to pay?\n%"))
a = (bill / people) * (1+(percentage/100))
price = round(a, 2)
#price = "{:.2f}".format(a)
print("Each person should pay : $" + str(price))