# Python Terminal Wordle
![Banner](https://img.youtube.com/vi/-Mzsvg7IrME/0.jpg)

Today you'll be fixing this broken Wordle game by completing the tasks below to make it run properly.

**Running the code**

  

You'll need to create a virtual environment to run this code in. Run these commands in order:

  

    python -m venv .venv
    
    .venv/bin/activate
    
    pip install rich

  

You can then run the program with

  

    python3 main.py


**Task 1**
Check if the letter is in the correct place and update guessed with correct_place(letter)

**Task 2**
Check if the letter is in the answer but not in the correct place and update guessed with correct_letter(letter)

**Task 3**
If the letter is not in the answer, update guessed with incorrect_letter(letter)

 **Task 4**
Add a check to make sure the guess is a 5 letter word or is in already_guessed

**Task 5**
Add a check to see if the guess is correct or if the player has used all their ALLOWED_GUESSES

**Task 6**
Check if the player has used all their guesses AND the guess is incorrect

***Challenges***

 - Change the number of guesses a player can make **(Easy)**
 - Edit the rich formatting to display different coloured backgrounds for a correct letter and place **(Intermediate)**
 - Make the game work with 6 letter words **(Hard)**
 *Hint - you'll need to find a corpus of 6 letter words and replace the word_list in words.py*
