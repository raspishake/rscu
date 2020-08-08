# GUI module template generated using PAGE version 5.2
#  in conjunction with Tcl version 8.6

import tkinter as tk
import tkinter.ttk as ttk

from rscu import rscu_arrivaldata_support

w = None
def create_arrival_data_window(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_arrival_data_window(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    rscu_arrivaldata_support.set_Tk_var()
    top = arrival_data_window (w)
    rscu_arrivaldata_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_arrival_data_window():
    global w
    w.destroy()
    w = None

class arrival_data_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("880x660")
        top.resizable(0, 0)
        top.title("Event Distance and Arrival Times")
        top.configure(highlightcolor="black")

        self.arrival_data_text_frame = tk.Frame(top)
        self.arrival_data_text_frame.place(x=20, y=20, height=580, width=840)
        self.arrival_data_text_frame.configure(relief='groove')
        self.arrival_data_text_frame.configure(borderwidth="2")

        self.arrival_data_text = tk.Text(self.arrival_data_text_frame)
        self.arrival_data_text.place(x=0, y=0, height=574, width=816)
        self.arrival_data_text.configure(font="TkTextFont")
        self.arrival_data_text.configure(wrap="none")

        self.data_text_scrollbar = ttk.Scrollbar(self.arrival_data_text_frame, orient='vertical')
        self.arrival_data_text.configure(yscrollcommand=self.data_text_scrollbar.set)
        self.data_text_scrollbar.configure(command=self.arrival_data_text.yview)
        self.data_text_scrollbar.place(x=816, y=0, height=574, width=20)

        self.arrival_data_text.insert(tk.END, rscu_arrivaldata_support.data_text)

        self.arrival_data_copy_button = tk.Button(top)
        self.arrival_data_copy_button.place(x=20, y=615,  height=31, width=140)
        self.arrival_data_copy_button.configure(command=rscu_arrivaldata_support.arrival_copy_button)
        self.arrival_data_copy_button.configure(text='''Copy to Clipboard''')

        self.arrival_data_save_button = tk.Button(top)
        self.arrival_data_save_button.place(x=370, y=615, height=31, width=140)
        self.arrival_data_save_button.configure(command=rscu_arrivaldata_support.arrival_save_button)
        self.arrival_data_save_button.configure(text='''Save to File''')

        self.arrival_data_close_button = tk.Button(top)
        self.arrival_data_close_button.place(x=720, y=615, height=31, width=140)
        self.arrival_data_close_button.configure(command=rscu_arrivaldata_support.destroy_window)
        self.arrival_data_close_button.configure(text='''Close''')
