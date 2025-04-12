import numpy as np

# Dimensions in Array
#0-D Array
arr_0d = np.array(42)
print(arr_0d)
#1-D array
arr_1d = np.array([1, 2, 3, 4, 5])
#add elements in this array
print(arr_1d[0]+arr_1d[3])
#2-D array
arr_2d = np.array([[1, 2, 3],[4, 5, 6]])
print("3rd element on 2nd row", arr_2d[1,2])
#3-D array
arr_3d =  np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d[1, 0, 1])

# To check number of dimensions (Note : ndim is attribute not a function)
print("number of dimensions : ", arr_3d.ndim)

#Higher Dimension Arrays
arr_higher = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr_higher)
print('number of dimensions :', arr_higher.ndim)

#Negative indexing (take 2-d array for example)
#Last element from 2nd dim
print("Last element from 2nd dim : ", arr_2d[1, -1]) # use normal indexing would br [1,2]

#------------------------------------------------------------------------------------------------------------------------

#Slicing Arrays => Slicing in python means taking elements from one given index to another given index [start:end]; [start, end, step]
#Note : The result includes the start index, but excludes the end index
print(arr_1d[1:4])
#how can we go through whole array with slice?
print(arr_1d[0:]) #same as [:6]
#Nevigating slice
print(arr_1d[-3:-1])
#step
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::1])

#Slicing in 2-d array arr_2d = np.array([[1, 2, 3],[4, 5, 6]])
print(arr_2d[1, 1:2])
print(arr_2d[0:2, 2]) #[3, 6]
print(arr_2d[0:2, 1:2]) #from both elements slice index 1 to index 4, will return a 2-D array

arr1 = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr1[1:4:2])

#------------------------------------------------------------------------------------------------------------------------
#The shape of an array is the number of elements in each dimension
print(arr_1d.shape)
print(arr_2d.shape)#means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4
print(arr_higher)
print(arr_higher.shape)

#Reshape the array
# 1-D to 2-D array
test_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(test_arr.reshape(4, 3))
print(test_arr.reshape(4, 3).base) #Note : the return of reshape is View
print(test_arr.reshape(2, 3, 2)) # test_arr.reshape(2, 3, -1) will return the same result, Pass -1 as the value, and NumPy will calculate this number for you(Note : can't pass -1 to more than 1 dimension).
# You can't reshape array into any shape(total elements are the same!)=> ValueError: cannot reshape array of size 8 into shape (3,3)
test_reshape = np.array([1, 2, 3, 4, 5, 6, 7, 8])
#print(test_reshape.reshape(3, 3))

#Flattening the arrays : converting a multidimensional array into a 1D array.
print(arr_2d.reshape(-1)) # or flatten() and other functions can do this too.

#------------------------------------------------------------------------------------------------------------------------

#iterating 3-D array
for i in arr_3d:
    print(i)
#print each elements
# for i in arr_3d:
#     for j in i:
#         for k in j:
#             print(k)
#using nditer() function in Numpy to  iterate arrays
for i in np.nditer(arr_3d):
    print(i)
#Iterating Array With Different Data Types, use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
diff_data_type_arr = np.array([1, 2, 3])
for i in np.nditer(diff_data_type_arr, flags=["buffered"], op_dtypes=['S']):
    print(i)
#Enumerated Iteration Using ndenumerate()
for index, i in np.ndenumerate(arr_2d):
    print(index, i)

#------------------------------------------------------------------------------------------------------------------------

#Joining NumPy Arrays : concatenate() function
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr3)

#2-D join , we use axis o or 1 to decide join along rows(0, default) or columns(1)
arr2d_1 = np.array([[1, 2], [3, 4]])
arr2d_2 = np.array([[5, 6], [7, 8]])
arr2d_3 = np.concatenate((arr2d_1, arr2d_2), axis=1)
print(arr2d_3)

#Split Into Arrays use array_split() function in Numpy
#Split 1-D array
array = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(array, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])
#Split 2-D array , also can use axis to spilit the array along with row or column
array2D = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new2Darr = np.array_split(array2D, 3)
print(new2Darr)

#------------------------------------------------------------------------------------------------------------------------

#searching arrays
array_sch = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(array_sch==4) # this will find the indexes where value==4
print(x)
#search multiple value


#searchsorted() which performs a "binary search" in the array, and returns the index where the specified value would be inserted to maintain the search order
#default is search from left side
arr123 = np.array([6, 7, 8, 9]) # 8 , 7
# z= np.searchsorted(arr123, 7) # 6, 7
z= np.searchsorted(arr123, 7, side="right")
print(z)
#to find the position of the values should be inserted into
array_sch2 = np.array([1, 3, 5, 7])
even = np.searchsorted(array_sch2, [2, 4, 6])
print(even)

#sort arrays
arr_unsort = np.array([3, 2, 0, 1])
print(np.sort(arr_unsort)) # this function return copy (leaving the original array unchanged)
arr_bool = np.array([True, False, True])
print(np.sort(arr_bool))
arr_unsort2D = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr_unsort2D))

#Filtering Arrays
arr_filter = np.array([41, 42, 43, 44])
n = arr_filter[[True, False, True, True]]
print(n)

#creating a filter array
#create an empty list
filter_arr = []

#go through every elements in arr_filter
for element in arr_filter:
    if element >42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_array_filtered = arr_filter[filter_arr]
print(filter_arr)
print(new_array_filtered)