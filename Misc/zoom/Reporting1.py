import json
from zoomus import ZoomClient

client = ZoomClient('MbEgB6LZRp6Xfl3tMxCLuw', 'LxiXNkKG6nyqpL0BxylQxn2pmeSTdPST6anh')

user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)

print(user_list)