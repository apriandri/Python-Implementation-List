
from pytube import YouTube

url = 'Your URL goes here'
my_video = YouTube(url)

print("+++++++++++++Title+++++++++++++")
#get Video Title
print(my_video.title)

print("********************Tumbnail+++++++++++++")
# Thumbnail Image
print(my_video.thumbnail_url)

print("********************Downloaded video+++++++++++++")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

my_video.download()