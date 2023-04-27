#comparison operators like <, >, <= and >= can apply to strings as well,
#searching for the first character that is different from the other if comparing words
#min & max functions also work on strings

# #sorting numbers, least->greatest by default
# points = [0, -10, 15, -2, 1, 12]
# sortedGame = sorted(points)
# print(sortedGame)

# #sorting words
# children = ["Sue", "Jerry", "Linda"]
# print(sorted(children))
# #sorting is case sensitive, Caps before lowers
# print(sorted(["Sue", 'jerry', 'linda']))
# #sorting words, case-insensitive
# print(sorted("My favorite child is Linda".split(), key=str.upper))
# #reverse sorting
# print(sorted(points, reverse=True))
# #sorting dictionaries
# leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
# print(sorted(leaderBoard, reverse=True))
# print(leaderBoard.get(432))
# #sorting tuples
# students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
# print(sorted(students, key=lambda student: student[0]))  #by name
# print(sorted(students, key=lambda student: student[1]))  #by grade
# print(sorted(students, key=lambda student: student[2]))  #by age

# #type functions
# class Car:
#   pass

# class Truck(Car):
#   pass

# c = Car()
# t = Truck()
# print(type(c))
# print(type(t))
# print(type(c) == type(t))  #type == does not account for inheritance
# print(isinstance(c, Car))
# print(isinstance(t, Car))  #isinstance DOES account for inheritance
# #isinstance tends to be better than type checking because it accounts for inheritance

# #math module has functions for trig, factorial, greatest common denominator, sqrt, etc
# #math module can also handle radians and degrees
# import math

# #random module allows for random selections of numbers or options
# import random

# lotteryWinners = random.sample(range(100), 5)
# print(lotteryWinners)
# possiblePets = ['cat', 'dog', 'fish']
# print(random.choice(possiblePets))
# cards = ['jack', 'queen', 'king', 'ace']
# random.shuffle(cards)
# print(cards)

# #statistics module will help with stats collection/calculation
# import statistics as stats  #use 'as' keyword to import with an alias

# print(stats.mean(lotteryWinners))
# print(stats.variance(lotteryWinners))
# print(stats.stdev(lotteryWinners))

# # #itertools module allows for iterative loops and infinite cycles
# import itertools as iter
# # for x in iter.count(50, 5):  #infinite counting
# #   print(x)
# #   if x == 100: break
# # x = 0
# # for c in iter.cycle("RACECAR"):  #infinite cycling
# #   print(c)
# #   x += 10
# #   if x > 60: break
# # for r in iter.repeat(True):  #infinite repeating
# #   print(r)
# #   x = x + 1
# #   if x > 65: break

# #itertools also gives tools for permutations and combinations
# election = {1: "Barb", 2: "Karen", 3: "Erin"}
# for p in iter.permutations(election):
#   print(p)
# for p1 in iter.permutations(election.values()):
#   print(p1)
# colors = ['red', 'blue', 'purple', 'orange', 'yellow', 'pink']
# for c in iter.combinations(colors, 2):
#   print(c)
# #command line arguments
# import sys
# print('Number of arguments: ', len(sys.argv), ' arguments.')
# print("Arugments ", sys.argv)
# #remove args
# sys.argv.remove(sys.argv[0])
# print("Arguments ", sys.argv)
# #sum args
# arguments = sys.argv
# sum=0
# for arg in arguments:
#   try:
#     number = int(arg)
#     sum = sum+number
#   except Exception:
#     print("bad Input")
# print(sum)

# #files and file writing
# myFile = open("scores.txt", "w")
# print("Name: ", myFile.name, " Mode: ", myFile.mode)
# myFile.write("GBJ: 100\nKHD: 99\nBBB: 89")
# myFile.close()

# myFile = open("scores.txt", "r")
# print("File Contents:\n", myFile.read(10))
# myFile.seek(0) #sets cursor to character 0

# print("Reading one line: ", myFile.readline())
# myFile.seek(0)

# #iterating through files
# for line in myFile:
#   newHighScorer=line.replace("BBB", "PDJ")
#   print(newHighScorer)

# myFile.close()

# #tempfile module
# import tempfile

# tempFile = tempfile.TemporaryFile()
# tempFile.write(b"Save this special number for me: 385485"
#                )  #leading b turns string into byte literal
# tempFile.seek(0)
# print(tempFile.read())
# tempFile.close()

# #zip files
# import zipfile

# zip = zipfile.ZipFile('Archive.zip', 'r')
# print(
#   zip.namelist())  #wont work in Replit because this zip folder doesn't exist
# #metadata in the zip folder
# for meta in zip.infolist():
#   print(meta)

# info = zip.getinfo("purchased.txt")
# print(info)

# #accessing files in zip folder
# print(zip.read("wishlist.txt"))
# with zip.open('wishlist.txt') as f:
#   print(f.read())

# #extract files
# zip.extract("purchased.txt") #specific file
# zip.extractall() #everything
# zip.close()

# #datetime module
# from datetime import datetime, timedelta
# import calendar

# now = datetime.now()
# # print(now.date())
# # print(now.year)
# # print(now.month)
# # print(now.hour)
# # print(now.second)
# # print(now.time())
# print(now.strftime("%a %A %d"))
# print(now.strftime("%b %B %m"))
# print(now.strftime("%A %B %d"))
# print(now.strftime("%H:%M:%S %p"))
# print(now.strftime("%y %Y"))
# testdate = now + timedelta(days=2)
# myFirstCourse = now - timedelta(weeks=3)
# print(testdate.date())
# print(myFirstCourse.date())
# if testdate > myFirstCourse:
#   print("Comparison Works")

# cal = calendar.month(2001, 10)
# print(cal)
# cal2 = calendar.weekday(2001, 10, 11)
# print(cal2)
# print(calendar.isleap(2000))
