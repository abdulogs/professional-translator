from googletrans import Translator
translator = Translator()
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
print(translation.text)


# from google_translator_simplified import Translator


# data = Translator.get_translation('ur', 'How are you', 'en')


# print(data)
