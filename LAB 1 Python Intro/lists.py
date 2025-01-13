# Exercise: Lists 
# (i)Play with some of the list functions. You can find the methods you can call on an object via the dir
# and get information about them via the help command: 
# >>> dir(list) 
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__ge__', 
# '__getattribute__', 
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', 
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
# '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__str__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 
# 'remove', 'reverse', 'sort']

array = [1,2,3,4,5,6,7,8]
# res = array.__add__([10,11]) #Not In-place
# print(array)
# print(res)
# newRes = res.reverse() # In-place modification
# print(res)
# print(newRes)
# index = array.index(8)
# print(array.index(8))
# print(index)

# insert = array.insert(1,9) #Insert value at the given index.Returns none and modifies an array.Inplace Modification
# print(array)
# print(array.__len__())
# res = array.append(23) #Returns none and add element at the last of an array
# print(res) 


# (ii)Write a Python program to count the number of strings where the string length is 2 or more and the 
# first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2. 

# variable = "abcd"
# myList = ['abc', 'xyz', 'aba', '1221']
# count = 0 
# for x in range(0,myList.__len__()) :
#     if (   (myList[x].__len__() >= 2 ) and ( myList[x][0] == myList[x][myList[x].__len__() - 1 ] ) ) :
#         print(myList[x])
#         count += 1
# print(count)


# Exercise: List Comprehensions 
# (i)Write a list comprehension which, from a list, generates a lowercased version of each string that has 
# length greater than five.

myList2 = ["ARHAM","MOIZ","SHAHEER","SAJJAD","ALI"]
print(myList2)
myNewList2 = [x.lower() for x in myList2 if x.__len__() > 5 ]
        
print(myNewList2)

#Not a list comprehension method
# for x in myList2 :
#     if ( x.__len__() > 5 ) :
#         elem_ind = myList2.index(x)
#         myList2[elem_ind] = x.lower()


# (ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']
myList3 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Teapink' ]
# is not used for identity like either those are same objects sharing same memory location while not in checks the equality
myNewList3 = [myList3[x]  for x in range(myList3.__len__() ) if x not in (0,4,5) ]
print(myNewList3)