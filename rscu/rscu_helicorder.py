import os
from datetime import timedelta, date
import tkinter as tk

from obspy import UTCDateTime

from rscu import rscu_support
from rscu import rscu_resolvetags
from rscu import rscu_validate

def plot_helicorder_chart():

#
# Collect input from GUI
#

    rs_station = rscu_support.rs_station.get().upper()                  # string
    station_component = rscu_support.station_component.get().upper()    # string
    wave_source = rscu_support.wave_source                              # string
    wave_source_type = rscu_support.wave_source_type                    # string
    wave_source_port = rscu_support.wave_source_port                    # int
    rscu_save_directory = rscu_support.rscu_save_directory.get()        # string
    pixels_wide = rscu_support.pixels_wide.get()                        # int
    pixels_tall = rscu_support.pixels_tall.get()                        # int
    chart_autosave = rscu_support.chart_autosave.get()                  # bool
    chart_format = rscu_support.chart_format.get().lower()              # string

    h_year = rscu_support.helicorder_year.get()                         # int
    h_month = rscu_support.helicorder_month.get()                       # int
    h_day = rscu_support.helicorder_day.get()                           # int
    h_start_hour = rscu_support.helicorder_start_hour.get()             # string

    minutes_per_line = rscu_support.helicorder_minutes_per_line.get()   # int
    hours_per_chart = rscu_support.helicorder_hours_per_chart.get()     # int
    auto_vertical_scaling = rscu_support.helicorder_auto_vertical_scaling.get()  # bool
    h_vertical_scaling = rscu_support.helicorder_vertical_scaling.get() # string
    line1_color = rscu_support.helicorder_line1_color.get()             # string
    line2_color = rscu_support.helicorder_line2_color.get()             # string
    line3_color = rscu_support.helicorder_line3_color.get()             # string
    line4_color = rscu_support.helicorder_line4_color.get()             # string
    h_chart_title = rscu_support.helicorder_chart_title.get()           # string
    h_chart_filename = rscu_support.helicorder_chart_filename.get()     # string

#
# Some minimal validation of user-specified arguments
#

    if( auto_vertical_scaling or not(h_vertical_scaling.isnumeric()) ):  # Test to see if either the "Auto Veritcal Scaling checkbox was checked, or no value or a non-numeric value was entered
        vertical_scaling = None                                          #   If "auto", then set the vertical scaling value to None (null value) so ObsPy will auto-scale the helicorder plot
    else:
        vertical_scaling = float(h_vertical_scaling)

    if( not rscu_validate.validate_component(v_component=station_component) ):
        return()

    if( minutes_per_line < 1 ):
        tk.messagebox.showwarning("Invalid Minutes per Line","Minutes per Line must be greater than or equal to 1." )
        return()

    if( minutes_per_line < 1 ):
        tk.messagebox.showwarning("Invalid Hours per Chart","Hours per Chart must be greater than or equal to 1." )
        return()

#
# Define the start and end times, the chart title, and the output file name
#

    if( h_start_hour == ''):
        start_hour = 0.0
    elif( (float(h_start_hour) < 0.0) or (float(h_start_hour) >= 24) ):
        return()
    else:
        start_hour = float(h_start_hour)

    start_time_minutes = int(start_hour * 60)

    if( rscu_validate.validate_date_time(v_year=h_year, v_month=h_month, v_day=h_day) ):
        start_time = UTCDateTime(date(h_year, h_month, h_day)) + timedelta(minutes=start_time_minutes)
        end_time = start_time + timedelta(hours=hours_per_chart)
    else:
        return()

    chart_title = rscu_resolvetags.resovle_tags(h_chart_title, start_time, end_time, station_component)
    if( chart_autosave ):                                               # Only need to resolve filename if chart is auto-saved
        chart_filename = rscu_resolvetags.resovle_tags(h_chart_filename, start_time, end_time, station_component).replace(':','-') + '.' + chart_format
        if( not rscu_support.validate ):
            return()                                                    # Return without generating chart if auto-save filename is invalid
        plot_full_path_name = os.path.join(rscu_support.chart_save_directory, chart_filename).replace('\\', '/')

#
# Determine the wave data source and retrieval mechanism
#

    if (wave_source_type == 'rs'):
        from obspy.clients.earthworm import Client                      # If the wave data is from a local Raspberry shake, use the OWS server client
        rs = Client(wave_source, wave_source_port)                      #   Tell ObsPy where to look for Raspberry Shake data (Note we are using the OWS port, 16032, instead of the standard WWS (Winston Wave Server) port, 16022)
    else:
        from obspy.clients.fdsn import Client                           # If the wave data is from the FDSN nework, use the FDSN client
        rs = Client(base_url=wave_source)                               #   Tell ObsPy where to look for the wave data

#
# Finally, create the helicorder plot from Raspberry Shake data and ObsPy dayplot
#

    waves = rs.get_waveforms('AM', rs_station, '00', station_component, start_time, end_time)  # Get wave data (data source, eather local form the Raspberry Shake OWS or from the FDSN network, as determined above)

    if( chart_autosave ):
        waves.plot(outfile=plot_full_path_name, type='dayplot', vertical_scaling_range=vertical_scaling, title=chart_title, title_size=18, size=(pixels_wide,pixels_tall), starttime=start_time, endtime=end_time, tick_format='%H:%M', interval=minutes_per_line, number_of_ticks=(minutes_per_line+1), one_tick_per_line=True, linewidth=0.2, color=(line1_color, line2_color, line3_color, line4_color), right_vertical_labels=True) # create the helicorder-style plot and save the image file
    waves.plot(outfile=None, type='dayplot', vertical_scaling_range=vertical_scaling, title=chart_title, title_size=18, size=(pixels_wide,pixels_tall), starttime=start_time, endtime=end_time, tick_format='%H:%M', interval=minutes_per_line, number_of_ticks=(minutes_per_line+1), one_tick_per_line=True, linewidth=0.2, color=(line1_color, line2_color, line3_color, line4_color), right_vertical_labels=True) # create the helicorder-style plot and save the image file
