def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    if key not in settings:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, updated_setting):
    key, value = updated_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    if key not in settings:
        return "Setting not found!"

def view_settings(settings):

    if not settings:
        return "No settings available."
    
    result = "Current User Settings:"

    for key, value in settings.items():
        result += "\n" + key.capitalize() + ": " + value
    return result + "\n"

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled', 
    'volume': 'high'
}
print(view_settings(test_settings))