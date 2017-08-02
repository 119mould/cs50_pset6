import cs50

def main():
    # prompt user for height until height is in correct range 
    while True:
        print("Height: ", end="")
        height = cs50.get_int()
        if height >= 0 and height <= 23:
            break
        
    # for each step    
    for i in range(height):
        # print spaces
        for s in range(height - (i + 1)):
            print(" ", end="")
        # print left side of pyramid 
        for h in range(i + 1):
            print("#", end="")
        # print space between pyramids
        print("  ", end="")
        # print right side of pyramid
        for r in range(i + 1):
            print("#", end="")
        #print new line
        print("")
        

if __name__ == "__main__":
    main()
        
    
  
   