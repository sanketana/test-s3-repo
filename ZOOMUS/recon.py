import json
from zoomus import ZoomClient

client = ZoomClient('GkmnFXBbSoWiHcQqxTlHIA', 'hyW6diTOehNs46N4hQeJkEkAxnDtMF2MFhxB')

data = {'id' : '85310550976'}

response = client.report.get_meeting_participants_report()
response_content = json.loads(response.content)


print(response_content)