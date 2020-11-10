"""
MadLibs
Author: Hannah Orris
Period/Core: 5
"""
gender = int(input("Type 1 for boy or 2 for girl: "))
name = input("Enter a name: ") 
teacher = input("Enter a teacher name: ") 
place = input("Enter a place: ")
verb = input("Enter a verb(in past tense): ") 
person = input("Enter a famous person: ")
adjective = input("Enter a adjective: ") 
noun = input("Enter a noun: ") 
beverage = input("Enter a beverage: ")
noun2 = input("Enter another noun(preferably an object): ") 
obj = input("Enter a strange object: ") 

print("   ") #anytime this is used, a space is added to make the story easier to read.

print("   ") 
print("   ") 
print("This is a short story based off your input.")
print("   ")
print("   ") 

if gender == 1:
  print(f"It was a beautiful Tuesday morning. {name} was on his way to history class.")
  print(f"When he got there, his teacher, {teacher} said, \n    \"Today we are going to learn about the history of {place}!\"")
else:
  print(f"It was a beautiful Tuesday morning. {name} was on her way to history class.")
  print(f"When she got there, her teacher, {teacher} said, \n    \"Today we are going to learn about the history of {place}!\"")

print("   ") 

print("The whole class " + verb + " in anger.")
print("They all decided to ditch class and watch a youtube documentery about " + person + ".")

print("   ") 

print(f"As they were watching the video, a {adjective} {noun} walked over holding a {beverage} in one arm and a {noun2} in the other. \nThe {adjective} {noun} said,")
print(f"    \"Hey, you guys wanna come over to my basement? I have a really cool {obj}!\"")
print("    \"Sure! The class replied.\"")