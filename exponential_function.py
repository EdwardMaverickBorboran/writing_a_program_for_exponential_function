# Create a program that will --

# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# Expected results: 
# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

# DEADLINE: JANUARY 26, 2024

# pseudocode

def exp(user_base, user_exp):

    base = user_base
    exponent = user_exp

    final_results = base ** exponent

    print(base, "raises to the power of", exponent,":", final_results)


# Asking the user to input a number
user_base = int(input("Enter number for base:"))
user_exp = int(input("Enter number for exp:"))


exp(user_base, user_exp)