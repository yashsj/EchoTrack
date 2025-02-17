from faster_whisper import WhisperModel
class Transcriber:
    def __init__(self, model_size="medium"):
        self.model = WhisperModel(model_size, device=device, compute_type="float16")

    def transcribe(self, audio_file):
        segments, _ = self.model.transcribe(audio_file, beam_size=5)
        text=" ".join([segment.text for segment in segments])
        return text