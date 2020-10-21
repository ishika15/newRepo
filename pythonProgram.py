print("Hello world")

#added a new feature
num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")
    
    # Program to add two matrices using nested loop 

X = [[1,2,3], 
	[4 ,5,6], 
	[7 ,8,9]] 

Y = [[9,8,7], 
	[6,5,4], 
	[3,2,1]] 


result = [[0,0,0], 
		[0,0,0], 
		[0,0,0]] 

# iterate through rows 
for i in range(len(X)): 
# iterate through columns 
	for j in range(len(X[0])): 
		result[i][j] = X[i][j] + Y[i][j] 

for r in result: 
	print(r) 

