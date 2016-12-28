#! /usr/bin/python3

import random

card_list = [#2
             'Moat 2', 'Chapel 2', 'Cellar 2',
             #3
             'Chancellor 3', 'Village 3', 'Woodcutter 3', 'Workshop 3',
             #4
             'Bureaucrat 4', 'Feast 4', 'Militia 4',
             'Moneylender 4', 'Remodel 4', 'Smithy 4',
             'Spy 4', 'Thief 4', 'Throne Room 4',
             #5
             'Gardens 5', 'Festival 5', 'Laboratory 5',
             'Library 5', 'Market 5', 'Mine 5', 'Witch 5', 
             #6
             'Adventurer 6']

def selectCards(deck):
    counter = 0
    while counter <= 9:
        randCard = random.randint(0, deck.index(deck[-1]))
        print(str(deck[randCard]).center(100))
        del deck[randCard]
        counter += 1

def selectCards_Weight(deck):
    counter = 0
    while counter <= 9:
        randCard = random.randint(0, deck.index(deck[-1]))
        randCardWeight = deck.index(deck[randCard - random.randint(0, randCard)])
        print(str(deck[randCardWeight]).center(100))
        del deck[randCardWeight]
        counter += 1

print()
welcome = 'Welcome to the Dominion Card Randomizer!'
print(welcome.center(100))
typeA = 'Input \'a\' to pick ten completely random cards.'
print(typeA.center(100))
typeB = 'Input \'b\' to make the randomizer select more low-cost cards.'
print(typeB.center(100))
typeC = 'Input \'c\' to make the randomizer select more high-cost cards.'
print(typeC.center(100))
print('Input anything else to exit.'.center(100))


choice = input()
if choice == 'a':
    selectCards(card_list)
if choice == 'b':
    selectCards_Weight(card_list)
if choice == 'c':
    card_list.reverse()
    selectCards_Weight(card_list)

exit()
