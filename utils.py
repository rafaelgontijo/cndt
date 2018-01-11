#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import os
import requests
import uuid
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


def transcript_mp3(cookies):
    url_mp3 = 'http://aplicacao.jt.jus.br/cndtCertidao/soundCaptcha?x.mp3'
    read = requests.get(url_mp3, cookies=cookies)
    filename = uuid.uuid4().hex
    with open('/tmp/{}.mp3'.format(filename), 'wb') as w:
        for chunk in read.iter_content(chunk_size=512):
            if chunk:
                w.write(chunk)
    process = os.popen(
        'ffmpeg -i /tmp/{filename}.mp3 -ac 1 /tmp/{filename}.flac -loglevel panic'.format(
            filename=filename))
    if not process._proc.wait():
        client = speech.SpeechClient()
        with io.open('/tmp/{}.flac'.format(filename), 'rb') as audio_file:
            content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
        config = types.RecognitionConfig(encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
                                         sample_rate_hertz=44100,
                                         language_code='pt-BR')
        response = client.recognize(config, audio)
        return response.results[0].alternatives[0].transcript
