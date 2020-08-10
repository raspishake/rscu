# Support module template generated using PAGE version 5.2
#  in conjunction with Tcl version 8.6

import os, sys
import tkinter as tk

from tkinter import filedialog, colorchooser, messagebox
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

from rscu import rscu
from rscu import rscu_settings
from rscu import rscu_wavesource

def set_Tk_var():
    '''
    All the variables used for gathering data from the main
    application window, including all tabs.
    '''
    # Common variables used by multiple tabs
    
    global rs_station
    rs_station = tk.StringVar()
    rs_station.set(rscu_settings.settings['common']['rs_station'])
    global station_latitude
    station_latitude = tk.StringVar()
    station_latitude.set(rscu_settings.settings['common']['station_latitude'])
    global station_longitude
    station_longitude = tk.StringVar()
    station_longitude.set(rscu_settings.settings['common']['station_longitude'])
    global wave_source
    wave_source = rscu_settings.settings['common']['wave_source']
    global wave_source_type
    wave_source_type = rscu_settings.settings['common']['wave_source_type']
    global wave_source_port
    wave_source_port = rscu_settings.settings['common']['wave_source_port']
    global wave_source_blabel
    wave_source_blabel = tk.StringVar()
    if(wave_source_type == 'rs'):
        wave_source_blabel.set(wave_source + ':' + str(wave_source_port))
    else:
        wave_source_blabel.set(wave_source)
    global rscu_save_directory
    rscu_save_directory = tk.StringVar()
    rscu_save_directory.set(rscu_settings.settings['common']['rscu_save_directory'])
    global chart_save_directory
    chart_save_directory = os.path.abspath(os.path.join(rscu_save_directory.get(),'charts')).replace('\\', '/')
    global data_save_directory
    data_save_directory = os.path.abspath(os.path.join(rscu_save_directory.get(),'data')).replace('\\', '/')
    global pixels_wide
    pixels_wide = tk.IntVar()
    pixels_wide.set(rscu_settings.settings['common']['pixels_wide'])
    global pixels_tall
    pixels_tall = tk.IntVar()
    pixels_tall.set(rscu_settings.settings['common']['pixels_tall'])
    
    global station_component
    station_component = tk.StringVar()
    station_component.set(rscu_settings.settings['common']['station_component'])
    
    global start_year
    start_year = tk.IntVar()
    global start_month
    start_month = tk.IntVar()
    global start_day
    start_day = tk.IntVar()
    global start_hour
    start_hour = tk.IntVar()
    global start_minute
    start_minute = tk.IntVar()
    global start_second
    start_second = tk.IntVar()
    global duration
    duration = tk.IntVar()
    duration.set(rscu_settings.settings['common']['duration'])
    
    global chart_autosave
    chart_autosave = tk.BooleanVar()
    chart_autosave.set(rscu_settings.settings['common']['chart_autosave'])
    global chart_format
    chart_format = tk.StringVar()
    chart_format.set(rscu_settings.settings['common']['chart_format'])
    global available_formats
    available_formats = plt.gcf().canvas.get_supported_filetypes()
    plt.close()
    
    global validate
    validate = True
    global verbose
    verbose = rscu_settings.settings['common']['verbose']
    
    # Platform specific geometry adjustment
    
    global macOS
    macOS = False
    global x_offset
    x_offset = 0
    global y_offset
    y_offset = 0
    if( sys.platform.startswith('darwin') ):
        macOS = True
        x_offset = 50
        y_offset = 30

    # Helicorder variables
    
    global helicorder_year
    helicorder_year = tk.IntVar()
    global helicorder_month
    helicorder_month = tk.IntVar()
    global helicorder_day
    helicorder_day = tk.IntVar()
    global helicorder_start_hour
    helicorder_start_hour = tk.StringVar()
    
    global helicorder_minutes_per_line
    helicorder_minutes_per_line = tk.IntVar()
    helicorder_minutes_per_line.set(rscu_settings.settings['helicorder']['helicorder_minutes_per_line'])
    global helicorder_hours_per_chart
    helicorder_hours_per_chart = tk.IntVar()
    helicorder_hours_per_chart.set(rscu_settings.settings['helicorder']['helicorder_hours_per_chart'])
    global helicorder_vertical_scaling_state
    global helicorder_auto_vertical_scaling
    helicorder_auto_vertical_scaling = tk.BooleanVar()
    global helicorder_vertical_scaling
    helicorder_vertical_scaling = tk.StringVar()
    if(rscu_settings.settings['helicorder']['helicorder_vertical_scaling'] == 'auto'):
        helicorder_auto_vertical_scaling.set(True)
        helicorder_vertical_scaling_state = 'disabled'
    else:
        helicorder_auto_vertical_scaling.set(False)
        helicorder_vertical_scaling_state = 'normal'
        helicorder_vertical_scaling.set(rscu_settings.settings['helicorder']['helicorder_vertical_scaling'])
    global helicorder_line1_color
    helicorder_line1_color = tk.StringVar()
    helicorder_line1_color.set(rscu_settings.settings['helicorder']['helicorder_line1_color'])
    global helicorder_line2_color
    helicorder_line2_color = tk.StringVar()
    helicorder_line2_color.set(rscu_settings.settings['helicorder']['helicorder_line2_color'])
    global helicorder_line3_color
    helicorder_line3_color = tk.StringVar()
    helicorder_line3_color.set(rscu_settings.settings['helicorder']['helicorder_line3_color'])
    global helicorder_line4_color
    helicorder_line4_color = tk.StringVar()
    helicorder_line4_color.set(rscu_settings.settings['helicorder']['helicorder_line4_color'])
    
    global helicorder_chart_title
    helicorder_chart_title = tk.StringVar()
    helicorder_chart_title.set(rscu_settings.settings['helicorder']['helicorder_chart_title'])
    global helicorder_chart_filename
    helicorder_chart_filename = tk.StringVar()
    helicorder_chart_filename.set(rscu_settings.settings['helicorder']['helicorder_chart_filename'])
    
    # Seismogram variables
    
    global seismogram_component
    seismogram_component = tk.StringVar()
    seismogram_component.set(rscu_settings.settings['seismogram']['seismogram_component'])
    
    global seismogram_filter_type
    seismogram_filter_type = tk.StringVar()
    seismogram_filter_type.set(rscu_settings.settings['seismogram']['seismogram_filter_type'].lower())
    global seismogram_filter_max_frequency
    seismogram_filter_max_frequency = tk.StringVar()
    seismogram_filter_max_frequency.set(rscu_settings.settings['seismogram']['seismogram_filter_max_frequency'])
    global seismogram_filter_max_state
    global seismogram_filter_min_frequency
    seismogram_filter_min_frequency = tk.StringVar()
    seismogram_filter_min_frequency.set(rscu_settings.settings['seismogram']['seismogram_filter_min_frequency'])
    global seismogram_filter_min_state
    global seismogram_filter_zerophase
    seismogram_filter_zerophase = tk.BooleanVar()
    seismogram_filter_zerophase.set(rscu_settings.settings['seismogram']['seismogram_filter_zerophase'])
    global seismogram_filter_zerophase_state
    global seismogram_filter_corners
    seismogram_filter_corners = tk.IntVar()
    seismogram_filter_corners.set(rscu_settings.settings['seismogram']['seismogram_filter_corners'])
    global seismogram_filter_corners_state
    
    global seismogram_chart_title
    seismogram_chart_title = tk.StringVar()
    seismogram_chart_title.set(rscu_settings.settings['seismogram']['seismogram_chart_title'])
    global seismogram_chart_filename
    seismogram_chart_filename = tk.StringVar()
    seismogram_chart_filename.set(rscu_settings.settings['seismogram']['seismogram_chart_filename'])
    
    # Spectrogram variables
    
    global spectrogram_max_frequency
    spectrogram_max_frequency = tk.StringVar()
    spectrogram_max_frequency.set(rscu_settings.settings['spectrogram']['spectrogram_max_frequency'])
    global spectrogram_min_frequency
    spectrogram_min_frequency = tk.StringVar()
    spectrogram_min_frequency.set(rscu_settings.settings['spectrogram']['spectrogram_min_frequency'])
    global spectrogram_log_frequency
    spectrogram_log_frequency = tk.BooleanVar()
    spectrogram_log_frequency.set(rscu_settings.settings['spectrogram']['spectrogram_log_frequency'])
    global spectrogram_log_color
    spectrogram_log_color = tk.BooleanVar()
    spectrogram_log_color.set(rscu_settings.settings['spectrogram']['spectrogram_log_color'])
    global spectrogram_show_seismogram
    spectrogram_show_seismogram = tk.BooleanVar()
    spectrogram_show_seismogram.set(rscu_settings.settings['spectrogram']['spectrogram_show_seismogram'])
    global spectrogram_show_colorbar
    spectrogram_show_colorbar = tk.BooleanVar()
    spectrogram_show_colorbar.set(rscu_settings.settings['spectrogram']['spectrogram_show_colorbar'])
    global spectrogram_colormap
    spectrogram_colormap = tk.StringVar()
    spectrogram_colormap.set(rscu_settings.settings['spectrogram']['spectrogram_colormap'])
    
    global spectrogram_chart_title
    spectrogram_chart_title = tk.StringVar()
    spectrogram_chart_title.set(rscu_settings.settings['spectrogram']['spectrogram_chart_title'])
    global spectrogram_chart_filename
    spectrogram_chart_filename = tk.StringVar()
    spectrogram_chart_filename.set(rscu_settings.settings['spectrogram']['spectrogram_chart_filename'])
    global spectrogram_plot_chart
    spectrogram_plot_chart = tk.StringVar()
    spectrogram_plot_chart.set('Plot Chart')
    
    # Spectrograph variables
    
    global spectrum_max_frequency
    spectrum_max_frequency = tk.StringVar()
    spectrum_max_frequency.set(rscu_settings.settings['spectrograph']['spectrum_max_frequency'])
    global spectrum_min_frequency
    spectrum_min_frequency = tk.StringVar()
    spectrum_min_frequency.set(rscu_settings.settings['spectrograph']['spectrum_min_frequency'])
    global spectrum_log_frequency
    spectrum_log_frequency = tk.BooleanVar()
    spectrum_log_frequency.set(rscu_settings.settings['spectrograph']['spectrum_log_frequency'])
    global spectrum_log_intensity
    spectrum_log_intensity = tk.BooleanVar()
    spectrum_log_intensity.set(rscu_settings.settings['spectrograph']['spectrum_log_intensity'])
    global spectrum_autoscale_intensity
    spectrum_autoscale_intensity = tk.BooleanVar()
    spectrum_autoscale_intensity.set(rscu_settings.settings['spectrograph']['spectrum_autoscale_intensity'])
    global spectrum_intensity_scale_state
    if(spectrum_autoscale_intensity.get()):
        spectrum_intensity_scale_state = 'disabled'
    else:
        spectrum_intensity_scale_state = 'normal'
    global spectrum_max_intensity
    spectrum_max_intensity = tk.StringVar()
    global spectrum_min_intensity
    spectrum_min_intensity = tk.StringVar()
    
    global spectrum_chart_title
    spectrum_chart_title = tk.StringVar()
    spectrum_chart_title.set(rscu_settings.settings['spectrograph']['spectrum_chart_title'])
    global spectrum_chart_filename
    spectrum_chart_filename = tk.StringVar()
    spectrum_chart_filename.set(rscu_settings.settings['spectrograph']['spectrum_chart_filename'])
    
    # Phase Arrival variables
    
    global event_year
    event_year = tk.IntVar()
    global event_month
    event_month = tk.IntVar()
    global event_day
    event_day = tk.IntVar()
    global event_hour
    event_hour = tk.IntVar()
    global event_minute
    event_minute = tk.IntVar()
    global event_second
    event_second = tk.IntVar()
    
    global event_latitude
    event_latitude = tk.StringVar()
    global event_longitude
    event_longitude = tk.StringVar()
    global event_depth
    event_depth = tk.StringVar()
    
    global arrival_degrees
    global arrival_km
    global arrival_miles
    
    global phases
    phases = tk.StringVar()
    phase_list = ','.join(rscu_settings.settings['arrival']['arrival_phase_list'])
    global arrival_phase_list
    arrival_phase_list = tk.StringVar()
    arrival_phase_list.set(phase_list)
    global arrival_phase_to_list
    arrival_phase_to_list = tk.StringVar()
    arrival_phase_to_list.set('Phases to Phase List')
    global arrival_ray_path_type
    arrival_ray_path_type = tk.StringVar()
    arrival_ray_path_type.set(rscu_settings.settings['arrival']['arrival_ray_path_type'])
    global arrival_show_legend
    arrival_show_legend = tk.BooleanVar()
    arrival_show_legend.set(rscu_settings.settings['arrival']['arrival_show_legend'])
    global arrival_annotate
    arrival_annotate = tk.BooleanVar()
    arrival_annotate.set(rscu_settings.settings['arrival']['arrival_annotate'])

    
    global arrival_chart_title
    arrival_chart_title = tk.StringVar()
    arrival_chart_title.set(rscu_settings.settings['arrival']['arrival_chart_title'])
    global arrival_chart_filename
    arrival_chart_filename = tk.StringVar()
    arrival_chart_filename.set(rscu_settings.settings['arrival']['arrival_chart_filename'])

#
# Command functions
#
# main Menu

def main_menu_about():
    '''Displays the "About" dialog when selected from the File menu.'''
    if( verbose ):
        print('rscu_support.main_menu_about')
    tk.messagebox.showinfo("About rscu", "Seismograph Charting Utility\n  Version 0.0.1\n  August 2020\n\nBy David Fowler")

#### Note: the Main Menu "Save Preferences" menu item command links directly to rscu_settings.main_menu_save_prefs():

#### Note: the Main Menu "Save Restore Saved Preferences" menu item command links directly to rscu_settings.main_menu_restore_prefs():

#### Note: the Main Menu "Save Reset Default Preferences" menu item command links directly to rscu_settings.main_menu_reset_defaults():

# Common frame

def get_wave_source():
    '''
    Opens the Wave Source selection window when the the user clicks on
    the wave source button
    '''
    if( verbose ):
        print('rscu_support.get_wave_source')
    rscu_wavesource.create_wave_source_window(root)

def get_rscu_save_directory():
    '''
    Opens the Chart Save Directory dialog when the user clicks on the
    chart save directory button. The appearance of the dialog is
    controlled by the platform OS.
    :return: full path to the default save-file directory
    :rtype: str
    '''
    if( verbose ):
        print('rscu_support.get_rscu_save_directory')
    savefile_directory = tk.filedialog.askdirectory(title="Save-File Directory", initialdir=rscu_save_directory.get(), mustexist=False)
    if( savefile_directory ):
        rscu_save_directory.set(savefile_directory)
        chart_save_directory = os.path.abspath(os.path.join(rscu_save_directory.get(),'chart')).replace('\\', '/')
        data_save_directory = os.path.abspath(os.path.join(rscu_save_directory.get(),'data')).replace('\\', '/')

# Helicorder

def helicorder_set_auto_vertical_scaling():
    '''
    Determines the state (normal or disabled) of the vertical scaling
    entry field depending on whether or not the "Auto Vertical Scaling"
    check box is checked, Auto Scaling checked = entry fields disabled.
    Auto Scaling not checked = entry field enabled ("normal").
    '''
    if( verbose ):
        print('rscu_support.helicorder_set_auto_vertical_scaling')
    if( helicorder_auto_vertical_scaling.get() ):
        helicorder_vertical_scaling_state = 'disabled'
    else:
        helicorder_vertical_scaling_state = 'normal'
    w.helicorder_vertical_scaling_label.configure(state=helicorder_vertical_scaling_state)
    w.helicorder_vertical_scaling_entry.configure(state=helicorder_vertical_scaling_state)

'''
The folowing pairs of functions change are for changing the color of the
next to the corresponding "Helicorder Line Color" field.

The first function of each pair changes the color based on the returned
color value from the OS specific color picker for the color button
being clicked upon.

The second function of each pair changes the color based on the value
typed into the entry field by the user. The function is called when the
user focus is moved from the field.
'''

def helicorder_color_line1():
    if( verbose ):
        print('rscu_support.helicorder_color_line1')
    line_color = helicorder_line_color(helicorder_line1_color.get())
    helicorder_line1_color.set(line_color)
    helicorder_color_entry_line1(None)
    
def helicorder_color_entry_line1(event):
    if( verbose ):
        print('rscu_support.helicorder_color_entry_line1')
    w.helicorder_line1_color_button.configure(background=helicorder_line1_color.get())
    if( macOS ):
        w.helicorder_line1_color_button.configure(highlightbackground=helicorder_line1_color.get())
        w.helicorder_line1_color_button.configure(highlightthickness=15)

def helicorder_color_line2():
    if( verbose ):
        print('rscu_support.helicorder_color_line2')
    line_color = helicorder_line_color(helicorder_line2_color.get())
    helicorder_line2_color.set(line_color)
    helicorder_color_entry_line2(None)

def helicorder_color_entry_line2(event):
    if( verbose ):
        print('rscu_support.helicorder_color_entry_line2')
    w.helicorder_line2_color_button.configure(background=helicorder_line2_color.get())
    if( macOS ):
        w.helicorder_line2_color_button.configure(highlightbackground=helicorder_line2_color.get())
        w.helicorder_line2_color_button.configure(highlightthickness=15)

def helicorder_color_line3():
    if( verbose ):
        print('rscu_support.helicorder_color_line3')
    line_color = helicorder_line_color(helicorder_line3_color.get())
    helicorder_line3_color.set(line_color)
    helicorder_color_entry_line3(None)

def helicorder_color_entry_line3(event):
    if( verbose ):
        print('rscu_support.helicorder_color_entry_line3')
    w.helicorder_line3_color_button.configure(background=helicorder_line3_color.get())
    if( macOS ):
        w.helicorder_line3_color_button.configure(highlightbackground=helicorder_line3_color.get())
        w.helicorder_line3_color_button.configure(highlightthickness=15)

def helicorder_color_line4():
    if( verbose ):
        print('rscu_support.helicorder_color_line4')
    line_color = helicorder_line_color(helicorder_line4_color.get())
    helicorder_line4_color.set(line_color)
    helicorder_color_entry_line4(None)

def helicorder_color_entry_line4(event):
    if( verbose ):
        print('rscu_support.helicorder_color_entry_line4')
    w.helicorder_line4_color_button.configure(background=helicorder_line4_color.get())
    if( macOS ):
        w.helicorder_line4_color_button.configure(highlightbackground=helicorder_line4_color.get())
        w.helicorder_line4_color_button.configure(highlightthickness=15)

def helicorder_line_color(initialcolor):
    '''
    Uses the OS specific Color Picker to allow the user to choose colors
    for lines on the Helicorder display. If the user clicks "OK," The
    chosen color value is returned. Otherwise, the initial color value
    is returned if the user clicks "Cancel" or closes the Color Picker
    dialog window.
    :param str initialcolor: the current line color value.
    :return: the hexidecimal RGB value of the new line color
    :rtype: str
    '''
    if( verbose ):
        print('rscu_support.helicorder_line_color')
    colorDialog = tk.colorchooser.Chooser(root,initialcolor=initialcolor)
    color = colorDialog.show()
    if( color[1] ):
        line_color = color[1]
    else:
        line_color = initialcolor
    return(line_color)

def set_current_date():
    '''
    Button command to set the helicorderchart to display the current
    24-hour UTC day starting at 0000 hours UTC. It will display the
    full 24-hours, but the chart will be blank beyond the current time.
    '''
    if( verbose ):
        print('rscu_support.set_current_date')
    utc_start_date = datetime.utcnow()
    set_start_date(utc_start_date, 0.0, 30, 24)

def set_last_full_date():
    '''
    Button command to set the helicorderchart to display the previous
    24-hour UTC day starting at 0000 hours UTC.
    '''
    if( verbose ):
        print('rscu_support.set_last_full_date')
    utc_start_date = datetime.utcnow() - timedelta(days=1)
    set_start_date(utc_start_date, 0.0, 30, 24)

def set_last_24h():
    '''
    Button command to set the helicorderchart to display the previous
    24-hour period, rounded up to the nearest half hour. This sets the
    Minutes per line to 30 minutes, and hours per chart to 24 hours.
    '''
    if( verbose ):
        print('rscu_support.set_last_24h')
    utc_start_time = datetime.utcnow() - timedelta(days=1)
    if ( int(utc_start_time.minute) < 30 ):
        hour_offset = 0.5
    else:
        hour_offset = 1.0
    start_hour = utc_start_time.hour + hour_offset
    if( start_hour == 24.0 ):
        start_hour = 0.0
        utc_start_time = utc_start_time + timedelta(minutes=60)
    set_start_date(utc_start_time, start_hour, 30, 24)

def set_last_12h():
    '''
    Button command to set the helicorderchart to display the previous
    12-hour period, rounded up to the nearest half hour. This sets the
    Minutes per line to 15 minutes, and hours per chart to 12 hours.
    '''
    if( verbose ):
        print('rscu_support.set_last_12h')
    utc_start_time = datetime.utcnow() - timedelta(minutes=720)
    if ( int(utc_start_time.minute) < 15 ):
        hour_offset = 0.25
    elif ( int(utc_start_time.minute) < 30 ):
        hour_offset = 0.50
    elif ( int(utc_start_time.minute) < 45 ):
        hour_offset = 0.75
    else:
        hour_offset = 1.00
    start_hour = utc_start_time.hour + hour_offset
    if( start_hour == 24.0 ):
        start_hour = 0.0
        utc_start_time = utc_start_time + timedelta(minutes=60)
    set_start_date(utc_start_time, start_hour, 15, 12)

def set_start_date(utc_start_date, start_hour, minutes_per_line, hours_per_chart):
    '''
    Sets the entries for the start year, month, day, hour, minutes
    per line, and hours per chart passed by the button commands above.
    '''
    helicorder_year.set(utc_start_date.year)
    helicorder_month.set(utc_start_date.month)
    helicorder_day.set(utc_start_date.day)
    helicorder_start_hour.set(start_hour)
    helicorder_minutes_per_line.set(minutes_per_line)
    helicorder_hours_per_chart.set(hours_per_chart)

#### Note: The Helicorder "Plot Chart" button command links directly to rscu_helicorder.plot_helicorder_chart()

# Seismogram

def seismogram_set_filter_state(event):
    '''
    Called by a "<<ComboboxSelected>>" bind event - when the user
    selects an item in the Filter Type combo box, this function is
    called. This function sets the available filter input field
    depending on the selected filter type:
      Type "none" = disable all filter input fields.
      Type "highpass" = enable minimum frequency, zero phase, and corners.
      Type "lowpass" = enable maximum frequency, zero phase, and corners.
      Types "bandpas" and "bandstop" = enable all input fields.
    :param str event: automatically generated by calling process, but ignored.
    '''
    if( verbose ):
        print('rscu_support.seismogram_set_filter_state')
    if(seismogram_filter_type.get().lower() == 'none'):
        seismogram_filter_max_state = 'disabled'
        seismogram_filter_min_state = 'disabled'
        seismogram_filter_zerophase_state = 'disabled'
        seismogram_filter_corners_state = 'disabled'
    elif(seismogram_filter_type.get().lower() == 'highpass'):
        seismogram_filter_max_state = 'disabled'
        seismogram_filter_min_state = 'normal'
        seismogram_filter_zerophase_state = 'normal'
        seismogram_filter_corners_state = 'normal'
    elif(seismogram_filter_type.get().lower() == 'lowpass'):
        seismogram_filter_max_state = 'normal'
        seismogram_filter_min_state = 'disabled'
        seismogram_filter_zerophase_state = 'normal'
        seismogram_filter_corners_state = 'normal'
    else:                                                               # "bandpas" or "bandstop" are what's left
        seismogram_filter_max_state = 'normal'
        seismogram_filter_min_state = 'normal'
        seismogram_filter_zerophase_state = 'normal'
        seismogram_filter_corners_state = 'normal'
    w.seismogram_filter_max_label.configure(state=seismogram_filter_max_state)
    w.seismogram_filter_max_entry.configure(state=seismogram_filter_max_state)
    w.seismogram_filter_max_Hz_label.configure(state=seismogram_filter_max_state)
    w.seismogram_filter_min_label.configure(state=seismogram_filter_min_state)
    w.seismogram_filter_min_entry.configure(state=seismogram_filter_min_state)
    w.seismogram_filter_min_Hz_label.configure(state=seismogram_filter_min_state)
    w.seismogram_filter_zerophase_check.configure(state=seismogram_filter_zerophase_state)
    w.seismogram_filter_corners_label.configure(state=seismogram_filter_corners_state)
    w.seismogram_filter_corners_entry.configure(state=seismogram_filter_corners_state)

#### Note: The Seismogram "Plot Chart" button command links directly to rscu_seismogram.plot_seismogram_chart()

# Spectrogram

#### Note: The Spectrogram "Plot Chart" button command links directly to rscu_spectrogram.plot_spectrogram_chart()

# Spectrograph

def spectrum_set_intensity_autoscale_options():
    '''
    Enables or disables the intensity (power) scale input fields
    based on the state of the "Auto Scale Intensity" check box. This
    function is called whenever the state of the check box is changed
    (when the user clicks on the check box).
    '''
    if( verbose ):
        print('rscu_support.spectrum_set_intensity_autoscale_options')
    if( spectrum_autoscale_intensity.get()):
        spectrum_intensity_scale_state = 'disabled'
    else:
        spectrum_intensity_scale_state = 'normal'
    w.spectrum_max_intensity_label.configure(state=spectrum_intensity_scale_state)
    w.spectrum_max_intensity_entry.configure(state=spectrum_intensity_scale_state)
    w.spectrum_min_intensity_label.configure(state=spectrum_intensity_scale_state)
    w.spectrum_min_intensity_entry.configure(state=spectrum_intensity_scale_state)

#### Note: The Spectrograph "Plot Chart" button command links directly to rscu_spectrograph.plot_spectrograph_chart()

# Phase Arrivals

def phase_to_phaselist(event=None):
    '''
    Copies the selected phase from the "Phases" list box the the
    "Phase List" entry field. This function is called either by
    selecting a phase in the "Phases" list box and then clicking on the
    "Phases to Phase List" button, or by double clicking on a phase in
    the "Phases" list box.
    :param str event: automatically generated by calling process, but ignored.
    '''
    if( verbose ):
        print('rscu_support.phase_to_phaselist')
    phase_list = arrival_phase_list.get().split(',')
    phase_list.append(w.arrival_phase_list.get(w.arrival_phase_list.curselection()))
    if( '' in phase_list ):                                             # If the Phase list entry field is initially blank, adding a phase results in two items in the list: A blank (zero length) item and the selected phase.
        phase_list.remove('')                                           #   Remove the initial blank item (if present) before copying phases to the phase list entry field.
    arrival_phase_list.set(','.join(phase_list))

#### Note: The Arrivals "Calculate Arrival Times and Plot Ray Path Diagram" button command links directly to rscu_arrival.plot_arrival_raypath()

# Initialize and close the main application window

def init(top, gui, *args, **kwargs):
    '''
    gui is the window instance which is mapped to the global name "w" which
    can be used to configure widgets as "w.widget.configure(param=value)"
    '''
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function to close the window.
    global top_level
    top_level.destroy()
    top_level = None
    plt.close('all')


if __name__ == '__main__':
    import rscu
    rscu.vp_start_gui()
