#1.streaming large data(youtube,netflix)
def stream_video(chunks):
    for chunk in chunks:
        yield chunk
video_chunks = ["chunk_1","chunk_2","chunks_3"]
player = stream_video(video_chunks)
print(next(player))
print(next(player))
print(next(player))



#2.infinite news feed(instagram, twitter,facebook)
def fetch_posts():
    post_id = 1
    while True:
        yield f"post{post_id}"
        post_id+=1
news_feed = fetch_posts()
print(next(news_feed))
print(next(news_feed))
print(next(news_feed))
print(next(news_feed))
print(next(news_feed))


#4.music streaming(spotify, music)
def stream_music(tracks):
    for track in tracks:
        yield track
playlist = stream_music(["song1","song2","song3"])
print(next(playlist))
print(next(playlist))
print(next(playlist))


