# # # n=int(input("First value :"))
# # # n1=int(input("enter second value:"))
# # # for i in range(n,n1+1):
# # #     if(i>1):
# # #         for j in range(2,i):
# # #             if(i%j)==0:
# # #                 #print(i)
# # #                 break
# # #         else:
# # #             print(i)



from tkinter import *
from tkinter import ttk
from tkinter import filedialog,messagebox
from tkinter import Button
import sys
root=Tk()
root.title("PDF Reader")
root.geometry("600x400")
root.maxsize(width=None,height=None)
root.resizable(False,False)
def getFolderPath():
    folder_selected=filedialog.askdirectory()
    folderPath.set(folder_selected)

def dostuff():
    folder=folderPath.get()

folderPath=StringVar()
a=Label(root,text="Path:")
a.grid(row=0,column=0)
e=Entry(root,textvariable=folderPath)
e.grid(row=0,column=1)
btnfind=ttk.Button(root,text="Browse",command=getFolderPath)
btnfind.grid(row=0,column=2)
c=Button(root,text="Run",command=dostuff)
c.grid(row=4,column=0)
root.mainloop()
