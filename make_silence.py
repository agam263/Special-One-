import wave
import struct
import shutil
import os

with wave.open('public/assets/audio/UI_MUSIC_STEM-2.mp3', 'w') as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(44100)
    for _ in range(44100):
        f.writeframesraw(struct.pack('<h', 0))

shutil.copy('public/assets/audio/UI_MUSIC_STEM-2.mp3', 'public/assets/audio/UI_MUSIC_STEM-3.mp3')
shutil.copy('public/assets/audio/UI_MUSIC_STEM-2.mp3', 'public/assets/audio/UI_MUSIC_STEM-4.mp3')

print("Silent stems 2, 3, and 4 created successfully.")
