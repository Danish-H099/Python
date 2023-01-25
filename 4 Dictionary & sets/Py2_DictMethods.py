myDict={
    "Name":"Danish", 
    "Roll":2106112,
    "Marks":[22,28,12,22,26], 
    "a":{"LastName":"Dar"}, 
    1:2
}
print(myDict) # op->{'Name': 'Danish', 'Roll': 2106112, 'Marks': [22, 28, 12, 22, 26], 'a': {'LastName': 'Dar'}, 1: 2}

# Key Method
print(myDict.keys()) # op-> dict_keys(['Name', 'Roll', 'Marks', 'a', 1])
#Making List of Keys
print(list(myDict.keys())) # op-> ['Name', 'Roll', 'Marks', 'a', 1]

# Value Method
print(myDict.values()) 
# op->dict_values(['Danish', 2106112, [22, 28, 12, 22, 26], {'LastName': 'Dar'}, 2])
#Making List of Values
print(list(myDict.values())) 
# op-> ['Danish', 2106112, [22, 28, 12, 22, 26], {'LastName': 'Dar'}, 2]

# Items-> prints all (key:value) pair for the dictionary
print(myDict.items()) 
#op-> dict_items([('Name', 'Danish'), ('Roll', 2106112), 
# ('Marks', [22, 28, 12, 22, 26]), ('a', {'LastName': 'Dar'}), (1, 2)])

#Update method
updateDict={
    "DOB":"05 Mar 2002",
    5:33,
    "Name":"Hussain" #->updates the name
}
myDict.update(updateDict) # appends the above updatedict into mydict
print(myDict) # Op-> {'Name': 'Hussain', 'Roll': 2106112, 
#'Marks': [22, 28, 12, 22, 26], 'a': {'LastName': 'Dar'}, 1: 2, 'DOB': '05 Mar 2002', 5: 33}

#get Method
print(myDict.get("Name")) #Hussain
#if You provide a key which isn't present in the dictionary then it gives None as outpur
# myDict["Name"] gives error if key isn't present in the dictionary