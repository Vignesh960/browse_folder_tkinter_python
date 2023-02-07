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
e=Entry(root,textvariable=folderPath,width=50)
e.grid(row=0,column=1)
btnfind=ttk.Button(root,text="Browse",command=getFolderPath,padding=8)
btnfind.grid(row=0,column=2)
run_btn=Button(root,text="Run",command=dostuff,width=30,padx=10)
run_btn.grid(row=4,column=1)
root.mainloop()

#==ofice==

import os

# print(os.path.dirname(str(os.getcwd())))
from tkinter import *
from tempi import *
root = Tk()
root.title("PDF Reader")
root.geometry("500x200")
root.maxsize(width=None, height=None)
root.resizable(False, False)


def getFolderPath():
    filetypes = (
        ('text files', '*.pdf')
    )
    folder_selected = filedialog.askdirectory(initialdir="")
    folderPath.set(folder_selected)


def on_exit():
    """When you click to exit, this function is called"""
    if run_btn['state'] == DISABLED:

        if (messagebox.askyesno("Exit", "Are you want to quit the application? Currently process being in running state.")):
            root.destroy()
    else:

        if (messagebox.askyesno(
                "Exit", "Are you want to quit the application?")):
            root.destroy()


def disable_event():
    messagebox.showinfo(
        "Processing", "Please wait until process being done.")


def dostuff():
    if (__name__ == "__main__"):
        try:
            folder = folderPath.get()

            if folder != "":
                if (os.path.exists(folder)):
                    run_btn['state'] = DISABLED
                    msg = "Please wait... Process being done.\n Dont close the app."
                    label = Label(root, text=msg, foreground="red")
                    label.grid(row=5, column=0, padx=20)
                    root.protocol("WM_DELETE_WINDOW", on_exit)
                    #root.protocol("WM_DELETE_WINDOW", disable_event)

                    pdfs_list = get_listof_files(folder, "pdf")
                    with multiprocessing.Manager() as manager:
                        failed = manager.list()
                        if pdfs_list:

                            p = multiprocessing.Pool(5)
                            p.map(partial(get_total_txt, failed),
                                  pdfs_list[:10])

                            # p.close()
                            # Process.join(p)
                        # print(failed)
                    run_btn['state'] = NORMAL
                    suss_files_count = len(pdfs_list)-len(failed)
                    print("Out of {} files {} Succeeded and {} files found without data {} Files Without Grid Numbers and {} loaded.".format(
                        len(pdfs_list), suss_files_count, len(
                            failed), len(No_grid_number),
                        str(round(suss_files_count/(len(pdfs_list))*100, 2))+"%"))
                    end_time = datetime.now()
                    print('Duration: {} Minutes'.format(end_time - start_time))
                else:
                    messagebox.showerror(
                        "Path Not Found", "Selected path not exists in the directory : "+folder)
            else:
                messagebox.showwarning("Warning", "Please Select path")

                # print(folder)
        except AttributeError as attbe:
            print(attbe)
        except FileNotFoundError as fne:
            print(fne, folder)


folderPath = StringVar()
a = Label(root, text="\nChoose Path:", font=('Arial'))
a.grid(row=0, column=0)
e = Entry(root, textvariable=folderPath, width=50)
e.grid(row=3, column=0, padx=35)
btn_browse = ttk.Button(root, text="Browse", command=getFolderPath, padding=5)
btn_browse.grid(row=3, column=1)
run_btn = Button(root, text="Run", command=dostuff,
                 width=30, height=2, padx=10)
run_btn.grid(row=4, column=0)
# root.protocol("WM_DELETE_WINDOW", on_exit)

root.mainloop()
