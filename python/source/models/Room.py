from .Music import Music


class Room:
    def __init__(self,
                 room_id : str,
                 host_nickname : str,
                 host_id : str,
                 music_instance : Music,
                 guests : dict,
                 ):
        self.room_id = room_id
        self.host_nickname = host_nickname
        self.host_id = host_id
        self.music_instance = music_instance
        self.guests = guests
    
    def to_dict(self):
        guests = {}
        for guest in self.guests:
            guests[guest] = self.guests[guest].to_dict()
        return {
            'room_id': self.room_id,
            'host_nickname': self.host_nickname,
            'host_id': self.host_id,
            'music_instance': self.music_instance.to_dict(),
            'guests': guests,
        }