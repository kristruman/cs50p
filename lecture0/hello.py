# Ask user for their name.
name = input("Please enter your name: ").strip().title()

# Say hello to the user!
print(f"Hello, {name}! It's nice to meet you.")
# alternate: print("Hello,", name) - multi argument version.

# name = name.strip() - strip whitespace
# name = name.capitalize() - capitalize first letter of string
# name = name.title() - capitalize first letter of each word of string
# methods can be chained .strip().title()