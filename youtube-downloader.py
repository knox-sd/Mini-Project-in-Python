# pip install pytube
## audio or video once at a time.

from pytube import YouTube

def Download(link):
    youtubeObj = YouTube(link)
    youtubeObj = youtubeObj.streams.get_audio_only() ##
    youtubeObj = youtubeObj.streams.get_highest_resolution() ##
    
    try:
        youtubeObj.download()
    except:
        print("An error has occrred")
    print("Download is completed successfully")

link = input("Enter the Youtube video URL: ")

Download(link)
