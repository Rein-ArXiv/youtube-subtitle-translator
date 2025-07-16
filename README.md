# YouTube Transcript Translator

A simple Python tool that extracts YouTube video transcripts and translates them to Korean using YouTube's built-in translation feature.

## Features

- 🎯 **Simple & Fast**: Extract and translate YouTube transcripts with minimal code
- 🌐 **YouTube Native Translation**: Uses YouTube's own translation engine (no API keys required)
- ⏱️ **Timestamped Output**: Each line includes timestamp for easy reference
- 📁 **Multiple URL Formats**: Supports various YouTube URL formats
- 🆓 **Completely Free**: No API keys, no registration, no usage limits

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/youtube-transcript-translator.git
cd youtube-transcript-translator
```

2. Install required dependency:
```bash
pip install youtube-transcript-api
```

## Usage

Run the script:
```bash
python main.py
```

Enter a YouTube URL when prompted:
```
Input youtube url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

The translated transcript will be saved in the `outputs/` directory as `{video_id}.txt`.

### Supported URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://www.youtube.com/watch?v=VIDEO_ID&t=30s`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `VIDEO_ID` (11-character video ID)

## Output Format

The generated file contains timestamped Korean translations:

```
[00:00] 안녕하세요 여러분, 오늘은 파이썬에 대해 알아보겠습니다.
[00:05] 파이썬은 간단하고 직관적인 프로그래밍 언어입니다.
[00:12] 데이터 분석부터 웹 개발까지 다양한 분야에서 사용됩니다.
```

## How It Works

1. **URL Parsing**: Extracts video ID from various YouTube URL formats using regex
2. **Transcript Fetching**: Retrieves English transcript using YouTube Transcript API
3. **Translation**: Uses YouTube's built-in translation to convert to Korean
4. **Formatting**: Adds timestamps and saves to text file

## Requirements

- Python 3.6+
- `youtube-transcript-api` library

## Limitations

- Only works with videos that have English transcripts available
- Translation quality depends on YouTube's translation engine
- Some videos may not have transcripts available

## Use Cases

- 📚 **Study Materials**: Convert English lectures to Korean for easier comprehension
- 📝 **Note Taking**: Get readable transcripts for video content
- 🎓 **Language Learning**: Compare original and translated content
- 🔍 **Content Analysis**: Quick access to video content in text format

## Example

```bash
$ python main.py
Input youtube url: https://www.youtube.com/watch?v=abc123
video_id: abc123
Saved!
Input youtube url: exit
```

Output file (`outputs/abc123.txt`):
```
[00:00] 이것은 번역된 첫 번째 문장입니다.
[00:03] 이것은 번역된 두 번째 문장입니다.
[00:07] 계속해서 더 많은 내용이 이어집니다.
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) for providing the core transcript extraction functionality
- YouTube's translation service for high-quality translations

---

**Note**: This tool is for educational and personal use only. Please respect YouTube's terms of service and content creators' rights.