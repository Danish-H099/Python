# Dictionary is the collection of key-value pair
# One Key will have only one Value if You try to have many values on same key
# Then key will store only last element you entered
# Unlike list Dictionary is Unordered

myDict={
    "Name":"Danish", # Name->Key & Danish->Value
    "Roll":2106112,
    "Marks":[22,28,12,22,26], #List in a Dictionary
    "a":{"LastName":"Dar"} #Dictionary in a Dictionary
}

print(type(myDict)) #op-><class 'dict'>
print(myDict["Name"]) #op-> Danish
print(myDict["Marks"]) #op-> [22, 28, 12, 22, 26]
print(myDict["a"]["LastName"]) #op-> Dar

# Dictionary is muttable i.e we can change key value pair 
myDict["Marks"]=[30,29,30,27,29] # Overridding of marks
print(myDict["Marks"]) # op-> [30,29,30,27,29]

