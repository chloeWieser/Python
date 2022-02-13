# #sequences practice

# #SMALL

# #1 sum the numbers- create list of numbers and print their sum
# # num = [1,2,3,4,5]

# # print (sum(num))


# #intended way to do it is to not use built in functions and make a for loop:
# # nums = [1,2,3,4,5]

# # sum = 0
# # for x in nums:
# #     sum += x
# # print(sum)



# # 2. Largest Number
# # Create a list of numbers, print the largest of the numbers.
# # num = [1,8,3,6,2]
# # num.sort()
# # print (num[-1])

# #intended way to do it is to not use built in functions and make a for loop:
# # nums = [1,2,3,4,5]

# # max = 0
# # for x in nums:
# #     if (max < x):
# #         max = x
# # print(max)


# # 3. Smallest Number
# # Create a list of numbers, print the smallest of the numbers.
# # num = [9,8,3,6,2]
# # num.sort()
# # print (num[0])


# # nums = [9,8,1,6,2]
# # min = nums[0]
# # for x in nums:
# #     if (min > x):
# #         min = x
# # print(min)

# # 4. Even numbers
# # Create a list of numbers, print each number in the list that is even.
# nums = [9,8,3,6,2]
# for num in nums:
#     if (num % 2) == 0:
#         result.append(num)
# print(result)

        
# #         print(num)

# # 5. Positive Numbers
# #Create a list of numbers, print each number in the list that is greater than zero.
# # nums = [9,8,0,6,2]
# # for num in nums:
# #     if (num > 0):
# #         print(num)

# # 6. Positive Numbers II
#!Create a list of numbers, create a new list which contains every number in the given list which is positive.
# nums = [9,-8,0,-6,2]
# posnums = []
# for num in nums:
#     if (num > 0):
#         posnums.append(num)
# print(posnums)

# # 7. Multiply a list
# ! Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.
# # nums = [9,8,0,6,2]  
# # factor = 2 
# # for num in nums:
# #     print(2*num)

#!did not create it as a new list:
# nums = [9,8,0,6,2]  
# factor = 2 
# newList = []
# for num in nums:
#     newList.append(factor*num)
# print(newList)

    
# #8. Reverse a String
# #Given a string, print the string reversed.
# # my_name = "chloe"
# # reverse = ""
# # for char in my_name:
# #     reverse = char + reverse
# # print (reverse)

#!intended way to do it as a for loop:
# my_name = "chloe"
# revstring = ""
# for char in my_name:
#     revstring = char + revstring
# print(revstring)

#!from class as a while loop:
# my_name = "chloe"
# revstring = ""  #need new list since you can't mutate a string
# index = 0
# while index < len(my_name):
#     revstring = my_name[index] + revstring  #each new loop, pushes the 'rest of the list' to the end, so the 'loop result' prior is essentially pushed to the right of the new 'loop result' 
#     index+=1
# print(revstring)

# #MEDIUM

# #1. Multiply Vectors
# #Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# # list1 = [2,4,5]
# # list2 = [2,3,6]
# # products = []


# # for num1, num2 in zip(list1, list2):
# #     products.append(num1 * num2)
# # print(products)


# # 2. Matrix Addition
# # Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
# #Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add
# list1 = [[1,3],
#          [2,4]]

# list2 = [[5,2],
#          [1,0]]
# sum = [[0,0], [0,0]]

# for x in range(len(list1)):
#     for y in range(len(list1[0])):
#         sum[x][y] = list1[x][y] + list2[x][y]

# for z in sum:
#     print(z)
    
# #3. Matrix Addition II
# #Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size. 

# *DIDNT GET THERE WITH THIS ONE
# list1 = [[1,3,1],
#          [2,4,1]]

# list2 = [[5,2,1],
#          [1,0,1]]
# sum = [[0 *(len(list1))], [0*(len(list1))]]

# for x in range(len(list1)):
#     for y in range(len(list1[0])):
#         sum[x][y] = list1[x][y] + list2[x][y]

# for z in sum:
#     print(z)


# #4. Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. 
# # Print the list.

# # animals = ["horse","chicken","chicken","goat"]
# # revised_animals = []
# # for x in animals:
# #     if x not in revised_animals:
# #         revised_animals.append(x)

# # print(revised_animals)


# # 5. Leetspeak
# # Given a paragraph of text as a String, print the paragraph in leetspeak (Links to an external site.).

# # To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):


#*THESE ARE ALL WRONG SKIP DOWN A BIT*
# statement = "I am a leet programmer"
# # index = 0
# # while index < len(statement):
# #     print(statement[index])
# #     index += 1
    
# statementlist = list(statement)
# print(statementlist)
# newstatementlist = []

# index = 0
# for x in statementlist:
#     if isinstance(x, A):

#FINAL ANSWER
# statement = input("enter text")
# statement = statement.upper()
# for char in (("A", "4"), ("E", "3"), ("G", "6"), ("I", "1"), ("O", "0"), ("S", "5"), ("T", "7")):
#     statement = statement.replace(*char)
#     statement = statement.lower()
# print (statement)

# # 6. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5.

# word = input("enter text")
# for char in (("a","a"*5),("e","e"*5),("i", "i"*5),("o", "o"*5), ("u", "u"*5)):
#     word = word.replace(*char)
# print (word)

# # 7. Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of the string.
# from ast import mod

# original = "caesar cipher"
# abc = "abcdefghijklmnopqrstuvwxyz"
# encrypted = "".join([abc[(abc.find(c)+13)%26] for c in original])
# print(encrypted)

# cleartxt = "lbh zhfg hayrnea jung lbh unir yrnearq"
# abc = "abcdefghijklmnopqrstuvwxyz"
# secret = "".join([abc[(abc.find(c)+13)%26] for c in cleartxt])
# print(secret)

#you must unlearn what you have learned