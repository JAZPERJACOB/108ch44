def students():
    names = ["Dave", "Jazper",  "Andy", "Corey", "Samuel", "Cesar", "Darius", "Demetri", "Janaye", "Donald", "Marco"]
    print(names)
    
    # add elements
    names.append("Sergio")
    
    # travel the list
    for name in names:
        print(name)
    # A) how many anmes are there?
    print(len(names))

def products():
    prices = [23, 234, 34, 672, 77, 214, 756, 76, 500, 479, 629, 325, 389, 29, 101, 50, 67, 800, 54]

    # A) print every price
    # B) sume of all prices
    # C) how many prices are lower than 500
    # D) how many are greater or equal to 500
    total = 0
    count = 0
    expensive = 0
    for price in prices:
        print(price)
        total = total + price
        
        if price >= 500:
            expensive += 1
        
        if price < 500:
            #count = count + 1
            count += 1
        print(total)
        print(count)
        print(expensive)
        
        
def art():
    colors = ["red", "blue", "pink", "blue", "white", "blak", "green", "blak", "red", "white", "blue", "yellow"]
    
    # a) how many colors are there in the list ?
    print(len(colors))
    # b) how many are blue
    # c) how many are white or black
    blue = 0
    black_white = 0
    
    for color in colors:
        if color == "blue":
            blue += 1
            
        if color == "white" or color == "blak":
            black_white += 1
            
    print("blues" + str(blue))
    print("Whites or Blacks" + str(black_white))
# calls
# students()
#products()
art()