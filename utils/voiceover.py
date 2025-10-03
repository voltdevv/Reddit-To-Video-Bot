from murf import Murf

client = Murf(
    api_key=""
)


def generate_voice(text):
    # visit link below for different voices. just change the name. i.e terrell to natalie
    # https://murf.ai/api/docs/voices-styles/voice-library#english---us--canada

    audio = client.text_to_speech.generate(
        text = '',
        voice_id= 'en-US-terrell'
    )
