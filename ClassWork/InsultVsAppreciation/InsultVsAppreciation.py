import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "363fbaf0-3c96-11ec-8609-075417c70bbf81fff4e9-b771-4d81-9fc5-17d212c0ffce"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()



question = input('Please enter your input: ')


# CHANGE THIS to something you want your machine learning model to classify
demo = classify(question)

label = demo["class_name"]
score = demo["confidence"]

print(demo)

output = f'The sentence that you typed was an {label}. I am {score} % sure about this.'

if int(score) < 70:
	print('I am not too sure')
else:
	print(output)

#label = demo["class_name"]
#confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
#print ("result: '%s' with %d%% confidence" % (label, confidence))