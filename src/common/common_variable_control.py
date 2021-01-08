# <editor-fold desc="File Header">
# Copyright   :
# Description : This python file contains classes, functions and scripts related to common variable conversions
# </editor-fold>


# <editor-fold desc="Function - Custom conversion of provided variable to string">
def custom_to_str(var):
    # <editor-fold desc="Function Info">
    # Copyright   : Copyright information (if applicable)
    # Author : Author Name
    # Date : 13/07/2019
    # Description : Function which converts the provided variable to a string
    #               The difference is any empty variable (None) will be converted to "" so it is not a "NoneType"
    # </editor-fold>
    if var is None:
        var_str = ''
    else:
        var_str = str(var)
    return var_str
# </editor-fold


# <editor-fold desc="Function - Custom conversion of provided variable to string">
def dict_extract_str(input_dict, key):
    # <editor-fold desc="Function Info">
    # Copyright   : Copyright information (if applicable)
    # Author : Author Name
    # Date : 13/07/2019
    # Description : Function which extracts a string value for the provided key from the provided dictionary
    #               If the key can't be found or the dictionary is none the string value is blank
    # </editor-fold>
    if input_dict is None:
        val_str = ''
    elif key in input_dict:
        val_str = custom_to_str(input_dict[key])
    else:  # Value not in dictionary
        val_str = ''
    return val_str
# </editor-fold


# <editor-fold desc="Function - Custom variable type conversion">
def custom_convert(var_type, str_value):
    # <editor-fold desc="Function Info">
    # Copyright   : Copyright information (if applicable)
    # Author : Author Name
    # Date : 13/07/2019
    # Description : Function which converts the provided string value to the specified data type
    #               The converted value is returned from the function
    # </editor-fold>
    value = None
    if var_type == "str":
        value = str_value
    elif var_type == "bool":
        if str_value == "True" or str_value == "1":
            value = True
        else:
            value = False
    elif var_type == "int":
        value = int(str_value)
    elif var_type == "float":
        value = float(str_value)
    return value
# </editor-fold


# <editor-fold desc="Function - Updates a dictionary with the provided key and value">
def auto_update_dict(dictionary, key, value):
    # <editor-fold desc="Function Info">
    # Copyright   : Copyright information (if applicable)
    # Author : Author Name
    # Date : 13/07/2019
    # Description : Function which updates the provided dictionary with the provided key and value
    #               If the key already exists the value is updated, otherwise it is created
    #               The updated dictionary is returned from the function
    # </editor-fold>
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]
    return dictionary
# </editor-fold
