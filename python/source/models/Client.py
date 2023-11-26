


class Client:
    def __init__(self,
                 user_id : str,
                 nickname : str,
                 device : int,
                 connectionID : str,
                 host : int = 0,
                 ):
        self.user_id = user_id
        self.nickname = nickname
        self.device = device
        self.connectionID = connectionID
        self.host = host
        
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'nickname': self.nickname,
            'device': self.device,
            'connectionID': self.connectionID,
            'host': self.host,
        }
