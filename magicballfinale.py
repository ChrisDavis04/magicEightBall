# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:29:22 2024

@author: chris
"""

import random

fortunes = ["The fiery pits of the inferno are more likely to freeze over.", "Only possible if the stars exactly align.", "I wouldn't bet my life on this...", "ehhhhhh....maybe.", "It could happen but it also couldn't. Honestly this is the perfect instance of a 50/50 that I, the magical crystal ball, have ever divined.", "It could be a possibility so have hope.", "You're in luck for the very stars in the celestial sky are shining upon thee! With this luck try out gambling as I'm sure it'll absolutely go well.", "This cannot but happen for it is etched into the weave of destiny that ordains the story of everything in the universe and I see that no matter what this will occur."]

print("Weary from your travels and ventures across the lands and a plethora of dungeons, you finally seek some rest and respite on a nearby abandoned fire pit. At the ragged location lies a mysterious chest that looks strangely untouched a stark contrast to greatly ravaged respite. Within the chest lies something...peculiar. There on a lavish lavender cushion lays a translucent crystal ball who's luster shines with the very light of the celestial sky.")
print("A sense of curiousity and intrigue floods your mind as the luster utterly enchants and draws you in. Then against your own intent, you bring your hand to the crystal ball and pick it up. Almost as if a greater being whispers into your ear, the ball tells you of a few possibilities of what it can do.")
print("1. Reveal all possible fortunes.")
print("2.Ask for a specific fortune.")
print("3.Ask for a random fortune.")
print("Please pick either 1, 2, or, 3")
print("Or you can pick '4' which entails you eating the crystal ball...for whatever reason.")

answer = input()

if answer == "1":
    for i, fortunes in enumerate(fortunes):
        print(f"{i}: {fortunes}")
elif answer == "2":
    number = input("Please pick a number between 0-7: ")
    if number.isdigit():
        intnumber = int(number)
        if intnumber in range(len(fortunes)):
            print(f"{fortunes[intnumber]}")
        else:
            print("Cracks begin to permeate throughout the crystal ball for the answer you gave it fractured the very weave of its abilities. Its translucent shell shattering releases an absolutely pitiful sound then booms with a roaring thunder as the magic contained within is fully unleashed resulting in a nuclear exposion of mana erasing anyone and anything within a 50 mile radius. You kinda dead lol.")
    else:
        print("The fog that swirls within the crystal ball condenses together and creates a frowny face meaning thaty you said something wrong. How rude of you!")
elif answer == "3":
    print("Please ask a question or query you would like to have answered:")
    question = input()
    numFortunes = len(fortunes)
    fortunesNum = random.randrange(numFortunes)
    print(f"{fortunes[fortunesNum]}")
elif answer == "4":
    print("You swallow the crystal ball and surprisingly it has a light salty flavor that almost reminds you of the ocean. It was as if the crystal ball itself originated from a mystical clam who resided in the very depths of the world that having livied for millenia attained the ability to divine the future. Wow what a cool thing to happen! However in an instance after you consumed the crystal ball a sheer influx of information floods your mind as visions of all possible futures and strings of fate strangle your brain until you are forever paralyzed by endless options of the universe.")
else:
    print("The crystal ball is bewildered by your intent and forms an expresson comprised of fog and it looks to be absolutely confused to no end. It seems that you can try again and actually play along...or don't. This is your story, a story with limited options but your story nonetheless.")


