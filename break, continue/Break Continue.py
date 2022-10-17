n = int(input("Value: "))
print("Table vales of,",n,"are: ")

sum = 0
for i in range(1,11):
    val = i*n
    print(val)
    sum = sum+val
    
print("Sum of table values is: ",sum)


avg = sum/10
print("Average value of table is: ", avg)

''' values above average value'''

print("Values above average value,",avg,",are: ")
i = 1
while i <=10:
    if i*n < avg :
        i+=1
        continue
    print(i*n, end=" ")
    i+=1
print()
    
''' values below average value'''

print("Values below average value,",avg,",are: ")
i = 1
while i <=10:
    if i*n > avg :
        i+=1
        break
    print(i*n, end=" ")
    i+=1
    
  

      
    
    
