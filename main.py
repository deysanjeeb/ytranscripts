from youtube_transcript_api import YouTubeTranscriptApi
def extract_text(url):
    start = url.find('watch?v=') + len('watch?v=')
    end = url.find('&', start)
    return url[start:end] if end != -1 else url[start:]

link=input()
video_id=extract_text(link)
print(video_id)
# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

# iterate over all available transcripts
for transcript in transcript_list:

    # the Transcript object provides metadata properties
    print(
        transcript.video_id,
        transcript.language,
        transcript.language_code,
        # whether it has been manually created or generated by YouTube
        transcript.is_generated,
        # whether this transcript can be translated or not
        transcript.is_translatable,
        # a list of languages the transcript can be translated to
        transcript.translation_languages,
    )

    # print(transcript.fetch())

    enTranscript=transcript.translate('en').fetch()
with open(video_id+'.txt', 'w') as f:
    f.write(enTranscript[0]['text'])