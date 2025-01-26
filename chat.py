from googletrans import Translator
import pywhatkit as kit
def whatsapp(translated_text):
    rec_num = input("RECEIVER mobile number (including country code, e.g., +1234567890): ")
    kit.sendwhatmsg_instantly(rec_num, translated_text)
def translate_text(text, target_language):
    translator = Translator()
    translation = Translator.translate(text, dest=target_language)
    translated_text = translation.text
    source_language = translation.src
    print(f"Source Language: {source_language}")
    whatsapp(translated_text)
if(True):
    text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'en' for English): ")
    translate_text(text, target_language)