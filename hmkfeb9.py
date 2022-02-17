#SMALL

# #1 #Prompt the user for his name using the input function. Example:
# name = input('What is your name? ')
# print("Hello,", name,"!")

#alternatively you can do an f'string like p28 of the python 101 course
#print(f"Hello, {firstName}")

#2 #Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name.
#(Hint: You'll want to search for documentation on how to uppercase a string.)

#aqString.ToUpper- to make it uppercase-(googled a bad page)
# aqString.ToUpper (this is how other peeps in study group found it on https://www.datacamp.com/search?q=python) and here: https://thehelloworldprogram.com/python/python-string-methods/#:~:text=Performing%20the%20.,of%20the%20characters%20to%20lowercase.

# name = input('WHAT IS YOUR NAME?')- this doesn't have to be caps
# name.upper()
# print("HELLO,", name.upper(),"!")
# print("YOUR NAME HAS", len(name), "LETTERS IN IT! AWESOME!")

# name = input('what is your name?')
# name.upper()
# print("HELLO,", name.upper(),"!")   
# or better to use an f string: print(f"HELLO, {name.upper()}!")
# print("YOUR NAME HAS", len(name), "LETTERS IN IT! AWESOME!")



#3. #Prompt the user for the missing words to a Madlib sentence using the input function. You can make up your own Madlib sentence, but here's an example:
# print("Please fill in the blanks below:")
# print("input('what is name?'), "'s favorite subject in school is," input('what is subject?'))

#formatting strings by keyword
#a = "Lavonte"
#b = "David"
#greeting2 = "Hello {first} {last}".format(a = first, last=b)

#print(greeting2)

# name = input('what is your name?')
# subject = input('what is subject?')
# # statement = "{}'s favorite subject in school is, {}".format(name, subject)
# # print(statement)

# # or f string: 
# statement = f"{name}'s favorite subject in school is, {subject}."
# print(statement)



#4.Given the following code which prompts the user for a day number (Remember that the int function converts a numeric string to a number):
#day = int(input('Day (0-6)? '))
#Fill in your code here

# day = int(input('Day (0-6)? '))

# if day == 0:
#     print("Sunday")
# elif day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4: 
#     print("Thursday")
# elif day == 5: 
#     print("Friday")
# else:
#     print("please choose a number from 0 to 6")


# 5. Work or Sleep in
 #Prompt the user for a day of the week just like the previous problem. But this time, print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. Example session:

# day = int(input('Day (0-6)? '))

# if day == 1:
#     print("Go to work")
# elif day == 2:
#     print("Go to work")
# elif day == 3:
#     print("Go to work")
# elif day == 4: 
#     print("Go to work")
# elif day == 5: 
#     print("Go to work")
# else:
#     print("Sleep in")



# 6. Celsius to Fahrenheit

# C = int(input('Temperature in C? '))

# F = (C * 9/5) + 32

# print(F)



#7. Looping from 1 to 10 Using a while loop, print out the numbers between 1 and 10 inclusive, one on a line. Example output:
# count = 0
# while count < 10:
#     count += 1
#     print(count)
    
#chloe question...what do you set the count at if you want it so start at 0?

# num = 1
# while num < 11:
#     num += 1
#     print(num)

# # num = 0
# # while num <= 10:
# #     num += 1
# #     print(num)

# # num = 0
# # while num < 10:
# #     num += 1
# #     print(num)


# #8. n to m Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:

# # start = int(input('Start from? '))
# # end = int(input('End on? '))
# # count = start-1
# # while count < end:
# #     count += 1
# #     print(count)


# #9 Print a 5x5 square of * characters. Example output:

# # count = 0

# # while count < 5:
# #     count += 1
# #     print("*****")

# #different way to do it
# num1=0
# num2=5
# while num2>=

# #another way to do it
# numStars = 5
# print('p' * numStars)

# #different way to do it with a for loop
# height = 5
# for i in range(height,0,-1):
#     print('*'*height)





#10 Print a NxN square of * characters. Prompt the user for N. Example output:

# Repeat_max= int(input('How big is the square? '))
# count = 0

# while count < Repeat_max:
#     count += 1
#     print("**********")


#MEDIUM
#1 Tip calculator- Your task is to write a program that calculates how much of a tip to leave at a restaurant.

# total= float(input('Total bill amount?'))
# service_choice= input('Level of service?')

# if(service_choice == "good"):
#     tip_amount = (20/total)*100 
# #     print("Tip amount: $%.2f" % tip_amount)
# #     print("Total amount: $%.2f" % (total + tip_amount))
# # elif(service_choice == "fair"):
# #     tip_amount = (15/total)*100 
# #     print("Tip amount: $%.2f" % tip_amount)
# #     print("Total amount:$%.2f" % total + tip_amount)
# # elif(service_choice == "bad"):
# #     tip_amount = (10/total)*100 
# #     print("Tip amount:$%.2f" % tip_amount)
# #     print("Total amount:$%.2f" %  total + tip_amount)
# # else print("please enter valid service level rating")



# #2 Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:
# #found $ sign info here https://thepythonguru.com/python-string-formatting/
# total= float(input('Total bill amount?'))
# service_choice= input('Level of service?')
# split_how_many= int(input('Split how many ways'))

# if(service_choice == "good"):
#     tip_amount = (20/total)*100 
#     print("Tip amount: $%.2f" % tip_amount)
#     print("Total amount: $%.2f" % (total + tip_amount))
# elif(service_choice == "fair"):
#     tip_amount = (15/total)*100 
#     print("Tip amount: $%.2f" % tip_amount)
#     print("Total amount:$%.2f" % total + tip_amount)
# elif(service_choice == "bad"):
#     tip_amount = (10/total)*100 
#     print("Tip amount:$%.2f" % tip_amount)
#     print("Total amount:$%.2f" %  total + tip_amount)
    
# amount_per_person = (total + tip_amount)/split_how_many
# print("Amount per person:$%.2f" %  amount_per_person)

# 6. Multiplication Table -Print the multiplication table for numbers from 1 up to 10. Example output: 


count = 1

while count <= 10:
    
    multiply_by = 1
    while multiply_by < 10:
        print(f"{count} x {multiply_by} = ",(count*multiply_by))
        multiply_by += 1
    
    print(f"{count} x {multiply_by} =",(count*multiply_by))
    count += 1