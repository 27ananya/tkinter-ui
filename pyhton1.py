import tkinter
from functools import partial
from DataHandler import Copy
window=tkinter.Tk()
window.title("window")
window.geometry("400x400")
data_handler=Copy("neww.json")
category_lists=data_handler.get_data()
print(category_lists)
category_data_labels=[]

def get_category_data(name):
    return data_handler.get_category(name)
def open_category(name):
    for element in category_data_labels:
        elenemt.configure(text="listss")
        del elenemt
    list_data_category=get_category_data(name)
    for j in range(len(list_data_category)):
        element=list_data_category[i]
        label=tkinter.Label(window,text=element)
        label.grid(row=i+1,column=0)
        category_data_labels.append(label)
    
for i in range(len(category_lists)):
    element=category_lists[i]
    command_function=partial(open_category,element)
    button=tkinter.Button(window,text=element,command=command_function)
    button.grid(row=0, column=i)
window.mainloop()
    
    
