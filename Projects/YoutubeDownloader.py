#Make sure you have installed pytube3 on your system. If not follow these steps:-
#Open windows terminal and type (First install PIP)
#pip install pytubeX

from pytube import YouTube

n = int(input("Enter the number of youtube videos to download:   "))
links = []
print("\nEnter all the links one per line:")

for i in range(0, n):
    temp = input()
    links.append(temp)

for i in range(0, n):
    link = links[i]
    yt = YouTube(link)
    print("\nDetails for Video", i + 1, "\n")
    print("Title of video:   ", yt.title)
    print("Number of views:  ", yt.views)
    print("Length of video:  ", yt.length, "seconds")
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll available options for downloads:\n")
    for i in range(0, len(streamlist)):
        st = streamlist[i].split(" ")
        print(i + 1, ") ", st[1], " and ", st[3], sep='')
    tag = int(
        input("\nEnter the itag of your preferred stream to download:   "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading...")
    ys.download()
    print("\nDownload completed!!")
    print()
