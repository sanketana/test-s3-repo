import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "85d67aa0-098c-11ec-bbd8-91542105649bbec5fbd2-76f8-4463-a32c-ba0249eac649"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()




def ask_questions():
	question = input('> ')
	answer = classify(question)
	answerClass = answer['class_name']

	if (answerClass == 'Food'):
		print('I love to eat mice')
	elif (answerClass == 'Lifespan'):
		print ('I live for 25 years')
	elif (answerClass == 'Country'):
		print('I live in Asian countries')
	else:
		print ('I am not sure!')


ask_questions()		