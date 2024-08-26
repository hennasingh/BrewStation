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

