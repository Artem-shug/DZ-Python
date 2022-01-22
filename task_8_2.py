
import re


with open('nginx_logs.txt', 'r') as file_1:
    content = file_1.read() 


remote_addr = re.findall(r'(\d{,3}.\d{,3}.\d{,3}.\d{,3})\s-\s-|(\d*:\d*:\d*:\d*:\w*\d*:\w*\d*:\w*\d*:\w*\d*)', content)
request_datetime = re.findall(r'(\d{2}/[A-z]+/\d{4}:\d\d:\d\d:\d\d\s[+-]\d{4})', content)
request_type = re.findall(r'"([A-Z]{3})',content)
requested_resource = re.findall(r'/\w*/\w*_\d', content)
response_code = re.findall(r'"\s(\d{3})\s', content)
response_size = re.findall(r'(\d*)\s"-"', content)

result = zip(remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)

print(*result)
