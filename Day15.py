def find_multiple(num1, num2, diff, start = 0):
    temp1 = start+num1
    temp2 = 0
    while True:
        if temp1 >= temp2:
            temp2+= num2
        elif temp2-temp1 != diff:
            temp1+=num1
        else:
            #print(temp1, temp2)
            break
    return temp1

# turn data into two lists
# one with all the time intervals
# one with all th departure time difference
original = [17,"x",13,19]
departure_interval = []
time_interval = []
t = 0
for item in original:
    if item == "x":
        t+= 1
    else:
        time_interval.append(item)
        departure_interval.append(t)
        t+=1
print(time_interval, departure_interval)

# use two lists to find when condition is met
a = [17,13,19]
b = [2,3]
start1 = 0
start2 = 0

first_pair = find_multiple(7,13,1,1068774)
second_pair = find_multiple(7,59,4,1068774)
print(first_pair, second_pair)
'''
while first_pair != second_pair:
    if first_pair > second_pair:
        start2 = first_pair
        start1 = first_pair
    else:
        start1 = second_pair
        start2 = second_pair
    first_pair = find_multiple(17,13,2,start1)
    second_pair = find_multiple(17,19,3,start2)
    #print(first_pair, second_pair)
'''
    
