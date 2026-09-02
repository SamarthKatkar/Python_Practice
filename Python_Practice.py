# 1/8/26

# i=1
# for i in range(1,11):
#     print(f"3 X {i} = {i*3}")

# i=1
# while i<=6:
#     print(i)
#     i +=1

# a=int(input("Enter your age:"))
# # print(a)
# if a<=18:
#     print("Not eligible")
# else:
#     print("Eligible")
# name = input("Enter your name:")
# age = int(input("Enter your age:"))  
# print(f"My name is {name} and my age is {age}")              

# 2/8/26

# for i in range(1,6):
#     if i==3:
#         break //break the loop and exit the loop
#     print(i)

# for i in range(1,6):
#     if i==3:
#         continue //dont execute the code below and continue with the next iteration
#     print(i)

# for i in range(1,6):
#     if i==3:
#         pass //do nothing and continue with the next iteration
#     print(i)
                    
# tab button is used to indent the code in python.
# and shift+tab is used to unindent the code in python.  

# ''' is uded to write multi line comments in python.

# name="Samarth"
# print(name[2])

# name = "Samarth"
# for i in name:
#     print(i)

# name = "S a m a r t h" // strings are immutable in python.
# #       0 1 2 3 4 5 6
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])

# name="samarth katkar"
# a=name.upper()
# print(a)
# b=name.lower()
# print(b)
# print(name.title()) # title() is used to capitalize the first letter of each word in a string.
# print(name.capitalize()) # capitalize() is used to capitalize the first letter of the string.
# print(name.strip()) # strip() is used to remove the leading and trailing spaces from a string.
# print(name.lstrip()) # lstrip() is used to remove the leading spaces from a string.
# print(name.rstrip()) # rstrip() is used to remove the trailing spaces from a string.
                                                                                                            
# fruits= "apple,banana,guava,pineapple"
# a= fruits.split(",")
# print(a)
# b="-".join(a)
# print(b)
# print(len(fruits))

# marks=[23,21,15,10,9,22,12,11]
# #print(marks[0:3])
# marks.append(20)#to add a number at the end of the list
# marks.insert(1,4) #to insert a number at specific position
# print(marks)
# marks.remove(23) #to remove a number from the list
# print(marks)
# marks.pop() #to remove the last number from the list
# print(marks)
# marks.reverse() #to reverse the list
# print(marks)
# marks.sort() #to sort the list in ascending order
# print(marks)

#Tuples are ordered but immutable collections
# marks=(23,21,15,10,9,22,12,11,22,23,31,19,17,4,9,10)
# print(marks)
# print(marks.count(22)) #to count the number of times a number appears in the tuple
# print(marks.index(19)) #to find the index of a number in the tuple

#Sets are unordered, unique collections (no duplicates).
# cities={"Pune","Mumbai","Nagpur","Nashik","Sangli","Kolhapur"}
# print(cities)
# cities.add("Solapur") #to add a city to the set
# print(cities)  
# cities.remove("Solapur")
# print(cities) #to remove a city from the set    
# cities.pop() #to remove a random city from the set
# print(cities)
# villages={"Pimpri","Chinchwad","Bhosari","Nigdi","Akurdi"}
# print(cities.union(villages)) #to combine two sets

#Dictionaries store key-value pairs and allow fast lookups.
# fruits={"apple":100,"banana":50,"guava":80,"pineapple":120}
# print(fruits["apple"]) #to access the value of a key in the dictionary
# fruits["mango"]=500
# print(fruits) #to add a new key-value pair to the dictionary    
# print(fruits.keys()) #to get all the keys in the dictionary
# print(fruits.values()) #to get all the values in the dictionary

