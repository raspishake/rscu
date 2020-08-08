# GUI module template generated using PAGE version 5.2
#  in conjunction with Tcl version 8.6

import tkinter as tk
import tkinter.ttk as ttk

from rscu import rscu_wavesource_support
from rscu import rscu_support

w = None
def create_wave_source_window(rt, *args, **kwargs):
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    rscu_wavesource_support.set_Tk_var()
    top = wave_source_window (w)
    rscu_wavesource_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_wave_source_window():
    global w
    w.destroy()
    w = None

class wave_source_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.style = ttk.Style()
        self.style.configure('.',font="TkDefaultFont")

        top.geometry(str(590+rscu_support.x_offset) + "x" + str(240+rscu_support.x_offset)) # y offset = x offset in the wave source window
        top.resizable(0, 0)
        top.title("Wave Source")
        top.configure(highlightcolor="black")

        self.wave_souce_explain_label = tk.Label(top)
        self.wave_souce_explain_label.place(x=30, y=20,  height=38, width=(530+rscu_support.x_offset))
        self.wave_souce_explain_label.configure(anchor='w')
        self.wave_souce_explain_label.configure(justify='left')
        self.wave_souce_explain_label.configure(text='''Connect to a source (wave server) for the wave data. The wave source may be a local Raspberry Shake or FDSN network wave server.''')
        self.wave_souce_explain_label.configure(wraplength=str(580+rscu_support.x_offset))

#
# Define Local and FSDN tabs
#

        self.wave_source_tab = ttk.Notebook(top)
        self.wave_source_tab.place(x=0, y=70, height=(170+rscu_support.x_offset), width=(590+rscu_support.x_offset))
        self.wave_source_tab.configure(takefocus="")
        self.wave_source_tab_t1 = tk.Frame(self.wave_source_tab)
        self.wave_source_tab.add(self.wave_source_tab_t1, padding=3)
        self.wave_source_tab.tab(0, text="Local Raspberry Shake", compound="left", underline="-1", )
        self.wave_source_tab_t2 = tk.Frame(self.wave_source_tab)
        self.wave_source_tab.add(self.wave_source_tab_t2, padding=3)
        self.wave_source_tab.tab(1, text="FDSN Network Wave Server", compound="left", underline="-1", )
        if(rscu_support.wave_source_type == 'fdsn'):
            self.wave_source_tab.select(1)

#
# Local wave source
#

        self.rs_explain_label = tk.Label(self.wave_source_tab_t1)
        self.rs_explain_label.place(x=20, y=10,  height=21, width=540)
        self.rs_explain_label.configure(anchor='w')
        self.rs_explain_label.configure(justify='left')
        self.rs_explain_label.configure(text='''Local Raspberry Shake network name (example: rs.local) or local IP address.''')

        self.rs_lname_label = tk.Label(self.wave_source_tab_t1)
        self.rs_lname_label.place(x=20, y=40,  height=21, width=261)
        self.rs_lname_label.configure(anchor='w')
        self.rs_lname_label.configure(justify='left')
        self.rs_lname_label.configure(text='''Local Wave Server Name or IP Address:''')

        self.rs_name_entry = tk.Entry(self.wave_source_tab_t1)
        self.rs_name_entry.place(x=290, y=40, height=22, width=270)
        self.rs_name_entry.configure(background="white")
        self.rs_name_entry.configure(font="TkFixedFont")
        self.rs_name_entry.configure(textvariable=rscu_wavesource_support.wave_source_rs_name)

        self.rs_port_label_1 = tk.Label(self.wave_source_tab_t1)
        self.rs_port_label_1.place(x=245, y=70,  height=21, width=34)
        self.rs_port_label_1.configure(text='''Port:''')

        self.rs_port_entry = tk.Entry(self.wave_source_tab_t1)
        self.rs_port_entry.place(x=290, y=70, height=22, width=90)
        self.rs_port_entry.configure(background="white")
        self.rs_port_entry.configure(font="TkFixedFont")
        self.rs_port_entry.configure(textvariable=rscu_wavesource_support.wave_source_port)

        self.rs_port_label_2 = tk.Label(self.wave_source_tab_t1)
        self.rs_port_label_2.place(x=390, y=70,  height=21, width=160)
        self.rs_port_label_2.configure(anchor='w')
        self.rs_port_label_2.configure(justify='left')
        self.rs_port_label_2.configure(text='''(OWS Default = 16032)''')

        self.wave_source_rs_ok_button = tk.Button(self.wave_source_tab_t1)
        self.wave_source_rs_ok_button.place(x=380, y=105,  height=31, width=80)
        self.wave_source_rs_ok_button.configure(command=rscu_wavesource_support.wave_source_rs_ok)
        self.wave_source_rs_ok_button.configure(text='''OK''')

        self.wave_source_rs_cancel_button = tk.Button(self.wave_source_tab_t1)
        self.wave_source_rs_cancel_button.place(x=480, y=105, height=31, width=80)
        self.wave_source_rs_cancel_button.configure(command=rscu_wavesource_support.wave_source_cancel)
        self.wave_source_rs_cancel_button.configure(text='''Cancel''')

#
# FDSN wave source
#

        self.fdsn_explain_lable = tk.Label(self.wave_source_tab_t2)
        self.fdsn_explain_lable.place(x=20, y=10,  height=21, width=540)
        self.fdsn_explain_lable.configure(anchor='w')
        self.fdsn_explain_lable.configure(justify='left')
        self.fdsn_explain_lable.configure(text='''FDSN Network Wave Server address or FDSN Alias.''')

        self.fdsn_name_label = tk.Label(self.wave_source_tab_t2)
        self.fdsn_name_label.place(x=20, y=40,  height=21, width=190)
        self.fdsn_name_label.configure(anchor='w')
        self.fdsn_name_label.configure(justify='left')
        self.fdsn_name_label.configure(text='''FDSN Network Wave Server:''')

        self.fsdn_name_entry = tk.Entry(self.wave_source_tab_t2)
        self.fsdn_name_entry.place(x=220, y=40, height=22, width=340)
        self.fsdn_name_entry.configure(background="white")
        self.fsdn_name_entry.configure(font="TkFixedFont")
        self.fsdn_name_entry.configure(textvariable=rscu_wavesource_support.wave_source_fdsn_name)

        self.wave_source_fdsn_ok_button = tk.Button(self.wave_source_tab_t2)
        self.wave_source_fdsn_ok_button.place(x=380, y=105, height=31, width=80)
        self.wave_source_fdsn_ok_button.configure(command=rscu_wavesource_support.wave_source_fdsn_ok)
        self.wave_source_fdsn_ok_button.configure(text='''OK''')

        self.wave_source_fsdn_cancel_button = tk.Button(self.wave_source_tab_t2)
        self.wave_source_fsdn_cancel_button.place(x=480, y=105, height=31, width=80)
        self.wave_source_fsdn_cancel_button.configure(command=rscu_wavesource_support.wave_source_cancel)
        self.wave_source_fsdn_cancel_button.configure(text='''Cancel''')
