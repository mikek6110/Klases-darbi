
import tkinter as tk
import tkinter.ttk as ttk
 
class Window:
    def __init__(self, master):
        self.master = master
 
        style = ttk.Style()
        style.theme_settings("default", {
           "TButton": {
               "configure": {"padding": 10},
               "map": {
                   "background": [("active", "yellow3"),
                                  ("!disabled", "yellow")],
                   "foreground": [("focus", "Red"),
                                  ("active", "green"),
                                  ("!disabled", "Blue")]
               }
           }
        })
 
        style.theme_use("default")
 
        button = ttk.Button(self.master, text = "Click Me!")
        button.pack(padx = 5, pady = 5)
 
root = tk.Tk()
root.geometry('200x200')
window = Window(root)
root.mainloop()

        #label = ttk.Label (master,text = 'This is a Label!')
        #label.pack(padx=5 , pady=5 )

        #checkbox= ttk.Combobox(master, values=['Option 1','Optopm 2'])
        #checkbox.set('Option 1')
        #checkbox.pack(padx=5,pady=5)

        #radiobutton=ttk.Radiobutton(master, text = 'Radio Button')
        #radiobutton.pack(padx=5,pady=5)

        #checkbutton = ttk.Checkbutton(master, text = 'Check Button')
        #checkbutton.pack(padx=5,pady=5)

        #scale = ttk.Scale(master, from_=0, to=10)
        #scale.pack(padx=5,pady=5) 