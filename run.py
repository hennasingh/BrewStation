from rich.console import Console 
from art import *

console = Console()

tprint("BrewStation")
console.print(r"""
        /~~~~~~~~~~~~~~~~~~~/|                   {
       /              /######/ / |       }    }    {  
      /              /______/ /  |      {    {  }   }
     ========================= /||        }   }{   { 
     |_______________________|/ ||       {  }{   }   }
      |  \****/     \__,,__/    ||      ( }{ }{    { )
      |===\**/       __,,__     ||     .-{   }     }-.
      |______________\====/%____||    ( ( } { }   { } ) 
      |   ___        /~~~~\ %  / |    |'-.._______..-'|
     _|  |===|===   /      \%_/  |    |               ;--.
    | |  |###|     |########| | /     |              (__  \
    |____\###/______\######/__|/      |               | )  )
    ~~~~~~~~~~~~~~~~~~~~~~~~~~        \               (   /
    ~~~~~~~~~~~~~~~~~~~~~~~~~~        '-.._______..-'  ''  
    """, style="bold yellow")

console.print("""
    Welcome to BrewStation! Whether you're a coffee newbie or a seasoned 
    sipper, BrewStation turns every brew into an adventure. 
    Ready to pour your passion into the perfect cup? Let’s get brewing! 
    """, style="bold green")


## Define variables

#status to control the flow of machine
status = True

# Default machine ingredients stats
machine_status = {
    'water':400,
    'milk' : 540,
    'coffee': 120,
    'cups': 9,
    'money': 550
}

# water, milk, coffee, cup, cost
espresso = [250, 0, 16, 1, -4]
latte = [350, 75, 20, 1, -7]
cappuccino = [200, 100, 12, 1, -6]

def machine_stats():
    """
    The function prints the ingredients available in the machine
    """
    console.print("The coffee machine has:", style="purple3")
    console.print(f"{machine_status['water']} ml of water")
    console.print(f"{machine_status['milk']} ml of milk")
    console.print(f"{machine_status['coffee']} g of coffee beans")
    console.print(f"{machine_status['cups']} disposable cups")
    console.print(f"${machine_status['money']} of money")


def take_money():
    """
    The function gives all the money within machine and change value to zero
    """
    if machine_status['money'] == 0:
        console.print(":unamused_face:\00 There is [red]0[/] balance in the machine, you have taken all !", style="plum4" )
        return
    
    console.print(f"I give you ${machine_status['money']} and machine has [red]0[/] balance", style="bold plum4")
    machine_status['money'] = 0


def fill_machine_ingredients():
    """
    The function replenishes the supply of ingredients in the machine 
    taking input from the user.
    """

    for key in machine_status:
        if key != "money":
            machine_status[key] += int(input("Write how much {} you want to add:\n".format(key)))    
    machine_stats()


def get_coffee(choice, coffee):
    """
    The function calculates the ingredients required for the choice of coffee and keep
    a log of remaining amount
    :param choice: The selected choice of coffee
    :return: message based on resources
    """

    if machine_status['water'] < choice[0]:
        return ":upside-down_face:\00 Sorry, not enough water!"
    elif machine_status['milk'] < choice[1]:
        return "upside-down_face:\00 Sorry, not enough milk!"
    elif machine_status['coffee'] < choice[2]:
        return ":upside-down_face:\00 Sorry, not enough coffee!"
    elif machine_status['cups'] < choice[3]:
        return ":upside-down_face:\00 Sorry, not enough disposable cups!"

    # Deduct the ingredients
    for key, value in zip(machine_status, choice):
        machine_status[key] -= value

    return ":smiley:\00 I have enough resources, making you a {}!".format(coffee)


def buy_coffee():
    """"
    The function displays coffee choices to the user and ask for a choice or go back to the main menu
    """
    user_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

    message = ''
        
    if user_choice == '1':
        message =  get_coffee(espresso, "espresso")
    elif user_choice == '2':
        message = get_coffee(latte, "latte")
    elif user_choice == '3':
        message = get_coffee(cappuccino, "cappuccino")
    elif user_choice == 'back':
        return
    else:
        console.print("Invalid choice. Please try again", style="dark_red")
        buy_coffee()

    console.print(message)



def check_machine_action(action):
    global status

    if action == "buy":
        buy_coffee()
    elif action == "fill":
        fill_machine_ingredients()
    elif action == "take":
        take_money()
    elif action == 'remaining':
        machine_stats()
    elif action == 'exit':
        status = False
    else:
        console.print("Invalid action, Please try again!", style="dark_red")


def start_coffee_machine():
    """
    The function that starts the machine and pass the input action
    """
    while status:
        action = input(":smile:\00 Write action (buy, fill, take, remaining, exit):\n")
        check_machine_action(action.lower())


start_coffee_machine()

