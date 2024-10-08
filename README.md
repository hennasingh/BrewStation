# BrewStation 

Brewstation is a Python terminal coffee simulator program, which runs in a mock terminal on Heroku.

Users can perform various actions like buy, fill or check machine status. The program displays some ASCII art and shows a coffee animation. The program is inspired by the Jetbrains Python Academy.

![Coffee Simulator Responsive Image](/readme-content/brewstation.png)

Live version: https://brewstation-4e76688e07ae.herokuapp.com/

## User Experience - UX

### Strategy

Python is a new language for me and I wanted to make a program that would help me be comfortable using Python programming concepts. As a big fan of coffee, animations and emoji, I decided to build a coffee machine with some ASCII art. I had build the same project in Kotlin, and decided to make it it in Python as well.

> The project has no prospective client, it is built purely for fun, engagement and learning purposes

#### User Stories
- I want to be able to understand the purpose of the program
- I want to able to make a choice from the displayed menu
- I want to able to see coffee machine stats
- I want to able to see coffee logo and animation
- I want to able to quit the program

#### User Goals
- Engage with a simple terminal program that is fun and easy to operate

#### Site Owner Goals
- Create an easy to operate, and interactive terminal program
- Add visually appealing features
- Add a fortune cookie option to engage the user
- Give an option to withdraw virtual money and exit

### Structure

The flowchart for the coffee machine simulator is as below:

<img src="./readme-content/brew-flowchart.webp" alt="Coffee Simulator logical flow from power on, making a coffee choice and exiting the program">

## User Interface - Surface

It took a bit of time to finalise the structure, flow and design of the coffee machine simulator. I was still confused whether this would need a class model implementation or not. I got confirmation from my mentor, as this is one machine and I wont be creating multiple objects for it, it is fine to create it without a class.

The menu flow was kept the same as advised in the project by Jetbrains Academy, but more colors, emojis, friendly messages, ASCII art was added to make it more engaging and fun.

ChatGPT was used for coffee animations. For text colors, Rich Text library was used. Coffee ASCII art is taken from https://ascii.co.uk/art/coffee with my own minor additions.

## Features

### Existing Features

#### Welcome Screen
A welcome screen with ASCII art and predefined menu is displayed.

![Welcome msg and Menu Options](./readme-content/welcomeMenu.png)

#### Buy Coffee Menu
 Entering buy coffee displays options to buy or go back to main meny again.

![Coffee menu display](./readme-content/buyMenu.png)

- If enough resources, coffee animation and a success displayed.

![Coffee animation and successful buy message](./readme-content/successBuy.png)

- If not enough resources, a message specifying the resource is displayed.

![Not enough resources for coffee message](./readme-content/failedBuy.png)

#### Take Menu Option
Entering take gives away collected money and money is updated.

![amount of money given and left message](./readme-content/takeMessage.png)

#### Remaining Menu Option
Entering  Remaining display machine ingredients status on that moment.

![coffee ingredients value message](./readme-content/statsMessage.png)

#### Fill Menu Option
Entering fill display machine stats and specify machine capacity and ask for amount of each ingredient

![coffee stats and capacity message](./readme-content/fillMessage.png)

### Error Handling

- Error Handling on Incorrect Action Input

![Invalid Action on incorrect prompt](./readme-content/wrongAction.png)

- Error Handling on Incorrect coffee menu input

![Incorrect input on coffee menu](./readme-content/wrongCoffee.png)

- Error Handling on Incorrect value input

![Incorrect Value on Fill Ingredients](./readme-content/wrongFillAmount.png)

-Error Handling on Exceeding Ingredient Amount

![Exceeding Fill Value](./readme-content/exceedFill.png)

### Future Features

- Allow user to fill the specified insufficient ingredient.
- Loop back through the fill ingredients menu, after an invalid entry.
- Allow user to set machine ingredients when the machine is started.
- Add a fortune cookie message along with a coffee animation

## Testing

Testing details can be found in [testing.md](testing.md)

## Technologies Used

### Languages

- HTML - For layout of the terminal
- CSS - For background and flex display of the mock terminal
- [Python](https://www.python.org/) - Main language for the terminal program

### Python Packages

- [Rich Text](https://pypi.org/project/rich/) - For adding colors to text
- [Art](https://pypi.org/project/art/) - For heading font style

### Other Softwares

- [Draw.io](https://app.diagrams.net/) - Used to create flowchart for the coffee machine
- [Gitpod](https://www.gitpod.io/#get-started) - Used to code the project and save to online repo
- [Github](https://github.com/) - For version control
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) - For python code validation
- [Heroku](https://id.heroku.com/login) - For terminal deployment


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

### Heroku 

- Create an account on Heroku.
- Navigate to Heroku Dashboard and "Create a New App".
- Input App name and choose a region you are closer to.
- Select "Settings" from the table, and search for "Buildpack"
- Add "python" and "nodejs" from the list, in that order.
- Go to Deploy section, connect to GitHub.
- Seach for the repository name to connect.
- Click on Deploy Branch or enable Automatic Deploy.
- Allow a few minutes and view the deployed program.

## Credits

### Content

- [Stack Overflow](https://stackoverflow.com/questions/52335970/how-to-fix-syntaxwarning-invalid-escape-sequence-in-python) - For correcting invalid excape sequence warning
- [Jetbrains Python Academy](https://github.com/Flor91/jetbrains-python-academy/tree/master/Coffee%20Machine) - For inspiration on Coffee Machine project
- [Typing Hints](https://docs.python.org/3/library/typing.html) - For python typing hints

### Media
- [Geeks for Geeks](https://www.geeksforgeeks.org/python-program-to-print-emojis/) - Unicodes to print emojis
- [ascii art](https://ascii.co.uk/art/coffee) - For Coffee ASCII Art
- [PythonGPT](https://openai.com/chatgpt/) - For Coffee animation code


## Acknowledgements
- [Code Institute](https://codeinstitute.net/) for Python essentials and Love Sandwiches project
- Spencer Barriball  - For his guidance and review on the project
- Code Institute Slack Community - For feedback, reviews and community support.
