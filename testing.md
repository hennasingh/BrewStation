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
