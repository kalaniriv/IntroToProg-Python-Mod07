#### Kaeli Rivera
#### August 23, 2022
#### Foundations in Programming: Python
#### Assignment07
#### https://github.com/kalaniriv/IntroToProg-Python-Mod07
#### https://kalaniriv.github.io/IntroToProg-Python-Mod07/


# Module07 - Pickling Python Script
## Introduction
In this assignment, I modified a python script that allows a user to input a list of IDs and names into a list and then pickle the list and save it to a .dat file.

## Step 1: Writing (Modifying) the Python Script
The first step was to copy the partially complete starter python script into PyCharm, then fill in the missing pieces so it would properly execute the steps indicated. The script starts by declaring the variables that will used throughout the script.

I then defined five functions in the ‘processing’ portion of the code. The first function saves the data to the file by pickling the user’s entries in list form. The second function reads the data from the file by unpicking it and putting into a list. The third function takes the user’s input when asking if they want to add an entry to the list. The fourth function takes the user’s input by asking them for an ID and a corresponding name, then creating a list from those variables and returning the list for later use. The final function takes the ID and name inputs and appends them to the existing entries (if any) in the list.

In the presentation portion of the code, I used a ‘while’ loop to first call the function that asks the user if they want to add an entry to the list. An ‘if/elif//else’ statement then begins so if the user says ‘y’ then the program will ask them to enter an ID and name. If the user says ’n’ then the loop breaks. If the user doesn’t enter a valid option, the program will re-prompt them to enter ‘y’ or ’n.’ Once the ‘while’ loop concludes when a user no longer wants to enter another entry, the program lets the user know their entries were saved and prompts them to press enter to display the final results. The program then concludes running.

## Step 2: Using PyCharm to Run the Script
The next step was to run the script using PyCharm (Figure 2). The program first asked me if I wanted to submit an entry, to which I responded ‘y.’ I entered ‘1’ and ‘Kaeli’ and the program let me know the entry was added to the list. I then added three more entries before telling the program I didn’t want to make any additional entries. The program then let me know my submissions were saved and then displayed the final results to me.

![Figure 1](https://github.com/kalaniriv/IntroToProg-Python-Mod07/blob/main/docs/Figure1.png)
***Figure 1. Running the script using PyCharm.***

## Step 3: Using the Terminal to Run the Python Script
The final step was to run the script using the terminal app. I first used the change directory (“cd”) command to navigate to my file (Documents > _PythonClass > Assignment07). Once in the proper folder, I ran the command “python Assignment07v2.py” to begin executing the script. I followed the prompts to provide add four different entries to the list. Once I told the program I did not want to make any further submissions, it informed me that the data had been saved and allowed me to view the final list before exiting.

![Figure 2](https://github.com/kalaniriv/IntroToProg-Python-Mod07/blob/main/docs/Figure2.png)
***Figure 2. Using the terminal to execute the python script.***

I then checked the AppData.dat file to ensure the edits I made by running the script in the terminal app were captured correctly (Figure 3).

![Figure 3](https://github.com/kalaniriv/IntroToProg-Python-Mod07/blob/main/docs/Figure3.png)
***Figure 3. AppData.dat file correctly logging my submissions from PyCharm and the terminal app.***

## Summary
In this assignment, I was able to gain more in-depth and hands-on experience with creating functions, properly separating my code, and learning how to use pickling. I tend to learn better by being able to do things myself, so while this assignment took more trial and error than last week, I feel like I have a better understanding of the concepts covered.
