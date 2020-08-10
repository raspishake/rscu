import sys, os
import json

from rscu import rscu_support

def init_settings():
    '''
    Loads settings to start the main window.
    '''
    global settings

    default_loc = get_settings_loc()
    settings_loc = os.path.join(default_loc, 'rscu_settings.json').replace('\\', '/')
    settings = json.loads(default_settings())
    test_settings_loc(default_loc, settings_loc)
    settings = read_settings(settings_loc)
    test_rscu_save_directory(settings['common']['rscu_save_directory'])
    return settings
    
def get_settings_loc():
    '''
    Determine the OS-specific location for the rs_settings.json file

    :return: user-relative path to the directory containing the
       rscu_settings.json file
    :rtype: str
    '''
    if( sys.platform.startswith('linux') ):
        default_loc = '~/.config/rscu/'
    elif( sys.platform.startswith('darwin') ):
        default_loc = '~/Library/Application Support/rscu/'
    elif( sys.platform.startswith('win') ):
        default_loc = '~/AppData/Local/rscu/'                           # I -think- this is where I should put the json file on windows...
    else:
        default_loc = sys.path[0]                                       # Save the json file with the application on all other systems
    return(default_loc)

def test_settings_loc(default_loc, settings_loc):
    '''
    Check to see if the rscu_settings.json file exists. If not, create
    the appropriate location and save the def_settings as rscu_settings.json.
    This function is called -after- the default settings are read, but
    -before- attempting to load the rscu_settings.json file - for obvious
    reasons.

    :param str default_loc: user-relative directory that should contain
       the json settings file
    :param str settings_loc: user-relative path to the json settings file
    '''
    default_path=os.path.abspath(os.path.expanduser(default_loc)).replace('\\', '/')
    settings_path=os.path.abspath(os.path.expanduser(settings_loc)).replace('\\', '/')
    if( not os.path.exists(settings_path) ):                            # Test to see if the rscu_settings.json file exists
        if( not os.path.exists(default_path) ):                         #   If not, test to see if the settings directory exists
            os.mkdir(default_path, 0o755)                               #     If no directory, create it 
        write_settings(settings_path)                                   #   Once the directory exists,write the rscu_settings.json file 

def get_default_save_loc():
    '''
    Determine the OS-specific location for the chart save directory

    :return: user-relative path to the chart save directory
    :rtype: str
    '''
    if( sys.platform.startswith('linux') ):
        def_chart_save_loc = '~/rscu/'
    elif( sys.platform.startswith('darwin') ):
        def_chart_save_loc = '~/Documents/rscu/'
    elif( sys.platform.startswith('win') ):
        def_chart_save_loc = '~/Documents/rscu/'                        # Windows 10 and up...
    else:
        def_chart_save_loc = '~/rscu/'
    return(def_chart_save_loc)

def test_rscu_save_directory(loc):
    '''
    Check to see if the chart save directory specified in the rscu_settings.json
    file exists. If not, create it. This function is called only -after-
    the settings file is loaded in case the user has changed the location
    of the chart save directory.

    :param str loc: user-relative directory designated for saving charts
    '''
    data_loc=os.path.join(loc, 'data/').replace('\\', '/')
    chart_loc=os.path.join(loc, 'charts').replace('\\', '/')
    chart_save_loc=os.path.abspath(os.path.expanduser(chart_loc)).replace('\\', '/')
    data_save_loc=os.path.abspath(os.path.expanduser(data_loc)).replace('\\', '/')
    if( not os.path.exists(chart_save_loc) ):
        os.makedirs(chart_save_loc, 0o755)
    if( not os.path.exists(data_save_loc) ):
        os.mkdir(data_save_loc, 0o755)

def read_settings(loc):
    '''
    Reads settings from a specific location.

    :param str loc: location on disk from which to read json settings file
    :return: settings dictionary read from JSON, or ``None``
    :rtype: dict or NoneType
    '''
    settings_loc = os.path.abspath(os.path.expanduser(loc)).replace('\\', '/')
    print('rscu_settings.read_settings, settings_loc:', settings_loc)
    settings = None
    with open(settings_loc, 'r') as f:
        data = f.read().replace('\\', '/')
        settings = json.loads(data)
    return settings

def write_settings(loc):
    '''
    Writes settings to a specific location.

    :param str loc: location on disk to which to write json settings file
    '''
    settings_loc = os.path.abspath(os.path.expanduser(loc)).replace('\\', '/')
    print('rs_settings.write_settings, settings_loc:', settings_loc)
    with open(settings_loc, 'w') as f:
        json.dump(settings, f, indent=4)

def default_settings():
    '''
    Returns a formatted json string of default settings.

    :return: default settings string in formatted json
    :rtype: str
    '''

    global def_settings

    rscu_save_dir=os.path.abspath(os.path.expanduser(get_default_save_loc())).replace('\\', '/')

    def_settings = r"""{
"common": {
    "rs_station": "Rxxxx",
    "station_component": "EHZ",
    "station_latitude": 37.22888,
    "station_longitude": -115.81113,
    "wave_source_type": "fsdn",
    "wave_source": "https://fdsnws.raspberryshakedata.com",
    "wave_source_port": 16032,
    "rscu_save_directory": "%s",
    "pixels_wide": 1200,
    "pixels_tall": 900,
    "duration": 120,
    "chart_autosave": true,
    "chart_format": "png",
    "verbose": false},
"helicorder": {
    "helicorder_minutes_per_line": 30,
    "helicorder_hours_per_chart": 24,
    "helicorder_vertical_scaling": "auto",
    "helicorder_line1_color": "#B2000F",
    "helicorder_line2_color": "#020208",
    "helicorder_line3_color": "#004C12",
    "helicorder_line4_color": "#0E01FF",
    "helicorder_chart_title": "AM.{station}.00.{component} - {start_date} UTC",
    "helicorder_chart_filename": "helicorder-{station}-{component}-{start_date}"},
"seismogram": {
    "seismogram_component": "EH?",
    "seismogram_filter_type": "none",
    "seismogram_filter_max_frequency": 30.0,
    "seismogram_filter_min_frequency": 0.2,
    "seismogram_filter_zerophase": true,
    "seismogram_filter_corners": 2,
    "seismogram_chart_title": "AM.{station}.00.{component} - {start_datetime} - {end_datetime} UTC",
    "seismogram_chart_filename": "seismogram-{station}-{component}-{start_datetime}-{duration}"},
"spectrogram": {
    "spectrogram_max_frequency": 25.0,
    "spectrogram_min_frequency": 0.05,
    "spectrogram_log_frequency": false,
    "spectrogram_log_color": true,
    "spectrogram_show_seismogram": true,
    "spectrogram_show_colorbar": true,
    "spectrogram_colormap": "nipy_spectral",
    "spectrogram_chart_title": "AM.{station}.00.{component} - {start_datetime} to {end_datetime} UTC",
    "spectrogram_chart_filename": "spectrogram-{station}-{component}-{start_datetime}-{duration}"},
"spectrograph": {
    "spectrum_max_frequency": 30.0,
    "spectrum_min_frequency": 0.006,
    "spectrum_log_frequency": true,
    "spectrum_log_intensity": true,
    "spectrum_autoscale_intensity": true,
    "spectrum_chart_title": "AM.{station}.00.{component} - {start_datetime} to {end_datetime} UTC",
    "spectrum_chart_filename": "spectrum-{station}-{component}-{start_datetime}-{duration}"},
"arrival": {
    "arrival_phase_list": ["P","S"],
    "arrival_ray_path_type": "spherical",
    "arrival_show_legend": true,
    "arrival_annotate": true,
    "arrival_chart_title": "AM.{station}.00 - Ray Paths {degrees} degrees distant from {event_lat} latitude, {event_lon} longitude",
    "arrival_chart_filename": "arrivals-{station}-{event_datetime}"}
}

""" % (rscu_save_dir)
    return def_settings

def main_menu_save_prefs():
    '''
    Saves all of the user-defined settings to a .json file when
    "Save Preferences" is selected from the File menu.
    '''
    if( rscu_support.verbose ):
        print('rscu_support.main_menu_save_prefs')
    settings['common']['rs_station'] = rscu_support.rs_station.get()
    settings['common']['station_component'] = rscu_support.station_component.get()
    settings['common']['station_latitude'] = float(rscu_support.station_latitude.get())
    settings['common']['station_longitude'] = float(rscu_support.station_longitude.get())
    settings['common']['wave_source_type'] = rscu_support.wave_source_type
    settings['common']['wave_source'] = rscu_support.wave_source
    settings['common']['wave_source_port'] = int(rscu_support.wave_source_port)
    settings['common']['rscu_save_directory'] = rscu_support.rscu_save_directory.get()
    settings['common']['pixels_wide'] = int(rscu_support.pixels_wide.get())
    settings['common']['pixels_tall'] = int(rscu_support.pixels_tall.get())
    settings['common']['duration'] = int(rscu_support.duration.get())
    settings['common']['chart_autosave'] = bool(rscu_support.chart_autosave.get())
    settings['common']['chart_format'] = rscu_support.chart_format.get()
    settings['common']['verbose'] = bool(rscu_support.verbose)
    settings['helicorder']['helicorder_minutes_per_line'] = int(rscu_support.helicorder_minutes_per_line.get())
    settings['helicorder']['helicorder_hours_per_chart'] = int(rscu_support.helicorder_hours_per_chart.get())
    if( rscu_support.helicorder_auto_vertical_scaling.get() or (rscu_support.helicorder_vertical_scaling.get() == "") ):
        settings['helicorder']['helicorder_vertical_scaling'] = 'auto'
    else:
        settings['helicorder']['helicorder_vertical_scaling'] = rscu_support.helicorder_vertical_scaling.get()
    settings['helicorder']['helicorder_line1_color'] = rscu_support.helicorder_line1_color.get()
    settings['helicorder']['helicorder_line2_color'] = rscu_support.helicorder_line2_color.get()
    settings['helicorder']['helicorder_line3_color'] = rscu_support.helicorder_line3_color.get()
    settings['helicorder']['helicorder_line4_color'] = rscu_support.helicorder_line4_color.get()
    settings['helicorder']['helicorder_chart_title'] = rscu_support.helicorder_chart_title.get()
    settings['helicorder']['helicorder_chart_filename'] = rscu_support.helicorder_chart_filename.get()
    settings['seismogram']['seismogram_component'] = rscu_support.seismogram_component.get()
    settings['seismogram']['seismogram_filter_type'] = rscu_support.seismogram_filter_type.get().lower()
    settings['seismogram']['seismogram_filter_max_frequency'] = float(rscu_support.seismogram_filter_max_frequency.get())
    settings['seismogram']['seismogram_filter_min_frequency'] = float(rscu_support.seismogram_filter_min_frequency.get())
    settings['seismogram']['seismogram_filter_zerophase'] = bool(rscu_support.seismogram_filter_zerophase.get())
    settings['seismogram']['seismogram_filter_corners'] = int(rscu_support.seismogram_filter_corners.get())
    settings['seismogram']['seismogram_chart_title'] = rscu_support.seismogram_chart_title.get()
    settings['seismogram']['seismogram_chart_filename'] = rscu_support.seismogram_chart_filename.get()
    settings['spectrogram']['spectrogram_max_frequency'] = float(rscu_support.spectrogram_max_frequency.get())
    settings['spectrogram']['spectrogram_min_frequency'] = float(rscu_support.spectrogram_min_frequency.get())
    settings['spectrogram']['spectrogram_log_frequency'] = bool(rscu_support.spectrogram_log_frequency.get())
    settings['spectrogram']['spectrogram_log_color'] = bool(rscu_support.spectrogram_log_color.get())
    settings['spectrogram']['spectrogram_show_seismogram'] = bool(rscu_support.spectrogram_show_seismogram.get())
    settings['spectrogram']['spectrogram_show_colorbar'] = bool(rscu_support.spectrogram_show_colorbar.get())
    settings['spectrogram']['spectrogram_colormap'] = rscu_support.spectrogram_colormap.get()
    settings['spectrogram']['spectrogram_chart_title'] = rscu_support.spectrogram_chart_title.get()
    settings['spectrogram']['spectrogram_chart_filename'] = rscu_support.spectrogram_chart_filename.get()
    settings['spectrograph']['spectrum_max_frequency'] = float(rscu_support.spectrum_max_frequency.get())
    settings['spectrograph']['spectrum_min_frequency'] = float(rscu_support.spectrum_min_frequency.get())
    settings['spectrograph']['spectrum_log_frequency'] = bool(rscu_support.spectrum_log_frequency.get())
    settings['spectrograph']['spectrum_log_intensity'] = bool(rscu_support.spectrum_log_intensity.get())
    settings['spectrograph']['spectrum_autoscale_intensity'] = bool(rscu_support.spectrum_autoscale_intensity.get())
    settings['spectrograph']['spectrum_chart_title'] = rscu_support.spectrum_chart_title.get()
    settings['spectrograph']['spectrum_chart_filename'] = rscu_support.spectrum_chart_filename.get()
    settings['arrival']['arrival_phase_list'] = rscu_support.arrival_phase_list.get().split(',')
    settings['arrival']['arrival_ray_path_type'] = rscu_support.arrival_ray_path_type.get()
    settings['arrival']['arrival_show_legend'] = bool(rscu_support.arrival_show_legend.get())
    settings['arrival']['arrival_annotate'] = bool(rscu_support.arrival_annotate.get())
    settings['arrival']['arrival_chart_title'] = rscu_support.arrival_chart_title.get()
    settings['arrival']['arrival_chart_filename'] = rscu_support.arrival_chart_filename.get()
    default_loc = get_settings_loc()
    settings_loc = os.path.join(default_loc, 'rscu_settings.json').replace('\\', '/')
    write_settings(settings_loc)

def main_menu_restore_prefs():
    '''
    Restores all of the settings from the "settings" dictionary when
    "Restore Saved Preferences" is selected from the File menu.
    '''
    if( rscu_support.verbose ):
        print('rscu_support.main_menu_restore_prefs')
    rscu_support.rs_station.set(settings['common']['rs_station'])
    rscu_support.station_component.set(settings['common']['station_component'])
    rscu_support.station_latitude.set(settings['common']['station_latitude'])
    rscu_support.station_longitude.set(settings['common']['station_longitude'])
    rscu_support.wave_source_type = settings['common']['wave_source_type']
    rscu_support.wave_source = settings['common']['wave_source']
    rscu_support.wave_source_port = settings['common']['wave_source_port']
    rscu_support.rscu_save_directory.set(settings['common']['rscu_save_directory'])
    rscu_support.pixels_wide.set(settings['common']['pixels_wide'])
    rscu_support.pixels_tall.set(settings['common']['pixels_tall'])
    rscu_support.duration.set(settings['common']['duration'])
    rscu_support.chart_autosave.set(settings['common']['chart_autosave'])
    rscu_support.chart_format.set(settings['common']['chart_format'])
    rscu_support.helicorder_minutes_per_line.set(settings['helicorder']['helicorder_minutes_per_line'])
    rscu_support.helicorder_hours_per_chart.set(settings['helicorder']['helicorder_hours_per_chart'])
    if(settings['helicorder']['helicorder_vertical_scaling'] == 'auto'):
        rscu_support.helicorder_auto_vertical_scaling.set(True)
        rscu_support.helicorder_vertical_scaling_state = 'disabled'
    else:
        rscu_support.helicorder_auto_vertical_scaling.set(False)
        rscu_support.helicorder_vertical_scaling_state = 'normal'
        rscu_support.helicorder_vertical_scaling.set(settings['helicorder']['helicorder_vertical_scaling'])
    rscu_support.w.helicorder_vertical_scaling_label.configure(state=rscu_support.helicorder_vertical_scaling_state)
    rscu_support.w.helicorder_vertical_scaling_entry.configure(state=rscu_support.helicorder_vertical_scaling_state)
    rscu_support.helicorder_line1_color.set(settings['helicorder']['helicorder_line1_color'])
    rscu_support.w.helicorder_line1_color_button.configure(background=rscu_support.helicorder_line1_color.get())
    rscu_support.helicorder_line2_color.set(settings['helicorder']['helicorder_line2_color'])
    rscu_support.w.helicorder_line2_color_button.configure(background=rscu_support.helicorder_line2_color.get())
    rscu_support.helicorder_line3_color.set(settings['helicorder']['helicorder_line3_color'])
    rscu_support.w.helicorder_line3_color_button.configure(background=rscu_support.helicorder_line3_color.get())
    rscu_support.helicorder_line4_color.set(settings['helicorder']['helicorder_line4_color'])
    rscu_support.w.helicorder_line4_color_button.configure(background=rscu_support.helicorder_line4_color.get())
    rscu_support.helicorder_chart_title.set(settings['helicorder']['helicorder_chart_title'])
    rscu_support.helicorder_chart_filename.set(settings['helicorder']['helicorder_chart_filename'])
    rscu_support.seismogram_component.set(settings['seismogram']['seismogram_component'])
    rscu_support.seismogram_filter_type.set(settings['seismogram']['seismogram_filter_type'].lower())
    rscu_support.seismogram_filter_max_frequency.set(settings['seismogram']['seismogram_filter_max_frequency'])
    rscu_support.seismogram_filter_min_frequency.set(settings['seismogram']['seismogram_filter_min_frequency'])
    rscu_support.seismogram_filter_zerophase.set(settings['seismogram']['seismogram_filter_zerophase'])
    rscu_support.seismogram_filter_corners.set(settings['seismogram']['seismogram_filter_corners'])
    rscu_support.seismogram_set_filter_state(None)
    rscu_support.seismogram_chart_title.set(settings['seismogram']['seismogram_chart_title'])
    rscu_support.seismogram_chart_filename.set(settings['seismogram']['seismogram_chart_filename'])
    rscu_support.spectrogram_max_frequency.set(settings['spectrogram']['spectrogram_max_frequency'])
    rscu_support.spectrogram_min_frequency.set(settings['spectrogram']['spectrogram_min_frequency'])
    rscu_support.spectrogram_log_frequency.set(settings['spectrogram']['spectrogram_log_frequency'])
    rscu_support.spectrogram_log_color.set(settings['spectrogram']['spectrogram_log_color'])
    rscu_support.spectrogram_show_seismogram.set(settings['spectrogram']['spectrogram_show_seismogram'])
    rscu_support.spectrogram_show_colorbar.set(settings['spectrogram']['spectrogram_show_colorbar'])
    rscu_support.spectrogram_colormap.set(settings['spectrogram']['spectrogram_colormap'])
    rscu_support.spectrogram_chart_title.set(settings['spectrogram']['spectrogram_chart_title'])
    rscu_support.spectrogram_chart_filename.set(settings['spectrogram']['spectrogram_chart_filename'])
    rscu_support.spectrum_max_frequency.set(settings['spectrograph']['spectrum_max_frequency'])
    rscu_support.spectrum_min_frequency.set(settings['spectrograph']['spectrum_min_frequency'])
    rscu_support.spectrum_log_frequency.set(settings['spectrograph']['spectrum_log_frequency'])
    rscu_support.spectrum_log_intensity.set(settings['spectrograph']['spectrum_log_intensity'])
    rscu_support.spectrum_autoscale_intensity.set(settings['spectrograph']['spectrum_autoscale_intensity'])
    rscu_support.spectrum_set_intensity_autoscale_options()
    rscu_support.spectrum_chart_title.set(settings['spectrograph']['spectrum_chart_title'])
    rscu_support.spectrum_chart_filename.set(settings['spectrograph']['spectrum_chart_filename'])
    rscu_support.arrival_phase_list.set(','.join(settings['arrival']['arrival_phase_list']))
    rscu_support.arrival_ray_path_type.set(settings['arrival']['arrival_ray_path_type'])
    rscu_support.arrival_show_legend.set(settings['arrival']['arrival_show_legend'])
    rscu_support.arrival_annotate.set(settings['arrival']['arrival_annotate'])
    rscu_support.arrival_chart_title.set(settings['arrival']['arrival_chart_title'])
    rscu_support.arrival_chart_filename.set(settings['arrival']['arrival_chart_filename'])

def main_menu_reset_defaults():
    '''
    Restores all of the defalt settings from that are hard-coded into
    the rscu_settings.py file when  "Restore Saved Preferences" is
    selected from the File menu.

    Please Note: This command leaves intact tha values of the Station ID,
    the Location Lattitude and Longitude, the Wave Source, and the
    Save Directory.
    '''
    if( rscu_support.verbose ):
        print('rscu_support.main_menu_reset_defaults')
    reset_settings = json.loads(default_settings())
    rscu_support.pixels_wide.set(reset_settings['common']['pixels_wide'])
    rscu_support.pixels_tall.set(reset_settings['common']['pixels_tall'])
    rscu_support.duration.set(reset_settings['common']['duration'])
    rscu_support.chart_autosave.set(reset_settings['common']['chart_autosave'])
    rscu_support.chart_format.set(reset_settings['common']['chart_format'])
    rscu_support.helicorder_minutes_per_line.set(reset_settings['helicorder']['helicorder_minutes_per_line'])
    rscu_support.helicorder_hours_per_chart.set(reset_settings['helicorder']['helicorder_hours_per_chart'])
    if(reset_settings['helicorder']['helicorder_vertical_scaling'] == 'auto'):
        rscu_support.helicorder_auto_vertical_scaling.set(True)
        rscu_support.helicorder_vertical_scaling_state = 'disabled'
    else:
        rscu_support.helicorder_auto_vertical_scaling.set(False)
        rscu_support.helicorder_vertical_scaling_state = 'normal'
        rscu_support.helicorder_vertical_scaling.set(reset_settings['helicorder']['helicorder_vertical_scaling'])
    rscu_support.w.helicorder_vertical_scaling_label.configure(state=rscu_support.helicorder_vertical_scaling_state)
    rscu_support.w.helicorder_vertical_scaling_entry.configure(state=rscu_support.helicorder_vertical_scaling_state)
    rscu_support.helicorder_line1_color.set(reset_settings['helicorder']['helicorder_line1_color'])
    rscu_support.w.helicorder_line1_color_button.configure(background=rscu_support.helicorder_line1_color.get())
    rscu_support.helicorder_line2_color.set(reset_settings['helicorder']['helicorder_line2_color'])
    rscu_support.w.helicorder_line2_color_button.configure(background=rscu_support.helicorder_line2_color.get())
    rscu_support.helicorder_line3_color.set(reset_settings['helicorder']['helicorder_line3_color'])
    rscu_support.w.helicorder_line3_color_button.configure(background=rscu_support.helicorder_line3_color.get())
    rscu_support.helicorder_line4_color.set(reset_settings['helicorder']['helicorder_line4_color'])
    rscu_support.w.helicorder_line4_color_button.configure(background=rscu_support.helicorder_line4_color.get())
    rscu_support.helicorder_chart_title.set(reset_settings['helicorder']['helicorder_chart_title'])
    rscu_support.helicorder_chart_filename.set(reset_settings['helicorder']['helicorder_chart_filename'])
    rscu_support.seismogram_component.set(reset_settings['seismogram']['seismogram_component'])
    rscu_support.seismogram_filter_type.set(reset_settings['seismogram']['seismogram_filter_type'].lower())
    rscu_support.seismogram_filter_max_frequency.set(reset_settings['seismogram']['seismogram_filter_max_frequency'])
    rscu_support.seismogram_filter_min_frequency.set(reset_settings['seismogram']['seismogram_filter_min_frequency'])
    rscu_support.seismogram_filter_zerophase.set(reset_settings['seismogram']['seismogram_filter_zerophase'])
    rscu_support.seismogram_filter_corners.set(reset_settings['seismogram']['seismogram_filter_corners'])
    rscu_support.seismogram_set_filter_state(None)
    rscu_support.seismogram_chart_title.set(reset_settings['seismogram']['seismogram_chart_title'])
    rscu_support.seismogram_chart_filename.set(reset_settings['seismogram']['seismogram_chart_filename'])
    rscu_support.spectrogram_max_frequency.set(reset_settings['spectrogram']['spectrogram_max_frequency'])
    rscu_support.spectrogram_min_frequency.set(reset_settings['spectrogram']['spectrogram_min_frequency'])
    rscu_support.spectrogram_log_frequency.set(reset_settings['spectrogram']['spectrogram_log_frequency'])
    rscu_support.spectrogram_log_color.set(reset_settings['spectrogram']['spectrogram_log_color'])
    rscu_support.spectrogram_show_seismogram.set(reset_settings['spectrogram']['spectrogram_show_seismogram'])
    rscu_support.spectrogram_show_colorbar.set(reset_settings['spectrogram']['spectrogram_show_colorbar'])
    rscu_support.spectrogram_colormap.set(reset_settings['spectrogram']['spectrogram_colormap'])
    rscu_support.spectrogram_chart_title.set(reset_settings['spectrogram']['spectrogram_chart_title'])
    rscu_support.spectrogram_chart_filename.set(reset_settings['spectrogram']['spectrogram_chart_filename'])
    rscu_support.spectrum_max_frequency.set(reset_settings['spectrograph']['spectrum_max_frequency'])
    rscu_support.spectrum_min_frequency.set(reset_settings['spectrograph']['spectrum_min_frequency'])
    rscu_support.spectrum_log_frequency.set(reset_settings['spectrograph']['spectrum_log_frequency'])
    rscu_support.spectrum_log_intensity.set(reset_settings['spectrograph']['spectrum_log_intensity'])
    rscu_support.spectrum_autoscale_intensity.set(reset_settings['spectrograph']['spectrum_autoscale_intensity'])
    rscu_support.spectrum_set_intensity_autoscale_options()
    rscu_support.spectrum_chart_title.set(reset_settings['spectrograph']['spectrum_chart_title'])
    rscu_support.spectrum_chart_filename.set(reset_settings['spectrograph']['spectrum_chart_filename'])
    rscu_support.arrival_phase_list.set(','.join(reset_settings['arrival']['arrival_phase_list']))
    rscu_support.arrival_ray_path_type.set(reset_settings['arrival']['arrival_ray_path_type'])
    rscu_support.arrival_show_legend.set(reset_settings['arrival']['arrival_show_legend'])
    rscu_support.arrival_annotate.set(reset_settings['arrival']['arrival_annotate'])
    rscu_support.arrival_chart_title.set(reset_settings['arrival']['arrival_chart_title'])
    rscu_support.arrival_chart_filename.set(reset_settings['arrival']['arrival_chart_filename'])

if __name__ == '__main__':
    init_settings()
