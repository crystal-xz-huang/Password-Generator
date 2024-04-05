#!/usr/bin/env python3

# Simple password generator in Python
# that generates a random password given the following input:
# - words 
# - whether to capitalise the first letter of each word
# - whether to include special characters
# - how many special characters to include

import random
import string

def generate_password(words, special_chars, num_special_chars, numbers, num_numbers):
    password = ''
    for word in words:
        password += word
    if special_chars:
        for _ in range(num_special_chars):
            password += random.choice(['!', '$', '-'])
    if numbers:
        for _ in range(num_numbers):
            password += random.choice(string.digits)
    return password

def main():
    words = input('Enter words separated by a space: ').split()
    print(words)
    capital = input('Capital letters? (y/n): ')
    if capital == 'y':
        words = [word.capitalize() for word in words]
    special_chars = input('Do you want special characters? (y/n): ')
    if special_chars == 'y':
        special_chars = True
        num_special_chars = int(input('How many special characters do you want? '))
    else:
        special_chars = False
        num_special_chars = 0
    numbers = input('Do you want numbers? (y/n): ')
    if numbers == 'y':
        numbers = True
        num_numbers = int(input('How many numbers do you want? '))
    else:
        numbers = False
        num_numbers = 0
    password = generate_password(words, special_chars, num_special_chars, numbers, num_numbers)
    print(f'Generated password: {password}')

if __name__ == '__main__':
    main()


