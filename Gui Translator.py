import tkinter as tk
from tkinter import ttk 
from googletrans import Translator 
from tkinter import messagebox,Text,RIDGE,Button

def translate():
    lang = t1.get("1.0","end-1c")
    cl = c_lang.get()

    if lang == '':
        messagebox.showerror('Language translator',
                            ' Please fill the box')
    else:
        
        translator = Translator()
        output = translator.translate(lang,dest=cl)
        t2.insert('end',output.text)

def clear():
    t1.delete(1.0,'end')
    t2.delete(1.0,'end')
root = tk.Tk()
root.title('GUI translator')
root.geometry("500x600")
a= tk.StringVar()
auto_detect = ttk.Combobox(root,width=20,textvariable=a,state='readonly',font=('verdana',10,'bold'),)
auto_detect['values'] = (
    'Auto Detect',
)
auto_detect.place(x=30,y=70)
auto_detect.current(0)
l = tk.StringVar()
c_lang = ttk.Combobox(root,width=20,textvariable=l,state='readonly',font=('verdana',10,'bold'))
c_lang['values'] = ('Hindi','Punjabi','Japanese','English','Spanish','French','Danish','Dutch','German','Indonesian','Irish','Italian','Javanese','Kannada','Kazakh',
'Khmer','Kinyarwanda','Korean','Kurdish','Kyrgyz','LaoLatin','Latvian','Lithuanian','Luxembourgish','Macedonian','Malagasy','Malay')
c_lang.place(x=290,y=70)
c_lang.current(0)
t1 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)
t2 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)
button = Button(root,text="Translate",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=translate)
button.place(x=150,y=280)
clear = Button(root,text="clear",relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor="hand2",command=clear)
clear.place(x=280,y=280)
root.mainloop()