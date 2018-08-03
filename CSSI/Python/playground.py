# #!/usr/bin/python
# print("Hello World!")
#
# num = int(input("Enter a number: "))
#
# if num > 0:
#     print("This number is nonnegative.")
# elif num < 0:
#     print("This is negative :")
# else:
#     print("This number is a zeroooooo.")
#
#
# i = 0
# while i  < 3:
#      num = int(input("Enter a number: "))
#      if num > 0:
#          print("This number is nonnegative.")
#      elif num < 0:
#          print("This is negative :")
#      else:
#          print("This number is a zeroooooo.")
#      i += 1
#
# greeting = "Hello "
# for letter in greeting:
#     print(letter.upper())
#
#
# for i in range(10,5,-1):
#     print(i)
#

# my_name = "Phoebe"
#
# friends = ["Ogechi", "Osase", "Brenda", "Timothy"]
# friends.append("Areeta")
# friends.insert(1, "Brian")
# friends.remove("Brenda")
#
#
# print("My name is %s and I have %s friends "
#     % (my_name, len(friends)))
#
# print("My friends are: ")
#
# for friend in friends:
#     print(friend)
#
# print(friend[0])
# print(friends[3])
#
# for i in range(len(friends)):
#     if i == 0:
#         print(friends[0])
#     else:
#         print("and " + friends[i]),


# google_age = 1.7
# print("My google-age is %s" %google_age)
# print("My google-age is %s"% 1.7)
#
# name = input("My input: ")
# print(name)
#
#
# def greetSecretAgent(first_name, last_name):
#     print("%s. %s, %s" % (last_name, first_name, last_name))
#
# greetSecretAgent("Rachel", "Mellon")
# greetSecretAgent("James", "Bond")
# greetSecretAgent("Just", "Q")
#
# def secretAgentGreeting(first_name, last_name):
#     return "%s, %s, %s." % (last_name, first_name, last_name)
#
# greeting = secretAgentGreeting("Julia", "Cordero")
# print(greeting)

# for i in range(1,11):
#     print(i)
#
# def mystery1(a):
#     return a + 5
#
# def mystery2(b):
#     return b * 2
#
# result = mystery1(mystery2(3))
# print result
#
# def mystery(word,number):
#     number = number * 2 #number is "hehe"
#     word = word.upper() #word is 2
#     return word * number #this is multiplying a string with a string which messes up
#
# print(mystery("2", "he"))

# states = {
# "CA" : "California",
# "AZ" : "Arizona",
# "AK" : "Arkansas"
# }
#
# for state in states:
#     print("%s is the abbreviation for %s" % (state, states[state]))

storePrices = {
    "cereal" : 2.00,
    "stapler" : 1.50,
    "fiber optic" : 25,
    "lambo" : 750000,
}


# print(storePrices["cereal"] + storePrices["lambo"])

inventory = {
    "cereal" : 750,
    "stapler" : 250,
    "fiber optic" : 5,
    "lambo" : 2
}

inventory["cereal"] -= 2
inventory["lambo"] -= 1

for price in storePrices:
    storePrices[price] *= 1.03

print(storePrices["cereal"] + storePrices["cereal"] + storePrices["lambo"])
print(inventory)
