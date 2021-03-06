import datetime
import re
import locale
from pytube import YouTube

locale.setlocale(locale.LC_ALL, '')


def display_all_variations_to_download(video):
    result = ""
    for i, v in enumerate(video.streams.filter(only_video=True, file_extension='mp4')):
        result += "Itag:" + str(v.itag) + " resolution:" + str(v.resolution) + " fps:" + str(v.fps) + "\n"
    print(result)


inp = input("URL YT video:")
video = YouTube(url=inp)

print(f"\nURL:{video.watch_url}\n"
      f"Title: {video.title}\n"
      f"Duration {str(datetime.timedelta(seconds=video.length))}\n"
      f"Author: {video.author}\n"
      f"Views: {video.views:n}\n")

display_all_variations_to_download(video)
video.streams.get_by_itag(int(re.sub(r'\D', '', input("Itag:")))).download(output_path='download/')
