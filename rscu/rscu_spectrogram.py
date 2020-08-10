import os
from datetime import datetime, timedelta

from obspy.imaging.spectrogram import spectrogram
from obspy import UTCDateTime
import matplotlib.pyplot as plt
import numpy as np

from rscu import rscu_support
from rscu import rscu_resolvetags
from rscu import rscu_validate

def plot_spectrogram_chart():

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

    s_max_freq = rscu_support.spectrogram_max_frequency.get()           # string
    s_min_freq = rscu_support.spectrogram_min_frequency.get()           # string
    log_freq = rscu_support.spectrogram_log_frequency.get()             # bool
    log_color = rscu_support.spectrogram_log_color.get()             # bool
    show_seismogram = rscu_support.spectrogram_show_seismogram.get()    # bool
    show_colorbar = rscu_support.spectrogram_show_colorbar.get()        # bool
    colormap = rscu_support.spectrogram_colormap.get()                  # string
    sp_chart_title = rscu_support.spectrogram_chart_title.get()         # string
    sp_chart_filename = rscu_support.spectrogram_chart_filename.get()   # string

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

    if( rscu_validate.validate_minmax(v_min=s_min_freq, v_max=s_max_freq, v_label='frequency', v_log=log_freq) ):
        min_freq = float(s_min_freq)
        max_freq = float(s_max_freq)
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

    chart_title = rscu_resolvetags.resovle_tags(sp_chart_title, start_time, end_time, station_component)
    if( chart_autosave ):                                               # Only need to resolve filename if chart is auto-saved
        chart_filename = rscu_resolvetags.resovle_tags(sp_chart_filename, start_time, end_time, station_component).replace(':','-') + '.' + chart_format
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
# Finally, get the data 
#

    waves = rs.get_waveforms('AM', rs_station, '00', station_component, start_time, end_time)  # Get wave data (data source, eather local form the Raspberry Shake OWS or from the FDSN network, as determined above)

#
# And create the figure using Matplotlib and ObsPy
#

    fig = plt.figure(figsize=(inches_wide,inches_tall), dpi=120)        # Figure size (width, height) in inches, raster resolution in pixels (dots) per inch

    if( show_colorbar and show_seismogram ):                            # Define sub-plot area with both the seismogram and frequency intensity color scale bar
        ax1 = fig.add_axes([0.14, 0.74, 0.70, 0.20], ylabel='Counts', title=chart_title)   # Chart axes as a proportion of the Figure dimensions [left bottom width height], ax1 is the seismogram
        ax2 = fig.add_axes([0.14, 0.09, 0.70, 0.60], sharex=ax1, ylabel='Frequency (Hz)', xlabel='Time (seconds)')  # ax2 is the spectrogram and shares the x-axis with ax1
        ax3 = fig.add_axes([0.87, 0.09, 0.03, 0.60])                    # ax3 is the colorbar
    elif( show_seismogram ):                                            # Define sub-plot area without the frequency intensity color scale bar
        ax1 = fig.add_axes([0.14, 0.74, 0.76, 0.20], ylabel='Counts', title=chart_title)   # Chart axes as a proportion of the Figure dimensions [left bottom width height], ax1 is the seismogram
        ax2 = fig.add_axes([0.14, 0.09, 0.76, 0.60], sharex=ax1, ylabel='Frequency (Hz)', xlabel='Time (seconds)')  # ax2 is the spectrogram and shares the x-axis with ax1
    elif( show_colorbar ):                                              # Define sub-plot area without the seismogram
        ax2 = fig.add_axes([0.14, 0.09, 0.70, 0.81], ylabel='Frequency (Hz)', xlabel='Time (seconds)', title=chart_title)   # Chart axes as a proportion of the Figure dimensions [left bottom width height], ax1 is the spectrogram
        ax3 = fig.add_axes([0.87, 0.09, 0.03, 0.81])                    # ax3 is the colorbar
    else:                                                               # Define sub-plot area with the spectrogram only
        ax2 = fig.add_axes([0.14, 0.09, 0.76, 0.81], ylabel='Frequency (Hz)', xlabel='Time (seconds)', title=chart_title)   # Chart axes as a proportion of the Figure dimensions [left bottom width height], ax1 is the spectrogram

    t = np.arange(waves[0].stats.npts) / waves[0].stats.sampling_rate   # Map time to x-axis values

    if( show_seismogram ):
        ax1.plot(t, waves[0].data, 'k', linewidth=0.5)                  # Plot the seismogram (waveform) as the top subfigure (ax1)

    fig = waves[0].spectrogram(show=False, log=log_freq, axes=ax2, cmap=colormap, dbscale=log_color)  # Plot the spectrogram as the bottom subfigure (ax2)

    if ( log_freq ):
        mappable = ax2.collections[0]                                   # To calculate the color bar, log plots use "matplotlib.collections.QuadMesh"
    else:
        mappable = ax2.images[0]                                        #   Linear plots use "matplotlib.image.AxesImage"

    if ( show_colorbar ):                                               # Plot the colorbar to the side of the spectrogram (ax3)
        plt.colorbar(mappable=mappable, cax=ax3)

    ax2.set_ylim(min_freq, max_freq)                                    # Set the frequency range for the spectrogram

    if( chart_autosave ):
        plt.savefig(fname=plot_full_path_name, format=chart_format, orientation='landscape')  # Save the image file - "orientation" only applies if format="pdf"
    plt.show()
