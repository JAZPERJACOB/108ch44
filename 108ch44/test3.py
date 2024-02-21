

def about_me():
    me = {
        "first": "Jazper",
        "last": "Jacob",
        "age": 29,
        "address": {
            "street": "Ocean Front",
            "number":"23",
            "city": "San Diego",
            "zip": "92188",
        }
    }

    print(me)
    #read values
    print(me["first"] + " " + me["last"])
    print(f"I'm {me['age']} years old")
    
    # read the address
    # print(me["address"]["street"])
    
    # address = me["address"]
    # print(address["street"])
    
    address = me["address"]
    street = address["street"]
    number = address["number"]
    city = address["city"]
    zip = address["zip"]
    print(street)
    
    # a) street #numb, city, zip.
    
    print(f"Return to: {street} #{number}, {city}, {zip}.")
    
    
# fn calls
about_me()