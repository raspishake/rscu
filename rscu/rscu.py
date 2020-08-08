#! /usr/bin/python3
#  -*- coding: utf-8 -*-
#
# GUI module template generated using PAGE version 5.2
#  in conjunction with Tcl version 8.6

import tkinter as tk
import tkinter.ttk as ttk

from rscu import rscu_support
from rscu import rscu_settings
from rscu import rscu_helicorder
from rscu import rscu_seismogram
from rscu import rscu_spectrogram
from rscu import rscu_spectrograph
from rscu import rscu_arrival
from rscu import rscu_validate

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    settings = rscu_settings.init_settings()
    global val, w, root
    root = tk.Tk()
    rscu_support.set_Tk_var()
    top = rscu_toplevel (root)
    rscu_support.init(root, top)
    root.mainloop()

w = None

def destroy_rscu_toplevel():
    global w
    w.destroy()
    w = None

class rscu_toplevel:
    def __init__(self, top=None):
        '''
        This class configures and populates the toplevel window.
        top is the toplevel containing window.
        '''
        self.style = ttk.Style()

        top.geometry(str(880+rscu_support.x_offset)+"x"+str(690+rscu_support.y_offset) + "+20+60")
        top.resizable(0, 0)
        top.title("Raspberry Shake Charting Utility")
        top.configure(highlightcolor="black")

#
# Menu Bar
#

        self.main_menubar = tk.Menu(top)
        top.configure(menu = self.main_menubar)

        self.main_menu_rscu = tk.Menu(top,tearoff=0)
        self.main_menubar.add_cascade(menu=self.main_menu_rscu, label="RSCU")
        self.main_menu_rscu.add_command(command=rscu_support.main_menu_about, label="About RSCU…")
        self.main_menu_rscu.add_separator()
        self.sub_pref_menu = tk.Menu(top,tearoff=0)
        self.main_menu_rscu.add_cascade(menu=self.sub_pref_menu, label="Preferences")
        self.sub_pref_menu.add_command(command=rscu_settings.main_menu_save_prefs, label="Save Preferences")
        self.sub_pref_menu.add_command(command=rscu_settings.main_menu_restore_prefs, label="Restore Saved Preferences")
        self.sub_pref_menu.add_command(command=rscu_settings.main_menu_reset_defaults, label="Reset Default Preferences")
        self.main_menu_rscu.add_separator()
        self.main_menu_rscu.add_command(command=rscu_support.destroy_window, label="Quit", accelerator="Ctrl+Q")
        top.bind("<Control-q>", lambda e: rscu_support.destroy_window())

#
# Common Data Frame
#

        self.common_data_frame = tk.Frame(top)
        self.common_data_frame.place(x=0, y=0, height=160, width=(880+rscu_support.x_offset))
        self.common_data_frame.configure(relief='groove')
        self.common_data_frame.configure(borderwidth="2")

        self.station_label = tk.Label(self.common_data_frame)
        self.station_label.place(x=(10+rscu_support.y_offset), y=15,  height=20, width=59)  # The offset is in the x direction, but it just happens to be the same as the y_offset value
        self.station_label.configure(anchor='w')
        self.station_label.configure(text='''Station:''')

        self.station_entry = tk.Entry(self.common_data_frame)
        self.station_entry.place(x=(75+rscu_support.y_offset), y=15, height=22, width=86)
        self.station_entry.configure(font="TkFixedFont")
        self.station_entry.configure(textvariable=rscu_support.rs_station)

        self.location_label = tk.Label(self.common_data_frame)
        self.location_label.place(x=(240+rscu_support.y_offset), y=15,  height=20, width=64)
        self.location_label.configure(text='''Location:''')

        self.latitude_entry = tk.Entry(self.common_data_frame)
        self.latitude_entry.place(x=(310+rscu_support.y_offset), y=15, height=22, width=86)
        self.latitude_entry.configure(font="TkFixedFont")
        self.latitude_entry.configure(justify='right')
        self.latitude_entry.configure(textvariable=rscu_support.station_latitude)
        self.latitude_entry.configure(validate="key")
        validate_fp = self.latitude_entry.register(rscu_validate.validate_fp)
        self.latitude_entry.configure(validatecommand=(validate_fp,"%P"))

        self.latitude_label = tk.Label(self.common_data_frame)
        self.latitude_label.place(x=(400+rscu_support.y_offset), y=15,  height=20, width=59)
        self.latitude_label.configure(anchor='w')
        self.latitude_label.configure(text='''Latitude,''')

        self.longitude_entry = tk.Entry(self.common_data_frame)
        self.longitude_entry.place(x=(470+rscu_support.y_offset), y=15, height=22, width=86)
        self.longitude_entry.configure(font="TkFixedFont")
        self.longitude_entry.configure(justify='right')
        self.longitude_entry.configure(textvariable=rscu_support.station_longitude)
        self.longitude_entry.configure(validate="key")
        validate_fp = self.longitude_entry.register(rscu_validate.validate_fp)
        self.longitude_entry.configure(validatecommand=(validate_fp,"%P"))

        self.longitude_label = tk.Label(self.common_data_frame)
        self.longitude_label.place(x=(560+rscu_support.y_offset), y=15,  height=20, width=67)
        self.longitude_label.configure(anchor='w')
        self.longitude_label.configure(text='''Longitude''')

        self.wave_source_label = tk.Label(self.common_data_frame)
        self.wave_source_label.place(x=(10+rscu_support.y_offset), y=50,  height=20, width=99)
        self.wave_source_label.configure(anchor='w')
        self.wave_source_label.configure(text='''Wave Source:''')

        self.wave_source_button = tk.Button(self.common_data_frame)
        self.wave_source_button.place(x=(110+rscu_support.y_offset), y=45,  height=31, width=730)
        self.wave_source_button.configure(command=rscu_support.get_wave_source)
        self.wave_source_button.configure(text='''(protocol://)Wave_Source(:port)''')
        self.wave_source_button.configure(textvariable=rscu_support.wave_source_blabel)

        self.default_save_directory_label = tk.Label(self.common_data_frame)
        self.default_save_directory_label.place(x=(10+rscu_support.y_offset), y=85, height=20, width=198)
        self.default_save_directory_label.configure(anchor='w')
        self.default_save_directory_label.configure(text='''Default RSCU Save Directory:''')

        self.rscu_save_directory_button = tk.Button(self.common_data_frame)
        self.rscu_save_directory_button.place(x=(210+rscu_support.y_offset), y=80,  height=31, width=630)
        self.rscu_save_directory_button.configure(command=rscu_support.get_rscu_save_directory)
        self.rscu_save_directory_button.configure(text='''RSCU_Save_Directory''')
        self.rscu_save_directory_button.configure(textvariable=rscu_support.rscu_save_directory)

        self.chrt_size_label = tk.Label(self.common_data_frame)
        self.chrt_size_label.place(x=(10+rscu_support.y_offset), y=120,  height=20, width=188)
        self.chrt_size_label.configure(anchor='w')
        self.chrt_size_label.configure(text='''Default Chart Size (pixels):''')

        self.x_pixels_entry = tk.Entry(self.common_data_frame)
        self.x_pixels_entry.place(x=(205+rscu_support.y_offset), y=120, height=22, width=86)
        self.x_pixels_entry.configure(font="TkFixedFont")
        self.x_pixels_entry.configure(justify='right')
        self.x_pixels_entry.configure(textvariable=rscu_support.pixels_wide)
        self.x_pixels_entry.configure(validate="key")
        validate_int = self.x_pixels_entry.register(rscu_validate.validate_int)
        self.x_pixels_entry.configure(validatecommand=(validate_int,"%S"))

        self.x_pixels_label = tk.Label(self.common_data_frame)
        self.x_pixels_label.place(x=(300+rscu_support.y_offset), y=120,  height=20, width=108)
        self.x_pixels_label.configure(anchor='w')
        self.x_pixels_label.configure(text='''pixels wide, by''')

        self.y_pixels_entry = tk.Entry(self.common_data_frame)
        self.y_pixels_entry.place(x=(415+rscu_support.y_offset), y=120, height=22, width=86)
        self.y_pixels_entry.configure(font="TkFixedFont")
        self.y_pixels_entry.configure(justify='right')
        self.y_pixels_entry.configure(textvariable=rscu_support.pixels_tall)
        self.y_pixels_entry.configure(validate="key")
        validate_int = self.y_pixels_entry.register(rscu_validate.validate_int)
        self.y_pixels_entry.configure(validatecommand=(validate_int,"%S"))

        self.y_pixels_label = tk.Label(self.common_data_frame)
        self.y_pixels_label.place(x=(510+rscu_support.y_offset), y=120,  height=20, width=80)
        self.y_pixels_label.configure(anchor='w')
        self.y_pixels_label.configure(text='''pixels tall''')

#
# Chart Tabs Frame
#

        self.chart_types_frame = tk.Frame(top)
        self.chart_types_frame.place(x=0, y=160, height=(530+rscu_support.y_offset), width=(880+rscu_support.x_offset))
        self.chart_types_frame.configure(relief='groove')
        self.chart_types_frame.configure(borderwidth="2")

        self.chart_type_tabs = ttk.Notebook(self.chart_types_frame)
        self.chart_type_tabs.place(x=0, y=0, height=(526+rscu_support.y_offset), width=(876+rscu_support.x_offset))
        self.chart_type_helicorder_tabs_t1_1 = tk.Frame(self.chart_type_tabs)
        self.chart_type_tabs.add(self.chart_type_helicorder_tabs_t1_1, padding=3)
        self.chart_type_tabs.tab(0, text="Helicorder", compound="left",underline="-1", )
        self.chart_type_seismogram_tabs_t2_2 = tk.Frame(self.chart_type_tabs)
        self.chart_type_tabs.add(self.chart_type_seismogram_tabs_t2_2, padding=3)
        self.chart_type_tabs.tab(1, text="Seismogram", compound="left",underline="-1", )
        self.chart_type_spectrogram_tabs_t3_3 = tk.Frame(self.chart_type_tabs)
        self.chart_type_tabs.add(self.chart_type_spectrogram_tabs_t3_3, padding=3)
        self.chart_type_tabs.tab(2, text="Spectrogram", compound="none",underline="-1", )
        self.chart_type_spectrograph_tabs_t4_4 = tk.Frame(self.chart_type_tabs)
        self.chart_type_tabs.add(self.chart_type_spectrograph_tabs_t4_4, padding=3)
        self.chart_type_tabs.tab(3, text="Spectrograph", compound="none",underline="-1", )
        self.chart_type_arrivals_tabs_t5_5 = tk.Frame(self.chart_type_tabs)
        self.chart_type_tabs.add(self.chart_type_arrivals_tabs_t5_5, padding=3)
        self.chart_type_tabs.tab(4, text="Phase Arrivals", compound="none",underline="-1", )

#
# Helicorder Tab
#

        self.helicorder_channel_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_channel_label.place(x=30, y=30,  height=20, width=93)
        self.helicorder_channel_label.configure(anchor='w')
        self.helicorder_channel_label.configure(justify='left')
        self.helicorder_channel_label.configure(text='''Component:''')

        self.helicorder_channel_combo = ttk.Combobox(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_channel_combo.place(x=130, y=30, height=22, width=77)
        self.value_list = ['SHZ','EHZ','EHN','EHE','ENZ','ENN','ENE','HDF']
        self.helicorder_channel_combo.configure(values=self.value_list)
        self.helicorder_channel_combo.configure(textvariable=rscu_support.station_component)

        self.helicorder_line_minutes_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line_minutes_label.place(x=30, y=70, height=20, width=115)
        self.helicorder_line_minutes_label.configure(anchor='w')
        self.helicorder_line_minutes_label.configure(text='''Minutes per Line:''')

        self.helicorder_minute_per_line_combo = ttk.Combobox(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_minute_per_line_combo.place(x=150, y=70, height=22, width=56)
        self.value_list = ['10','15','30','60']
        self.helicorder_minute_per_line_combo.configure(values=self.value_list)
        self.helicorder_minute_per_line_combo.configure(textvariable=rscu_support.helicorder_minutes_per_line)
        self.helicorder_minute_per_line_combo.configure(validate="key")
        validate_int = self.helicorder_minute_per_line_combo.register(rscu_validate.validate_int)
        self.helicorder_minute_per_line_combo.configure(validatecommand=(validate_int,"%S"))

        self.helicorder_hours_per_chart_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_hours_per_chart_label.place(x=30, y=110, height=20, width=109)
        self.helicorder_hours_per_chart_label.configure(anchor='w')
        self.helicorder_hours_per_chart_label.configure(text='''Hours per Chart:''')

        self.helicorder_hours_per_chart_combo = ttk.Combobox(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_hours_per_chart_combo.place(x=150, y=110, height=22, width=56)
        self.value_list = ['4','6','12','24']
        self.helicorder_hours_per_chart_combo.configure(values=self.value_list)
        self.helicorder_hours_per_chart_combo.configure(textvariable=rscu_support.helicorder_hours_per_chart)
        self.helicorder_hours_per_chart_combo.configure(validate="key")
        validate_int = self.helicorder_hours_per_chart_combo.register(rscu_validate.validate_int)
        self.helicorder_hours_per_chart_combo.configure(validatecommand=(validate_int,"%S"))

        self.helicorder_auto_vertical_scaling_check = tk.Checkbutton(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_auto_vertical_scaling_check.place(x=20, y=150, height=23, width=180)
        self.helicorder_auto_vertical_scaling_check.configure(anchor='w')
        self.helicorder_auto_vertical_scaling_check.configure(command=rscu_support.helicorder_set_auto_vertical_scaling)
        self.helicorder_auto_vertical_scaling_check.configure(justify='left')
        self.helicorder_auto_vertical_scaling_check.configure(text='''Auto Vertical Scaling''')
        self.helicorder_auto_vertical_scaling_check.configure(variable=rscu_support.helicorder_auto_vertical_scaling)

        self.helicorder_vertical_scaling_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_vertical_scaling_label.place(x=30, y=190, height=21, width=112)
        self.helicorder_vertical_scaling_label.configure(anchor='w')
        self.helicorder_vertical_scaling_label.configure(state=rscu_support.helicorder_vertical_scaling_state)
        self.helicorder_vertical_scaling_label.configure(text='''Vertical Scaling:''')

        self.helicorder_vertical_scaling_entry = tk.Entry(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_vertical_scaling_entry.place(x=150, y=190, height=22, width=106)
        self.helicorder_vertical_scaling_entry.configure(font="TkFixedFont")
        self.helicorder_vertical_scaling_entry.configure(state=rscu_support.helicorder_vertical_scaling_state)
        self.helicorder_vertical_scaling_entry.configure(textvariable=rscu_support.helicorder_vertical_scaling)
        self.helicorder_vertical_scaling_entry.configure(validate="key")
        validate_fp = self.helicorder_vertical_scaling_entry.register(rscu_validate.validate_fp)
        self.helicorder_vertical_scaling_entry.configure(validatecommand=(validate_fp,"%P"))

        self.helicorder_line1_color_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line1_color_label.place(x=30, y=230, height=21, width=86)
        self.helicorder_line1_color_label.configure(anchor='w')
        self.helicorder_line1_color_label.configure(text='''Line 1 Color:''')

        self.helicorder_line1_color_entry = tk.Entry(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line1_color_entry.place(x=120, y=230, height=22, width=146)
        self.helicorder_line1_color_entry.configure(font="TkFixedFont")
        self.helicorder_line1_color_entry.configure(textvariable=rscu_support.helicorder_line1_color)
        self.helicorder_line1_color_entry.bind('<FocusOut>', rscu_support.helicorder_color_entry_line1)

        self.helicorder_line1_color_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line1_color_button.place(x=270, y=230, height=22, width=22)
        self.helicorder_line1_color_button.configure(background=rscu_support.helicorder_line1_color.get())
        if( rscu_support.macOS ):
            self.helicorder_line1_color_button.configure(highlightbackground=rscu_support.helicorder_line1_color.get())
            self.helicorder_line1_color_button.configure(highlightthickness=15)
        self.helicorder_line1_color_button.configure(command=rscu_support.helicorder_color_line1)

        self.helicorder_line2_color_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line2_color_label.place(x=30, y=260, height=21, width=86)
        self.helicorder_line2_color_label.configure(anchor='w')
        self.helicorder_line2_color_label.configure(text='''Line 2 Color:''')

        self.helicorder_line2_color_entry = tk.Entry(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line2_color_entry.place(x=120, y=260, height=22, width=146)
        self.helicorder_line2_color_entry.configure(font="TkFixedFont")
        self.helicorder_line2_color_entry.configure(textvariable=rscu_support.helicorder_line2_color)
        self.helicorder_line2_color_entry.bind('<FocusOut>', rscu_support.helicorder_color_entry_line2)

        self.helicorder_line2_color_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line2_color_button.place(x=270, y=260, height=22, width=22)
        self.helicorder_line2_color_button.configure(background=rscu_support.helicorder_line2_color.get())
        if( rscu_support.macOS ):
            self.helicorder_line2_color_button.configure(highlightbackground=rscu_support.helicorder_line2_color.get())
            self.helicorder_line2_color_button.configure(highlightthickness=15)
        self.helicorder_line2_color_button.configure(command=rscu_support.helicorder_color_line2)

        self.helicorder_line3_color_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line3_color_label.place(x=30, y=290, height=20, width=86)
        self.helicorder_line3_color_label.configure(anchor='w')
        self.helicorder_line3_color_label.configure(text='''Line 3 Color:''')

        self.helicorder_line3_color_entry = tk.Entry(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line3_color_entry.place(x=120, y=290, height=22, width=146)
        self.helicorder_line3_color_entry.configure(font="TkFixedFont")
        self.helicorder_line3_color_entry.configure(textvariable=rscu_support.helicorder_line3_color)
        self.helicorder_line3_color_entry.bind('<FocusOut>', rscu_support.helicorder_color_entry_line3)

        self.helicorder_line3_color_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line3_color_button.place(x=270, y=290, height=22, width=22)
        self.helicorder_line3_color_button.configure(background=rscu_support.helicorder_line3_color.get())
        if( rscu_support.macOS ):
            self.helicorder_line3_color_button.configure(highlightbackground=rscu_support.helicorder_line3_color.get())
            self.helicorder_line3_color_button.configure(highlightthickness=15)
        self.helicorder_line3_color_button.configure(command=rscu_support.helicorder_color_line3)

        self.helicorder_line4_lcolor_abel = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line4_lcolor_abel.place(x=30, y=320, height=20, width=86)
        self.helicorder_line4_lcolor_abel.configure(anchor='w')
        self.helicorder_line4_lcolor_abel.configure(text='''Line 4 Color:''')

        self.helicorder_line4_color_entry = tk.Entry(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line4_color_entry.place(x=120, y=320, height=22, width=146)
        self.helicorder_line4_color_entry.configure(font="TkFixedFont")
        self.helicorder_line4_color_entry.configure(textvariable=rscu_support.helicorder_line4_color)
        self.helicorder_line4_color_entry.bind('<FocusOut>', rscu_support.helicorder_color_entry_line4)

        self.helicorder_line4_color_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_line4_color_button.place(x=270, y=320, height=22, width=22)
        self.helicorder_line4_color_button.configure(background=rscu_support.helicorder_line4_color.get())
        if( rscu_support.macOS ):
            self.helicorder_line4_color_button.configure(highlightbackground=rscu_support.helicorder_line4_color.get())
            self.helicorder_line4_color_button.configure(highlightthickness=15)
        self.helicorder_line4_color_button.configure(command=rscu_support.helicorder_color_line4)

        self.helicorder_date_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_date_label.place(x=380, y=30,  height=20, width=180)
        self.helicorder_date_label.configure(anchor='w')
        self.helicorder_date_label.configure(justify='left')
        self.helicorder_date_label.configure(text='''Date (yyyy-mm-dd, UTC):''')

        self.helicorder_year_spin = tk.Spinbox(self.chart_type_helicorder_tabs_t1_1, from_=2018, to=2030, increment=1)
        self.helicorder_year_spin.place(x=560, y=30, height=22, width=56)
        self.helicorder_year_spin.configure(font="TkDefaultFont")
        self.helicorder_year_spin.configure(justify='right')
        self.helicorder_year_spin.configure(textvariable=rscu_support.helicorder_year)
        self.helicorder_year_spin.configure(validate="key")
        validate_int = self.helicorder_year_spin.register(rscu_validate.validate_int)
        self.helicorder_year_spin.configure(validatecommand=(validate_int,"%S"))

        self.helicorder_month_spin = tk.Spinbox(self.chart_type_helicorder_tabs_t1_1, from_=1, to=12, increment=1)
        self.helicorder_month_spin.place(x=620, y=30, height=22, width=36)
        self.helicorder_month_spin.configure(font="TkDefaultFont")
        self.helicorder_month_spin.configure(justify='right')
        self.helicorder_month_spin.configure(wrap=True)
        self.helicorder_month_spin.configure(textvariable=rscu_support.helicorder_month)
        self.helicorder_month_spin.configure(validate="key")
        validate_int = self.helicorder_month_spin.register(rscu_validate.validate_int)
        self.helicorder_month_spin.configure(validatecommand=(validate_int,"%S"))

        self.helicorder_day_spin = tk.Spinbox(self.chart_type_helicorder_tabs_t1_1, from_=1, to=31, increment=1)
        self.helicorder_day_spin.place(x=660, y=30, height=22, width=36)
        self.helicorder_day_spin.configure(font="TkDefaultFont")
        self.helicorder_day_spin.configure(justify='right')
        self.helicorder_day_spin.configure(wrap=True)
        self.helicorder_day_spin.configure(textvariable=rscu_support.helicorder_day)
        self.helicorder_day_spin.configure(validate="key")
        validate_int = self.helicorder_day_spin.register(rscu_validate.validate_int)
        self.helicorder_day_spin.configure(validatecommand=(validate_int,"%S"))

        self.helicorder_start_hour_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_start_hour_label.place(x=710, y=30, height=20, width=78)
        self.helicorder_start_hour_label.configure(anchor='w')
        self.helicorder_start_hour_label.configure(text='''Start Hour:''')

        self.helicorder_start_hour_spin = tk.Spinbox(self.chart_type_helicorder_tabs_t1_1, from_=0.00, to=23.75, increment=0.25, format='%0.2f', wrap=True)
        self.helicorder_start_hour_spin.place(x=790, y=30, height=23, width=56)
        self.helicorder_start_hour_spin.configure(font="TkDefaultFont")
        self.helicorder_start_hour_spin.configure(justify='right')
        self.helicorder_start_hour_spin.configure(wrap=True)
        self.helicorder_start_hour_spin.configure(textvariable=rscu_support.helicorder_start_hour)
        self.helicorder_start_hour_spin.configure(validate="key")
        validate_fp = self.helicorder_start_hour_spin.register(rscu_validate.validate_fp)
        self.helicorder_start_hour_spin.configure(validatecommand=(validate_fp,"%P"))

        self.helicorder_date_today_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_date_today_button.place(x=380, y=60, height=31, width=215)
        self.helicorder_date_today_button.configure(command=rscu_support.set_current_date)
        self.helicorder_date_today_button.configure(text='''Set to Current UTC Date''')

        self.helicorder_date_yesterdat_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_date_yesterdat_button.place(x=615, y=60, height=31, width=215)
        self.helicorder_date_yesterdat_button.configure(command=rscu_support.set_last_full_date)
        self.helicorder_date_yesterdat_button.configure(text='''Set to Last Full UTC Date''')

        self.helicorder_last_24_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_last_24_button.place(x=380, y=100, height=31, width=215)
        self.helicorder_last_24_button.configure(command=rscu_support.set_last_24h)
        self.helicorder_last_24_button.configure(text='''Set to Last 24 Hours''')

        self.helicorder_last_12_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_last_12_button.place(x=615, y=100, height=31, width=215)
        self.helicorder_last_12_button.configure(command=rscu_support.set_last_12h)
        self.helicorder_last_12_button.configure(text='''Set to Last 12 Hours''')

        self.helicorder_chart_title_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_chart_title_label.place(x=380, y=160, height=20, width=75)
        self.helicorder_chart_title_label.configure(anchor='w')
        self.helicorder_chart_title_label.configure(text='''Chart Title:''')

        self.helicorder_chart_title_entry = tk.Entry(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_chart_title_entry.place(x=380, y=180, height=22, width=466)
        self.helicorder_chart_title_entry.configure(font="TkFixedFont")
        self.helicorder_chart_title_entry.configure(textvariable=rscu_support.helicorder_chart_title)

        self.helicorder_autosave_check = tk.Checkbutton(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_autosave_check.place(x=370, y=220, height=22, width=190)
        self.helicorder_autosave_check.configure(anchor='w')
        self.helicorder_autosave_check.configure(justify='left')
        self.helicorder_autosave_check.configure(text='''Auto Save Chart to File''')
        self.helicorder_autosave_check.configure(variable=rscu_support.chart_autosave)

        self.helicorder_chart_filename_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_chart_filename_label.place(x=380, y=250, height=20, width=114)
        self.helicorder_chart_filename_label.configure(anchor='w')
        self.helicorder_chart_filename_label.configure(text='''Chart File Name:''')

        self.helicorder_chart_filename_entry = tk.Entry(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_chart_filename_entry.place(x=378, y=270, height=22, width=466)
        self.helicorder_chart_filename_entry.configure(font="TkFixedFont")
        self.helicorder_chart_filename_entry.configure(textvariable=rscu_support.helicorder_chart_filename)

        self.helicorder_chart_format_label = tk.Label(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_chart_format_label.place(x=380, y=300, height=20, width=121)
        self.helicorder_chart_format_label.configure(text='''Chart File Format:''')

        x_val = 280
        if( 'png' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.helicorder_chart_format_png_radio = tk.Radiobutton(self.chart_type_helicorder_tabs_t1_1)
            self.helicorder_chart_format_png_radio.place(x=x_val, y=320, height=22, width=60)
            self.helicorder_chart_format_png_radio.configure(anchor='w')
            self.helicorder_chart_format_png_radio.configure(justify='left')
            self.helicorder_chart_format_png_radio.configure(text='''.png''')
            self.helicorder_chart_format_png_radio.configure(value="png")
            self.helicorder_chart_format_png_radio.configure(variable=rscu_support.chart_format)

        if( 'svg' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.helicorder_chart_format_svg_radio = tk.Radiobutton(self.chart_type_helicorder_tabs_t1_1)
            self.helicorder_chart_format_svg_radio.place(x=x_val, y=320, height=22, width=65)
            self.helicorder_chart_format_svg_radio.configure(anchor='w')
            self.helicorder_chart_format_svg_radio.configure(justify='left')
            self.helicorder_chart_format_svg_radio.configure(text='''.svg''')
            self.helicorder_chart_format_svg_radio.configure(value="svg")
            self.helicorder_chart_format_svg_radio.configure(variable=rscu_support.chart_format)

        if( 'pdf' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.helicorder_chart_format_pdf_radio = tk.Radiobutton(self.chart_type_helicorder_tabs_t1_1)
            self.helicorder_chart_format_pdf_radio.place(x=x_val, y=320, height=22, width=60)
            self.helicorder_chart_format_pdf_radio.configure(anchor='w')
            self.helicorder_chart_format_pdf_radio.configure(justify='left')
            self.helicorder_chart_format_pdf_radio.configure(text='''.pdf''')
            self.helicorder_chart_format_pdf_radio.configure(value="pdf")
            self.helicorder_chart_format_pdf_radio.configure(variable=rscu_support.chart_format)

        if( 'jpg' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.helicorder_chart_format_jpg_radio = tk.Radiobutton(self.chart_type_helicorder_tabs_t1_1)
            self.helicorder_chart_format_jpg_radio.place(x=x_val, y=320, height=22, width=60)
            self.helicorder_chart_format_jpg_radio.configure(anchor='w')
            self.helicorder_chart_format_jpg_radio.configure(justify='left')
            self.helicorder_chart_format_jpg_radio.configure(text='''.jpg''')
            self.helicorder_chart_format_jpg_radio.configure(value="jpg")
            self.helicorder_chart_format_jpg_radio.configure(variable=rscu_support.chart_format)

        self.helicorder_plot_chart_button = tk.Button(self.chart_type_helicorder_tabs_t1_1)
        self.helicorder_plot_chart_button.place(x=390, y=440, height=31, width=100)
        self.helicorder_plot_chart_button.configure(command=rscu_helicorder.plot_helicorder_chart)
        self.helicorder_plot_chart_button.configure(text='''Plot Chart''')

#
# Seismogram Tab
#

        self.seismogram_channel_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_channel_label.place(x=30, y=30,  height=20, width=93)
        self.seismogram_channel_label.configure(anchor='w')
        self.seismogram_channel_label.configure(text='''Component:''')

        self.seismogram_channel_combo = ttk.Combobox(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_channel_combo.place(x=130, y=30, height=22, width=77)
        self.value_list = ['SHZ','SH?','EHZ','EHN','EHE','EH?','ENZ','ENN','ENE','EN?','E??','HDF','HD?']
        self.seismogram_channel_combo.configure(values=self.value_list)
        self.seismogram_channel_combo.configure(textvariable=rscu_support.seismogram_component)

        self.seismogram_filter_lable = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_lable.place(x=30, y=70,  height=20, width=132)
        self.seismogram_filter_lable.configure(anchor='w')
        self.seismogram_filter_lable.configure(text='''Butterworth Filter:''')

        self.seismogram_filter_combo = ttk.Combobox(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_combo.place(x=30, y=100, height=22, width=232)
        self.value_list = ['none','highpass','lowpass','bandpass','bandstop']
        self.seismogram_filter_combo.configure(values=self.value_list)
        self.seismogram_filter_combo.configure(textvariable=rscu_support.seismogram_filter_type)
        self.seismogram_filter_combo.bind('<<ComboboxSelected>>', rscu_support.seismogram_set_filter_state)

        self.seismogram_filter_max_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_max_label.place(x=30, y=140, height=20, width=146)
        self.seismogram_filter_max_label.configure(anchor='w')
        if(rscu_support.seismogram_filter_type.get() in ['none','highpass']):
            rscu_support.seismogram_filter_max_state = 'disabled'
        else:
            rscu_support.seismogram_filter_max_state = 'normal'
        self.seismogram_filter_max_label.configure(state=rscu_support.seismogram_filter_max_state)
        self.seismogram_filter_max_label.configure(text='''Maximum Frequency:''')

        self.seismogram_filter_max_entry = tk.Entry(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_max_entry.place(x=180, y=140, height=22, width=86)
        self.seismogram_filter_max_entry.configure(font="TkFixedFont")
        self.seismogram_filter_max_entry.configure(justify='right')
        self.seismogram_filter_max_entry.configure(state=rscu_support.seismogram_filter_max_state)
        self.seismogram_filter_max_entry.configure(textvariable=rscu_support.seismogram_filter_max_frequency)
        self.seismogram_filter_max_entry.configure(validate="key")
        validate_fp = self.seismogram_filter_max_entry.register(rscu_validate.validate_fp)
        self.seismogram_filter_max_entry.configure(validatecommand=(validate_fp,"%P"))

        self.seismogram_filter_max_Hz_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_max_Hz_label.place(x=270, y=140, height=20, width=21)
        self.seismogram_filter_max_Hz_label.configure(anchor='w')
        self.seismogram_filter_max_Hz_label.configure(state=rscu_support.seismogram_filter_max_state)
        self.seismogram_filter_max_Hz_label.configure(text='''Hz''')

        self.seismogram_filter_min_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_min_label.place(x=30, y=180, height=20, width=144)
        self.seismogram_filter_min_label.configure(anchor='w')
        if(rscu_support.seismogram_filter_type.get() in ['none','lowpass']):
            rscu_support.seismogram_filter_min_state = 'disabled'
        else:
            rscu_support.seismogram_filter_min_state = 'normal'            
        self.seismogram_filter_min_label.configure(state=rscu_support.seismogram_filter_min_state)
        self.seismogram_filter_min_label.configure(text='''Minimum Frequency:''')

        self.seismogram_filter_min_entry = tk.Entry(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_min_entry.place(x=180, y=180, height=22, width=86)
        self.seismogram_filter_min_entry.configure(font="TkFixedFont")
        self.seismogram_filter_min_entry.configure(justify='right')
        self.seismogram_filter_min_entry.configure(state=rscu_support.seismogram_filter_min_state)
        self.seismogram_filter_min_entry.configure(textvariable=rscu_support.seismogram_filter_min_frequency)
        self.seismogram_filter_min_entry.configure(validate="key")
        validate_fp = self.seismogram_filter_min_entry.register(rscu_validate.validate_fp)
        self.seismogram_filter_min_entry.configure(validatecommand=(validate_fp,"%P"))

        self.seismogram_filter_min_Hz_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_min_Hz_label.place(x=270, y=180, height=20, width=21)
        self.seismogram_filter_min_Hz_label.configure(anchor='w')
        self.seismogram_filter_min_Hz_label.configure(state=rscu_support.seismogram_filter_min_state)
        self.seismogram_filter_min_Hz_label.configure(text='''Hz''')

        self.seismogram_filter_zerophase_check = tk.Checkbutton(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_zerophase_check.place(x=20, y=220, height=22, width=150)
        self.seismogram_filter_zerophase_check.configure(anchor='w')
        self.seismogram_filter_zerophase_check.configure(justify='left')
        if(rscu_support.seismogram_filter_type.get() == 'none'):
            rscu_support.seismogram_filter_zerophase_state = 'disabled'
        else:
            rscu_support.seismogram_filter_zerophase_state = 'normal'            
        self.seismogram_filter_zerophase_check.configure(state=rscu_support.seismogram_filter_zerophase_state)
        self.seismogram_filter_zerophase_check.configure(text='''Zero Phase Shift''')
        self.seismogram_filter_zerophase_check.configure(variable=rscu_support.seismogram_filter_zerophase)

        self.seismogram_filter_corners_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_corners_label.place(x=30, y=260, height=20, width=58)
        self.seismogram_filter_corners_label.configure(anchor='w')
        if(rscu_support.seismogram_filter_type.get() == 'none'):
            rscu_support.seismogram_filter_corners_state = 'disabled'
        else:
            rscu_support.seismogram_filter_corners_state = 'normal'            
        self.seismogram_filter_corners_label.configure(state=rscu_support.seismogram_filter_corners_state)
        self.seismogram_filter_corners_label.configure(text='''Corners:''')

        self.seismogram_filter_corners_entry = tk.Entry(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_filter_corners_entry.place(x=90, y=260, height=22, width=36)
        self.seismogram_filter_corners_entry.configure(font="TkFixedFont")
        self.seismogram_filter_corners_entry.configure(state=rscu_support.seismogram_filter_corners_state)
        self.seismogram_filter_corners_entry.configure(textvariable=rscu_support.seismogram_filter_corners)
        self.seismogram_filter_corners_entry.configure(validate="key")
        validate_int = self.seismogram_filter_corners_entry.register(rscu_validate.validate_int)
        self.seismogram_filter_corners_entry.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_date_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_date_label.place(x=380, y=30,  height=20, width=141)
        self.seismogram_date_label.configure(anchor='w')
        self.seismogram_date_label.configure(justify='left')
        self.seismogram_date_label.configure(text='''Date and Time (UTC):''')

        self.seismogram_year_spin = tk.Spinbox(self.chart_type_seismogram_tabs_t2_2, from_=2018, to=2030, increment=1)
        self.seismogram_year_spin.place(x=530, y=30, height=22, width=56)
        self.seismogram_year_spin.configure(font="TkDefaultFont")
        self.seismogram_year_spin.configure(justify='right')
        self.seismogram_year_spin.configure(textvariable=rscu_support.start_year)
        self.seismogram_year_spin.configure(validate="key")
        validate_int = self.seismogram_year_spin.register(rscu_validate.validate_int)
        self.seismogram_year_spin.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_month_spin = tk.Spinbox(self.chart_type_seismogram_tabs_t2_2, from_=1, to=12, increment=1)
        self.seismogram_month_spin.place(x=590, y=30, height=22, width=36)
        self.seismogram_month_spin.configure(font="TkDefaultFont")
        self.seismogram_month_spin.configure(justify='right')
        self.seismogram_month_spin.configure(wrap=True)
        self.seismogram_month_spin.configure(textvariable=rscu_support.start_month)
        self.seismogram_month_spin.configure(validate="key")
        validate_int = self.seismogram_month_spin.register(rscu_validate.validate_int)
        self.seismogram_month_spin.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_day_spin = tk.Spinbox(self.chart_type_seismogram_tabs_t2_2, from_=1, to=31, increment=1)
        self.seismogram_day_spin.place(x=630, y=30, height=22, width=36)
        self.seismogram_day_spin.configure(font="TkDefaultFont")
        self.seismogram_day_spin.configure(justify='right')
        self.seismogram_day_spin.configure(wrap=True)
        self.seismogram_day_spin.configure(textvariable=rscu_support.start_day)
        self.seismogram_day_spin.configure(validate="key")
        validate_int = self.seismogram_day_spin.register(rscu_validate.validate_int)
        self.seismogram_day_spin.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_hour_spin = tk.Spinbox(self.chart_type_seismogram_tabs_t2_2, from_=0, to=23, increment=1)
        self.seismogram_hour_spin.place(x=680, y=30, height=22, width=36)
        self.seismogram_hour_spin.configure(font="TkDefaultFont")
        self.seismogram_hour_spin.configure(justify='right')
        self.seismogram_hour_spin.configure(wrap=True)
        self.seismogram_hour_spin.configure(textvariable=rscu_support.start_hour)
        self.seismogram_hour_spin.configure(validate="key")
        validate_int = self.seismogram_hour_spin.register(rscu_validate.validate_int)
        self.seismogram_hour_spin.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_minute_spin = tk.Spinbox(self.chart_type_seismogram_tabs_t2_2, from_=0, to=59, increment=1)
        self.seismogram_minute_spin.place(x=720, y=30, height=22, width=36)
        self.seismogram_minute_spin.configure(font="TkDefaultFont")
        self.seismogram_minute_spin.configure(justify='right')
        self.seismogram_minute_spin.configure(wrap=True)
        self.seismogram_minute_spin.configure(textvariable=rscu_support.start_minute)
        self.seismogram_minute_spin.configure(validate="key")
        validate_int = self.seismogram_minute_spin.register(rscu_validate.validate_int)
        self.seismogram_minute_spin.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_seconds_spin = tk.Spinbox(self.chart_type_seismogram_tabs_t2_2, from_=0, to=59, increment=1)
        self.seismogram_seconds_spin.place(x=760, y=30, height=22, width=36)
        self.seismogram_seconds_spin.configure(font="TkDefaultFont")
        self.seismogram_seconds_spin.configure(justify='right')
        self.seismogram_seconds_spin.configure(wrap=True)
        self.seismogram_seconds_spin.configure(textvariable=rscu_support.start_second)
        self.seismogram_seconds_spin.configure(validate="key")
        validate_int = self.seismogram_seconds_spin.register(rscu_validate.validate_int)
        self.seismogram_seconds_spin.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_year_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_year_label.place(x=535, y=50,  height=21, width=36)
        self.seismogram_year_label.configure(text='''yyyy''')

        self.seismogram_month_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_month_label.place(x=590, y=50,  height=21, width=30)
        self.seismogram_month_label.configure(text='''mm''')

        self.seismogram_day_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_day_label.place(x=635, y=50,  height=21, width=21)
        self.seismogram_day_label.configure(text='''dd''')

        self.seismogram_hour_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_hour_label.place(x=685, y=50,  height=20, width=20)
        self.seismogram_hour_label.configure(anchor='w')
        self.seismogram_hour_label.configure(text='''hh''')

        self.seismogram_minute_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_minute_label.place(x=720, y=50,  height=20, width=30)
        self.seismogram_minute_label.configure(anchor='w')
        self.seismogram_minute_label.configure(text='''mm''')

        self.seismogram_second_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_second_label.place(x=765, y=50,  height=20, width=16)
        self.seismogram_second_label.configure(anchor='w')
        self.seismogram_second_label.configure(text='''ss''')

        self.seismogram_duration_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_duration_label.place(x=380, y=80,  height=20, width=64)
        self.seismogram_duration_label.configure(anchor='w')
        self.seismogram_duration_label.configure(text='''Duration:''')

        self.seismogram_duration_entry = tk.Entry(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_duration_entry.place(x=450, y=80, height=22, width=96)
        self.seismogram_duration_entry.configure(font="TkFixedFont")
        self.seismogram_duration_entry.configure(justify='right')
        self.seismogram_duration_entry.configure(textvariable=rscu_support.duration)
        self.seismogram_duration_entry.configure(validate="key")
        validate_int = self.seismogram_duration_entry.register(rscu_validate.validate_int)
        self.seismogram_duration_entry.configure(validatecommand=(validate_int,"%S"))

        self.seismogram_duration_label2 = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_duration_label2.place(x=550, y=80, height=20, width=58)
        self.seismogram_duration_label2.configure(anchor='w')
        self.seismogram_duration_label2.configure(text='''seconds''')

        self.seismogram_chart_title_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_chart_title_label.place(x=380, y=120, height=20, width=75)
        self.seismogram_chart_title_label.configure(anchor='w')
        self.seismogram_chart_title_label.configure(text='''Chart Title:''')
        self.seismogram_chart_title_label.configure(state='disabled')

        self.seismogram_chart_title_entry = tk.Entry(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_chart_title_entry.place(x=380, y=140, height=22, width=466)
        self.seismogram_chart_title_entry.configure(font="TkFixedFont")
        self.seismogram_chart_title_entry.configure(textvariable=rscu_support.seismogram_chart_title)
        self.seismogram_chart_title_entry.configure(state='disabled')

        self.seismogram_autosave_check = tk.Checkbutton(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_autosave_check.place(x=370, y=180, height=20, width=190)
        self.seismogram_autosave_check.configure(anchor='w')
        self.seismogram_autosave_check.configure(justify='left')
        self.seismogram_autosave_check.configure(text='''Auto Save Chart to File''')
        self.seismogram_autosave_check.configure(variable=rscu_support.chart_autosave)

        self.seismogram_chart_filename_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_chart_filename_label.place(x=380, y=210, height=20, width=114)
        self.seismogram_chart_filename_label.configure(anchor='w')
        self.seismogram_chart_filename_label.configure(text='''Chart File Name:''')

        self.seismogram_chart_filename_entry = tk.Entry(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_chart_filename_entry.place(x=380, y=230, height=22, width=466)
        self.seismogram_chart_filename_entry.configure(font="TkFixedFont")
        self.seismogram_chart_filename_entry.configure(textvariable=rscu_support.seismogram_chart_filename)

        self.seismogram_chart_format_label = tk.Label(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_chart_format_label.place(x=380, y=260, height=20, width=121)
        self.seismogram_chart_format_label.configure(anchor='w')
        self.seismogram_chart_format_label.configure(text='''Chart File Format:''')

        x_val = 280
        if( 'png' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.seismogram_chart_format_png_radio = tk.Radiobutton(self.chart_type_seismogram_tabs_t2_2)
            self.seismogram_chart_format_png_radio.place(x=x_val, y=280, height=22, width=60)
            self.seismogram_chart_format_png_radio.configure(anchor='w')
            self.seismogram_chart_format_png_radio.configure(justify='left')
            self.seismogram_chart_format_png_radio.configure(text='''.png''')
            self.seismogram_chart_format_png_radio.configure(value="png")
            self.seismogram_chart_format_png_radio.configure(variable=rscu_support.chart_format)

        if( 'svg' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.seismogram_chart_format_svg_radio = tk.Radiobutton(self.chart_type_seismogram_tabs_t2_2)
            self.seismogram_chart_format_svg_radio.place(x=x_val, y=280, height=22, width=65)
            self.seismogram_chart_format_svg_radio.configure(anchor='w')
            self.seismogram_chart_format_svg_radio.configure(justify='left')
            self.seismogram_chart_format_svg_radio.configure(text='''.svg''')
            self.seismogram_chart_format_svg_radio.configure(value="svg")
            self.seismogram_chart_format_svg_radio.configure(variable=rscu_support.chart_format)

        if( 'pdf' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.seismogram_chart_format_pdf_radio = tk.Radiobutton(self.chart_type_seismogram_tabs_t2_2)
            self.seismogram_chart_format_pdf_radio.place(x=x_val, y=280, height=22, width=60)
            self.seismogram_chart_format_pdf_radio.configure(anchor='w')
            self.seismogram_chart_format_pdf_radio.configure(justify='left')
            self.seismogram_chart_format_pdf_radio.configure(text='''.pdf''')
            self.seismogram_chart_format_pdf_radio.configure(value="pdf")
            self.seismogram_chart_format_pdf_radio.configure(variable=rscu_support.chart_format)

        if( 'jpg' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.seismogram_chart_formant_jpg_radio = tk.Radiobutton(self.chart_type_seismogram_tabs_t2_2)
            self.seismogram_chart_formant_jpg_radio.place(x=x_val, y=280, height=22, width=60)
            self.seismogram_chart_formant_jpg_radio.configure(anchor='w')
            self.seismogram_chart_formant_jpg_radio.configure(justify='left')
            self.seismogram_chart_formant_jpg_radio.configure(text='''.jpg''')
            self.seismogram_chart_formant_jpg_radio.configure(value="jpg")
            self.seismogram_chart_formant_jpg_radio.configure(variable=rscu_support.chart_format)

        self.seismogram_plot_chart_button = tk.Button(self.chart_type_seismogram_tabs_t2_2)
        self.seismogram_plot_chart_button.place(x=390, y=440, height=31, width=100)
        self.seismogram_plot_chart_button.configure(command=rscu_seismogram.plot_seismogram_chart)
        self.seismogram_plot_chart_button.configure(text='''Plot Chart''')

#
# Spectrogram Tab
#

        self.spectrogram_channel_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_channel_label.place(x=30, y=30,  height=20, width=82)
        self.spectrogram_channel_label.configure(anchor='w')
        self.spectrogram_channel_label.configure(text='''Component:''')

        self.spectrogram_channel_combo = ttk.Combobox(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_channel_combo.place(x=130, y=30, height=22, width=77)
        self.value_list = ['SHZ','EHZ','EHN','EHE','ENZ','ENN','ENE','HDF',]
        self.spectrogram_channel_combo.configure(values=self.value_list)
        self.spectrogram_channel_combo.configure(textvariable=rscu_support.station_component)

        self.spectrogram_max_frequency_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_max_frequency_label.place(x=30, y=70, height=20, width=141)
        self.spectrogram_max_frequency_label.configure(anchor='w')
        self.spectrogram_max_frequency_label.configure(text='''Maximum Frequency:''')

        self.spectrogram_max_frequency_entry = tk.Entry(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_max_frequency_entry.place(x=180, y=70, height=22, width=86)
        self.spectrogram_max_frequency_entry.configure(font="TkFixedFont")
        self.spectrogram_max_frequency_entry.configure(justify='right')
        self.spectrogram_max_frequency_entry.configure(textvariable=rscu_support.spectrogram_max_frequency)
        self.spectrogram_max_frequency_entry.configure(validate="key")
        validate_fp = self.spectrogram_max_frequency_entry.register(rscu_validate.validate_fp)
        self.spectrogram_max_frequency_entry.configure(validatecommand=(validate_fp,"%P"))

        self.spectrogram_max_frequency_label2 = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_max_frequency_label2.place(x=270, y=70, height=20, width=21)
        self.spectrogram_max_frequency_label2.configure(anchor='w')
        self.spectrogram_max_frequency_label2.configure(text='''Hz''')

        self.spectrogram_min_frequency_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_min_frequency_label.place(x=30, y=110, height=20, width=145)
        self.spectrogram_min_frequency_label.configure(anchor='w')
        self.spectrogram_min_frequency_label.configure(text='''Minimum Frequency:''')

        self.spectrogram_min_frequency_entry = tk.Entry(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_min_frequency_entry.place(x=180, y=110, height=22, width=86)
        self.spectrogram_min_frequency_entry.configure(font="TkFixedFont")
        self.spectrogram_min_frequency_entry.configure(justify='right')
        self.spectrogram_min_frequency_entry.configure(textvariable=rscu_support.spectrogram_min_frequency)
        self.spectrogram_min_frequency_entry.configure(validate="key")
        validate_fp = self.spectrogram_min_frequency_entry.register(rscu_validate.validate_fp)
        self.spectrogram_min_frequency_entry.configure(validatecommand=(validate_fp,"%P"))

        self.spectrogram_min_frequency_label2 = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_min_frequency_label2.place(x=270, y=110, height=20, width=21)
        self.spectrogram_min_frequency_label2.configure(anchor='w')
        self.spectrogram_min_frequency_label2.configure(text='''Hz''')

        self.spectrogram_log_frequency_check = tk.Checkbutton(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_log_frequency_check.place(x=20, y=150, height=22, width=180)
        self.spectrogram_log_frequency_check.configure(anchor='w')
        self.spectrogram_log_frequency_check.configure(justify='left')
        self.spectrogram_log_frequency_check.configure(text='''Log Frequency Scale''')
        self.spectrogram_log_frequency_check.configure(variable=rscu_support.spectrogram_log_frequency)

        self.spectrogram_show_seismogram_check = tk.Checkbutton(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_show_seismogram_check.place(x=20, y=190, height=22, width=160)
        self.spectrogram_show_seismogram_check.configure(anchor='w')
        self.spectrogram_show_seismogram_check.configure(justify='left')
        self.spectrogram_show_seismogram_check.configure(text='''Show seismogram''')
        self.spectrogram_show_seismogram_check.configure(variable=rscu_support.spectrogram_show_seismogram)

        self.spectrogram_show_colorbar_check = tk.Checkbutton(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_show_colorbar_check.place(x=20, y=230, height=22, width=140)
        self.spectrogram_show_colorbar_check.configure(anchor='w')
        self.spectrogram_show_colorbar_check.configure(justify='left')
        self.spectrogram_show_colorbar_check.configure(text='''Show Color Bar''')
        self.spectrogram_show_colorbar_check.configure(variable=rscu_support.spectrogram_show_colorbar)

        self.spectrogram_colormap_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_colormap_label.place(x=30, y=270, height=20, width=72)
        self.spectrogram_colormap_label.configure(anchor='w')
        self.spectrogram_colormap_label.configure(text='''Colormap:''')

        self.spectrogram_colormap_combo = ttk.Combobox(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_colormap_combo.place(x=110, y=270, height=22, width=176)
        self.value_list = ['nipy_spectral','jet','rainbow','brg','inferno','plasma','viridis','spring','summer','autumn','winter','cool','hot','hsv']
        self.spectrogram_colormap_combo.configure(values=self.value_list)
        self.spectrogram_colormap_combo.configure(textvariable=rscu_support.spectrogram_colormap)

        self.spectrogram_date_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_date_label.place(x=380, y=30,  height=20, width=142)
        self.spectrogram_date_label.configure(anchor='w')
        self.spectrogram_date_label.configure(text='''Date and Time (UTC):''')

        self.spectrogram_year_spin = tk.Spinbox(self.chart_type_spectrogram_tabs_t3_3, from_=2018, to=2030, increment=1)
        self.spectrogram_year_spin.place(x=530, y=30, height=22, width=56)
        self.spectrogram_year_spin.configure(font="TkDefaultFont")
        self.spectrogram_year_spin.configure(increment="2018.0")
        self.spectrogram_year_spin.configure(justify='right')
        self.spectrogram_year_spin.configure(textvariable=rscu_support.start_year)
        self.spectrogram_year_spin.configure(validate="key")
        validate_int = self.spectrogram_year_spin.register(rscu_validate.validate_int)
        self.spectrogram_year_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrogram_month_spin = tk.Spinbox(self.chart_type_spectrogram_tabs_t3_3, from_=1, to=12, increment=1)
        self.spectrogram_month_spin.place(x=590, y=30, height=22, width=36)
        self.spectrogram_month_spin.configure(font="TkDefaultFont")
        self.spectrogram_month_spin.configure(justify='right')
        self.spectrogram_month_spin.configure(wrap=True)
        self.spectrogram_month_spin.configure(textvariable=rscu_support.start_month)
        self.spectrogram_month_spin.configure(validate="key")
        validate_int = self.spectrogram_month_spin.register(rscu_validate.validate_int)
        self.spectrogram_month_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrogram_day_spin = tk.Spinbox(self.chart_type_spectrogram_tabs_t3_3, from_=1, to=31, increment=1)
        self.spectrogram_day_spin.place(x=630, y=30, height=22, width=36)
        self.spectrogram_day_spin.configure(font="TkDefaultFont")
        self.spectrogram_day_spin.configure(justify='right')
        self.spectrogram_day_spin.configure(wrap=True)
        self.spectrogram_day_spin.configure(textvariable=rscu_support.start_day)
        self.spectrogram_day_spin.configure(validate="key")
        validate_int = self.spectrogram_day_spin.register(rscu_validate.validate_int)
        self.spectrogram_day_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrogram_hour_spin = tk.Spinbox(self.chart_type_spectrogram_tabs_t3_3, from_=0, to=23, increment=1)
        self.spectrogram_hour_spin.place(x=680, y=30, height=22, width=36)
        self.spectrogram_hour_spin.configure(font="TkDefaultFont")
        self.spectrogram_hour_spin.configure(justify='right')
        self.spectrogram_hour_spin.configure(wrap=True)
        self.spectrogram_hour_spin.configure(textvariable=rscu_support.start_hour)
        self.spectrogram_hour_spin.configure(validate="key")
        validate_int = self.spectrogram_hour_spin.register(rscu_validate.validate_int)
        self.spectrogram_hour_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrogram_minute_spin = tk.Spinbox(self.chart_type_spectrogram_tabs_t3_3, from_=0, to=59, increment=1)
        self.spectrogram_minute_spin.place(x=720, y=30, height=22, width=36)
        self.spectrogram_minute_spin.configure(font="TkDefaultFont")
        self.spectrogram_minute_spin.configure(justify='right')
        self.spectrogram_minute_spin.configure(wrap=True)
        self.spectrogram_minute_spin.configure(textvariable=rscu_support.start_minute)
        self.spectrogram_minute_spin.configure(validate="key")
        validate_int = self.spectrogram_minute_spin.register(rscu_validate.validate_int)
        self.spectrogram_minute_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrogram_second_spin = tk.Spinbox(self.chart_type_spectrogram_tabs_t3_3, from_=0, to=59)
        self.spectrogram_second_spin.place(x=760, y=30, height=22, width=36)
        self.spectrogram_second_spin.configure(font="TkDefaultFont")
        self.spectrogram_second_spin.configure(justify='right')
        self.spectrogram_second_spin.configure(wrap=True)
        self.spectrogram_second_spin.configure(textvariable=rscu_support.start_second)
        self.spectrogram_second_spin.configure(validate="key")
        validate_int = self.spectrogram_second_spin.register(rscu_validate.validate_int)
        self.spectrogram_second_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrogram_year_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_year_label.place(x=535, y=50,  height=20, width=36)
        self.spectrogram_year_label.configure(anchor='w')
        self.spectrogram_year_label.configure(text='''yyyy''')

        self.spectrogram_month_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_month_label.place(x=590, y=50,  height=20, width=30)
        self.spectrogram_month_label.configure(anchor='w')
        self.spectrogram_month_label.configure(text='''mm''')

        self.spectrogram_day_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_day_label.place(x=635, y=50,  height=20, width=21)
        self.spectrogram_day_label.configure(anchor='w')
        self.spectrogram_day_label.configure(text='''dd''')

        self.spectrogram_hour_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_hour_label.place(x=685, y=50,  height=20, width=20)
        self.spectrogram_hour_label.configure(anchor='w')
        self.spectrogram_hour_label.configure(text='''hh''')

        self.spectrogram_minute_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_minute_label.place(x=720, y=50,  height=20, width=30)
        self.spectrogram_minute_label.configure(anchor='w')
        self.spectrogram_minute_label.configure(text='''mm''')

        self.spectrogram_second_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_second_label.place(x=765, y=50,  height=20, width=16)
        self.spectrogram_second_label.configure(anchor='w')
        self.spectrogram_second_label.configure(text='''ss''')

        self.spectrogram_duration_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_duration_label.place(x=380, y=80, height=20, width=64)
        self.spectrogram_duration_label.configure(anchor='w')
        self.spectrogram_duration_label.configure(text='''Duration:''')

        self.spectrogram_duration_entry = tk.Entry(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_duration_entry.place(x=450, y=80, height=22, width=96)
        self.spectrogram_duration_entry.configure(font="TkFixedFont")
        self.spectrogram_duration_entry.configure(justify='right')
        self.spectrogram_duration_entry.configure(textvariable=rscu_support.duration)
        self.spectrogram_duration_entry.configure(validate="key")
        validate_int = self.spectrogram_duration_entry.register(rscu_validate.validate_int)
        self.spectrogram_duration_entry.configure(validatecommand=(validate_int,"%S"))

        self.spectrogram_duration_label2 = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_duration_label2.place(x=550, y=80, height=20, width=58)
        self.spectrogram_duration_label2.configure(anchor='w')
        self.spectrogram_duration_label2.configure(text='''seconds''')

        self.spectrogram_chart_title_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_chart_title_label.place(x=380, y=120, height=20, width=75)
        self.spectrogram_chart_title_label.configure(anchor='w')
        self.spectrogram_chart_title_label.configure(text='''Chart Title:''')

        self.spectrogram_chart_title_entry = tk.Entry(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_chart_title_entry.place(x=380, y=140, height=22, width=466)
        self.spectrogram_chart_title_entry.configure(font="TkFixedFont")
        self.spectrogram_chart_title_entry.configure(textvariable=rscu_support.spectrogram_chart_title)

        self.spectrogram_chart_autosave_check = tk.Checkbutton(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_chart_autosave_check.place(x=370, y=180, height=22, width=190)
        self.spectrogram_chart_autosave_check.configure(anchor='w')
        self.spectrogram_chart_autosave_check.configure(justify='left')
        self.spectrogram_chart_autosave_check.configure(text='''Auto Save Chart to File''')
        self.spectrogram_chart_autosave_check.configure(variable=rscu_support.chart_autosave)

        self.spectrogram_chart_filename_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_chart_filename_label.place(x=380, y=211, height=20, width=114)
        self.spectrogram_chart_filename_label.configure(anchor='w')
        self.spectrogram_chart_filename_label.configure(text='''Chart File Name:''')

        self.spectrogram_chart_filename_entry = tk.Entry(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_chart_filename_entry.place(x=380, y=230, height=22, width=466)
        self.spectrogram_chart_filename_entry.configure(font="TkFixedFont")
        self.spectrogram_chart_filename_entry.configure(textvariable=rscu_support.spectrogram_chart_filename)

        self.spectrogram_chart_format_label = tk.Label(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_chart_format_label.place(x=380, y=260, height=20, width=121)
        self.spectrogram_chart_format_label.configure(anchor='w')
        self.spectrogram_chart_format_label.configure(text='''Chart File Format:''')

        x_val = 280
        if( 'png' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrogram_chart_format_png_radio = tk.Radiobutton(self.chart_type_spectrogram_tabs_t3_3)
            self.spectrogram_chart_format_png_radio.place(x=x_val, y=281, height=22, width=65)
            self.spectrogram_chart_format_png_radio.configure(anchor='w')
            self.spectrogram_chart_format_png_radio.configure(justify='left')
            self.spectrogram_chart_format_png_radio.configure(text='''.png''')
            self.spectrogram_chart_format_png_radio.configure(value="png")
            self.spectrogram_chart_format_png_radio.configure(variable=rscu_support.chart_format)

        if( 'svg' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrogram_chart_format_svg_radio = tk.Radiobutton(self.chart_type_spectrogram_tabs_t3_3)
            self.spectrogram_chart_format_svg_radio.place(x=x_val, y=281, height=22, width=60)
            self.spectrogram_chart_format_svg_radio.configure(anchor='w')
            self.spectrogram_chart_format_svg_radio.configure(justify='left')
            self.spectrogram_chart_format_svg_radio.configure(text='''.svg''')
            self.spectrogram_chart_format_svg_radio.configure(value="svg")
            self.spectrogram_chart_format_svg_radio.configure(variable=rscu_support.chart_format)

        if( 'pdf' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrogram_chart_format_pdf_radio = tk.Radiobutton(self.chart_type_spectrogram_tabs_t3_3)
            self.spectrogram_chart_format_pdf_radio.place(x=x_val, y=281, height=22, width=60)
            self.spectrogram_chart_format_pdf_radio.configure(anchor='w')
            self.spectrogram_chart_format_pdf_radio.configure(justify='left')
            self.spectrogram_chart_format_pdf_radio.configure(text='''.pdf''')
            self.spectrogram_chart_format_pdf_radio.configure(value="pdf")
            self.spectrogram_chart_format_pdf_radio.configure(variable=rscu_support.chart_format)

        if( 'jpg' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrogram_chart_format_jpg_radio = tk.Radiobutton(self.chart_type_spectrogram_tabs_t3_3)
            self.spectrogram_chart_format_jpg_radio.place(x=x_val, y=281, height=22, width=60)
            self.spectrogram_chart_format_jpg_radio.configure(anchor='w')
            self.spectrogram_chart_format_jpg_radio.configure(justify='left')
            self.spectrogram_chart_format_jpg_radio.configure(text='''.jpg''')
            self.spectrogram_chart_format_jpg_radio.configure(value="jpg")
            self.spectrogram_chart_format_jpg_radio.configure(variable=rscu_support.chart_format)

        self.spectrogram_plot_chart_button = tk.Button(self.chart_type_spectrogram_tabs_t3_3)
        self.spectrogram_plot_chart_button.place(x=390, y=440, height=31, width=100)
        self.spectrogram_plot_chart_button.configure(command=rscu_spectrogram.plot_spectrogram_chart)
        self.spectrogram_plot_chart_button.configure(text='''Plot Chart''')

#
# Spectrograph Tab
#

        self.spectrum_channel_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_channel_label.place(x=30, y=30,  height=20, width=82)
        self.spectrum_channel_label.configure(anchor='w')
        self.spectrum_channel_label.configure(text='''Component:''')

        self.spectrum_channel_combo = ttk.Combobox(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_channel_combo.place(x=130, y=30, height=22, width=77)
        self.value_list = ['SHZ','EHZ','EHN','EHE','ENZ','ENN','ENE','HDF']
        self.spectrum_channel_combo.configure(values=self.value_list)
        self.spectrum_channel_combo.configure(textvariable=rscu_support.station_component)

        self.spectrum_log_frequency_check = tk.Checkbutton(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_log_frequency_check.place(x=20, y=70, height=23, width=170)
        self.spectrum_log_frequency_check.configure(anchor='w')
        self.spectrum_log_frequency_check.configure(justify='left')
        self.spectrum_log_frequency_check.configure(text='''Log Frequency Axis''')
        self.spectrum_log_frequency_check.configure(variable=rscu_support.spectrum_log_frequency)

        self.spectrum_max_frequency_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_max_frequency_label.place(x=30, y=110, height=21, width=145)
        self.spectrum_max_frequency_label.configure(text='''Maximum Frequency:''')

        self.spectrum_max_frequency_entry = tk.Entry(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_max_frequency_entry.place(x=180, y=110, height=22, width=86)
        self.spectrum_max_frequency_entry.configure(font="TkFixedFont")
        self.spectrum_max_frequency_entry.configure(justify='right')
        self.spectrum_max_frequency_entry.configure(textvariable=rscu_support.spectrum_max_frequency)
        self.spectrum_max_frequency_entry.configure(validate="key")
        validate_fp = self.spectrum_max_frequency_entry.register(rscu_validate.validate_fp)
        self.spectrum_max_frequency_entry.configure(validatecommand=(validate_fp,"%P"))

        self.spectrum_max_frequency_label2 = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_max_frequency_label2.place(x=270, y=110, height=20, width=21)
        self.spectrum_max_frequency_label2.configure(anchor='w')
        self.spectrum_max_frequency_label2.configure(text='''Hz''')

        self.spectrum_min_frequency_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_min_frequency_label.place(x=30, y=150, height=21, width=141)
        self.spectrum_min_frequency_label.configure(anchor='w')
        self.spectrum_min_frequency_label.configure(text='''Minimum Frequency:''')

        self.spectrum_min_frequency_entry = tk.Entry(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_min_frequency_entry.place(x=180, y=150, height=22, width=86)
        self.spectrum_min_frequency_entry.configure(font="TkFixedFont")
        self.spectrum_min_frequency_entry.configure(justify='right')
        self.spectrum_min_frequency_entry.configure(textvariable=rscu_support.spectrum_min_frequency)
        self.spectrum_min_frequency_entry.configure(validate="key")
        validate_fp = self.spectrum_min_frequency_entry.register(rscu_validate.validate_fp)
        self.spectrum_min_frequency_entry.configure(validatecommand=(validate_fp,"%P"))

        self.spectrum_min_frequency_label2 = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_min_frequency_label2.place(x=270, y=150, height=20, width=21)
        self.spectrum_min_frequency_label2.configure(text='''Hz''')

        self.spectrum_log_intensity_check = tk.Checkbutton(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_log_intensity_check.place(x=20, y=190, height=23, width=160)
        self.spectrum_log_intensity_check.configure(anchor='w')
        self.spectrum_log_intensity_check.configure(justify='left')
        self.spectrum_log_intensity_check.configure(text='''Log Intensity Axis''')
        self.spectrum_log_intensity_check.configure(variable=rscu_support.spectrum_log_intensity)

        self.spectrum_autoscale_intensity_check = tk.Checkbutton(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_autoscale_intensity_check.place(x=20, y=230, height=22, width=200)
        self.spectrum_autoscale_intensity_check.configure(anchor='w')
        self.spectrum_autoscale_intensity_check.configure(command=rscu_support.spectrum_set_intensity_autoscale_options)
        self.spectrum_autoscale_intensity_check.configure(justify='left')
        self.spectrum_autoscale_intensity_check.configure(text='''Auto Scale Intensity Axis''')
        self.spectrum_autoscale_intensity_check.configure(variable=rscu_support.spectrum_autoscale_intensity)

        self.spectrum_max_intensity_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_max_intensity_label.place(x=30, y=270, height=22, width=134)
        self.spectrum_max_intensity_label.configure(anchor='w')
        self.spectrum_max_intensity_label.configure(text='''Maximum Intensity:''')
        self.spectrum_max_intensity_label.configure(state=rscu_support.spectrum_intensity_scale_state)

        self.spectrum_max_intensity_entry = tk.Entry(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_max_intensity_entry.place(x=170, y=270, height=22, width=86)
        self.spectrum_max_intensity_entry.configure(font="TkFixedFont")
        self.spectrum_max_intensity_entry.configure(justify='right')
        self.spectrum_max_intensity_entry.configure(state=rscu_support.spectrum_intensity_scale_state)
        self.spectrum_max_intensity_entry.configure(textvariable=rscu_support.spectrum_max_intensity)
        self.spectrum_max_intensity_entry.configure(validate="key")
        validate_fp = self.spectrum_max_intensity_entry.register(rscu_validate.validate_fp)
        self.spectrum_max_intensity_entry.configure(validatecommand=(validate_fp,"%P"))

        self.spectrum_min_intensity_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_min_intensity_label.place(x=30, y=310, height=21, width=130)
        self.spectrum_min_intensity_label.configure(text='''Minimum Intensity:''')
        self.spectrum_min_intensity_label.configure(state=rscu_support.spectrum_intensity_scale_state)

        self.spectrum_min_intensity_entry = tk.Entry(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_min_intensity_entry.place(x=170, y=310, height=22, width=86)
        self.spectrum_min_intensity_entry.configure(font="TkFixedFont")
        self.spectrum_min_intensity_entry.configure(justify='right')
        self.spectrum_min_intensity_entry.configure(state=rscu_support.spectrum_intensity_scale_state)
        self.spectrum_min_intensity_entry.configure(textvariable=rscu_support.spectrum_min_intensity)
        self.spectrum_min_intensity_entry.configure(validate="key")
        validate_fp = self.spectrum_min_intensity_entry.register(rscu_validate.validate_fp)
        self.spectrum_min_intensity_entry.configure(validatecommand=(validate_fp,"%P"))

        self.spectrum_date_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_date_label.place(x=380, y=30,  height=20, width=144)
        self.spectrum_date_label.configure(anchor='w')
        self.spectrum_date_label.configure(text='''Date and Time (UTC):''')

        self.spectrum_year_spin = tk.Spinbox(self.chart_type_spectrograph_tabs_t4_4, from_=2018, to=2030, increment=1)
        self.spectrum_year_spin.place(x=530, y=30, height=22, width=56)
        self.spectrum_year_spin.configure(font="TkDefaultFont")
        self.spectrum_year_spin.configure(justify='right')
        self.spectrum_year_spin.configure(textvariable=rscu_support.start_year)
        self.spectrum_year_spin.configure(validate="key")
        validate_int = self.spectrum_year_spin.register(rscu_validate.validate_int)
        self.spectrum_year_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrum_month_spin = tk.Spinbox(self.chart_type_spectrograph_tabs_t4_4, from_=1, to=12, increment=1)
        self.spectrum_month_spin.place(x=590, y=30, height=22, width=36)
        self.spectrum_month_spin.configure(font="TkDefaultFont")
        self.spectrum_month_spin.configure(justify='right')
        self.spectrum_month_spin.configure(wrap=True)
        self.spectrum_month_spin.configure(textvariable=rscu_support.start_month)
        self.spectrum_month_spin.configure(validate="key")
        validate_int = self.spectrum_month_spin.register(rscu_validate.validate_int)
        self.spectrum_month_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrum_day_spin = tk.Spinbox(self.chart_type_spectrograph_tabs_t4_4, from_=1, to=31, increment=1)
        self.spectrum_day_spin.place(x=630, y=30, height=22, width=36)
        self.spectrum_day_spin.configure(font="TkDefaultFont")
        self.spectrum_day_spin.configure(justify='right')
        self.spectrum_day_spin.configure(wrap=True)
        self.spectrum_day_spin.configure(textvariable=rscu_support.start_day)
        self.spectrum_day_spin.configure(validate="key")
        validate_int = self.spectrum_day_spin.register(rscu_validate.validate_int)
        self.spectrum_day_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrum_hour_spin = tk.Spinbox(self.chart_type_spectrograph_tabs_t4_4, from_=0, to=23, increment=1)
        self.spectrum_hour_spin.place(x=680, y=30, height=23, width=36)
        self.spectrum_hour_spin.configure(font="TkDefaultFont")
        self.spectrum_hour_spin.configure(justify='right')
        self.spectrum_hour_spin.configure(wrap=True)
        self.spectrum_hour_spin.configure(textvariable=rscu_support.start_hour)
        self.spectrum_hour_spin.configure(validate="key")
        validate_int = self.spectrum_hour_spin.register(rscu_validate.validate_int)
        self.spectrum_hour_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrum_minute_spin = tk.Spinbox(self.chart_type_spectrograph_tabs_t4_4, from_=0, to=59, increment=1)
        self.spectrum_minute_spin.place(x=720, y=30, height=22, width=36)
        self.spectrum_minute_spin.configure(font="TkDefaultFont")
        self.spectrum_minute_spin.configure(justify='right')
        self.spectrum_minute_spin.configure(wrap=True)
        self.spectrum_minute_spin.configure(textvariable=rscu_support.start_minute)
        self.spectrum_minute_spin.configure(validate="key")
        validate_int = self.spectrum_minute_spin.register(rscu_validate.validate_int)
        self.spectrum_minute_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrum_second_spin = tk.Spinbox(self.chart_type_spectrograph_tabs_t4_4, from_=0, to=59, increment=1)
        self.spectrum_second_spin.place(x=760, y=30, height=22, width=36)
        self.spectrum_second_spin.configure(font="TkDefaultFont")
        self.spectrum_second_spin.configure(justify='right')
        self.spectrum_second_spin.configure(wrap=True)
        self.spectrum_second_spin.configure(textvariable=rscu_support.start_second)
        self.spectrum_second_spin.configure(validate="key")
        validate_int = self.spectrum_second_spin.register(rscu_validate.validate_int)
        self.spectrum_second_spin.configure(validatecommand=(validate_int,"%S"))

        self.spectrum_year_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_year_label.place(x=535, y=50,  height=20, width=36)
        self.spectrum_year_label.configure(anchor='w')
        self.spectrum_year_label.configure(text='''yyyy''')

        self.spectrum_month_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_month_label.place(x=590, y=50,  height=20, width=30)
        self.spectrum_month_label.configure(anchor='w')
        self.spectrum_month_label.configure(text='''mm''')

        self.spectrum_day_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_day_label.place(x=635, y=50,  height=20, width=21)
        self.spectrum_day_label.configure(anchor='w')
        self.spectrum_day_label.configure(text='''dd''')

        self.bespectrum_hour_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.bespectrum_hour_label.place(x=685, y=50,  height=20, width=20)
        self.bespectrum_hour_label.configure(anchor='w')
        self.bespectrum_hour_label.configure(text='''hh''')

        self.spectrum_minute_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_minute_label.place(x=720, y=50,  height=20, width=30)
        self.spectrum_minute_label.configure(anchor='w')
        self.spectrum_minute_label.configure(text='''mm''')

        self.spectrum_second_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_second_label.place(x=765, y=50,  height=20, width=16)
        self.spectrum_second_label.configure(anchor='w')
        self.spectrum_second_label.configure(text='''ss''')

        self.spectrum_duration_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_duration_label.place(x=380, y=80,  height=20, width=64)
        self.spectrum_duration_label.configure(anchor='w')
        self.spectrum_duration_label.configure(text='''Duration:''')

        self.spectrum_duration_entry = tk.Entry(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_duration_entry.place(x=450, y=80, height=22, width=96)
        self.spectrum_duration_entry.configure(font="TkFixedFont")
        self.spectrum_duration_entry.configure(justify='right')
        self.spectrum_duration_entry.configure(textvariable=rscu_support.duration)
        self.spectrum_duration_entry.configure(validate="key")
        validate_int = self.spectrum_duration_entry.register(rscu_validate.validate_int)
        self.spectrum_duration_entry.configure(validatecommand=(validate_int,"%S"))

        self.spectrum_duration_label2 = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_duration_label2.place(x=550, y=80, height=20, width=57)
        self.spectrum_duration_label2.configure(anchor='w')
        self.spectrum_duration_label2.configure(text='''seconds''')

        self.spectrum_chart_title_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_chart_title_label.place(x=380, y=120, height=20, width=75)
        self.spectrum_chart_title_label.configure(anchor='w')
        self.spectrum_chart_title_label.configure(text='''Chart Title:''')

        self.spectrum_chart_title_entry = tk.Entry(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_chart_title_entry.place(x=380, y=140, height=22, width=466)
        self.spectrum_chart_title_entry.configure(font="TkFixedFont")
        self.spectrum_chart_title_entry.configure(textvariable=rscu_support.spectrum_chart_title)

        self.spectrum_chart_autosave_check = tk.Checkbutton(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_chart_autosave_check.place(x=370, y=180, height=22, width=190)
        self.spectrum_chart_autosave_check.configure(anchor='w')
        self.spectrum_chart_autosave_check.configure(justify='left')
        self.spectrum_chart_autosave_check.configure(text='''Auto Save Chart to File''')
        self.spectrum_chart_autosave_check.configure(variable=rscu_support.chart_autosave)

        self.spectrum_chart_filename_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_chart_filename_label.place(x=380, y=210, height=20, width=114)
        self.spectrum_chart_filename_label.configure(anchor='w')
        self.spectrum_chart_filename_label.configure(text='''Chart File Name:''')

        self.spectrum_chart_filename_entry = tk.Entry(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_chart_filename_entry.place(x=380, y=230, height=22, width=466)
        self.spectrum_chart_filename_entry.configure(font="TkFixedFont")
        self.spectrum_chart_filename_entry.configure(textvariable=rscu_support.spectrum_chart_filename)

        self.sprectrum_chart_format_label = tk.Label(self.chart_type_spectrograph_tabs_t4_4)
        self.sprectrum_chart_format_label.place(x=380, y=260, height=20, width=121)
        self.sprectrum_chart_format_label.configure(text='''Chart File Format:''')

        x_val = 280
        if( 'png' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrum_chart_format_png_radio = tk.Radiobutton(self.chart_type_spectrograph_tabs_t4_4)
            self.spectrum_chart_format_png_radio.place(x=370, y=280, height=22, width=65)
            self.spectrum_chart_format_png_radio.configure(anchor='w')
            self.spectrum_chart_format_png_radio.configure(justify='left')
            self.spectrum_chart_format_png_radio.configure(text='''.png''')
            self.spectrum_chart_format_png_radio.configure(value="png")
            self.spectrum_chart_format_png_radio.configure(variable=rscu_support.chart_format)

        if( 'png' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrum_chart_format_svg_radio = tk.Radiobutton(self.chart_type_spectrograph_tabs_t4_4)
            self.spectrum_chart_format_svg_radio.place(x=460, y=280, height=22, width=60)
            self.spectrum_chart_format_svg_radio.configure(anchor='w')
            self.spectrum_chart_format_svg_radio.configure(justify='left')
            self.spectrum_chart_format_svg_radio.configure(text='''.svg''')
            self.spectrum_chart_format_svg_radio.configure(value="svg")
            self.spectrum_chart_format_svg_radio.configure(variable=rscu_support.chart_format)

        if( 'png' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrum_chart_format_pdf_radio = tk.Radiobutton(self.chart_type_spectrograph_tabs_t4_4)
            self.spectrum_chart_format_pdf_radio.place(x=550, y=280, height=22, width=60)
            self.spectrum_chart_format_pdf_radio.configure(anchor='w')
            self.spectrum_chart_format_pdf_radio.configure(justify='left')
            self.spectrum_chart_format_pdf_radio.configure(text='''.pdf''')
            self.spectrum_chart_format_pdf_radio.configure(value="pdf")
            self.spectrum_chart_format_pdf_radio.configure(variable=rscu_support.chart_format)

        if( 'jpg' in rscu_support.available_formats ):
            x_val = x_val + 90
            self.spectrum_chart_format_jpg_radio = tk.Radiobutton(self.chart_type_spectrograph_tabs_t4_4)
            self.spectrum_chart_format_jpg_radio.place(x=640, y=280, height=22, width=60)
            self.spectrum_chart_format_jpg_radio.configure(anchor='w')
            self.spectrum_chart_format_jpg_radio.configure(justify='left')
            self.spectrum_chart_format_jpg_radio.configure(text='''.jpg''')
            self.spectrum_chart_format_jpg_radio.configure(value="jpg")
            self.spectrum_chart_format_jpg_radio.configure(variable=rscu_support.chart_format)

        self.spectrum_plot_chart_button = tk.Button(self.chart_type_spectrograph_tabs_t4_4)
        self.spectrum_plot_chart_button.place(x=390, y=440, height=31, width=100)
        self.spectrum_plot_chart_button.configure(command=rscu_spectrograph.plot_spectrograph_chart)
        self.spectrum_plot_chart_button.configure(text='''Plat Chart''')

#
# Arrivals
#

        self.arrival_event_date_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_date_label.place(x=30, y=30,  height=20, width=184)
        self.arrival_event_date_label.configure(anchor='w')
        self.arrival_event_date_label.configure(text='''Event Date and Time (UTC):''')

        self.arrival_event_year_spin = tk.Spinbox(self.chart_type_arrivals_tabs_t5_5, from_=2018, to=2030, increment=1)
        self.arrival_event_year_spin.place(x=220, y=30, height=22, width=56)
        self.arrival_event_year_spin.configure(font="TkDefaultFont")
        self.arrival_event_year_spin.configure(justify='right')
        self.arrival_event_year_spin.configure(textvariable=rscu_support.event_year)
        self.arrival_event_year_spin.configure(validate="key")
        validate_int = self.arrival_event_year_spin.register(rscu_validate.validate_int)
        self.arrival_event_year_spin.configure(validatecommand=(validate_int,"%S"))

        self.arrival_event_month_spin = tk.Spinbox(self.chart_type_arrivals_tabs_t5_5, from_=1, to=12, increment=1)
        self.arrival_event_month_spin.place(x=280, y=30, height=22, width=36)
        self.arrival_event_month_spin.configure(font="TkDefaultFont")
        self.arrival_event_month_spin.configure(justify='right')
        self.arrival_event_month_spin.configure(wrap=True)
        self.arrival_event_month_spin.configure(textvariable=rscu_support.event_month)
        self.arrival_event_month_spin.configure(validate="key")
        validate_int = self.arrival_event_month_spin.register(rscu_validate.validate_int)
        self.arrival_event_month_spin.configure(validatecommand=(validate_int,"%S"))

        self.arrival_event_day_spin = tk.Spinbox(self.chart_type_arrivals_tabs_t5_5, from_=1, to=31, increment=1)
        self.arrival_event_day_spin.place(x=320, y=30, height=22, width=36)
        self.arrival_event_day_spin.configure(font="TkDefaultFont")
        self.arrival_event_day_spin.configure(justify='right')
        self.arrival_event_day_spin.configure(wrap=True)
        self.arrival_event_day_spin.configure(textvariable=rscu_support.event_day)
        self.arrival_event_day_spin.configure(validate="key")
        validate_int = self.arrival_event_day_spin.register(rscu_validate.validate_int)
        self.arrival_event_day_spin.configure(validatecommand=(validate_int,"%S"))

        self.arrival_event_hour_spin = tk.Spinbox(self.chart_type_arrivals_tabs_t5_5, from_=0, to=23, increment=1)
        self.arrival_event_hour_spin.place(x=370, y=30, height=22, width=36)
        self.arrival_event_hour_spin.configure(font="TkDefaultFont")
        self.arrival_event_hour_spin.configure(justify='right')
        self.arrival_event_hour_spin.configure(wrap=True)
        self.arrival_event_hour_spin.configure(textvariable=rscu_support.event_hour)
        self.arrival_event_hour_spin.configure(validate="key")
        validate_int = self.arrival_event_hour_spin.register(rscu_validate.validate_int)
        self.arrival_event_hour_spin.configure(validatecommand=(validate_int,"%S"))

        self.arrival_event_minute_spin = tk.Spinbox(self.chart_type_arrivals_tabs_t5_5, from_=0, to=59, increment=1)
        self.arrival_event_minute_spin.place(x=410, y=30, height=22, width=36)
        self.arrival_event_minute_spin.configure(font="TkDefaultFont")
        self.arrival_event_minute_spin.configure(justify='right')
        self.arrival_event_minute_spin.configure(wrap=True)
        self.arrival_event_minute_spin.configure(textvariable=rscu_support.event_minute)
        self.arrival_event_minute_spin.configure(validate="key")
        validate_int = self.arrival_event_minute_spin.register(rscu_validate.validate_int)
        self.arrival_event_minute_spin.configure(validatecommand=(validate_int,"%S"))

        self.arrival_event_second_spin = tk.Spinbox(self.chart_type_arrivals_tabs_t5_5, from_=0, to=59, increment=1)
        self.arrival_event_second_spin.place(x=450, y=30, height=22, width=36)
        self.arrival_event_second_spin.configure(font="TkDefaultFont")
        self.arrival_event_second_spin.configure(justify='right')
        self.arrival_event_second_spin.configure(wrap=True)
        self.arrival_event_second_spin.configure(textvariable=rscu_support.event_second)
        self.arrival_event_second_spin.configure(validate="key")
        validate_int = self.arrival_event_second_spin.register(rscu_validate.validate_int)
        self.arrival_event_second_spin.configure(validatecommand=(validate_int,"%S"))

        self.arrival_event_year_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_year_label.place(x=225, y=50,  height=20, width=36)
        self.arrival_event_year_label.configure(anchor='w')
        self.arrival_event_year_label.configure(text='''yyyy''')

        self.arrival_event_month_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_month_label.place(x=280, y=50,  height=20, width=30)
        self.arrival_event_month_label.configure(anchor='w')
        self.arrival_event_month_label.configure(text='''mm''')

        self.arrival_event_day_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_day_label.place(x=325, y=50,  height=20, width=20)
        self.arrival_event_day_label.configure(anchor='w')
        self.arrival_event_day_label.configure(text='''dd''')

        self.arrival_event_hour_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_hour_label.place(x=375, y=50,  height=20, width=21)
        self.arrival_event_hour_label.configure(anchor='w')
        self.arrival_event_hour_label.configure(text='''hh''')

        self.arrival_event_minute_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_minute_label.place(x=410, y=50, height=20, width=30)
        self.arrival_event_minute_label.configure(anchor='w')
        self.arrival_event_minute_label.configure(text='''mm''')

        self.arrival_event_second_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_second_label.place(x=455, y=50, height=20, width=18)
        self.arrival_event_second_label.configure(anchor='w')
        self.arrival_event_second_label.configure(text='''ss''')

        self.arrival_event_location_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_location_label.place(x=30, y=80, height=20, width=109)
        self.arrival_event_location_label.configure(anchor='w')
        self.arrival_event_location_label.configure(text='''Event Location:''')

        self.arrival_event_latitude_entry = tk.Entry(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_latitude_entry.place(x=140, y=80, height=22, width=86)
        self.arrival_event_latitude_entry.configure(font="TkFixedFont")
        self.arrival_event_latitude_entry.configure(textvariable=rscu_support.event_latitude)
        self.arrival_event_latitude_entry.configure(justify='right')
        self.arrival_event_latitude_entry.configure(validate="key")
        validate_fp = self.arrival_event_latitude_entry.register(rscu_validate.validate_fp)
        self.arrival_event_latitude_entry.configure(validatecommand=(validate_fp,"%P"))

        self.arrival_event_latitude_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_latitude_label.place(x=230, y=80, height=20, width=57)
        self.arrival_event_latitude_label.configure(text='''Latitude,''')

        self.arrival_event_longitude_entry = tk.Entry(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_longitude_entry.place(x=300, y=80, height=22, width=86)
        self.arrival_event_longitude_entry.configure(font="TkFixedFont")
        self.arrival_event_longitude_entry.configure(justify='right')
        self.arrival_event_longitude_entry.configure(textvariable=rscu_support.event_longitude)
        self.arrival_event_longitude_entry.configure(validate="key")
        validate_fp = self.arrival_event_longitude_entry.register(rscu_validate.validate_fp)
        self.arrival_event_longitude_entry.configure(validatecommand=(validate_fp,"%P"))

        self.arrival_event_longitude_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_longitude_label.place(x=390, y=80, height=20, width=78)
        self.arrival_event_longitude_label.configure(text='''Longitude,''')

        self.arrival_event_depth_entry = tk.Entry(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_depth_entry.place(x=480, y=80, height=22, width=86)
        self.arrival_event_depth_entry.configure(font="TkFixedFont")
        self.arrival_event_depth_entry.configure(justify='right')
        self.arrival_event_depth_entry.configure(textvariable=rscu_support.event_depth)
        self.arrival_event_depth_entry.configure(validate="key")
        validate_fp = self.arrival_event_depth_entry.register(rscu_validate.validate_fp)
        self.arrival_event_depth_entry.configure(validatecommand=(validate_fp,"%P"))

        self.arrival_event_depth_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_event_depth_label.place(x=570, y=80,  height=20, width=75)
        self.arrival_event_depth_label.configure(anchor='w')
        self.arrival_event_depth_label.configure(text='''km deep''')

        self.arrival_chart_title_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_chart_title_label.place(x=30, y=120, height=20, width=158)
        self.arrival_chart_title_label.configure(anchor='w')
        self.arrival_chart_title_label.configure(text='''Ray Path Diagram Title:''')

        self.arrival_chart_title_entry = tk.Entry(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_chart_title_entry.place(x=30, y=140, height=22, width=820)
        self.arrival_chart_title_entry.configure(font="TkFixedFont")
        self.arrival_chart_title_entry.configure(textvariable=rscu_support.arrival_chart_title)

        self.arrival_chart_autosave_check = tk.Checkbutton(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_chart_autosave_check.place(x=20, y=180, height=22, width=390)
        self.arrival_chart_autosave_check.configure(anchor='w')
        self.arrival_chart_autosave_check.configure(justify='left')
        self.arrival_chart_autosave_check.configure(text='''Auto Save Ray Path Diagram and Arrivals Data to Files''')
        self.arrival_chart_autosave_check.configure(variable=rscu_support.chart_autosave)

        self.arrival_chart_filename_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_chart_filename_label.place(x=30, y=210, height=20, width=324)
        self.arrival_chart_filename_label.configure(anchor='w')
        self.arrival_chart_filename_label.configure(text='''Ray Path Diagram and Arrivals Data File Names:''')

        self.arrival_chart_filename_entry = tk.Entry(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_chart_filename_entry.place(x=30, y=230, height=22, width=466)
        self.arrival_chart_filename_entry.configure(font="TkFixedFont")
        self.arrival_chart_filename_entry.configure(textvariable=rscu_support.arrival_chart_filename)

        self.arrival_chart_format_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_chart_format_label.place(x=540, y=210, height=20, width=204)
        self.arrival_chart_format_label.configure(text='''Ray Path Diagram File Format:''')

        x_val = 460
        if( 'png' in rscu_support.available_formats ):
            x_val = x_val + 70
            self.arrival_chart_format_png_radio = tk.Radiobutton(self.chart_type_arrivals_tabs_t5_5)
            self.arrival_chart_format_png_radio.place(x=x_val, y=230, height=22, width=65)
            self.arrival_chart_format_png_radio.configure(anchor='w')
            self.arrival_chart_format_png_radio.configure(justify='left')
            self.arrival_chart_format_png_radio.configure(text=''',png''')
            self.arrival_chart_format_png_radio.configure(value="png")
            self.arrival_chart_format_png_radio.configure(variable=rscu_support.chart_format)

        if( 'svg' in rscu_support.available_formats ):
            x_val = x_val + 70
            self.arrival_chart_format_svg_radio = tk.Radiobutton(self.chart_type_arrivals_tabs_t5_5)
            self.arrival_chart_format_svg_radio.place(x=x_val, y=230, height=22, width=60)
            self.arrival_chart_format_svg_radio.configure(anchor='w')
            self.arrival_chart_format_svg_radio.configure(justify='left')
            self.arrival_chart_format_svg_radio.configure(text='''.svg''')
            self.arrival_chart_format_svg_radio.configure(value="svg")
            self.arrival_chart_format_svg_radio.configure(variable=rscu_support.chart_format)

        if( 'pdf' in rscu_support.available_formats ):
            x_val = x_val + 70
            self.arrival_chart_format_pdf_radio = tk.Radiobutton(self.chart_type_arrivals_tabs_t5_5)
            self.arrival_chart_format_pdf_radio.place(x=x_val, y=230, height=22, width=60)
            self.arrival_chart_format_pdf_radio.configure(anchor='w')
            self.arrival_chart_format_pdf_radio.configure(justify='left')
            self.arrival_chart_format_pdf_radio.configure(text='''.pdf''')
            self.arrival_chart_format_pdf_radio.configure(value="pdf")
            self.arrival_chart_format_pdf_radio.configure(variable=rscu_support.chart_format)

        if( 'jpg' in rscu_support.available_formats ):
            x_val = x_val + 70
            self.arrival_chart_format_jpg_radio = tk.Radiobutton(self.chart_type_arrivals_tabs_t5_5)
            self.arrival_chart_format_jpg_radio.place(x=x_val, y=230, height=22, width=60)
            self.arrival_chart_format_jpg_radio.configure(anchor='w')
            self.arrival_chart_format_jpg_radio.configure(justify='left')
            self.arrival_chart_format_jpg_radio.configure(text=''',jpg''')
            self.arrival_chart_format_jpg_radio.configure(value="jpg")
            self.arrival_chart_format_jpg_radio.configure(variable=rscu_support.chart_format)

        self.arrival_phases_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_phases_label.place(x=30, y=270,  height=20, width=54)
        self.arrival_phases_label.configure(anchor='w')
        self.arrival_phases_label.configure(text='''Phases:''')

        self.arrival_phase_list_frame = tk.Frame(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_phase_list_frame.place(x=30, y=288, height=185, width=160)
        self.arrival_phase_list_frame.configure(relief='flat')
        self.arrival_phase_list_frame.configure(borderwidth="2")

        self.arrival_phase_list = tk.Listbox(self.arrival_phase_list_frame)
        self.arrival_phase_list.place(x=0, y=0, height=181, width=142)
        self.arrival_phase_list.configure(font="TkFixedFont")
        self.arrival_phase_list.configure(borderwidth="4")
        self.arrival_phase_list.configure(relief="flat")
        self.arrival_phase_list.configure(selectmode = "browse")
        self.arrival_phase_list.configure(listvariable=rscu_support.phases)
        arrival_pahse_list_items = ['P', 'S', 'PP', 'Pdiff', 'PKP', 
                'PKiKP', 'PKIKP', 'p', 'Pn', 's', 'Sn', 'Sdiff', 'SKS', 
                'SKIKS', 'PcP', 'pP', 'pPdiff', 'pPKP', 'pPKIKP', 'pPKiKP', 
                'sP', 'sPdiff', 'sPKP', 'sPKIKP', 'sPKiKP', 'sS', 'sSdiff', 
                'sSKS', 'sSKIKS', 'ScS', 'pS', 'pSdiff', 'pSKS', 'pSKIKS', 
                'ScP', 'SKP', 'SKIKP', 'PKKP', 'PKIKKIKP', 'SKKP', 'SKIKKIKP', 
                'PKPPKP', 'PKIKPPKIKP', 'SKiKP', 'ScS', 'PcS', 'PKS', 'PKIKS', 
                'PKKS', 'PKIKKIKS', 'SKKS', 'SKIKKIKS', 'SKSSKS', 'SKIKSSKIKS', 
                'SS', 'SP', 'PS']
        for item in arrival_pahse_list_items:
            self.arrival_phase_list.insert('end', item)
        self.phase_list_scrollbar = ttk.Scrollbar(self.arrival_phase_list_frame, orient='vertical')
        self.arrival_phase_list.configure(yscrollcommand=self.phase_list_scrollbar.set)
        self.phase_list_scrollbar.configure(command=self.arrival_phase_list.yview)
        self.phase_list_scrollbar.place(x=142, y=0, height=181, width=14)
        self.arrival_phase_list.bind('<Double-Button-1>', rscu_support.phase_to_phaselist)


        self.arrival_phase_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_phase_label.place(x=210, y=270, height=20, width=78, bordermode='ignore')
        self.arrival_phase_label.configure(anchor='w')
        self.arrival_phase_label.configure(text='''Phase List:''')

        self.arrival_phase_entry = tk.Entry(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_phase_entry.place(x=210, y=290, height=22, width=640, bordermode='ignore')
        self.arrival_phase_entry.configure(font="TkFixedFont")
        self.arrival_phase_entry.configure(textvariable=rscu_support.arrival_phase_list)

        self.arrival_phase_to_list_button = tk.Button(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_phase_to_list_button.place(x=210, y=330, height=31, width=161, bordermode='ignore')
        self.arrival_phase_to_list_button.configure(command=rscu_support.phase_to_phaselist)
        self.arrival_phase_to_list_button.configure(text='''Phases to Phase List''')

        self.arrival_ray_path_label = tk.Label(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_ray_path_label.place(x=480, y=330, height=20, width=160, bordermode='ignore')
        self.arrival_ray_path_label.configure(anchor='w')
        self.arrival_ray_path_label.configure(text='''Ray Path Diagram Type:''')

        self.arrival_ray_path_polar_radio = tk.Radiobutton(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_ray_path_polar_radio.place(x=640, y=330, height=22, width=100)
        self.arrival_ray_path_polar_radio.configure(anchor='w')
        self.arrival_ray_path_polar_radio.configure(justify='left')
        self.arrival_ray_path_polar_radio.configure(text='''spherical''')
        self.arrival_ray_path_polar_radio.configure(value="spherical")
        self.arrival_ray_path_polar_radio.configure(variable=rscu_support.arrival_ray_path_type)

        self.arrival_ray_path_cartesian_radio = tk.Radiobutton(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_ray_path_cartesian_radio.place(x=740, y=330, height=22, width=100)
        self.arrival_ray_path_cartesian_radio.configure(anchor='w')
        self.arrival_ray_path_cartesian_radio.configure(justify='left')
        self.arrival_ray_path_cartesian_radio.configure(text='''cartesian''')
        self.arrival_ray_path_cartesian_radio.configure(value="cartesian")
        self.arrival_ray_path_cartesian_radio.configure(variable=rscu_support.arrival_ray_path_type)

        self.arrival_show_legend_check = tk.Checkbutton(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_show_legend_check.place(x=470, y=360, height=22, width=230)
        self.arrival_show_legend_check.configure(anchor='w')
        self.arrival_show_legend_check.configure(justify='left')
        self.arrival_show_legend_check.configure(text='''Show Phase Legend on Chart''')
        self.arrival_show_legend_check.configure(variable=rscu_support.arrival_show_legend)

        self.arrival_annotate_check = tk.Checkbutton(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_annotate_check.place(x=470, y=390, height=22, width=330)
        self.arrival_annotate_check.configure(anchor='w')
        self.arrival_annotate_check.configure(justify='left')
        self.arrival_annotate_check.configure(text='''Annotate Ray Path Diagram (Shperical only)''')
        self.arrival_annotate_check.configure(variable=rscu_support.arrival_annotate)

        self.arrival_plot_chart_button = tk.Button(self.chart_type_arrivals_tabs_t5_5)
        self.arrival_plot_chart_button.place(x=300, y=440, height=31, width=359, bordermode='ignore')
        self.arrival_plot_chart_button.configure(command=rscu_arrival.calc_arrival_raypath)
        self.arrival_plot_chart_button.configure(text='''Calculate Arrival Times and Plot Ray Path Diagram''')


if __name__ == '__main__':
    vp_start_gui()

