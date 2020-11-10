"""
MadLibs
Author: Hannah Orris
Period/Core: 5
"""
noun = input("Enter a noun: ") #used
name = input("Enter a name: ") #used
verb = input("Enter a verb(in past tense): ") #used
place = input("Enter a place: ") #used
adjective = input("Enter a adjective: ") #used
beverage = input("Enter a beverage: ")
person = input("Enter a famous person: ") #used
noun2 = input("Enter another noun: ") #used
obj = input("Enter a strange object: ") #used
print("   ")
#Prompts match up with the order the words are used in the story.
#At least 8 inputs/variables
#Inputs should use a variety of parts of speech (noun, adjective, verb, etc.) and/or specific types of nouns (place, food, etc.)

#Has proper spelling and grammar
#Is at least 6 sentences/lines long.

#At least one print() statement that outputs on multiple lines (ie. uses "\n")
#At least one print() statement that concatenates (“adds”) two strings together (eg. "Hello " + "world")
#At least one f-string or .format() that correctly inserts the variables.

print("   ")
print("This is a short story based off your input.")
print("   ")
print(name + " was on their way to history class.")
print("When they got there, their teacher, Mr. Smith said," "\n" "    Today we are going to learn about the history of " + place +"!")
print("The whole class " + verb + ".")
print("The whole class decided to ditch and watch a youtube documentery about " + person + ".")
print("As they were watching the video, a " + adjective + noun +" walked over holding a " + beverage + " in one arm and a " + noun2 +" in the other." "\n" "The " + adjective + noun + "said,")
print("    \"Hey, you guys wanna come over to my basement? I have a really cool " + obj + "!\"")
print("    \"Sure! The class replied.\"")