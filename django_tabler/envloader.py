import os

env_settings = None


def env(key, default=None):
    global env_settings
    env_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if os.path.exists(env_file_path) and env_settings is None:
        print('env_settings not set (first)')
        env_reader = open(env_file_path, mode='rt', encoding='utf-8')
        env_settings = env_reader.readlines()
        env_reader.close()
    for setting in env_settings:
        setting_key, value = setting.split('=')
        value = value.strip()
        if setting_key.strip() == key:
            if value[0] == '[':     # A list type of setting
                return [item for item in value.strip('[').strip(']').split(',')]
            return value.strip()
    return default
