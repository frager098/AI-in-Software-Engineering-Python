# (i)Use dir and help to learn about the functions you can call on dictionaries and implement it. 

# help(dict)
# dictionary = { "firstName":"Arham" ,"lastName": "Khalid", "age" : "20" }
# print (dictionary.__contains__("firstName") ) #Returns true if key is present
# print( dictionary.items()  ) #Returns items as tuples of key , value pairs 
# temp = dictionary.__delitem__("firstName") #deletes an item from original dictionary and returns None
# print(dictionary)


# (ii)Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

myDictionary1 = { "1":10 , "2" : 20}
myDictionary2 = { "3":30 , "4" : 40}
myDictionary3 = { "5":50 , "6" : 60}
# myDictionary = myDictionary1 + myDictionary2 + myDictionary3 
# print(myDictionary)
myDictionary = {}
myDictionary.update(myDictionary1)
myDictionary.update(myDictionary2)
myDictionary.update(myDictionary3)
print(myDictionary)