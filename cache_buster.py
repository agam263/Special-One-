import sys

with open("public/main.js", "r") as f:
    content = f.read()

# Replace mp3 and srt paths with cache buster
content = content.replace('asset_url("audio/"+a+".mp3")', 'asset_url("audio/"+a+".mp3?v=" + Date.now())')
content = content.replace('asset_url("audio/"+a+".srt")', 'asset_url("audio/"+a+".srt?v=" + Date.now())')

with open("public/main.js", "w") as f:
    f.write(content)

print("Cache busters added to main.js")
