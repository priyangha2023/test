from tkinter import *
import pyshorteners
import pyperclip

root=Tk()
root.geometry('600x300')
root.title("URL Shortener")
root.config(bg='aqua')

def shorturl():
    urls=pyshorteners.Shortener().tinyurl.short(url1.get())
    url2.set(urls)

def copyurl():
    c_url=url2.get()
    pyperclip.copy(c_url)


url1=StringVar()
url2=StringVar()

lb1=Label(root,text="Enter URL Here",font=('Broadway,28,bold'),bg='aqua')
lb1.pack(pady=5)
En1=Entry(root,textvariable=url1,font=('Broadway,20,bold'))
En1.pack()


lb2=Label(root,text="Shortened URL",font=('Broadway,35,bold'),bg='aqua')
lb2.pack(pady=5)
En2=Entry(root,textvariable=url2,font=('Broadway,35,bold'))
En2.pack()

bt1=Button(root,text="Generate URL",font=('Broadway,25,bold'),bg='yellow',fg='black',bd=5,command=shorturl)
bt1.pack(pady=10)
btn2=Button(root,text="Copy URL",font=('Broadway,25,bold'),bg='yellow',fg='black',bd=5,command=copyurl)
btn2.pack(pady=10)

root.mainloop()
