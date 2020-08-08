import os
from datetime import datetime, timedelta
import tkinter as tk

from obspy import UTCDateTime

from rscu import rscu_support
from rscu import rscu_resolvetags
from rscu import rscu_validate

def plot_seismogram_chart():

#
# Collect input from GUI
#

    rs_station = rscu_support.rs_station.get().upper()                  # string
    wave_source = rscu_support.wave_source                              # string
    wave_source_type = rscu_support.wave_source_type                    # string
    wave_source_port = rscu_support.wave_source_port                    # int
    pixels_wide = rscu_support.pixels_wide.get()                        # int
    pixels_tall = rscu_support.pixels_tall.get()                        # int
    chart_autosave = rscu_support.chart_autosave.get()                  # bool
    chart_format = rscu_support.chart_format.get().lower()              # string

    start_year = rscu_support.start_year.get()                          # int
    start_month = rscu_support.start_month.get()                        # int
    start_day = rscu_support.start_day.get()                            # int
    start_hour = rscu_support.start_hour.get()                          # int
    start_minute = rscu_support.start_minute.get()                      # int
    start_second = rscu_support.start_second.get()                      # int
    duration = rscu_support.duration.get()                              # int

    s_component = rscu_support.seismogram_component.get().upper()       # string
    filter_type = rscu_support.seismogram_filter_type.get().lower()     # string
    s_filter_max_freq = rscu_support.seismogram_filter_max_frequency.get()  # string
    s_filter_min_freq = rscu_support.seismogram_filter_min_frequency.get()  # string
    filter_zerophase = rscu_support.seismogram_filter_zerophase.get()   # bool
    filter_corners = rscu_support.seismogram_filter_corners.get()       # int
    s_chart_title = rscu_support.seismogram_chart_title.get()           # string
    s_chart_filename = rscu_support.seismogram_chart_filename.get()     # wtring 

#
# dosome minimal validation
#

    if( not rscu_validate.validate_component(v_component=s_component, v_seis=True) ):
        return()

    if( filter_type not in ['none', 'bandpass', 'bandstop', 'lowpass', 'highpass'] ):  # Filter the wave if specified
        tk.messagebox.showwarning('invalid Filter Type', 'The filter type must be one of "lowpass", "highpass", "bandpass", "bandstop", or "none"')
        return()
    elif( filter_type in ['bandpass', 'bandstop'] ):
        if( rscu_validate.validate_minmax(v_min=s_filter_min_freq, v_max=s_filter_max_freq, v_label='frequency') ):
            filter_min_freq = float(s_filter_min_freq)
            filter_max_freq = float(s_filter_max_freq)
        else:
            return()
    elif( filter_type == 'lowpass' ):
        filter_max_freq = rscu_validate.validate_stringtofloat(s_filter_max_freq)
        if( filter_max_freq == 0 ):
            tk.messagebox.showwarning('Invalid Frequency Value', 'The frequency must be a non-zero, positive number')
            return()
    elif( filter_type == 'highpass' ):
        filter_min_freq = rscu_validate.validate_stringtofloat(s_filter_min_freq)
        if( filter_min_freq == 0 ):
            tk.messagebox.showwarning('Invalid Frequency Value', 'The frequency must be a non-zero, positive number')
            return()
    
#
# Define the start and end times, the chart title, and the output file name
#

    if( rscu_validate.validate_date_time(v_year=start_year, v_month=start_month, v_day=start_day, v_hour=start_hour, v_minute=start_minute, v_second=start_second) ):
        start_time = UTCDateTime(datetime(start_year, start_month, start_day, start_hour, start_minute, start_second))
        end_time = start_time + timedelta(seconds=duration)
    else:
        return()        

#    chart_title = rscu_resolvetags.resovle_tags(s_chart_title, start_time, end_time, s_component)
    if( chart_autosave ):                                               # Only need to resolve filename if chart is auto-saved
        chart_filename = rscu_resolvetags.resovle_tags(s_chart_filename, start_time, end_time, s_component).replace(':','-').replace('?','x') + '.' + chart_format
        if( not rscu_support.validate ):
            return()                                                    # Return without generating chart if auto-save filename is invalid
        plot_full_path_name = os.path.join(rscu_support.chart_save_directory, chart_filename).replace('\\', '/')

#
# Determine the wave data source and retrieval mechanism
#

    if( wave_source_type == 'rs' ):
        from obspy.clients.earthworm import Client                      # If the wave data is from a local Raspberry shake, use the OWS server client
        rs = Client(wave_source, wave_source_port)                      #   Tell ObsPy where to look for Raspberry Shake data (Note we are using the OWS port, 16032, instead of the standard WWS (Winston Wave Server) port, 16022)
    else:
        from obspy.clients.fdsn import Client                           # If the wave data is from the FDSN nework, use the FDSN client
        rs = Client(base_url=wave_source)                               #   Tell ObsPy where to look for the wave data

#
# Finally, get the data
#

    waves = rs.get_waveforms('AM', rs_station, '00', s_component, start_time, end_time)  # Get wave data (data source, eather local form the Raspberry Shake OWS or from the FDSN network, as determined above)

#
# Apply any specified filter and then plot the seismogram using ObsPy
#

#    sampling_rate = waves[0].stats.sampling_rate                        #   Get the sampling rate from the wave data
    if( filter_type in ['bandpass', 'bandstop'] ):
        waves.filter(filter_type, freqmin=filter_min_freq, freqmax=filter_max_freq, zerophase=filter_zerophase, corners=filter_corners) # Apply bandpass or bandstop filter, the filtered stream replaces the original stream
    elif( filter_type == 'lowpass' ):
        waves.filter(filter_type, freq=filter_max_freq, zerophase=filter_zerophase, corners=filter_corners)  # Apply lowpass filter, the filtered stream replaces the original stream
    elif( filter_type == 'highpass' ):
        waves.filter(filter_type, freq=filter_min_freq, zerophase=filter_zerophase, corners=filter_corners)  # Apply highpass filter, the filtered stream replaces the original stream

        
    if( chart_autosave ):
        waves.plot(outfile=plot_full_path_name, format=chart_format, size=(pixels_tall,pixels_wide), equal_scale=True, linewidth=0.5)  # Plot the seismogram (waveform)
    waves.plot(outfile=None, format=None, size=(pixels_tall,pixels_wide), equal_scale=True, linewidth=0.5)  # Plot the seismogram (waveform)
