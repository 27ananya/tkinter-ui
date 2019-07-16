import tkinter
from functools import partial
from data import Copy

window=tkinter.Tk()
window.title("window")
window.geometry("400x400")

data_handler=Copy("data.json")
category_lists=data_handler.get_data()
print(category_lists)
category_data_labels=[]

def get_category_data(name):
    return data_handler.get_list(name)
def open_category(name):
    for element in category_data_labels:
        element.configure(text="listss")
        del element
    list_data_category=get_category_data(name)
    for j in range(len(list_data_category)):
        element=list_data_category[j]
        label=tkinter.Label(frame3,text=element)
        label.grid(row=j+1,column=0)
        category_data_labels.append(label)
    
button_containeer=tkinter.Frame(window,bg="red")
button_containeer.pack(side=tkinter.TOP,fill=tkinter.X)
for i in range(len(category_lists)):
    element=category_lists[i]
    command_function=partial(open_category,element)
    button=tkinter.Button(button_containeer,text=element,command=command_function)
    button.grid(row=0,column=i)
frame2=tkinter.Frame(window,bg="green")
frame2.pack(side=tkinter.TOP,expand=True,fill=tkinter.BOTH)

frame3=tkinter.Frame(window,bg="yellow")
frame3.pack()

scroll=tkinter.Scrollbar(frame2)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)

canvas=tkinter.Canvas(frame2,bg="blue",height=200,width=200)
canvas.pack(expand=True,fill=tkinter.BOTH)
canvas.create_window((50,100),window=frame3)

window.mainloop()



    
    
