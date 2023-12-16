from pymongo import MongoClient


def get_midi( filename ):
    client = MongoClient('mongodb://artist:1234@13.124.50.132:8484/')
    db = client['artist']
    collection = db['MidiFile']

    # find one document in collection by filename
    document = collection.find_one({"filename": filename})

    download_url = f"/midi/download/{document['filename']}"
    delete_url = f"/midi/delete/{document['filename']}"
    imgurl = f"/midi/img/{document['imgurl']}"
    document['download_url'] = download_url
    document['delete_url'] = delete_url
    document['imgurl'] = imgurl
    
    return document