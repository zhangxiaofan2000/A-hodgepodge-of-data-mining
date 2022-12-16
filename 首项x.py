# -*- coding: utf-8 -*-
# Auther : ZhangYiLong
# Mail : 503302425@qq.com
# Date : 2022/12/14 22:54
# File : 首项x.py
# define the number of items in the sequence
# Define the number of zeros we are looking for and the number of terms in the sequence
num_zeros = 100
num_terms = 2022

# Iterate over a range of possible values for x
for x in range(-100, 100):
  # Initialize the sequence with the first term
  sequence = [x]

  # Generate the remaining terms in the sequence using the given formula
  for i in range(1, num_terms):
    sequence.append(abs(sequence[i-1] - 1))

  # Count the number of zeros in the sequence
  if sequence.count(0) == num_zeros:
    # If the number of zeros matches the given condition, save the value of x
    x_values.append(x)

# Print the list of values for x that satisfy the given conditions
print(x_values)
