import os
import glob
import re
from gtts import gTTS
from mutagen.mp3 import MP3

def format_timestamp(seconds):
    # returns HH:MM:SS,mmm
    millis = int((seconds - int(seconds)) * 1000)
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

srt_dir = "public/assets/audio"
srt_files = glob.glob(os.path.join(srt_dir, "*.srt"))

for srt_path in srt_files:
    print(f"Processing {srt_path}...")
    with open(srt_path, "r") as f:
        content = f.read()
    
    # Parse SRT
    lines = content.split('\n')
    text_blocks = []
    current_text = []
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_text:
                text_blocks.append(" ".join(current_text))
                current_text = []
            continue
        if line.isdigit() or '-->' in line:
            continue
        
        # Remove HTML tags for audio generation, but keep them for SRT
        # Actually, let's just keep the original text line for the new SRT
        current_text.append(line)
        
    if current_text:
        text_blocks.append(" ".join(current_text))

    if not text_blocks:
        continue
        
    # Full text for TTS
    clean_blocks = [re.sub('<[^<]+>', '', block) for block in text_blocks]
    full_text = " ".join(clean_blocks)
    
    # Generate MP3
    mp3_path = srt_path.replace('.srt', '.mp3')
    # Use slow=True to make it more story-like and give it time
    tts = gTTS(text=full_text, lang='en', slow=True)
    tts.save(mp3_path)
    
    # Get Duration
    audio = MP3(mp3_path)
    duration = audio.info.length
    print(f"  Duration: {duration:.2f}s")
    
    # Rewrite SRT based on character count proportion
    total_chars = sum(len(block) for block in clean_blocks)
    
    new_srt_content = []
    current_time = 0.0
    
    for i, (block, clean_block) in enumerate(zip(text_blocks, clean_blocks)):
        char_count = len(clean_block)
        # Proportion of time
        # Give a small padding to the last block
        time_share = (char_count / total_chars) * duration if total_chars > 0 else 0
        
        start_time = current_time
        end_time = current_time + time_share
        
        # If it's the last block, make sure it reaches the end
        if i == len(text_blocks) - 1:
            end_time = duration
            
        new_srt_content.append(str(i + 1))
        new_srt_content.append(f"{format_timestamp(start_time)} --> {format_timestamp(end_time)}")
        new_srt_content.append(block)
        new_srt_content.append("")
        
        current_time = end_time
        
    with open(srt_path, "w") as f:
        f.write("\n".join(new_srt_content))
    print(f"  Rewrote {srt_path} to match audio length.")
