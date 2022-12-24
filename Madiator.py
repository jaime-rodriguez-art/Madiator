from time import sleep

from essential_generators import DocumentGenerator

import randomword

import pywhatkit

import keyboard

gen = DocumentGenerator()

#number = 0

#random_word = randomword.get_random_word(1000)

#search = input("Search anything:")

#search = random_word[number]

search = gen.sentence()

count = 0

cpt = 1


try:

    
    while (count < 3000):   
        count = count + 1
        pywhatkit.search(search)
        print (cpt)
        sleep(10)
        cpt+=1
        keyboard.press_and_release('ctrl+w')
        search = gen.sentence()

    
finally:
    print("unknown error")