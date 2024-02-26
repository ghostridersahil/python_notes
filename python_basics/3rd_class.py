# array

from array import *
arr= array('i',[1,2,3])
print(arr[0])  #it will print 1 
# typecode --- type+code
print(arr[1])

arr.append(5)
arr.insert(1,10)

arr2=array("a",[11,12,13,14,15])
arr.extend(arr2)
print(arr)

