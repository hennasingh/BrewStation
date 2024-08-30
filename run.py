from rich.console import Console 
from art import *
import coffee

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
    console.print("\nThe coffee machine has:", style="purple3")
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
        console.print("\n:unamused_face:\u0020 There is [red]0[/] balance in the machine, you have taken all !", style="plum4" )
        return
    
    console.print(f"\nI give you ${machine_status['money']} and machine has [red]0[/] balance", style="bold plum4")
    machine_status['money'] = 0


def fill_machine_ingredients():
    """
    The function replenishes the supply of ingredients in the machine 
    taking input from the user.
    """

    console.print("\n Please enter water in ml and coffee in grams\n", style="green")
    console.print("The machine cannot take more than 2000 ml of water, 2000 ml of milk, 1000 grams of coffee and 20 disposable cups\n", style="yellow")
    machine_stats()

    try:
        for key in machine_status:
            if key != "money":
                value = int(input("\nWrite how much amount of {} you want to add:\n".format(key)).strip())
                if value < 0:
                    raise ValueError("Please enter a positive value")
                if (key == "water" or key == "milk") and machine_status[key] + value > 2000:
                    raise ValueError("The entered value exceeds 2000 ml for {}, please enter amount below 2000".format(key))
                if(key == "coffee" and machine_status[key] + value > 1000):
                    raise ValueError("The entered value exceeds 1000 grams for coffee. Please enter a value equal to or below {}".format((1000 - machine_status[key])))
                if key == "cups" and machine_status[key] + value > 20:
                    raise ValueError("The entered value exceeds 20 disposable cups that machine can take. please enter a value equal or below {}".format((20 - machine_status[key])))                  
            machine_status[key]+= value
        machine_stats()
    except ValueError as e:
        console.print("\nInvalid data: {}, please try again". format(e), style="dark_red")



def get_coffee(choice, coffee):
    """
    The function calculates the ingredients required for the choice of coffee and keep
    a log of remaining amount
    :param choice: The selected choice of coffee
    :return: message based on resources
    """

    if machine_status['water'] < choice[0]:
        return ":upside-down_face:\u0020 Sorry, not enough water!"
    elif machine_status['milk'] < choice[1]:
        return "upside-down_face:\u0020 Sorry, not enough milk!"
    elif machine_status['coffee'] < choice[2]:
        return ":upside-down_face:\u0020 Sorry, not enough coffee!"
    elif machine_status['cups'] < choice[3]:
        return ":upside-down_face:\u0020 Sorry, not enough disposable cups!"

    # Deduct the ingredients
    for key, value in zip(machine_status, choice):
        machine_status[key] -= value

    return ":smiley:\u0020 I have enough resources, making you a {}!".format(coffee)


def buy_coffee():
    """"
    The function displays coffee choices to the user and ask for a choice or go back to the main menu
    """

    user_choice = input("\nWhat do you want to buy?\n 1 - espresso\n 2 - latte\n 3 - cappuccino\n  back - to main menu:\n").strip()

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
        console.print("\nInvalid choice. Please enter numeric numbers (1 -3) or enter 'back", style="dark_red")
        buy_coffee()

    console.print(message)

    if "I have" in message:
        # Run the animation
        coffee.fill_coffee_mug()
    



def check_machine_action(action):
    global status

    if action in ("buy", "buy coffee"):
        buy_coffee()
    elif action in ("fill", "fill ingredients"):
        fill_machine_ingredients()
    elif action in ("take", "take money"):
        take_money()
    elif action == 'remaining':
        machine_stats()
    elif action == 'exit':
        status = False
    else:
        console.print("\nInvalid action, Please try again!", style="dark_red")


def start_coffee_machine():
    """
    The function that starts the machine and pass the input action
    """
    while status:
        action = input(
        "\nWrite action (buy, fill...): \n \U0001F60B \u0020 Buy coffee \n \U0001F47E \u0020 Fill Ingredients \n \U0001F911 \u0020 Take money \n \U0001F47B \u0020 Remaining \n \U0001F62D \u0020 Exit\n")
        check_machine_action(action.strip().lower())


start_coffee_machine()

