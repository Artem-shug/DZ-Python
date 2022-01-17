

with open('nginx_logs.txt', 'r') as file_1:
    content = file_1.read().replace('"', ' ')
    spisok = content.splitlines()

remote_addr = [i.split(' ')[0] for i in spisok]
request_type = [i.split(' ')[6] for i in spisok]
requested_resource = [i.split(' ')[7] for i in spisok]  

result = list(zip(remote_addr, request_type, requested_resource))
    
print(result)

