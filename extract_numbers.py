import sys

# Open the file
f = open('subjects.txt','r')
arrayList = []
for line in f.readlines():
	arrayList.extend(line.split())
f.close()

# Strip a char from an array list
def stripChar(ar, ch):
	i = 0
	for i in range(len(ar)):
		ar[i] = ar[i].replace(ch, '')

# Call the function for stripting chars
stripChar(arrayList, ',')

# a list for storing the numbers
pages = []
for i in range(0,len(arrayList)):  # chect if the string begins with a number
	if (arrayList[i][0] == '1' or arrayList[i][0] == '2' or
		arrayList[i][0] == '3' or arrayList[i][0] == '4' or arrayList[i][0] == '5' or arrayList[i][0] == '6' or
		arrayList[i][0] == '7' or arrayList[i][0] == '8' or arrayList[i][0] == '9'):
			# add numbers to the array pages
			pages.append(arrayList[i]) 
			
# NOW, WE'VE GOT A NEW LIST FROM NUMBERS :)
# Convert all the numbers to the integer which its type is string
for i in range(0, len(pages)):
	pages[i] = int(pages[i])

# sort the list
pages.sort()

f = open("page_list.txt", 'a')
for n in pages:
	f.write("%s\n" % n)
f.close()
