# BrewStation - Testing
This page talks about testing the python program code.

## PEP8 Testing

Finding the right tool for validating python code was tricky. I tried with pycodestyle as previously used by other students but it did not work the same way. The [Python Linter](https://pep8ci.herokuapp.com/) tool provided by Code Institute was used for successfully validating the Python code.

The initial run pointed some errors as shown. The other errors were length of the line being longer than 79 characters. The code was split to multiple lines to fix the error.

![python validation errors](/readme-content/pep8Errors.png)

All errors were fixed except one, as it was difficult to split the condition in two lines:

![successful python code validation](/readme-content/pep8noErrors.png)
