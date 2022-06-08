import configparser

config = configparser.ConfigParser()
config.read('test.ini')

str_value = config.get('section_a', 'key')

print(str_value)