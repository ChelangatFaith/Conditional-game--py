import random
#Rock , Paper, Scissor game
#The outcomes could either be rock, paper, scissor
outcomes =['rock','paper','scissor']
random_num = random.randint(0,2)
computer_out =outcomes[random_num]
  
print(computer_out)
#Getting input from the user
user_input = input('Please enter your geuss')
print (user_input)

#Conditions
#rock wins against scissors 
#Scissors win against paper
#Paper wins against rock

if computer_out == 'rock': #Testing the condition that the output from the 
    #computer is a rock
    if user_input== 'paper': #My input is paper and the conditions states that 
        #paper wins against rock so i win
        print("i win")
    elif user_input =="scissor":# my iput is scissor and the rock wins aginst 
        #scissor thats why computer wins
        print("computer win")
    else:#if both of our conditions are the same
        #computer geuss is rock and my geuss is a rock we draw
        print("Drawn")

elif computer_out == "scissor":#Testing the condition that the output from the 
    #computer is a scissor
    if user_input == 'paper':# my input is paper and the scissor wins aginst 
        #paper thats why computer wins
        print("computer win")
    elif user_input =="rock":
        #My input is rock and the conditions states that 
        #rock wins against paper so i win
        print("i win")
    else:#if both of our conditions are the same
        #computer geuss is scissor and my geuss is a scissor we draw
        print("Drawn")

else:#Testing the remaining condition apart from rock and scissor
    #that is if the computer input is paper
    if user_input == 'rock':#my input is rock and paper wins aginst 
        #rock thats why computer wins
        print ("computer win")  
    elif user_input == 'scissor': #My input is scissor and the conditions states that 
        #scissor wins against paper so i win
        print ("i win")
    else:#if both of our conditions are the same
        #computer geuss is paper and my geuss is a paper so we draw
        print("drawn")                        