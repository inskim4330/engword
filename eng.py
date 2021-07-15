import csv
import random
import sys
import os

def print_mainmenu():
	os.system("cls")
	print("name:"+sys.argv[1])
	print("r:random         s:series        q:quit")
	
	

def print_word(idx):
	print(str(current_index)+"/"+str(max_index))
	print(lists_from_csv[0][idx])

file = open(sys.argv[1],'rt',encoding='UTF8')
csv_reader = csv.reader(file)
global current_index
global max_index
random_or_series = "series"
current_index = 0
max_index = 0
storage_index = list()
lists_from_csv = []
exit = False

for row in csv_reader:
	lists_from_csv.append(row)
	max_index = len(row)



print_mainmenu()
result = input()
if result == 'r':
	random_or_series = "random"
elif result == 's':
	random_or_series = "series"
print(random_or_series + ", enter is next, b is back")

print_word(current_index)

count = 0
try:
	while exit == False:
		value = input()
		if value == "":
			os.system("cls")
			if random_or_series == "series":
				current_index +=1
			elif random_or_series == "random":
				current_index = random.randrange(max_index)

		if value == "q":
			exit = True
		if value == "b":
			current_index -= 1
		print_word(current_index)
except IndexError as exception:
	print(":END:")


file.close()
