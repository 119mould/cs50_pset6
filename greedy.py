import cs50

def main():
    # prompts the user for change until change is greater than 0
    while True:
        print("O hai! How much change is owed?")
        change = cs50.get_float()
        if (change >= 0):
            break
        
    change = round(change * 100)
    # keep track of the number of coins used to give change
    count = 0
        
    # give coins and increase count until change equals 0
    while True:
        if change >= 25:
            count += 1
            change -= 25
        if change >= 10 and change < 25:
            count += 1
            change -= 10
        if change >= 5 and change < 10:
            count += 1
            change -= 5
        if change >= 1 and change < 5:
            count += 1
            change -= 1
        if change == 0:
            break
            
    print(count)
        
    
    
    
if __name__ == "__main__":
    main()