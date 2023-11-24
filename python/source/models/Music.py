class Music:
    def __init__(self, data):
        self.timestamp = data["timestamp"]
        self.filename = data["filename"]
        self.title = data["title"]
        self.imgurl = data["imgurl"]
        self.subtitle = data["subtitle"]
        self.rank = data["rank"]
        self.poster = data["poster"]
        self.like = data["like"]
        self.views = data["views"]
        self.music_length = data["music_length"]
        self.downloadUrl = data["downloadUrl"]
        self.deleteUrl = data["deleteUrl"]
        self.id = data["id"]