import tkinter
from functools import partial
from json_file import Copy
window=tkinter.Tk()
window.title("window")
window.geometry("400x400")
c=Copy("neww.json")
category_lists=c.get_data()
print(category_lists)
category_data_labels=[]

def get_category_data(name):
    return c.get_category(name)
def open_category(name):
    for element in category_data_labels:
        element.configure(text="listss")
        del element
    list_data_category=get_category_data(name)
    for j in range(len(list_data_category)):
        element=list_data_category[j]
        label=tkinter.Label(window,text=element)
        label.grid(row=j+1,column=0)
        category_data_labels.append(label)

buttons_container=tkinter.Frame(window,bg="green")
buttons_container.pack(side=tkinter.TOP,fill=tkinter.X)
    
for i in range(len(category_lists)):
    element=category_lists[i]
    command_function=partial(open_category,element)
    button=tkinter.Button(buttons_container,text=element,command=command_function)
    button.grid(row=0, column=i)
frame_2=tkinter.Frame(window,bg="red")
frame_2.pack(side=tkinter.TOP,expand=True,fill=tkinter.BOTH)
frame_3=tkinter.Frame(window,bg="yellow")
frame_3.pack()
scroll=tkinter.Scrollbar(window)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
canvas=tkinter.Canvas(frame_2,bg="white")
canvas.pack(expand=True,fill=tkinter.BOTH)
canvas.create_window((100,100),window=frame_3)
window.mainloop()










    
