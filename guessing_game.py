# MIT License

# Copyright (c) 2024 Lawi Corp

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.



import random

positive_list = ['yes', 'true', 'correct']
strategy_dict = {'1': 'binary_search', '2': 'truly_random', '3': 'quarter_slice'}

def binary_search(number):
    guessing = True
    guesses = 0
    nums = range(1, 101)

    while guessing:
        guess = nums[int(len(nums)/2)-1]

        user_input = input(f'Is your number {guess}? No --> (Lesser / Greater) >>> ')

        guesses += 1

        if user_input.lower() in positive_list and guess == number:
            print(f'GGs! [guesses: {guesses}]')
            guessing = False
        elif user_input.lower() == 'greater' and guess < number:
            nums = nums[nums.index(guess)+1:]
        elif user_input.lower() == 'lesser' and guess > number:
            nums = nums[:nums.index(guess)]
        else: guesses -= 1

def truly_random(number):
    guessing = True
    guesses = 0
    nums = range(1, 101)

    while guessing:
        guess = random.choice(nums)
        while True:

            user_input = input(f'Is your number {guess}? No --> (lesser / greater) >>> ')

            guesses += 1

            if user_input.lower() in positive_list and guess == number:
                print(f'GGs! [guesses = {guesses}]')
                guessing = False
            elif user_input.lower() == 'greater' and guess < number:
                nums = nums[nums.index(guess)+1:]
            elif user_input.lower() == 'lesser' and guess > number:
                nums = nums[:nums.index(guess)]
            else: guesses -= 1; continue
            break

def quarter_slice(number):
    guessing = True
    guesses = 0
    nums = range(1, 101)

    while guessing:
        s = random.randint(0, 1)

        while True:
            if s == 0:
                guess = nums[int(len(nums)/4)-1]
            else:
                guess = nums[int((3*len(nums))/4)-1]

            user_input = input(f'Is your number {guess}? No --> (Lesser / Greater)')

            if user_input.lower() in positive_list and guess == number:
                guesses += 1
                print(f'GGs! [guesses: {guesses}]')
                guessing = False
            elif user_input.lower() == 'greater' and guess < number:
                nums = nums[nums.index(guess)+1:]; guesses += 1
            elif user_input.lower() == 'lesser' and guess > number:
                nums = nums[:nums.index(guess)]; guesses += 1
            else: continue
            break
while True:
    try: num = int(input('Pick a number between 1 & 100 (inclusive range) >>> '))
    except Exception as e: print(e); continue

    print(f'strategies: {strategy_dict}')
    user_input = input('Which strategy should I use to find your number? (1 / 2 / 3) >>> ')

    exec(strategy_dict[user_input] + '(num)')
