OPERATOR = ['+','-','*','/','%']

def restart() -> bool:
    """  
    Restart function:
    the input ask to user if he wants to keep calculating or leave

    if answer is [r] then return True
    else return False
    """
    answer = input(f"Type r-[restart] or press enter -[exit]: ").lower()
    if answer == 'r': 
        return True
    return False

# Loop to run the main code
while True:
    operator = input(f"Type the operator: ")
    if not operator in OPERATOR or operator.isdigit():
        print("It's not valid")
        continue
    try:
        number_1 = float(input(f"Number 1: "))  # Ask for the first number
        number_2 = float(input("Number 2: "))  # Ask for the second number      
    except ValueError as e:
        print(f"{e}")     # Display the ValueError
        continue

    if number_2 == 0:   # Check if the user is dividing to 0 
        print(f"It's not possible divide to 0")
        input("Press enter")
        continue
    
    
    match operator:
        case '+': # Sum print
            print(f"The result {number_1 + number_2}")
            if not restart():
                break
        case '-':   # Subtract print
            print(f"The result {number_1 - number_2}")
            if not restart():
                break
        case '*': # Mutiplication print
            print(f"The result {number_1 * number_2}")
            if not restart():
                break
        case '/': # Divide print
            print(f"The result {number_1 / number_2}")
            if not restart():
                break
        case '%': # Rest of divide print
            print(f"The result {number_1 % number_2}")
            if not restart():
                break
        