
def hello ():
    print("Hello there")
    print("Hello there")
    print("Hello there")

def about_me():
    me = {
        "name": "Jesse",
        "last": "Whatley",
        "age": 32,
        "address": {
            "street": "case",
            "city": "LaBelle"
        }
    }
    print(me)
    # read
    print(me["name"] + " " + me["last"])
    
    if "email" in me:
        print(me["email"])
    
    email = me.get("email", "NO EMAIL")
    print(email)
    
    # print the address
    # print(me["address"]["street"] + " " + me["address"]["city"])
    address = me["address"]
    print(address["street"] + ", " + address["city"])
    
    # add fields
    #email = 

def print_names():
    names = ["Alexis", "Alexis", "Jay", "Kevin", "Jesse"]
    
    print(names)
    print(len(names))
    
    for name in names:
        print(name)
        


# function 
#hello()
#about_me()
print_names()