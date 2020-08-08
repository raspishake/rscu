import os
from datetime import datetime, timedelta

from obspy import UTCDateTime
import matplotlib.pyplot as plt

from rscu import rscu_support
from rscu import rscu_resolvetags
from rscu import rscu_validate

def plot_spectrograph_chart():

#
# Collect input from GUI
#

    rs_station = rscu_support.rs_station.get().upper()                  # string
    station_component = rscu_support.station_component.get().upper()    # string
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
    
    s_max_freq = rscu_support.spectrum_max_frequency.get()              # str
    s_min_freq = rscu_support.spectrum_min_frequency.get()              # str
    log_frequency = rscu_support.spectrum_log_frequency.get()           # bool
    log_intensity = rscu_support.spectrum_log_intensity.get()           # bool
    autoscale_intensity = rscu_support.spectrum_autoscale_intensity.get() # bool
    s_max_intensity = rscu_support.spectrum_max_intensity.get()         # str
    s_min_intensity = rscu_support.spectrum_min_intensity.get()         # str
    s_chart_title = rscu_support.spectrum_chart_title.get()             # str
    s_chart_filename = rscu_support.spectrum_chart_filename.get()       # str

#
# Set the plot size
#

    inches_tall = pixels_tall / 120.0                                   # Convert pixels to inches for plotting with Matplotlib, assume 120 dpi
    inches_wide = pixels_wide / 120.0

#
# Do some minimal validation
#

    if( not rscu_validate.validate_component(v_component=station_component) ):
        return()

    if( rscu_validate.validate_minmax(v_min=s_min_freq, v_max=s_max_freq, v_label='frequency', v_log=log_frequency) ):
        min_freq = float(s_min_freq)
        max_freq = float(s_max_freq)
    else:
        return()
    
    if( not autoscale_intensity ):
        if( rscu_validate.validate_minmax(v_min=s_min_intensity, v_max=s_max_intensity, v_label='intensity', v_log=log_intensity) ):
            min_intensity = float(s_min_intensity)
            max_intensity = float(s_max_intensity)
        else:
            return()
    
#
# Define the start and end times, the chart title, and the output file name
#

    if( rscu_validate.validate_date_time(v_year=start_year, v_month=start_month, v_day=start_day, v_hour=start_hour, v_minute=start_minute, v_second=start_second) ):
        start_time = UTCDateTime(datetime(start_year, start_month, start_day, start_hour, start_minute, start_second))
        end_time = start_time + timedelta(seconds=duration)
    else:
        return()

    chart_title = rscu_resolvetags.resovle_tags(s_chart_title, start_time, end_time, station_component)
    if( chart_autosave ):                                               # Only need to resolve filename if chart is auto-saved
        chart_filename = rscu_resolvetags.resovle_tags(s_chart_filename, start_time, end_time, station_component).replace(':','-') + '.' + chart_format
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
# Finally, get the data from from Raspberry Shake OSOP Wave Server (OWS) using ObsPy earthworm client 
#

    waves = rs.get_waveforms('AM', rs_station, '00', station_component, start_time, end_time) # Get data from Raspberry Shake wave server

#
# Initialize the figure and spectrum axes
#

    fig = plt.figure(figsize=(inches_wide,inches_tall), dpi=120)        # Figure size in inches (required by Matplotlib), raster resolution in pixels (dots) per inch

    ax = fig.add_axes([0.12, 0.09, 0.82, 0.80], ylabel='Power', title=chart_title)  # Chart axes as a proportion of the Figure dimensions [left bottom width height]

    if ( log_frequency ):
        plt.xscale('log')                                               # Set the frequency scale to log or linear
    else:
        plt.xscale('linear')

    ax.set_xlim(min_freq, max_freq)                                     # Set the frequency scale to either the default limits (0.006, 30.0) or the user specified limits

    if ( log_intensity ):
        plt.yscale('log')                                               # Set the power scale to log or linear
    else:
        plt.yscale('linear')

    if ( not autoscale_intensity ):
        ax.set_ylim(min_intensity, max_intensity)                       # Set the power scale to specified limits if theu were given on the command line

    plt.grid(which='both')                                              # Show major and minor gridlines

    Fs = waves[0].stats.sampling_rate
    plt.magnitude_spectrum(waves[0], Fs=Fs, linewidth=0.25)             # Generate the spectrograph using Matplotlib "magnitude_spectrum"

    if ( chart_autosave ):
        plt.savefig(fname=plot_full_path_name, format=chart_format, orientation='landscape')  # Save the image file - "orientation" only applies if format="pdf"
    plt.show()
