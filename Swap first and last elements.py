a=[ ] 
n=int(input("Enter the number of elements in the list :")) 
for x in range(0,n): 
    element=int(input(" Enter the element" +str(x+1) +" : ")) 
    a.append(element) 
temp=a[0] 
a[0]=a[n-1] 
a[n-1]=temp 
print(" new list is :") 
print(a) 
