#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------
# COPYRIGHT (C) 2014-2025 Mitsuo KONDOU.
# This software is released under the MIT License.
# https://github.com/konsan1101
# Thank you for keeping the rules.
# ------------------------------------------------



import sys
import os
import time
import datetime
import codecs

import subprocess



# watson 音声合成
import speech_api_watson     as watson_api
import speech_api_watson_key as watson_key



if __name__ == '__main__':

    outLang = 'ja'
    outFile = 'temp/temp_speech.txt'
    tmpFile = 'temp/temp_voice.mp3'

    if (len(sys.argv) >= 2):
        outLang = sys.argv[1]
    if (len(sys.argv) >= 3):
        outFile = sys.argv[2]
    if (len(sys.argv) >= 4):
        tmpFile = sys.argv[3]



    print('')
    print('speech_output_watson.py')
    print(' 1)outLang = ' + str(outLang))
    print(' 2)outFile = ' + str(outFile))
    print(' 3)tmpFile = ' + str(tmpFile))



    if (os.path.exists(tmpFile)):
        os.remove(tmpFile)

    outText = ''
    if (os.path.exists(outFile)):

        rt = codecs.open(outFile, 'r', 'shift_jis')
        for t in rt:
            outText = (outText + ' ' + str(t)).strip()
        rt.close
        rt = None

    print(' ' + outText)
    if (outText != ''):
        #try:

        watsonAPI = watson_api.SpeechAPI()
        res = watsonAPI.authenticate('tts',
                        watson_key.getkey('tts','username'),
                        watson_key.getkey('tts','password'), )
        if (res == True):

            res, api = watsonAPI.vocalize(outText=outText, outLang=outLang, outFile=tmpFile)
            if (res != ''):

                sox = subprocess.Popen(['sox', tmpFile, '-d', '-q'], )
                sox.wait()
                sox.terminate()
                sox = None

        #except Exception as e:
        #print(' Error!', sys.exc_info()[0])



