#Iterating over range 0 to n-1
n=10
print('033[1m' + 'Use for loop: "+"\033[0m')

for i in range(0, n):
    print(i)
    print('033[1m' + 'Use while loop: ' + '\033[0m')

count=0
while (count <3):
    count = count +1
    print(count)

else:
    print('No value')