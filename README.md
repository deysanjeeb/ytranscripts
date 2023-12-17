# ytranscripts
 YouTube Transcript Extractor

This Python script uses the `youtube_transcript_api` to extract the transcript from a YouTube video and save it to a text file.

## Requirements

- Python 3
- pip

## Installation

First, clone the repository to your local machine:

```bash
git clone <repository_url>
```

Navigate to the project directory:
```bash
cd ytranscripts
```
Install the required Python packages:
```bash
pip install -r requirements.txt
```

Usage
Run the script with:
```bash
python main.py
```

When prompted, enter the URL of the YouTube video you want to extract the transcript from. The transcript will be saved to a text file with the same name as the video ID.

Note
This script currently only supports English transcripts. If the video's transcript is not in English, the script will attempt to translate it to English.
