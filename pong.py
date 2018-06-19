from tkinter import *
import random
import time
root=Tk()
counter1=0
counter2=0
root.title("saicharan")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas=Canvas(root,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg="black")
canvas.pack()
root.update()

canvas.create_line(250,0,250,500,fill="white")

class Ball:
    def __init__(self,canvas,color,paddle1,paddle2):
        self.canvas=canvas
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,235,180)
        start=[-3,3]
        random.shuffle(start)
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.x=start[0]
        self.y=-3
    
    def hit_paddle1(self,pos):
         paddlepos=self.canvas.coords(self.paddle1.id)
         if pos[1]>=paddlepos[1]  and pos[1]<=paddlepos[3]:
             if pos[0]>=paddlepos[0] and pos[0]<=paddlepos[2]:
                 return True
             return False

    def  hit_paddle2(self,pos):
         paddlepos=self.canvas.coords(self.paddle2.id)
         if pos[1]>=paddlepos[1]  and pos[1]<=paddlepos[3]:
             if pos[2]>=paddlepos[0] and pos[2]<=paddlepos[2]:
                 return True
             return False   

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0:
            self.x=3
            self.score(True)
        if pos[2]>=self.canvas_width:
            self.x=-3
            self.score(False)
        if self.hit_paddle1(pos)==True:
            self.x=3
        if self.hit_paddle2(pos)==True:
            self.x=-3

    def score(self,val):
        global counter1
        global counter2
        if val==True:
            a=self.canvas.create_text(125,40,text=counter1,font=("Arial",60),fill="white")
            canvas.itemconfig(a,fill="black")
            counter1+=1
            a=self.canvas.create_text(125,40,text=counter1,font=("Arial",60),fill="white")

        if val==False:
            a=self.canvas.create_text(375,40,text=counter2,font=("Arial",60),fill="white")
            canvas.itemconfig(a,fill="black")
            counter2+=1
            a=self.canvas.create_text(375,40,text=counter2,font=("Arial",60),fill="white")    

        
        
class Paddle1:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(0,150,30,250,fill="blue")
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('q',self.turn_left)
        self.canvas.bind_all('a',self.turn_right)

    def draw(self):
         self.canvas.move(self.id,0,self.y)
         pos=self.canvas.coords(self.id)
         if pos[1]<=0:
             self.y=0
         if pos[3]>=self.canvas_height:
             self.y=0

    def turn_left(self,evt):
         self.y=-3
    def turn_right(self,evt):
         self.y=3
        

class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(470,180,500,280,fill="blue")
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_right)

    def draw(self):
         self.canvas.move(self.id,0,self.y)
         pos=self.canvas.coords(self.id)
         if pos[1]<=0:
             self.y=0
         if pos[3]>=self.canvas_height:
             self.y=0


    def turn_left(self,evt):
         self.y=-3
    def turn_right(self,evt):
         self.y=3     

paddle1=Paddle1(canvas,"blue")
paddle2=Paddle2(canvas,"blue")
ball=Ball(canvas,"red",paddle1,paddle2)

while 1:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
    if counter1==5:
        ball.x=0
        ball.y=0
        paddle1.y=0
        paddle2.y=0
        canvas.create_text(250,200,text="congrats player 1 you win",font=32,fill="red")
        canvas.create_text(250,215,text="Score:"+str(counter1)+" - "+str(counter2),font=32,fill="red" )

    if counter2==5:
        ball.x=0
        ball.y=0
        paddle1.y=0
        paddle2.y=0
        canvas.create_text(250,200,text="congrats player 2 you win",font=32,fill="red")
        canvas.create_text(250,215,text="Score:"+str(counter1)+" - "+str(counter2),font=32,fill="red" )

    if counter1==5 or counter2==5:
        canvas.create_text(250,215,text="Score:"+str(counter1)+" - "+str(counter2),font=32,fill="red" )
        time.sleep(100000)
         
root.mainloop()
