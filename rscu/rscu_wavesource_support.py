# Support module template generated using PAGE version 5.2
#  in conjunction with Tcl version 8.6

import sys

import tkinter as tk
import tkinter.ttk as ttk

from rscu import rscu_support

from obspy.clients.fdsn.header import URL_MAPPINGS
from urllib.parse import urlparse

def set_Tk_var():
    '''
    All the variables used for the child window to set the "wave source"
    '''
    global wave_source_rs_name
    wave_source_rs_name = tk.StringVar()
    if(rscu_support.wave_source_type == 'rs'):
        wave_source_rs_name.set(rscu_support.wave_source)
    else:
        wave_source_rs_name.set('rs.local')
    global wave_source_port
    wave_source_port = tk.IntVar()
    wave_source_port.set(16032)
    global wave_source_fdsn_name
    wave_source_fdsn_name = tk.StringVar()
    if(rscu_support.wave_source_type == 'fdsn'):
        wave_source_fdsn_name.set(rscu_support.wave_source)
    else:
        wave_source_fdsn_name.set('fdsnws.raspberryshakedata.com')
    
def wave_source_cancel():
    '''
    "Cancel" Button command from either local or FDSN tab.
    '''
    if( rscu_support.verbose ):
        print('rscu_wavesource_support.wave_source_fdsn_cancel')
    destroy_window()

def wave_source_fdsn_ok():
    '''
    "OK" Button command from the FDSN tab.
    '''
    if( rscu_support.verbose ):
        print('rscu_wavesource_support.wave_source_fdsn_ok')
    wave_source = wave_source_fdsn_name.get()
    valid = False

    if( urlparse(wave_source)[1] ):                                     # Users may enter FDSN address with or without a protocol, so...
        wave_source = urlparse(wave_source)[1]                          # Strip the protocol if included to allow easier validation of address - it will be added back later.

    if( wave_source.lower() == 'fdsnws.raspberryshakedata.com' or wave_source.upper() == 'RASPISHAKE' ):  # Check to see if the source is the Raspberry Shake "IRIS Federator" system ("FDSN") - We check specifically for the raspberryshakedata address because it is not returned in the latest URL_MAPPINGS list - matches are case insensitive
        wave_source = 'https://fdsnws.raspberryshakedata.com'           # Set the wave client and source URL
        valid = True
    else:
        for key in sorted(URL_MAPPINGS.keys()):                         # Check for any other FDSN source location or key
            if (wave_source.lower() == urlparse(URL_MAPPINGS[key])[1] or wave_source.upper() == key):  # All returned keys are all upper case, but the match should be case insensitive
                wave_source = URL_MAPPINGS[key]                         # If there is a match, set the client and source
                valid = True
                break                                                   # Stop searching once a match is found
    if( not valid ):
        tk.messagebox.showwarning('Unknown FDSN Server','The address or key "' + wave_source + '" is not a recognised FDSN server')
        destroy_window()
        return()
                
    if( rscu_support.verbose ):
        print(wave_source)
    rscu_support.wave_source = wave_source
    rscu_support.wave_source_blabel.set(wave_source)                    # "blabel" is the text displayed on the wave source button
    rscu_support.wave_source_type = 'fdsn'
    sys.stdout.flush()
    destroy_window()

def wave_source_rs_ok():
    '''
    "OK" Button command from the local source tab.
    '''
    if( rscu_support.verbose ):
        print('rscu_wavesource_support.wave_source_rs_ok')
    rscu_support.wave_source = wave_source_rs_name.get()
    rscu_support.wave_source_port = wave_source_port.get()
    rscu_support.wave_source_blabel.set(rscu_support.wave_source + ':' + str(rscu_support.wave_source_port))  # "blabel" is the text displayed on the wave source button and is the concatination of the source URI and the port number
    rscu_support.wave_source_type = 'rs'
    sys.stdout.flush()
    destroy_window()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import rscu_wavesource
    rscu_wavesource.vp_start_gui()

