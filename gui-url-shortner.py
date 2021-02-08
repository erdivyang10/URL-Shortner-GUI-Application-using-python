#Welcome to the Github Page
#Author: Divyang Goswami
#email: erdivyang10@gmail.com
#Linkedin: https://in.linkedin.com/in/divyang-goswami-a0885246
#website: https://divyanggoswami.github.io/


from tkinter import*
import pyshorteners
import webbrowser
import os


root = Tk()
root.title("URL Shortner using Python")
root.geometry("550x550")
'''frame = Frame(root,width=150, height=150)
frame.pack()'''

#title of window
# setting GUI title   
url_label = Label(root, text="URL Shortner", font="Helvtica 25 bold",height=2).pack()

entry1 = Entry(root, width=70,border=2, borderwidth=2, relief=FLAT)
entry1.pack()


def button_command():
    url = entry1.get()
    if url == '':
        Label(root,text="Link should not be blank").pack()
        
    else:

        #webbrowser.open(pyshorteners.Shortener().tinyurl.short(url))
        win_url= pyshorteners.Shortener().tinyurl.short(url)
        print(win_url)
        lab = Label(root,text="Your Short URL",height=2)
        lab.pack()
        entry = Entry(root, width=70,border=2, borderwidth=2)
        entry.insert(0,win_url) # insert short URL
        entry.pack()
        Button(root, text="Open ShortLink in Browser", command=open_browser, padx=10, pady=10 ).pack()
        return None  

def close_window():
    root.destroy()

def open_browser():
    url = entry1.get()
    webbrowser.open(pyshorteners.Shortener().tinyurl.short(url))

def clear_all():
    root.destroy()
    os.popen("python gui-url-shortner.py")   

Button(root, text=" Click to get Short URL ", command=button_command, padx=10, pady=10 ).pack(side=LEFT)
Button(root, text="Quit", command=close_window, padx=10, pady=10 ).pack(side=RIGHT)
Button(root, text="Clear All", command=clear_all, padx=10, pady=10 ).pack(side=LEFT)


author = Label(root, text= " GUI Application By Divyang Goswami")
author.place(relx = 0.0,  rely = 1.0, anchor ='sw')

root.mainloop()

