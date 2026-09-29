
# ---------------------------------------------------------
# 3. AUGMENTED ASSIGNMENT OPERATORS
# ---------------------------------------------------------
# Shortcuts for "update a variable based on its own value."

balance = 100
print("3. Augmented assignment")
print("Start:", balance)

balance += 50     # same as balance = balance + 50
print("After deposit:", balance)

balance -= 30     # same as balance = balance - 30
print("After withdrawal:", balance)

balance *= 2      # same as balance = balance * 2
print("After doubling:", balance)

balance //= 3     # floor division: divides and drops the remainder
print("After floor-dividing by 3:", balance)

balance %= 7      # modulus: gives the REMAINDER after division
print("Remainder when divided by 7:", balance)
print()
