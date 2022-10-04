# Import Modules
import random

# Global Constants
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3    # Number of rows
COLS = 3    # Number of columns

# Symbols for each reel
symbol_count = {    #dictionary
    "A": 2,
    "B": 4, 
    "C": 6,
    "D": 8
}

# Values for each reel
symbol_value = {    
    "A": 5,
    "B": 4, 
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bets, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            
            if symbol != symbol_to_check:
                break
        else:
            winnings += ((values[symbol] * bets) + bets) # should be adding to the current amount after bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    # List randomly choosen
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
              
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]    # Copies from all_symbols list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns
        
        
def print_slot_machine(columns): # Prints the values of the Slot Machine
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
                
        print() # At the end of the row 


def deposit(): # Gets deposit
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():    #Checks if input is valued amount
            amount = int(amount)
            if amount > 0:
                break
            else :
                print("Amount is not value. Must be greater than zero.")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines(): # Gets number of lines
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():    
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else :
                print("Enter a valid number of lines ")
        else:
            print("Please enter a number")
    return lines

def get_bet(): # Gets bet in '$' amount for each line
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():    #Checks if input is valued amount
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else :
                print(f"Amount must be betweem ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number") 
            
    return amount    

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, you current balance is ${balance}")
        else: 
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won: ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main(): # Main function
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}") # if balance is 0 then break
        if balance <= 0:
            answer = input("Press enter to play again or 'q' to quit).")
            if answer == "q":
                break
            else:
                balance = deposit()
        balance += spin(balance)
        
    print(f"You left with ${balance}")
    
main() # Calls main function