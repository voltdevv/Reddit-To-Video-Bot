from murf import Murf

class Voice:

    def __init__(self, api):
        self.client = Murf(
            api_key = api
        )

    def generate(self, text, name="terrell"):
        audio = self.client.text_to_speech.generate(
            text = text,
            voice_id = f"en-US-{name}"
        )

        return audio.audio_file

        