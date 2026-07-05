names = ["vidhi", "nirali", "prijal", "janvi"]
search = "hetvi"

ispresent = False
for i in names:
    if(search == i):
        ispresent = True
        print("yes "+i+" is present")

if not ispresent:
    print("no "+search+" is not present")
