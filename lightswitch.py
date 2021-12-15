import tkinter as tk

window = tk.Tk()

# schijf hier tussen je code

def lightswitch():
    if button["text"] == "lightswitch off":
        button["text"] = "lightswitch on"
        window['background']='yellow'
        print("light is on")
    else:
        button["text"] = "lightswitch off"
        window['background']='black'
        print("light is off")

# schijf hier tussen je code

button = tk.Button(text='lightswitch off', bg="white", fg="black", command=lightswitch)
button.pack(pady = 20, padx = 20)
window['background']='black'


window.mainloop()