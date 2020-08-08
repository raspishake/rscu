# Support module template generated using PAGE version 5.2
#  in conjunction with Tcl version 8.6

import sys

import tkinter as tk

from rscu import rscu_support

def set_Tk_var():
    global data_text
    global data_out

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def arrival_copy_button():                                              # Function to put "data_out" onto the system clipgoard
    if( rscu_support.verbose ):
        print('rscu_arrivaldata_support.arrival_copy_button')
    root.clipboard_clear()
    root.clipboard_append(data_out)
    root.update()
    sys.stdout.flush()

def arrival_save_button():                                              # Function to save "data_out" to a text file, allowing the user to desigbate the location and file name with a standard file dialog
    if( rscu_support.verbose ):
        print('rscu_arrivaldata_support.arrival_save_button')
    csv_out_file = tk.filedialog.asksaveasfilename(parent=top_level, title="Save-File Directory", initialdir=rscu_support.rscu_save_directory.get(), filetypes=[('default','*.csv'),('Comma Separated Value','*.csv'),('Text','*.txt'),('All','*.*')], defaultextension=".csv")
    if( len(csv_out_file) > 0 ):                                        # Save only if a text string is returned (in other words, do not attempt to save if "Cancel" was clicked
        rf = open(csv_out_file, 'w')
        rf.write(data_out)
        rf.close()
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import rscu_arrivaldata
    rscu_arrivaldata.vp_start_gui()

