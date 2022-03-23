# definig two or more variables at the same code line
name, age = "Nathália", 21

print(name)
print(age)

# ways to name variables that have more than 1 word
fullName = "Nathália Magre Guerra Pinto"
full_name = "N Magre"

brand = "Amigoscode"
age = 2
numbers = []
pi = 3.14
isAdult = True

# discovering the type of the variable
print(type(brand))
print(type(age))
print((type(numbers)))
print((type(pi)))
print((type(isAdult)))

# defining a variable and saying is supposed type
course: str = "Python"
isCool: bool = True

"""
I am a comment
a second comment
third comment
"""

# Strings - useful to store any text
# if we put a dot after the string name there are many methods
print(brand.upper())
print(brand.replace('A', 'u'))
print(len(brand))
print(brand == "amigoscode")
print(brand == "Amigoscode")
print("code" in brand)
print("code" not in brand)

# Multiline and Formatting Strings
comment = """"
nathalia magre guerra pinto
is doing 
a python course
"""
print(comment)

email = f"""
Hello {name},
it was nice talking to you
"""
print(email)

