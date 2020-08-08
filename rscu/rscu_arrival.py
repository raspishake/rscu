import os
from datetime import datetime, timedelta

from obspy.taup import TauPyModel
from obspy.taup.tau import plot_ray_paths
from obspy import UTCDateTime

import tkinter as tk
import matplotlib.pyplot as plt
import math

from rscu import rscu_support
from rscu import rscu_resolvetags
from rscu import rscu_arrivaldata
from rscu import rscu_arrivaldata_support
from rscu import rscu_validate

def calc_arrival_raypath():

#
# Collect input from GUI
#

    rs_station = rscu_support.rs_station.get().upper()                  # string
    station_component = rscu_support.station_component.get().upper()    # string
    pixels_wide = rscu_support.pixels_wide.get()                        # int
    pixels_tall = rscu_support.pixels_tall.get()                        # int
    chart_autosave = rscu_support.chart_autosave.get()                  # bool
    chart_format = rscu_support.chart_format.get().lower()              # string
    a_station_latitude = rscu_support.station_latitude.get()            # string
    a_station_longitude = rscu_support.station_longitude.get()          # string

    event_year = rscu_support.event_year.get()                          # int
    event_month = rscu_support.event_month.get()                        # int
    event_day = rscu_support.event_day.get()                            # int
    event_hour = rscu_support.event_hour.get()                          # int
    event_minute = rscu_support.event_minute.get()                      # int
    event_second = rscu_support.event_second.get()                      # int
    a_event_latitude = rscu_support.event_latitude.get()                # string
    a_event_longitude = rscu_support.event_longitude.get()              # string
    a_event_depth = rscu_support.event_depth.get()                      # string

    a_phase_list = rscu_support.arrival_phase_list.get()                # string
    ray_path_type = rscu_support.arrival_ray_path_type.get()            # string
    show_legend = rscu_support.arrival_show_legend.get()                # bool
    annotate = rscu_support.arrival_annotate.get()                      # bool
    a_chart_title = rscu_support.arrival_chart_title.get()              # string
    a_chart_filename = rscu_support.arrival_chart_filename.get()        # string
    

#
# Validate the station and event location
#

    station_latitude = rscu_validate.validate_stringtofloat(a_station_latitude)
    station_longitude = rscu_validate.validate_stringtofloat(a_station_longitude)
    event_latitude = rscu_validate.validate_stringtofloat(a_event_latitude)
    event_longitude = rscu_validate.validate_stringtofloat(a_event_longitude)
    event_depth = rscu_validate.validate_stringtofloat(a_event_depth)

    if ((station_latitude < -99.0 or station_latitude > 90.0) or (station_longitude < -180 or station_longitude > 180.0)):
        tk.messagebox.showwarning("Invalid Station Lat/Lon","The Station Latitude or Longitude is not valid.\nLatitude values must be between -90.0 and +90.0.\nLongitude values must be between -180.0 and +180.0.")
        return()
    elif ((event_latitude < -99.0 or event_latitude > 90.0) or (event_longitude < -180 or event_longitude > 180.0)):
        tk.messagebox.showwarning("Invalid Event Lat/Lon","The Event Latitude or Longitude is not valid.\nLatitude values must be between -90.0 and +90.0.\nLongitude values must be between -180.0 and +180.0.")
        return()

#
# Set the plot size
#

    inches_tall = pixels_tall / 120.0                                   # Convert pixels to inches for plotting with Matplotlib, assume 120 dpi
    inches_wide = pixels_wide / 120.0

#
# Event UTC time
#
    if( rscu_validate.validate_date_time(v_year=event_year, v_month=event_month, v_day=event_day, v_hour=event_hour, v_minute=event_minute, v_second=event_second) ):
        utc_event_time = UTCDateTime(datetime(event_year, event_month, event_day, event_hour, event_minute, event_second))  # Create a DateTime object from the specified event date and time
    else:
        return()

#
# Calculate the Great Circle distance between the station and event. Note: This assumes a smooth, spherical Earth, which it is not, but it's close enough
#

    station_lat_radians = math.radians(station_latitude)                # Convert the Decimal Degree locations to Radians (required for Python trigonometry)
    station_lon_radians = math.radians(station_longitude)
    event_lat_radians = math.radians(event_latitude)
    event_lon_radians = math.radians(event_longitude)
                                                                        # Calculater the Great Circle distance between the event and station in Degrees of Arc
    event_degrees_distant = math.degrees(math.acos( (math.sin(station_lat_radians) * math.sin(event_lat_radians)) + (math.cos(station_lat_radians) * math.cos(event_lat_radians) * math.cos( (event_lon_radians) - (station_lon_radians) )) ))
    event_km_distant = event_degrees_distant * 111.133                  # Convert degrees arc to kilometers
    event_miles_distant = event_degrees_distant * 69.0548               # Convert degrees arc to miles

    rscu_support.arrival_degrees = event_degrees_distant
    rscu_support.arrival_km = event_km_distant
    rscu_support.arrival_miles = event_miles_distant

#
# Create Diagram title abd file names
#

    chart_title = rscu_resolvetags.resovle_tags(a_chart_title, utc_event_time, utc_event_time, station_component)
    if( chart_autosave ):                                               # Only need to resolve filename if chart is auto-saved
        chart_filename = rscu_resolvetags.resovle_tags(a_chart_filename, utc_event_time, utc_event_time, station_component).replace(':','-')
        if( not rscu_support.validate ):
            return()                                                    # Return without generating chart if auto-save filename is invalid
        data_filename = chart_filename + '.csv'
        chart_filename = chart_filename + '.' + chart_format
        plot_full_path_name = os.path.join(rscu_support.chart_save_directory, chart_filename).replace('\\', '/')
        data_full_path_name = os.path.join(rscu_support.data_save_directory, data_filename).replace('\\', '/')

#
# Calculate the travel times and arrival times for the specified phases
#

    event_phase_list = a_phase_list.split(',')
    model = TauPyModel(model='iasp91')                                  # Designate the iasp91 model for calculating phase travel times
    arrival_times = model.get_travel_times(source_depth_in_km=event_depth, distance_in_degree=event_degrees_distant, phase_list=event_phase_list) # Use ObsPy's "get_travel_times" to calculate the travel times for the specified phases

#
# Format text for both the output window and the csv file
#
    data_out = 'Station,Event Date (UTC),Event Time (UTC)\n' + rs_station + ',' + utc_event_time.strftime('%Y-%m-%d,%H:%M:%S.%f') + '\nStation Latitude,Station Longitude\n' + str(station_latitude) + ',' + str(station_longitude)
    data_out = data_out + '\nEvent Latitude,Event Longitude,Event Depth (km)\n' + str(event_latitude) + ',' + str(event_longitude) + ',' + str(event_depth)
    data_out = data_out + '\nDistance in Degrees Arc,Distance in km,Distans in Miles\n' + str('{:.5f}'.format(event_degrees_distant)) + ',' + str('{:.3f}'.format(event_km_distant)) + ',' + str('{:.3f}'.format(event_miles_distant))

    data_text = 'Great Circle distance from the event at '+ str('{:.5f}'.format(event_latitude)) + ', ' + str('{:.5f}'.format(event_longitude)) + ' to ' + rs_station + ':\n'
    data_text = data_text + '   Degrees distant:    ' + str('{:.5f}'.format(event_degrees_distant)) + '\n'
    data_text = data_text + '   Kilometers distant: ' + str('{:.3f}'.format(event_km_distant)) + '\n'
    data_text = data_text + '   Miles distant:      ' + str('{:.3f}'.format(event_miles_distant)) + '\n\n'
    data_text = data_text + 'The event occurred at ' + utc_event_time.strftime('%Y-%m-%d %H:%M:%S.%f') + ' UTC.\n'

    if ( len(arrival_times) == 0 ):                                     # Don't look for any phase arriva data if if there are none (the distant to the event is still shown)
        data_text = data_text + '   No arrival times were calculated (the event was either too close to the station, or not visible with chosen phases)'
        data_out = data_out + '\nNo arrival times were calculated for the requested phases (the event was either too close to the station, or not visible with chosen phases)'
    else:
        data_out = data_out + '\nPhase,Arrival Date (UTC),Arrival Time (UTC),Travel Time (seconds)'
        for i in range(len(arrival_times)):                             # Setp through the phase arrivals and calculate the arrival times by adding the travel time to the event time
            utc_arrival_time = utc_event_time + timedelta(seconds=arrival_times[i].time)
            data_text = data_text + '   Arrival of ' + arrival_times[i].name + ' phase expected at ' + utc_arrival_time.strftime('%Y-%m-%d %H:%M:%S') + ', ' + str('{:.3f}'.format(arrival_times[i].time)) + ' seconds after the initial event.\n'
            data_out = data_out + '\n' + arrival_times[i].name + ',' + utc_arrival_time.strftime('%Y-%m-%d,%H:%M:%S.%f') + ',' + str('{:.6f}'.format(arrival_times[i].time))
        
    if( chart_autosave ):
        rf = open(data_full_path_name, 'w')
        rf.write(data_out)
        rf.close

    rscu_arrivaldata_support.data_text = data_text
    rscu_arrivaldata_support.data_out = data_out
    rscu_arrivaldata.create_arrival_data_window(rscu_support.root)

#
# Plot a ray path diagram showing the paths from the event to the station of the specified phases
#

    if ( len(arrival_times) > 0 ):                                      # Don't ty to generate any ray paths if there are no phases
        fig = plt.figure(figsize=(inches_wide,inches_tall), dpi=120)        # Figure size (width, height) in inches, raster resolution in pixels (dots) per inch
        arrivals = model.get_ray_paths(event_depth, event_degrees_distant, phase_list=event_phase_list)   # Generate the phase ray paths
        ax = arrivals.plot_rays(show=False, plot_type=ray_path_type, legend=show_legend, fig=fig)
        ax.set_title(chart_title)

# Annotate diagram

        if( annotate and (ray_path_type == 'spherical') ):
            ax.text(0, 0, 'Solid\ninner\ncore', horizontalalignment='center', verticalalignment='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
            ocr = (model.model.radius_of_planet - (model.model.s_mod.v_mod.iocb_depth + model.model.s_mod.v_mod.cmb_depth) / 2)
            ax.text(math.radians(180), ocr, 'Fluid outer core', horizontalalignment='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
            mr = model.model.radius_of_planet - model.model.s_mod.v_mod.cmb_depth / 2
            ax.text(math.radians(180), mr, 'Solid mantle', horizontalalignment='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
            ax.text(math.radians(30), (model.model.radius_of_planet * 1.045), '30°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(60), (model.model.radius_of_planet * 1.06), '60°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(90), (model.model.radius_of_planet * 1.065), '90°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(120), (model.model.radius_of_planet * 1.08), '120°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(150), (model.model.radius_of_planet * 1.08), '150°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(180), (model.model.radius_of_planet * 1.07), '180°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(210), (model.model.radius_of_planet * 1.08), '150°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(240), (model.model.radius_of_planet * 1.08), '120°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(270), (model.model.radius_of_planet * 1.065), '90°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(300), (model.model.radius_of_planet * 1.06), '60°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(330), (model.model.radius_of_planet * 1.045), '30°', fontsize='x-small', color='blue', horizontalalignment='center')
            ax.text(math.radians(103), (model.model.radius_of_planet * 1.08), '103°', fontsize='x-small', color='red', horizontalalignment='center')
            ax.text(math.radians(257), (model.model.radius_of_planet * 1.08), '103°', fontsize='x-small', color='red', horizontalalignment='center')
            ax.text(math.radians(140), (model.model.radius_of_planet * 1.08), '140°', fontsize='x-small', color='orange', horizontalalignment='center')
            ax.text(math.radians(220), (model.model.radius_of_planet * 1.08), '140°', fontsize='x-small', color='orange', horizontalalignment='center')
            ax.text(math.radians(event_degrees_distant), (model.model.radius_of_planet * 1.12), 'AM.' + rs_station + '.00', fontsize='medium', horizontalalignment='left')

# Display and save the ray path diagram

        if( chart_autosave ):
            plt.savefig(fname=plot_full_path_name, format=chart_format, orientation='landscape')  # "orientation" only applies for pdf files
        plt.show()
    
