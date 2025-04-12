# Default Data Types in Python : strings、integer、float、boolean、complex
# Data Types in Numpy : i - integer、b - boolean、u - unsigned integer、f - float、c - complex float、m - timedelta、M - datetime、O - object、S - string、U - unicode string、V - fixed chunk of memory for other type ( void )

#To check ndarray's data type
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

#create array with a defined data type
arr_s = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr_s)
print(arr_s.dtype)


#Copy : copy is a new array, so if change the value of the original array will not affect the copy one's
x = arr.copy()
#arr[0] = 7
print(x)
#view : view is just a view of the original array
y= arr.view()
print(y)
#Check if Array Owns its Data e.g. copy owns the data but view doesn't, base can check this if the array owns the data it will return None
print(x.base)
print(y.base) # this will return the original array
