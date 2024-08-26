from rich.console import Console 
from art import *

console = Console()

tprint("Arya's BrewStation", font="bulbhead")
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
    Welcome to Arya's BrewStation! Whether you're a coffee newbie or a seasoned 
    sipper, BrewStation turns every brew into an adventure. 
    Ready to pour your passion into the perfect cup? Let’s get brewing! 
    """, style="bold green")

status = True

machine_status = {
    'water':400,
    'milk' : 540,
    'coffee': 120,
    'cups': 9,
    'money': 550
}

def machine_stats():
    """
    The function prints the ingredients available in the machine
    """
    console.print("The coffee machine has:")
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
        console.print(":unamused_face: There is [red]0[/] balance in the machine, you have taken all !" )
        return
    
    console.print(f"I give you ${machine_status['money']} and machine has [red]0[/] balance", style="bold grey37")
    machine_status['money'] = 0


def check_machine_action(action):
    global status

    if action == "buy":
        pass
    elif action == "fill":
        fill_machine_ingredients()
    elif action == "take":
        take_money()
    elif action == 'remaining':
        machine_stats()
    elif action == 'exit':
        status = False
    else:
        print("Invalid action")


def start_coffee_machine():
    """
    The function that starts the machine and pass the input action
    """
    while status:
        action = input(f"Write action (buy, fill, take, remaining, exit):")
        check_machine_action(action.lower())


start_coffee_machine()

