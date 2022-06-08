import json
from zoomus import ZoomClient

client = ZoomClient('DRQAFMs1ReycjwjnbVzHrQ', 'lobkT1HWlnpCwKVI2H0YzhrmPRLfucbX1AAh')

user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)

for user in user_list['users']:
    user_id = user['id']
    #print(json.loads(client.meeting.list(user_id=user_id).content))


meeting_list_reponse = client.meeting.list(user_id="sanketana.zoom@gmail.com")
meeting_list = json.loads(meeting_list_reponse.content)

#print(meeting_list)


report_response = client.report.get_user_report(user_id="sanketana.zoom@gmail.com")
report_list = json.loads(report_response.content)

print(report_list)