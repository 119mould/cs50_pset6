import cs50
import sys

def main():
    
    # ensure proper usage
    if len(sys.argv) != 2:
        print("Wrong number of arguments!")
        exit(1)
    
    # ensure that key contain only alhabetic characters    
    if sys.argv[1].isalpha() == False:
        print("Wrong keyword format!")
        exit(1)
    
    # store key numbers in array       
    key = []
    for c in sys.argv[1]:
        if (c.isupper()):
            key.append(ord(c) - 65)
        if (c.islower()):
            key.append(ord(c) - 97)
     
    # prompt user for plaintext        
    print("plaintext: ", end="")
    text = input()
    
    result = ""
    tracker = 0
    # iterate over plaintext
    for i in range(len(text)):
        index = tracker % len(key)
        # if current element is empty space, continue to next element
        if (text[i] == " "):
            result += " "
            i += 1 
        # get characters position in alphabet and number (diff) to move  
        elif (text[i].islower()):
            position = ord(text[i]) - 97
            diff = (position + key[index]) % 26
            result += chr(diff + 97) # --> add modified character to result
            tracker += 1 # --> increment tracker only when current element is alphabetical
        elif (text[i].isupper()):
            position = ord(text[i]) - 65
            diff = (position + key[index]) % 26
            result += chr(diff + 65)
            tracker += 1
        else:
            result += text[i]
     
    #success        
    print("ciphertext: {}".format(result))
    exit(0)
    
    
    
if __name__ == "__main__":
    main()