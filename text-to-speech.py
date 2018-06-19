from google.cloud import translate, texttospeech
import six

translate_client = translate.Client()
speech_client = texttospeech.TextToSpeechClient()

def text_to_speech(target_lang, text):

    # recognize the source language
    result = translate_client.detect_language(text)
    
    # if source language and target are not the same
    # translate the source to target
    if target_lang != result['language']:
        text = translate_text(target_lang, text) 

    create_response(target_lang, text)


# configure all properties of the text and voice 
# and create an mp3 file with the proper response
def create_response(target_lang, text):
    
    # return they type of text
    input_text = texttospeech.types.SynthesisInput(text=text)
    
    # return the  voice type (female in this case)
    voice = texttospeech.types.VoiceSelectionParams(
         language_code=target_lang,
         ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
    
    # chose audio type (mp3 in this case)
    audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # create a response from all properties above
    response = speech_client.synthesize_speech(input_text, voice, audio_config)

    #create an mp3 file from the response
    with open('speak.mp3', 'wb') as out:
        out.write(response.audio_content)
        print("created a file!!")


# recognized the text's origin language 
# and returns a translation to the target language
def translate_text(target_lang, text):

    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    result = translate_client.translate(text, target_language=target_lang)
    
    return result['translatedText']




# EXAMPLE from english to french 
text_to_speech("en", "games crib baby toys mister magoo my sister always talks about babys")
