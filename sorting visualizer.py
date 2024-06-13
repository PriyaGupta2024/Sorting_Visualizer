from tkinter import *
from tkinter import ttk
import random
from Bubblesort import bubble_sort 
from Quicksort import Quick_sort
from Mergesorts import merge_sort

root = Tk()
root.title('sorting algorithm visualizer')
root.geometry("900x600+200+80")                                                                                 
root.config(bg='cyan')





def drawData(data,colorArray):                             #where the sorting algo perform that part it is
     
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data)+1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i / max(data) for i in data]

 
    for i , height in enumerate(normalised_data):
        x0 = i*x_width + offset + spacing_bet_rect
        y0 = canvas_height - height*400                  #we have multiple 400 because we willnormalised our values with one
                                                         #one farmula so that our data won't exceed our canva
        x1 = (i+1) * x_width
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,  fill = colorArray[i])
        canvas.create_text(x0+2 , y0 ,anchor = SW , text = str(data[i]),font = ("new roman" , 15, "italic bold"),
                    fill = "red"  )
    root.update_idletasks()    

def StartAlgorithm():
  global data
  if not data :
     return
  if(algo_menu.get() == 'Quick Sort'):
     Quick_sort(data , 0 , len(data)-1 , drawData , speedscale.get())
     drawData(data, ['pink' for x in range(len(data))])

  elif algo_menu.get() == "Bubble Sort":   
     bubble_sort(data,drawData,speedscale.get())

  elif algo_menu.get() == "Merge Sort":
     merge_sort(data , drawData , speedscale.get())
  drawData(data , ['green' for x in range(len(data))])      

def Generate():
    global data 
    print('selected Algorithm: '+ selected_algorithm.get() )
    #data = [1,5,6,2,4,8,5,8,7,9,3,3,7,8]                    #through this line we got bar as per the given values
    #we will take values from our speed scale now
    #now here we don't need try and except block as we are using values to insert as a scale  

    #try :
      #minivalue = int(minvalue.get())
    #except :  # if value is wrong we will keep by default as 1
      #minivalue = 1

    #try :
      #maxivalue = int(maxvalue.get())
    #except :  # if value is wrong we will keep by default as 100
      #maxivalue = 100

    #try :
      #sizeevalue = int(sizevalue.get())
    #except :  # if value is wrong we will keep by default as 10
      #sizeevalue = 10


    #if minivalue < 0:
      #minivalue = 0
    #if maxivalue > 100:
      #maxivalue = 100
    #if sizeevalue > 40 or sizeevalue < 3:
      #sizeevalue = 29

    # if in case max  value is smaller than min value we will swap data
    #if minivalue > maxivalue:
      #minivalue , maxivalue = maxivalue , minivalue
    #data = []
    #for _ in range(sizeevalue):
        #we will add that speed scaled by appending it 
     #data.append(random.randrange(minivalue,maxivalue+1))
    #drawData(data)
          
    minivalue = int(minvalue.get())
    maxivalue = int(maxvalue.get())
    sizeevalue = int(sizevalue.get())


    data = []
    for _ in range(sizeevalue):
        #we will add that speed scaled by appending it 
     data.append(random.randrange(minivalue,maxivalue+1))
    drawData(data, ['yellow' for x in range(len(data))])

selected_algorithm = StringVar()
# lable1, button, speed scale

mainlabel1 = Label(root, text = "Algorithm : " , font = ("new roman",16, "italic bold"),bg = "white",
                  width = 10, fg = "black",relief = GROOVE,bd = 5)
mainlabel1.place(x=0,y=0) 



algo_menu = ttk.Combobox(root, width = 15 , font = ("new roman",20,"italic bold"), textvariable = selected_algorithm,
                         values = ['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algo_menu.place(x=145,y=0)
algo_menu.current(0)           # by deafualt bubble sort

random_generate = Button(root, text ="Genrerate",bg = "#2DAE9A" , font = ("arial",12,"italic bold"),relief = SUNKEN,
                        activebackground = "#05945B", activeforeground = "white",bd = 5,width = 10,command = Generate)
random_generate.place(x=750,y=60)

#size of array/height of array
sizevaluelabel = Label(root,text = " Size : " , font = ("new roman",12, "italic bold"),bg = "#0E6DA5",
                  width = 10, fg = "black",height =2,relief = GROOVE,bd = 5)
sizevaluelabel.place(x=0,y=60)

sizevalue = Scale(root,from_ = 0 , to = 30,resolution = 1, orient = HORIZONTAL,font = ("arial",14,"italic bold"),
                  relief = GROOVE,bd = 2,width = 10)
sizevalue.place(x=120,y=60)


#minimum valu of array
minvaluelabel = Label(root,text = " Min Value : " , font = ("new roman",12, "italic bold"),bg = "#0E6DA5",
                  width = 10, fg = "black",height =2,relief = GROOVE,bd = 5)
minvaluelabel.place(x=250,y=60)

minvalue = Scale(root,from_ = 0 , to = 10,resolution = 1, orient = HORIZONTAL,font = ("arial",14,"italic bold"),
                  relief = GROOVE,bd = 2,width = 10)
minvalue.place(x=370,y=60)



#maximum value of array
maxvaluelabel = Label(root,text = " Max Value: " , font = ("new roman",12, "italic bold"),bg = "#0E6DA5",
                  width = 10, fg = "black",height =2,relief = GROOVE,bd = 5)
maxvaluelabel.place(x=500,y=60)

maxvalue = Scale(root,from_ = 0 , to = 100,resolution = 1, orient = HORIZONTAL,font = ("arial",14,"italic bold"),
                  relief = GROOVE,bd = 2,width = 10)
maxvalue.place(x=620,y=60)


Start = Button(root, text ="Start",bg = "#c45B09" , font = ("arial",12,"italic bold"),relief = SUNKEN,
                        activebackground = "#05945B", activeforeground = "white",bd = 5,width = 10, command = StartAlgorithm )
Start.place(x=750,y=0)


speedlabel = Label(root,text = " Speed : " , font = ("new roman",12, "italic bold"),bg = "#0E6DA5",
                  width = 10, fg = "black",relief = GROOVE,bd = 5)
speedlabel.place(x=400,y=0)

speedscale = Scale(root,from_ = 0.1 , to = 5.0,resolution = 0.2,length = 200,digits = 2, orient = HORIZONTAL,font = ("arial",14,"italic bold"),
                  relief = GROOVE,bd = 2,width = 10)
speedscale.place(x=520,y=0)


canvas = Canvas(root,width = 870 , height = 450 , bg = "black")
canvas.place(x=10,y=130)




root.mainloop()