#WAP to create a dictionary of hindi words and values will be their English translation

Dict={
    "mera":"My",
    "kaam":"Work",
    "pakana":"Cooking"
}
print("Available options are ",list(Dict.keys()))
a=input("Enter the Hindi word whose English You want :")
print(Dict.get(a))
