## A fun 13 char shift to the right 

### The Algo

Add the salt to the input. Example input = test, salt = salty, salted input = testsalty\
Get the ascii code for each character and shift it by +13\
Take the salted and encrpyed input and loop through it. If i %2 == 0 and the ascii code % 2 == 0 char = ascii code += 2

#### How to use

Navigate to the hash.py file in the terminal. Example ~/Downloads/PYTHON_HASHED/hash.py\
Enter "python hash.py", enter input\
The terminal will print the input, salted and encrpyed input, and the deencrpyted output
