#replay, improve colours, finish prog
import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
guessActive = 'false'
programOver='false'
attempts = 10
n=0
guessedLetterList=[]

def letterInWord(wordToGuess, currentGuess, currentWord, attempts, wordToGuessLength):
    letterFound = False
    i = 0
    if len(currentGuess)==wordToGuessLength:
        wordGuess(wordToGuess, currentGuess, currentWord, attempts, wordToGuessLength)
    if currentGuess in currentWord:
        reGuess = True
    else:
        reGuess = False
    while letterFound == False and i < wordToGuessLength-1 and (currentGuess not in currentWord):
        for i in range (0, wordToGuessLength):
            if currentGuess.lower() == wordToGuess[i]:
                currentWord[i] = currentGuess.lower()
                letterFound = True
                
    if reGuess == True:
        attempts = attempts - 1
        resultLightbox["text"] = ('Letter already guessed! Try Again')
        return currentWord, attempts
    elif letterFound == True:
        resultLightbox["text"] = ('Correct!')
        return currentWord, attempts
    else:
        attempts = attempts - 1
        resultLightbox["text"] = ('Incorrect! Try Again')
        global n
        n=n+1
        global image
        image = ImageTk.PhotoImage((Image.open(image_file_path_dict[str(n)])).resize((200, 200)))
        hangmanGraphic.configure(image=image)
        hangmanGraphic.image=image
        hangmanGraphic.image = image
        if (' '+currentGuess) not in guessedLetterList:
                guessedLetterList.append(" "+currentGuess)
                guessedLetterListLabel["text"]=listToStringWithoutSpaces(guessedLetterList)
        return currentWord, attempts

def fullWordGuess(wordToGuess, currentGuess, currentWord, attempts, wordToGuessLength):
    wordFound = False
    if currentGuess==listToStringWithoutSpaces(wordToGuess):
        currentWord = split(currentGuess.lower())
        wordFound = True
    if wordFound == True:
        resultLightbox["text"] = ('Correct!')
        return currentWord, attempts
    else:
        attempts = attempts - 1
        global n
        n=n+1
        global image
        image = ImageTk.PhotoImage((Image.open(image_file_path_dict[str(n)])).resize((200, 200)))
        hangmanGraphic.configure(image=image)
        hangmanGraphic.image=image
        hangmanGraphic.image = image
        resultLightbox["text"] = ('Incorrect! Try Again')
        if (' '+currentGuess) not in guessedLetterList:
                guessedLetterList.append(" "+currentGuess)
                guessedLetterListLabel["text"]=listToStringWithoutSpaces(guessedLetterList)
        return currentWord, attempts

def split(word):
    return [char for char in word]

def listToStringWithoutSpaces(currentWord): 
    
    str1 = "" 
    return (str1.join(currentWord))

def listToStringWithSpaces(currentWord): 
    
    str1 = " " 
    return (str1.join(currentWord))

image_file_path_dict = {
    '1': 'Hangman1.jpg',
    '2': 'Hangman2.jpg',
    '3': 'Hangman3.jpg',
    '4': 'Hangman4.jpg',
    '5': 'Hangman5.jpg',
    '6': 'Hangman6.jpg',
    '7': 'Hangman7.jpg',
    '8': 'Hangman8.jpg',
    '9': 'Hangman9.jpg',
    '10': 'HangmanFull.jpg'}

wordToGuessInput = (input('Enter the word you would like to guess: ').lower())
wordToGuessLength = len(wordToGuessInput)
wordToGuess = split(wordToGuessInput)
currentWord = ['_']*wordToGuessLength 
currentGuess = ''

titleFrame = tk.Frame(master=window, relief=tk.RAISED,borderwidth=1)
title = tk.Label(master=titleFrame, text="Hangman", font=("Courier", 20))
title.pack()
titleFrame.pack(pady=10)

currentWordFrame = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2, height=50)
currentWordLabel = tk.Label(master=currentWordFrame, text= listToStringWithSpaces(currentWord), font=("Courier", 35))
currentWordLabel.pack()
currentWordFrame.pack(fill=tk.X, padx=20, pady=20)

entryFrame = tk.Frame(master=window,borderwidth=1)
guessEntry = tk.Entry(master=entryFrame)
guessEntry.insert(0, "Enter guess...")
guessEntry.pack(fill=tk.X)
entryFrame.pack(fill=tk.X, padx=20, pady=20)

graphicFrame = tk.Frame(master=window,borderwidth=1, relief=tk.SUNKEN, width=20, height=20)
image = ImageTk.PhotoImage((Image.open('Hangman0.jpg').resize((200, 200), Image.ANTIALIAS)))
hangmanGraphic = tk.Label(master=graphicFrame, image = image, width=200, height=200)
hangmanGraphic.pack()
graphicFrame.pack(fill=tk.BOTH, padx=20, pady=20, expand = 'True')

scoreBoxFrame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2, width=200, height=200)
scoreBoxLabel = tk.Label(master=scoreBoxFrame, text="attempts" +"\n" + "remaining", font=("Courier", 18))
scoreBoxLabel.pack(side="bottom")
score = tk.Label(master=scoreBoxFrame, text=str(attempts),  font=("Courier", 22))
score.pack(side="top")
scoreBoxFrame.pack(side='bottom', anchor='se', padx=20, pady=20)

guessedLettersFrame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=1, width=100, height=100)
guessedLetterInfo = tk.Label(text='Incorrect Guesses:', padx=5, pady=5, master=guessedLettersFrame,  font=("Courier", 20))
guessedLetterInfo.grid(row=0, column=0)
guessedLetterListLabel = tk.Label(text=listToStringWithoutSpaces(guessedLetterList), padx=5, pady=5, master=guessedLettersFrame)
guessedLetterListLabel.grid(row=0, column=1)
guessedLettersFrame.pack(fill=tk.BOTH, padx=20, pady=20, expand = 'True')

resultLightboxFrame = tk.Frame(master = window, borderwidth=5)
resultLightbox = tk.Label(master=resultLightboxFrame, text="", font=("Courier", 25), width = 200, height = 200)
resultLightbox.pack()
resultLightboxFrame.pack(padx=20, pady=20)

def make_guess(event):
    guessEntry.delete(0, tk.END)

def enter_guess(events):
    global guessActive
    global attempts
    global currentWord
    global wordToGuess
    global programOver
    guessActive = 'true'
    currentGuess = (guessEntry.get()).lower()
    guessEntry.delete(0, tk.END)
    currentWord, attempts = runProgram(wordToGuess, listToStringWithoutSpaces(currentGuess), currentWord, attempts, wordToGuessLength)
    if attempts == 0 or currentWord == wordToGuess:
        programOver='true'
    if programOver == 'true' and currentWord != wordToGuess:
        resultLightbox["text"] = ('You have lost, better luck next time!' '\n'  'The correct word is above' )
        currentWordLabel.configure(fg='#ff0000')
        currentWordLabel["text"] = (listToStringWithSpaces(wordToGuess))
    elif programOver == 'true':
        currentWordLabel.configure(fg='#33cc33')
        resultLightbox["text"] = ('Congratulations, you have won!')

guessEntry.bind("<Button>", make_guess)
window.bind("<Return>", enter_guess)


def runProgram(wordToGuess, currentGuess, currentWord, attempts, wordToGuessLength):
    global guessActive
    while attempts > 0 and currentWord != wordToGuess and guessActive == 'true':
        guessActive = 'false'
        if len(currentGuess)==wordToGuessLength:
            currentWord, attempts = fullWordGuess(wordToGuess, currentGuess, currentWord, attempts, wordToGuessLength)
            currentWordLabel["text"] = (currentWord)
            score["text"] = str(attempts)
            return currentWord, attempts
        elif len(currentGuess)==1:
            currentWord, attempts = letterInWord(wordToGuess, currentGuess, currentWord, attempts, wordToGuessLength)
            currentWordLabel["text"] = (currentWord)
            score["text"] = str(attempts)
            return currentWord, attempts
        else:
            attempts = attempts - 1
            resultLightbox["text"] = ('Invalid guess length! Try Again')
            if (' '+currentGuess) not in guessedLetterList:
                guessedLetterList.append(" "+currentGuess)
                guessedLetterListLabel["text"]=listToStringWithoutSpaces(guessedLetterList)
            currentWordLabel["text"] = (currentWord)
            score["text"] = str(attempts)
            global n
            n=n+1
            global image
            image = ImageTk.PhotoImage((Image.open(image_file_path_dict[str(n)])).resize((200, 200)))
            hangmanGraphic.configure(image=image)
            hangmanGraphic.image=image
            return attempts

window.mainloop()
