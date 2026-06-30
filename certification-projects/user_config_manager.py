def add_setting(dictionary, tup):
    # unpack and normalize inputs for case-insensitive matching
    key, val = tup
    key = key.lower()
    val = val.lower()
    
    # prevent overwriting existing keys
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictionary[key] = val
        return f"Setting '{key}' added with value '{val}' successfully!"

def update_setting(dictionary, tup):
    key, val = tup
    key = key.lower()
    val = val.lower()
    
    # only modify configuration if setting already exists
    if key in dictionary:
        dictionary[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, key):
    key = key.lower()
    
    # remove key from dictionary if found
    if key in dictionary:
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dictionary):
    if not dictionary:
        return 'No settings available.'

    # generate a formatted, title-case string of all current configurations
    view = "Current User Settings:\n"
    for key, val in dictionary.items():
        view += f"{key.title()}: {val}\n"
    return view

# sample data for testing configuration
test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
