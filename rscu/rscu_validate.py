from datetime import datetime, date
import tkinter as tk

from rscu import rscu_support

def validate_fp(char):
    '''
    Restrict user input to floating point values in entry boxes.
    A tkinter validation callback function to allow only float values
    to be entered. The function is called with every key press in the
    entry box. The full text plus the new key press is tested (the value
    that will be displayed in the entry box it the ne key press is
    accepted). If the full string plus the new key press is a floating
    point number, it is accepted. If not, no change will be made to the
    entry box.
    
    :param: string "char": the full entry box string value including the new key-press.
    :return: "result":  True if char is type float, false if not.
    :rtype: boolean
    '''
    result = True
    if( char not in ['','-','+','.'] ):
        try:
            float( char )
        except ValueError:
            result = False
    return(result)

def validate_int(char):
    '''
    Restrict user input to integer values in entry boxes.
    A tkinter validation callback function to allow only int values
    to be entered. The function is called with every key press in the
    entry box. Only the new keystroke is tested. If it is a positive
    integer (a digit 0 through 9), it is accepted and added to the entry
    box string. If not, no change will be made to the entry box.
    
    :param: string "char": the single new key stroke.
    :return: "result":  True if char is 0 through 9, false if not.
    :rtype: boolean
    '''
    result = char.isdecimal()
    return(result)

def validate_component(v_component=None, v_seis=False):
    '''
    Check to make sure the three-characher component code is a valid
    Raspberry Shake or BOOM type. Called by the chart plotting modules
    after the user clicks on the "Plot Chart" button. This is not
    implemented as a tkinter validation callback.
    
    :param: string "v_component": the component code.
    :param: boolean "v_seis": True if from the Seismogram tab, otherwise False.
    :return: "result":  True if the component code is a valid Raspberry
        Sake or BOOM component. Otherwise False.
    :rtype: boolean
    '''
    if( rscu_support.verbose ):
        print('rscu_support.validate_component')
    result = True
    if( v_seis ):
        if (v_component not in ['SHZ', 'SH?', 'EHZ', 'EHN', 'EHE', 'EH?', 'ENZ', 'ENN', 'ENE', 'EN?', 'E??', 'HDF', 'HD?']):  # Check to see if the resulting component is a valid Raspberry Shake component - i.e. not someting like "SNF" or "EDZ" 
            tk.messagebox.showwarning("Unknown Component","Component " + v_component + " is not recognized as a Raspberry Shake or Raspberry BOOM component")
            result = False
    else:
        if(v_component not in ['SHZ', 'EHZ', 'EHN', 'EHE', 'ENZ', 'ENN', 'ENE', 'HDF']):  # Check to see if the resulting component is a valid Raspberry Shake component - i.e. not someting like "SNF" or "EDZ" 
            tk.messagebox.showwarning("Unknown Component","Component " + v_component + " is not recognized as a Raspberry Shake or Raspberry BOOM component")
            result = False
    return(result)

def validate_minmax(v_min=None, v_max=None, v_label=None, v_log=False):
    '''
    Check the fequesncy and intensity scale limits. The maximum must be
    greater than the minimum. If log scales are specified, the minimum
    value cannot be 0. Called by the chart plotting modules after the
    user clicks on the "Plot Chart" button. This is not implemented as a
    tkinter validation callback.
    
    :param: float "v_min": the minimum value.
    :param: float "v_max": the maximum value.
    :param: string "v_label": either "Frequency" or "Intensity". Used
       for the error message, if displayed.
    :param: boolean "v_log": True if log scale, False if linear scale.
    :return: "result":  True if max value is greater than min value, and
       if log scale is used, values are non-zero.
    :rtype: boolean    
    '''
    if( rscu_support.verbose ):
        print('rscu_support.validate_maxmin')
    result=True
    min_value = validate_stringtofloat(v_min)
    max_value = validate_stringtofloat(v_max)
    if( v_log and ((min_value <= 0) or (max_value <= 0)) ):
        tk.messagebox.showwarning('Invalid ' + v_label + ' Value', v_label + ' values must be a non-zero, positive number with log axes.')
        result=False
    elif( (min_value < 0) or (max_value < 0)):
        tk.messagebox.showwarning('Invalid ' + v_label + ' Value', v_label + ' values must be a positive number.')
        result=False
    elif( min_value >= max_value ):
        tk.messagebox.showwarning('Invalid ' + v_label + ' Value', 'Maximum ' + v_label + ' value must greater than the Minimum ' + v_label + ' value.')
        result=False        
    return(result)

def validate_date_time(v_year=None, v_month=None, v_day=None, v_hour=None, v_minute=None, v_second=None):
    '''
    Check to make sure user entered dates and times are valid. Called by
    the chart plotting modules after the user clicks on the "Plot Chart"
    button. This is not implemented as a tkinter validation callback.
    
    :params: int "v_year", "v_month", "v_day", "v_hour", "v_minute",
       "v_second": date components.
    :return: "result":  True if values are a valid date or date and time.
    :rtype: boolean    
    '''
    if( rscu_support.verbose ):
        print('rscu_support.validate_date_time')
    result = True
    if( v_hour ):
        try:
            datetime(v_year, v_month, v_day, v_hour, v_minute, v_second)  # Check to see if the user-specified date values are a valid date and time
        except ValueError:
            result = False
            tk.messagebox.showwarning("invalid Date or Time","Invalid date-time: " + str(v_year) + '-' + str(v_month) + '-' + str(v_day) + ' ' + str(v_hour) + ':' + str(v_minute) + ':' + str(v_second) )
    else:
        try:
            date(v_year, v_month, v_day)                                # Check to see if the user-specified date values are a valid date
        except ValueError:
            result = False
            tk.messagebox.showwarning("invalid Date","Invalid date: " + str(v_year) + '-' + str(v_month) + '-' + str(v_day) )
    return(result)

def validate_stringtofloat(in_string):
    '''
    Check for an empty string and, if found, define it as 0.0, otherwise
    convert the input string to a float value. The input string does not
    need to be tested further since it has already been validated by the
    "validate_fp" validation callback.
    
    :param: string "in_string", the input string to convert.
    :return: "out_value":  the floating point value of the string.
    :rtype: float    
    '''
    if( in_string == '' ):
        out_value = 0.0
    else:
        out_value = float(in_string)
    return(out_value)
