import tkinter as tk

from rscu import rscu_support

def resovle_tags(string_to_resolve, start_time, end_time, component):
    '''
    Replaces the tagged keys in the Title and File Name strings with the
    corresponding value.

    :param string "string_to_resolve": input string containg tagged keys
       to resolve.
    :param datetime "start_time": start time.
    :param datetime "end_time": end time (both start and end times are
       the event time in the case of the Arrival tab).
    :param string "Component": the station component.
    :return: resoved_string: String qith the tagged keys resolved.
    :rtype: str
    '''    

    try:
        rscu_support.arrival_degrees                                    # For all tabs except the Arrival tab, the degrees, km, and miles may not yet be calculated, If these values do not exist, set them to 0.
    except AttributeError:
        rscu_support.arrival_degrees = 0
        rscu_support.arrival_km = 0
        rscu_support.arrival_miles = 0
    
    kwords = {'station': rscu_support.rs_station.get().upper(),
        'component': component,
        'full_station': 'AM.' + rscu_support.rs_station.get().upper() + ".00." + rscu_support.station_component.get().upper(),
        'start_date': start_time.strftime("%Y-%m-%d"),
        'end_date': end_time.strftime("%Y-%m-%d"),
        'start_datetime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'end_datetime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'duration': rscu_support.duration.get(),
        'degrees': str('{:.3f}'.format(rscu_support.arrival_degrees)),
        'km': str('{:.3f}'.format(rscu_support.arrival_km)),
        'miles': str('{:.3f}'.format(rscu_support.arrival_miles)),
        'event_lat': rscu_support.event_latitude.get(),
        'event_lon': rscu_support.event_longitude.get(),
        'event_date': start_time.strftime("%Y-%m-%d"),
        'event_datetime': start_time.strftime("%Y-%m-%dT%H:%M:%S")}
    
    try:
        resolved_string = string_to_resolve.format(**kwords)
    except KeyError as Argument:
        tk.messagebox.showwarning("Unknown Tag","Cannot resolve the chart title or file name because a tag," + str(Argument) + ", was used that does not match any of the available tags.")
        resolved_string = string_to_resolve
        rscu_support.chart_autosave.set(False)
    except ValueError:
        tk.messagebox.showwarning("Tag Error","Cannot resolve the chart title or file name because of an unbalanced tag (missing '}').")
        resolved_string = string_to_resolve
        rscu_support.chart_autosave.set(False)
    
    return(resolved_string)
