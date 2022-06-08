import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "78d43530-492a-11ec-9290-ed7d80d5d4bb6b8b24dd-75e4-414c-b04e-b4c36b8b0f6b"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify("The text that you want to test")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))