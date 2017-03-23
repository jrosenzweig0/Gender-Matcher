from collections import Counter
from random import * 

def write_text():
	boys_w = open("Boys.txt", "w")
	girls_w = open("Girls.txt", "w")
	for i in range(len(bset)):
		boys_w.write(str(bset[i]) + "\n")
	for i in range(len(gset)):
		girls_w.write(str(gset[i]) + "\n")
	boys_w.close()
	girls_w.close()


boys = open("Boys.txt", "r")
girls = open("Girls.txt", "r")
friends = open("Friends.txt", "r")

bset = []
gset = []
guys = []
gals = []
unname  = []
count = 0

for line in boys:
	bset.append(line.strip("\n"))


for line in girls:
	gset.append(line.strip("\n"))


for line in friends:
	z = True
	count += 1
	if (str(line.strip("\n"))) in bset:
		guys.append(line.strip("\n"))
		z = False

	if (str(line.strip("\n"))) in gset:
		gals.append(line.strip("\n"))
		z = False

	if z == True:
		unname.append(line.strip("\n"))

correction = (len(guys)+len(gals)+len(unname) - count)//2
len_guys = len(guys) - correction
len_gals = len(gals) - correction

print("Total:", count)
print("Male:", len_guys)
print("Female:", len_gals)
print("Unmatched:", len(unname))
print("Matched percentage: " + str(round(((len_guys+len_gals)/count)*100)) + "%")
print("Male percentage: " + str(round((len_guys/(len_guys+len_gals))*100)) + "%")
print("Female percentage: " + str(round((len_gals/(len_guys+len_gals))*100)) + "%")
print()
#print(sorted(unname))
Total = guys + gals + unname
data = Counter(Total)
#print(data.most_common())

data_nomatch = Counter(unname)
top_20_percent = round(len(data_nomatch.most_common())*.2)
top_20_set = list(range(1,top_20_percent))

for i in range(len(top_20_set)):
	j = choice(top_20_set)
	top_20_set.remove(j)
	if j == 1:
		name_length = 0
	else:
		name_length = len(str(data_nomatch.most_common(j-1)))
	n = 3 + name_length
	while True:
		if str(data_nomatch.most_common(j))[n] == '\'':
			break
		else:
			n += 1
	#print(data_nomatch.most_common())
	gender = input("Does " + str(data_nomatch.most_common(j))[3 + name_length:n] + " sound like a:" + "\n" +"a) Boy's Name" + "\n" + "b) Girl's name" + "\n" + "c) Both" + "\n" + "d) Not sure" + "\n")
	print()
	if gender == 'a':
		bset.append(str(data_nomatch.most_common(j))[3 + name_length:n])
	elif gender == 'b':
		gset.append(str(data_nomatch.most_common(j))[3 + name_length:n])	
	elif gender == 'c':
		bset.append(str(data_nomatch.most_common(j))[3 + name_length:n])
		gset.append(str(data_nomatch.most_common(j))[3 + name_length:n])
	else:
		continue
for i in range (1,6):
	rand_b = choice(bset)
	boys_check = input("Does " + rand_b + " sound like a boy? " + "\n" +"a) Yes" + "\n" + "b) No" + "\n" + "c) Not Sure" + "\n")
	print()
	if boys_check == "b":
		bset.remove(rand_b)

	rand_g = choice(gset)
	girls_check = input("Does " + rand_g + " sound like a girl? " + "\n" +"a) Yes" + "\n" + "b) No" + "\n" + "c) Not Sure" + "\n")
	print()
	if girls_check == "b":
		gset.remove(rand_g)

write_text()
print()

		#NEED TO FIX
		#data_nomatch.most_common(i) is returning a list needs to be a string
		#remove case sensitivity 
