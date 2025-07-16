import re
import os
from youtube_transcript_api import YouTubeTranscriptApi
# URL 입력

FILE_PATH = os.path.join("outputs")

def extract_video_id(url):
    """
    """
    
    # 패턴 1: https://www.youtube.com/watch?v=<video_id>
    # 패턴 2: https://youtu.be/<video_id>
    # 패턴 3: https://www.youtube.com/watch?v=<video_id>&t=<time>s
    # 패턴 4: https://www.youtube.com/embed/<video_id>
    # 패턴 5: <video_id>


    # 패턴 5
    if len(url) == 11 and not (url.startswith('http') or url.startswith('www')):
        return url
    
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    
    match = re.search(r"embed/([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    
    match = re.search(r"youtu\.be/([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    
    return None

def save_transcript_translate(url, target_lang='ko'):
    ytt_api = YouTubeTranscriptApi()
    video_id = extract_video_id(url)

    print(f"video_id: {video_id}")
    transcripts_list = ytt_api.list(video_id)
    transcripts = transcripts_list.find_transcript(['en'])
    translated_transcript = transcripts.translate('ko').fetch()
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)

    with open(f"{FILE_PATH}/{video_id}.txt", 'w', encoding="utf-8") as f:
        for transcript in translated_transcript:
            time = transcript.start
            text = transcript.text
            f.write(f"[{format_time(time)}] " + text + '\n')

def format_time(seconds):
    minute = int(seconds // 60)
    second = int(seconds % 60)
    return f"{minute:02d}:{second:02d}"

def main():
    url_input = None
    while (url_input != 'exit'):
        url_input = input("Input youtube url: ")
        save_transcript_translate(url_input)
        print("Saved!")

if __name__ == "__main__":
    main()
    