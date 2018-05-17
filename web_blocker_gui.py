from tkinter import *
from tkinter import messagebox
import validators

host_path="C:\\Windows\\System32\\Drivers\\etc\hosts"

def url_valid():
    a = validators.url("https://" + web.get())
    if a == True:
        print('valid url')
        blocker()
    else:
        messagebox.showerror('Error', 'Invalid URL')


def blocker():
    website = web.get()
    redirect = "127.0.0.1"
    if '.' in website:
        with open("H:\\PythonTester\\Udemy\\testhost", "r+") as f:
            content = f.read()
            if website in content:
                messagebox.showwarning('Info', 'Website already added')
            else:
                f.write(redirect + ' ' + website + '\n')
                messagebox.showinfo('Success', 'Website added to host file')
    else:
        messagebox.showerror('Error', "The web address format is incorrect\n(Example: 'www.google.com' or 'google.com')")


def url_del():
    website = web.get()
    webs = web.get()
    with open(host_path, "r+") as f:
        content = f.readlines()
        f.seek(0)
        for line in content:
            if webs not in line:
                f.write(line)
        f.truncate()
        messagebox.showinfo('Done!', 'URL Removed')


window = Tk()
window.wm_title('Website Blocker')

b1 = Button(window, text='Add Website', command=url_valid)
b1.grid(row=3, column=2, columnspan=3)

b2 = Button(window, text='Remove Website', command=url_del)
b2.grid(row=3, column=5, columnspan=6)

web = StringVar()
e1 = Entry(window, textvariable=web)
e1.grid(row=0, column=1, columnspan=10)

l1 = Label(window, text='Enter Website: ')
l1.grid(row=0, column=0)

window.mainloop()
