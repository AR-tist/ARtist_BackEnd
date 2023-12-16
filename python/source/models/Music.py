class Music:
    def __init__(self, data):
        self.download_url = f"/midi/download/{data['filename']}"
        self.delete_url = f"/midi/delete/{data['filename']}"
        self.imgurl = f"/midi/download/{data['imgurl']}"
        self.timestamp = data["timestamp"]
        self.filename = data["filename"]
        self.title = data["title"]
        self.imgurl = data["imgurl"]
        self.subtitle = data["subtitle"]
        self.rank = data["rank"]
        self.poster = data["poster"]
        self.like = data["like"]
        self.views = data["views"]
        self.imgurl = data["imgurl"]
        self.music_length = data["music_length"]
        self.download_url = data["download_url"]
        self.delete_url = data["delete_url"]

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "filename": self.filename,
            "title": self.title,
            "imgurl": self.imgurl,
            "subtitle": self.subtitle,
            "rank": self.rank,
            "poster": self.poster,
            "like": self.like,
            "views": self.views,
            "music_length": self.music_length,
            "download_url": self.download_url,
            "delete_url": self.delete_url,
        }