# BrewStation - Testing
This page talks about testing the python program code.

> Note: The program is not suitable to work on small screens or mobiles. The application code runs on mock terminal provided by Code Institute.

## PEP8 Testing

Finding the right tool for validating python code was tricky. I tried with pycodestyle as previously used by other students but it did not work the same way. The [Python Linter](https://pep8ci.herokuapp.com/) tool provided by Code Institute was used for successfully validating the Python code.

__Testing run.py__
The initial run pointed some errors as shown. The other errors were length of the line being longer than 79 characters. The code was split to multiple lines to fix the error.

![python validation errors](/readme-content/pep8Errors.png)

All errors were fixed except one, as it was difficult to split the condition in two lines:

![successful python code validation](/readme-content/pep8noErrors.png)

__Testing coffee.py__

The initial run pointed few length and space errors as shown below:

![python code errors on coffee animation code](/readme-content/pep8errorCoffee.png)

After fixing the pointed errors, another validation was done:

![python code with no errors in coffee animation code](/readme-content/pep8noErrorCoffee.png)

## Manual Testing

### Testing User Stories

The following user stories were considered in the UX -Strategy phase

> I want to be able to understand the purpose of the program

> I want to be able to make a choice from the displayed menu

The start of the program introduces the coffee machine simulation and provides user a menu to select a choice.

![coffee ascii art welcoming user and displaying menu options to choose from](/readme-content/welcomeArtMenu.png)


> I want to be able to see coffee machine stats

The user can choose the option from the menu to see the remaining coffee ingredients.

![coffee ingredients remaining](/readme-content/statsMessage.png)

> I want to be able to see my coffee filling.

The program shows a coffee animation, after a choice is selected.

[![Coffee Animation Video](https://raw.githubusercontent.com/hennasingh/BrewStation/main/readme-content/welcomeArtMenu.png)](https://raw.githubusercontent.com/hennasingh/BrewStation/readme-content/coffeeAnime.mp4)

> I want to able to quit the program

The exit option in the menu stops further execution of the program.




