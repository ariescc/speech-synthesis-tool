from aip import AipSpeech
import wave
from pyaudio import PyAudio
import pygame
import time

APP_ID = '10348056'
API_KEY = 'pXCd82qbjL8Gi3qZ1wMeEXUP'
SECRET_KEY = 'P0o70lPEtGE6BrfwZ7cSlm3GGpcEsOe9'

chunk = 2014

aipSpeech = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

def voice_hecheng(line,per,spd,pit):
    result = aipSpeech.synthesis(line,'zh',1,{
        'vol': 15,
        'spd': spd,
        'pit': pit,
        'per': per
    })
    if not isinstance(result,dict):
        with open('test.mp3','wb') as file:
            file.write(result);

def play_voice(filepath):
    file = filepath
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)

    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()

if __name__ == '__main__':
    file1 = r'word.mp3'
    play_voice(file1)
    print('请输入需要语音合成的话：')
    play_voice
    line = input()
    file2 = r'per.mp3'
    play_voice(file2)
    print('请输入声音性质（女0，男1，嗲男3，嗲女4）：')
    per = input()
    file3 = r'spd.mp3'
    play_voice(file3)
    print('请输入语速0-9：')
    spd = input()
    file4 = r'pit.mp3'
    play_voice(file4)
    print('请输入音调0-9：')
    pit = input()
    voice_hecheng(line,per,spd,pit)
    file = r'test.mp3'
    play_voice(file)