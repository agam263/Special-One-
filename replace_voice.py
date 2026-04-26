import os
import glob
import re
import subprocess

def format_timestamp(seconds):
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis == 1000:
        millis = 0
        seconds += 1
    mins, secs = divmod(int(seconds), 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02d}:{mins:02d}:{secs:02d},{millis:03d}"

srt_dir = "public/assets/audio"
srt_files = sorted(glob.glob(os.path.join(srt_dir, "*.srt")))
input_audio = "/tmp/Brookefield_enhanced.mp3"
total_duration = 111.41

# Read all SRTs and collect data
all_data = []
total_chars = 0

for srt_path in srt_files:
    with open(srt_path, "r") as f:
        content = f.read()
    
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
        current_text.append(line)
        
    if current_text:
        text_blocks.append(" ".join(current_text))
        
    clean_blocks = [re.sub('<[^<]+>', '', block) for block in text_blocks]
    file_chars = sum(len(block) for block in clean_blocks)
    total_chars += file_chars
    
    all_data.append({
        'path': srt_path,
        'text_blocks': text_blocks,
        'clean_blocks': clean_blocks,
        'chars': file_chars
    })

# Slice and rewrite
current_start_time = 0.0

for data in all_data:
    file_duration = (data['chars'] / total_chars) * total_duration if total_chars > 0 else 0
    file_end_time = current_start_time + file_duration
    
    mp3_path = data['path'].replace('.srt', '.mp3')
    
    print(f"Slicing {mp3_path} from {current_start_time:.2f} for {file_duration:.2f}s...")
    
    # Use ffmpeg to slice
    cmd = [
        "ffmpeg", "-y", "-i", input_audio,
        "-ss", str(current_start_time),
        "-t", str(file_duration),
        "-c:a", "libmp3lame", "-q:a", "2",
        mp3_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Rewrite SRT
    new_srt_content = []
    block_start = 0.0
    
    for i, (block, clean_block) in enumerate(zip(data['text_blocks'], data['clean_blocks'])):
        block_chars = len(clean_block)
        block_duration = (block_chars / data['chars']) * file_duration if data['chars'] > 0 else 0
        
        b_end = block_start + block_duration
        if i == len(data['text_blocks']) - 1:
            b_end = file_duration
            
        new_srt_content.append(str(i + 1))
        new_srt_content.append(f"{format_timestamp(block_start)} --> {format_timestamp(b_end)}")
        new_srt_content.append(block)
        new_srt_content.append("")
        
        block_start = b_end
        
    with open(data['path'], "w") as f:
        f.write("\n".join(new_srt_content))
        
    current_start_time = file_end_time

print("All audio and SRT files updated successfully!")
