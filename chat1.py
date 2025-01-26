from deep_translator import GoogleTranslator
import pywhatkit as kit

def whatsapp(translated_text):
    """
    Sends the translated text as a WhatsApp message.
    """
    rec_num = input("Receiver's mobile number (including country code, e.g., +1234567890): ").strip()
    try:
        kit.sendwhatmsg_instantly(rec_num, translated_text)
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send message: {e}")

def translate_text(text, target_language):
    """
    Translates the input text to the specified target language and sends it via WhatsApp.
    """
    try:
        # Translate the text using deep_translator
        translated_text = GoogleTranslator(target=target_language).translate(text)
        print(f"Translated Text: {translated_text}")
        # Send the translated text via WhatsApp
        whatsapp(translated_text)
    except Exception as e:
        print(f"Translation failed: {e}")

if __name__ == "__main__":
    try:
        # Get user inputs
        text = input("Enter the text to translate: ")
        target_language = input("Enter the target language (e.g., 'en' for English): ")
        translate_text(text, target_language)
    except Exception as e:
        print(f"An error occurred: {e}")
