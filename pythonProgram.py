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

num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
