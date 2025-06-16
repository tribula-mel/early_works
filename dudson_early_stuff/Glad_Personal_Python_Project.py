

command1 = ""
command2 = ""
fight = ""
pity_points = 0


print("My name is <Glad>, no that's not my real name but I can't remember my given one... it's not necessary... all I remember is how to swing a sword and how to behave in front of guards, I can't remember why but it seems like I've been fighting in the ring forever, survival is second nature")


print()
print("[Location: Gladitorial ring] ---- I am located in what appears to be the pre-fight chamber, I am expected to arm myself for battle. The room smells of despair and there are dents as well as blood stains on the walls... This room clearly has a lot of history. There doesn't seem to be anyone here but I should armor up before someone catches me unprepared")
print()
print("[commands]: Armor up")
print()

#1 command to armor up and continue the story
while True:
    try:
        command1 = input("What will you do?: ")
    except ValueError:
        continue

    if command1.lower() == "armor up":
        break
    else:
        print("read the option for the commands")
        continue

print("A guard walks into the pre-fight chamber")
print("<Alver>: Time to go pay for your crimes monster")
print()
print("[commands]: take him by surprise")

print("             slander his family")
print("             gain pity points")
print("             talk sarcastically")
print()

#What will you say/do to Alver the guard that is going to force you into the arena
while True:
    try:
        command1 = input("What will you do?: ")
    except ValueError:
        continue
        
    if command1.lower() == "slander his family":
        print("<Glad>: Shut up and pay for your crimes loser, the size of your tummy is a crime and your families lack of intelligence is enlightening")
        print()
        print("I get carried away with my insults so much that I spit in his face")
        print()
        print("Alver doesn't take kindly to this and punishes me with a quick barrage of punches")
        print("After roughing you up, Alver opens the gates and hurls you out into the stadium")
        break


    elif command1.lower() == "gain pity points":
        print("Your eyes get teary and amid your unmanly crying you blabber a few words <Glad>: my life is ruined, RUINED, all I did was kneel with the wrong leg in front of sir Richelle de la Casta... PLEASE Alver, help me")
        print()
        print("A tear comes to alvers eye <Alver>: I am sorry my friend despite your hardship if I let you go it will be me in that ring")
        print("Alver opens the colosseum gate and gently motions you forward <Alver>: Goodluck")
        pity_points = pity_points + 1
        break

    elif command1.lower() == "talk sarcastically":
        print("Why thank you kind sir, when I get out I'll be sure to buy you a drink")
        print()
        print("Alver chuckles idiotically... As you are being led into the arena you give Alver a swift kick to the groin, he is unable to retaliate since the gates are already closing and getting revenge on you would likely get him stuck in the ring as well")
        print()
        print("At least you get to feel triumphant in this battle knowing Alver is rolling over in pain")
        break   

    elif command1.lower()== "take him by surprise":
        print("You position yourself next to Alver.... As he turns around you slug him in the face and get in a few body blows before he pulls out a metal projectile launching weapon and ends your mutiny")
        print()
        print("Alver violently throws you out the gates into the arena")
        break
    else:
        continue


print("You see a monster of a man on a desert like plain surrounded by tens of thousands of cheering fans, this man is roughly 7 ft tall according to your estimates and he caries a massive bludgeon. Your feet tremble in awe as you meet the strongest fighter in the country")
print("After a brief pause he charges at you and swings his massive weapon at you!")
print()
print("[commands]: dive left")
print("            swing sword")
print("            block")


#Fight action 1 against massive gladiator
while True:
    try:
        fight = input("What will you do?: ")
    except ValueError:
        continue

    if fight.lower() == "block":
        print("you realize a blow from this guy can't be blocked")
        continue

    elif fight.lower() == "swing sword":
        print("You realize trying to counter an attack from this monster will be futile")
        continue
    
    elif fight.lower() == "dive left":
        print("You narrowly avoid the swing... The impact of the bludgeon on the ground sends waves of chills down your spine")
        break

    else:
        continue


print("The big man attacks again ready to finish you off with this next swing")
print()
print("[commands]: dive forward")
print("            swing sword")
print("            block")


#Fight action 2 against massive gladiator
while True:
    try:
        fight = input("What will you do?: ")
    except ValueError:
        continue

    if fight.lower() == "block":
        print("you realize a blow from this guy can't be blocked")
        continue

    elif fight.lower() == "swing sword" and pity_points ==0:
        print("You realize trying to counter an attack from this monster will be futile")
        continue
    
    elif fight.lower() == "dive forward":
        print("You narrowly avoid the attack... The impact of the bludgeon leaves a small crater on the ground, you hear tyranically laughter from the audience")
        break

    elif fight.lower() == "swing_sword" and pity_points ==1:
        print("The pep talk from Alver motivates you to counter the giant's blow and you slash his leg with shear luck giving the giant a big cut")
        break
    else:
        continue

print("You pitch a rock at full strength at the giant but he is unfazed after what seems like a critical blow to the head")
print("The man steps in angrily to finish you off, you realize that his step in is sloppy and he is off balance")
print()
print("[commands]: trip")
print("            swing sword")
print("            block")
print("            dive backward")


#Fight action 3 against massive gladiator
while True:
    try:
        fight = input("What will you do?: ")
    except ValueError:
        continue

    if fight.lower() == "block":
        print("you realize a blow from this guy can't be blocked")
        continue

    elif fight.lower() == "swing sword":
        print("You realize trying to counter an attack from this monster will be futile")
        continue
    
    elif fight.lower() == "dive backward":
        print("You are about to dodge backward but you hesitate, if you back up, you will be trapped between the gladiator and the wall")
        continue

    elif fight.lower() == "trip":
        print("You send the man flying forward by sticking your foot out and tripping him, his face slams into the ground")
        print("The crowd eagerly waits for the massive gladiator to stand up and finish you off.... But he doesn't stand up")
        print("Apparently being 7 ft tall means you are more susceptible to injuries from falling")
        break

    else:
        continue

print("the audience is dissapointed and boos you")
print("According to the emporers promise you are hearby cleared of all baseless charges and are free")
    
print()
print()

while True:
    try:
        print("<Emporer>: Do you want your freedom simpleton? ")
        print()
        print("[commands]: Yes/No ")
        command2 = input("What will you say?: ")

    except ValueError:
        continue

    if command2.lower() == "yes":
        print("<Emporer>: BE FREEEEE")
        print("You smile with genuine happiness as you fry out FREEDOM, you can go home and play chucky egg")
        print("CHUCKY EGGGG")
        break
        
    elif fight.lower() == "no":
        print("<Emporer>: Are you dumb, you just survived with 1 in a million odds and your saying you don't want to be free?? GO JOIN ALVER")
        print("You immediately regret trying to be honorable and wish you had just taken the reward")
        break

    else:
        continue
















































