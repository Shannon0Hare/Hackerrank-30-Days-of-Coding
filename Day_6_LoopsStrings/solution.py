# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input()) #input int
temp = [] # temp array
for i in range(0,n): #loop from 0 to n
    s = input() # let s = input
    temp.append(s) # append the i letter of the input into temp

for i in range(0,n): 
    for j in range(0,len(temp[i]),2): # Starting from 0, print that index then add 2
        print(temp[i][j],end='')
    print(end=' ') #print a gap
    for j in range(1,len(temp[i]),2): # Starting from 1, print that index then add 2
        print(temp[i][j],end='')
    print() # print enter
