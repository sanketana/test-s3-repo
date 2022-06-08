from googletrans import Translator

translator = Translator()

data = ['Dobrý deň', 'majestátny orol', 'krehká dohoda']

translated = translator.translate(data, src='sk', dest='en')

for trans in translated:
    print(f'{trans.origin} -> {trans.text}')