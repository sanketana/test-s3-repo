import json

# Open file and load json string into a string object
with open('input.json') as input_json:
	json_data = json.load(input_json)


def pprint(json_str):
	print(json.dumps(json_str, indent=4))


#pprint(json_data)

all_results = json_data['results']
total_questions = 0
total_replies = 0
titles = {}
users_name = {}


#print(type(all_results))

for result in all_results:
	total_questions += 1
	#print(pprint(result))
	#print('*******')
	course = result['course']
	title = course['title']
	titles[title] = titles.get(title, 0) + 1;
	all_replies = result['replies']
	for reply in all_replies:
		total_replies += 1
		user = reply['user']
		display_name = user['display_name']
		users_name[display_name] = users_name.get(display_name, 0) + 1


# Report
print(f'1) Total number of questions asked: {total_questions}')
print(f'\n2) Total number of replies: {total_replies}')
print('\n3) List of unique titles: ')
for title in titles.keys():
	print(title)
print('\n4) List of unique display names: ')
for name in users_name.keys():
	print(name)

most_active_user = max(users_name, key=users_name.get)
print(f'\n5) User name who has given maximum number of replies is: {most_active_user}')

least_active_user = min(users_name, key=users_name.get)
print(f'\n6) User name who has given minimum number of replies is: {least_active_user}')
		