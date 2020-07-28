# Import random below:
from decimal import Decimal
from string_methods_lab import count_char_x
import random

# Create random_list below:
random_list = [random.randint(1, 101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)


# Add your code below:
numbers_a = range(1, 13)
print(numbers_a)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)

# Import Decimal below:

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)

#imported count_char_x function
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
