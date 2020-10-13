#!/usr/bin/env python3
"""
    Use google ASR system recognize wav file.
    Also can compute character error rate and word error rate
"""
import io
import os
from google.cloud import speech


class Google_ASR(object):
    """Google ASR server"""

    def __init__(self, language, sample_rate):
        self.language = language
        self.sample_rate = sample_rate
        # {key: None for key in string.punctuation} for deleting punctuation
        self.config = speech.types.RecognitionConfig(
            encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code=language,
            sample_rate_hertz=sample_rate,
        )

    def recognize(self, filename):
        """
            Do Google ASR.
            Return the sentence with the highest probability.
        """

        client = speech.SpeechClient()
        with io.open(filename, 'rb') as stream:
            requests = [speech.types.StreamingRecognizeRequest(
                audio_content=stream.read()
            )]

        responses = client.streaming_recognize(
            requests=requests,
            config=speech.types.StreamingRecognitionConfig(config=self.config),
        )

        for response in responses:
            # Once the transcription has settled,
            # the first result will contain the is_final result.
            # The other results will be for subsequent portions of the audio.
            for result in response.results:
                # The alternatives are ordered from most likely to least.
                for alternative in result.alternatives:
                    transcript = alternative.transcript
                    out_path = f"{os.path.splitext(filename)[0]}_transcript.txt"
                    with open(out_path, 'w') as f:
                        print(transcript, file=f)

                    return transcript
