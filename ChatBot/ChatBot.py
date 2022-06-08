import requests

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


answer = classify('Would you like to eat some pizza')

answerClass = answer['class_name']

print(answer)