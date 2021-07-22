#Required Imports
import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT
from tkinter import messagebox
import random as rd
from playsound import playsound
from pygame import mixer

#Global variables
moves = ["rock","paper","scissor","lizard","spock"]
comScore = 0
youScore = 0
result="Yo...Let's Go!!"
scorebg="seagreen"

def welcomescreen():
    global welcome
    welcome = tk.Frame(root,bg="azure")
    titletext = tk.Label(welcome,text="Dr. Sheldon Cooper's...",font="Verdana 10 italic",fg="hotpink4",bg="azure")
    titletext.pack(pady=10)
    gamename = tk.Label(welcome,text="Rock Paper Scissors\nLizard Spock",font="Impact 28 bold",fg="deepskyblue2",bg="azure")
    gamename.pack(pady=20)
    buttons = tk.Frame(welcome,bg="azure")
    startbtn = tk.Button(buttons,text="Start Game",font="Courier 14 bold",fg="white",bg="seagreen",activebackground="white",activeforeground="seagreen",command=startgame)
    startbtn.pack(pady=5,padx=5,side=LEFT)
    closebtn = tk.Button(buttons,text="Close Game",font="Courier 14 bold",fg="white",bg="tomato2",activebackground="white",activeforeground="tomato2",command=closeapp)
    closebtn.pack(pady=5,padx=5,side=RIGHT)
    buttons.pack()
    rules = tk.Label(welcome,text="Remember...\nScissors cuts Paper\n Paper covers Rock\n Rock crushes Lizard\n Lizard poisons Spock\n Spock smashes Scissors\n Scissors decapitates Lizard\n Lizard eats Paper\n Paper disproves Spock\n Spock vaporizes Rock\n (and as it always has) Rock crushes Scissors\n So simple right!",font="Modern",fg="orangered2",bg="azure")
    rules.pack(pady=10)
    welcome.pack()
    
def gamescreen():
    global gameframe, btnframe, scoreframe
    scoreframe = tk.Frame(root,bg="azure")
    score = tk.Label(scoreframe,text="You V/S Computer",font="Serif 10 bold",fg="hotpink4",bg="azure").pack()
    label2 = tk.Label(scoreframe,text="You: "+str(youScore)+" ~ "+str(comScore)+" :Com",font="Impact 28 bold",bg=scorebg,fg="white",borderwidth=2, relief="groove",padx=15,pady=5).pack()
    label4 = tk.Label(scoreframe,text="Computer's move:",font="Serif 10 bold",fg="hotpink4",bg="azure").pack()
    comImage = tk.Label(scoreframe,image=comMove,bg="azure").pack()
    label3 = tk.Label(scoreframe,text=result,font="Courier 16 bold",fg=scorebg,bg="azure").pack()
    scoreframe.pack()
    gameframe = tk.Frame(root,bg="azure")
    label1 = tk.Label(gameframe,text="Make your move...",font="Impact 16",bg="azure",fg="hotpink4")
    label1.pack()
    stonebtn = tk.Button(gameframe,image=stoneimg,command=rocklogic).pack(side=LEFT)
    spockbtn = tk.Button(gameframe,image=spockimg,command=spocklogic).pack(side=RIGHT)
    lizardbtn = tk.Button(gameframe,image=lizardimg,command=lizardlogic).pack(side=RIGHT)
    scissorbtn = tk.Button(gameframe,image=scissorimg,command=scissorlogic).pack(side=RIGHT)
    paperbtn = tk.Button(gameframe,image=paperimg,command=paperlogic).pack(side=RIGHT)
    gameframe.pack(pady=20)
    btnframe = tk.Frame(root,bg="azure")
    rulesbtn = tk.Button(btnframe,text="Rules",fg="white",bg="tomato2",font="Courier 12 bold",command=showrules,padx=10).pack(side=LEFT,padx=5) 
    resetbtn = tk.Button(btnframe,text="Reset Game",fg="white",bg="tomato2",font="Courier 12 bold",command=reset,padx=10).pack(side=LEFT,padx=5)
    backtomenubtn = tk.Button(btnframe,text="Back to home",fg="white",bg="tomato2",font="Courier 12 bold",command=back,padx=10).pack(side=RIGHT,padx=5)
    btnframe.pack()


def paperlogic():
    global youScore,comScore,result,scorebg,comMove
    global gameframe, btnframe, scoreframe
    gameframe.destroy()
    btnframe.destroy()
    scoreframe.destroy()
    com = moves[rd.randint(0,4)]
    if(com=="rock"):
        comMove=stoneimg
        youScore+=1
        result = "Paper covers Rock... You win!!"
        playsound("win.wav")
    elif(com=="spock"):
        comMove=spockimg
        youScore+=1
        result = "Paper disproves Spock... You win!!"
        playsound("win.wav")
    elif(com=="paper"):
        comMove=paperimg
        result = "Paper equals Paper... Tie!"
        playsound("tie.wav")
    elif(com=="lizard"):
        comMove=lizardimg
        result = "Lizard eats Paper... Comp win!"
        comScore+=1
        playsound("loose.wav")
    else:
        comMove=scissorimg
        result = "Scissor cuts Paper... Comp win!"
        comScore+=1
        playsound("loose.wav")
    if(comScore>youScore):
        scorebg="tomato2"
    elif(comScore==youScore):
        scorebg="gold"
    else:
        scorebg="seagreen"    
    gamescreen()

def scissorlogic():
    global youScore,comScore,result,scorebg,comMove
    global gameframe, btnframe, scoreframe
    gameframe.destroy()
    btnframe.destroy()
    scoreframe.destroy()
    com = moves[rd.randint(0,4)]
    if(com=="paper"):
        comMove=paperimg
        youScore+=1
        result = "Scissor cuts Paper... You win!!"
        playsound("win.wav")
    elif(com=="lizard"):
        comMove=lizardimg
        youScore+=1
        result = "Scissor decapitates Lizard... You win!!"
        playsound("win.wav")
    elif(com=="scissor"):
        comMove=scissorimg
        result = "Scissor equals Scissor... Tie!"
        playsound("tie.wav")
    elif(com=="rock"):
        comMove=stoneimg
        result = "Rock breaks Scissor... Comp win!"
        comScore+=1
        playsound("loose.wav")
    else:
        comMove=spockimg
        result = "Spock smashes Scissor... Comp win!"
        comScore+=1
        playsound("loose.wav")
    if(comScore>youScore):
        scorebg="tomato2"
    elif(comScore==youScore):
        scorebg="gold"
    else:
        scorebg="seagreen"    
    gamescreen()

def rocklogic():
    global youScore,comScore,result,scorebg,comMove
    global gameframe, btnframe, scoreframe
    gameframe.destroy()
    btnframe.destroy()
    scoreframe.destroy()
    com = moves[rd.randint(0,4)]
    if(com=="lizard"):
        comMove=lizardimg
        youScore+=1
        result = "Rock smashes Lizard... You win!!"
        playsound("win.wav")
    elif(com=="scissor"):
        comMove=scissorimg
        youScore+=1
        result = "Rock crushes Scissor... You win!!"
        playsound("win.wav")
    elif(com=="rock"):
        comMove=stoneimg
        result = "Rock equals Rock... Tie!"
        playsound("tie.wav")
    elif(com=="paper"):
        comMove=paperimg
        result = "Paper covers Rock... Comp win!"
        comScore+=1
        playsound("loose.wav")
    else:
        comMove=spockimg
        result = "Spock vapourises Rock... Comp win!"
        comScore+=1
        playsound("loose.wav")
    if(comScore>youScore):
        scorebg="tomato2"
    elif(comScore==youScore):
        scorebg="gold"
    else:
        scorebg="seagreen"    
    gamescreen()

def spocklogic():
    global youScore,comScore,result,scorebg,comMove
    global gameframe, btnframe, scoreframe
    gameframe.destroy()
    btnframe.destroy()
    scoreframe.destroy()
    com = moves[rd.randint(0,4)]
    if(com=="rock"):
        comMove=stoneimg
        youScore+=1
        result = "Spock vapourises Rock... You win!!"
        playsound("win.wav")
    elif(com=="scissors"):
        comMove=scissorimg
        youScore+=1
        result = "Spock smashes Scissors... You win!!"
        playsound("win.wav")
    elif(com=="spock"):
        comMove=spockimg
        result = "Spcok equals Spock... Tie!"
        playsound("tie.wav")
    elif(com=="lizard"):
        comMove=lizardimg
        result = "Lizard poisons spock... Comp win!"
        comScore+=1
        playsound("loose.wav")
    else:
        comMove=paperimg
        result = "Paper disproves Spock... Comp win!"
        comScore+=1
        playsound("loose.wav")
    if(comScore>youScore):
        scorebg="tomato2"
    elif(comScore==youScore):
        scorebg="gold"
    else:
        scorebg="seagreen"    
    gamescreen()

def lizardlogic():
    global youScore,comScore,result,scorebg,comMove
    global gameframe, btnframe, scoreframe
    gameframe.destroy()
    btnframe.destroy()
    scoreframe.destroy()
    com = moves[rd.randint(0,4)]
    if(com=="spock"):
        comMove=spockimg
        youScore+=1
        result = "Lizard poisons Spock... You win!!"
        playsound("win.wav")
    elif(com=="paper"):
        comMove=paperimg
        youScore+=1
        result = "Lizard eats Paper... You win!!"
        playsound("win.wav")
    elif(com=="lizard"):
        comMove=lizardimg
        result = "Lizard equals Lizard... Tie!"
        playsound("tie.wav")
    elif(com=="rock"):
        comMove=stoneimg
        result = "Rock crushes Lizard... Comp win!"
        comScore+=1
        playsound("loose.wav")
    else:
        comMove=scissorimg
        result = "Scissor decapitates Lizard... Comp win!"
        comScore+=1
        playsound("loose.wav")
    if(comScore>youScore):
        scorebg="tomato2"
    elif(comScore==youScore):
        scorebg="gold"
    else:
        scorebg="seagreen"    
    gamescreen()

def reset():
    global youScore,comScore,result,scorebg,comMove
    global gameframe, btnframe, scoreframe
    gameframe.destroy()
    btnframe.destroy()
    scoreframe.destroy()
    youScore=0
    comScore=0
    result="Yo...Let's Go!!"
    scorebg="seagreen"
    comMove = tk.PhotoImage(file = "yo.png")
    gamescreen()
    playsound("btn.wav")

def closeapp():
    playsound("exit.wav")
    root.destroy()

def startgame():
    welcome.destroy()
    gamescreen()
    playsound("btn.wav")

def back():
    global welcome,gameframe,btnframe
    reset()
    gameframe.destroy()
    btnframe.destroy()
    scoreframe.destroy()
    welcomescreen()

def showrules():
    playsound("btn.wav")
    messagebox.showinfo("Rule Book", "Scissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors")

root = tk.Tk()
root.geometry("700x500")
root.title("RockPaperScissorsLizardSpock")
root.wm_iconbitmap("favicon.ico")
root.configure(bg="azure")

mixer.init()
mixer.music.load("bg-music.mp3")
mixer.music.play(-1)

stoneimg = tk.PhotoImage(file = "rock.png")
paperimg = tk.PhotoImage(file = "paper.png")
scissorimg = tk.PhotoImage(file = "scissors.png")
lizardimg = tk.PhotoImage(file = "lizard.png")
spockimg = tk.PhotoImage(file = "spock.png")
comMove=tk.PhotoImage(file = "yo.png")

welcomescreen()

root.mainloop()