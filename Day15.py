# Day 15
# Part 1
def last_occurance(spoken, number):
	for index in range(len(spoken)-2,-1,-1):
		# count backwards from second last to find the previous occurance
		if spoken[index] == number:
			return index 

a = [2,15,0,9,1,20]
spoken = []
counter = 0
prev = 0

while counter < 2020:
	if counter < len(a):
		# read out the given list first and store it in spoken
		spoken.append(a[counter])
		prev = a[counter]
	elif prev not in spoken[0:-1]:
		# check if it's the first time the number is said
		spoken.append(0)
		prev = 0
	else:
		# if it's been spoken, find the index last time prev was spoken
		num = counter - 1 - last_occurance(spoken,prev)
		spoken.append(num)
		prev = num
	counter += 1

print(spoken[-1])

# Part 2