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

The program shows a coffee animation, after a choice is selected. (The coffee video could not be uploaded)

![coffee mug with foam and coffee message](/readme-content/coffeeMug.png)

> I want to able to quit the program

The exit option in the menu stops further execution of the program.

## Manual Feature Tests

After fixing the spaces and line character length pointed by Python Linter, manually testing the code discoverd some errors that were fixed.
- The return statement was one line before the string message and empty message was being returned. This made the animation to not run, and introduced type error.
- There have been new lines and tabs introduced in the display of messages because of the length of the message. I do not yet know how to make then appear justified.
- The conditional statements can be separated on different lines and hence one if statment was kept longer than others

Other Actions and Outcomes are as below:

### Testing Buy Option

| Action | Expected Outcome | Result |
| ------ | ---------------- | ------ |
| Click on the run program button | The program displays coffee art and menu choices | Pass |
| Type "buy" at the prompt | The coffee menu options are displayed | Pass |
| Type 12 at the prompt and enter | Invalid input message and prompt to enter between (1-3) is displayed | Pass |
| Type random text at the prompt | Invalid message and prompt to enter (1-3) is displayed | Pass |
| Type 2 with a whitespace | Success Message and coffee animation is played | Pass |
| Type "buy again followed by "back" at the prompt | Menu goes back to main | Pass |
| Type "buy" followed by 2 at the prompt | Sorry message specifying missing ingredient is displayed | Pass |

### Testing Fill Ingredients Option

For recurring testing, the menu option "Fill" has to be typed everytime an invalid message is displayed. The program goes back to the main menu and does not loop through same options. For the tests below, it is assumed you type "fill" prompt everytime it goes back to main menu.

| Action | Expected Outcome | Result |
| ------ | ---------------- | ------ |
| Type "fill" at the prompt | Coffee Machine Stats, Guideline message and input asking for water quantity is displayed | Pass |
| Type alphanumeric data like chs13 | Invalid message displayed | Pass |
| Type number > 2000 | Exceed machine capacity message displayed | Pass |
| Type any number below 2000 | The program accepts value and ask for milk quantity | Pass |
| Type any number below 2000 | The program accepts value and asks for coffee quantity | Pass |
| Type "100 grams" | Invalid message pointing to grams displayed | Pass |
| Type any number below 1000 | The program accepts value and ask for number of cups | Pass |
| Type value below 20 | The program displays revised machine stats and main menu | Pass |

### Testing Take Money Option

| Action | Expected Outcome | Result |
| ------ | ---------------- | ------ |
| Type "take" at the prompt | Message on total money given and balance left displayed | Pass |
| Type "take" again at the prompt | Unamused emoji and 0 balance left dislayed | Pass |

### Testing Remaining and Exit  Option

| Action | Expected Outcome | Result |
| ------ | ---------------- | ------ |
| Type "remaining" at the prompt | The coffee ingredients stats displayed | Pass |
| Type "exit" at the prompt | The program stops executing further | Pass |


## Struggles, Learnings and AHA Moments

This is my first time using python and I learnt a lot while working on this python program. I think I found the language very fascinating.

1. The first struggle and AHA moment was font and color choosing. I had no idea terminal programs could be colorful. I saw previous students projects and found out about colors and ASCII art. A friend of mine suggested rich python library and I discovered about art library while researching for coffee art. The [coffee ASCII art](https://ascii.co.uk/art/coffee) was another AHA moment. I only discovered then that the art is printed as is. It took a bit of patience to print both machine and coffee mug adjacent to each other.

2. Another struggle was on putting the right spaces and new line characters after each dialogue. It appeared very close to each other. Adding space did not work as I expected. I explored about unicode characters and added unicode alongside each emoji to put a space. Adding "\n" within the print statement of the dialogue adding some spacing in the conversation.

3. Input error handling for "fill" menu was challenging. The strategic way I finalized was adding maximum capacity to the machine so random numbers are not added. The user experience for this section can be improved, as the function comes back to the main menu, if an invalid input is provided.

4. Finalizing on Python Linter took time. The previous students mentioned about pycodestyle , while vs code complained about deprecation of the same. I installed Pylint and then Flake8 and also tried Ruff. This was quite an exploration to number of linters available for Python. I finally validated using Linter provided by Code Institute. Although, some lines are longer than others as I was not able to move condition statement to new line. Some longer lines messed up print messages. They appeared halfway in the new line. 

![message on taking the money](/readme-content/takeMsg.png)

As this was a simple coffee machine simulator, I did not have encountered lot of bugs while designing it. There were some gotchas in input values that needed error handling but other than that, it was easy to build. I am happy to make somthing in a language I have never used before.

## Unresolved Bugs

There are no known unresolved bugs in the program.






