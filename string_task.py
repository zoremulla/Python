
answer1=int(input("Please write a number from 1 to 12 : "))
answer2=input("Please mention a random item in your mind : ")
answer3=input("Please write your favourite actor : ")
answer4=input("Please write a sentence: ")
answer5=input("Please write a verb : ")
story="\nIt was %do'clock when I hears a knock at the door.\nI opened the door and there was a box full of %s with a note saying 'Mr. %s'.\nJust as I closed the door I heard a scream '%s'.\nI %s in place and all I could do was run. " % (answer1, answer2, answer3, answer4.upper(), answer5)
print(story)