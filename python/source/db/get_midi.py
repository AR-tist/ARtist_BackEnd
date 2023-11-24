from pymongo import MongoClient


def get_midi( filename ):
    client = MongoClient('mongodb://13.124.50.132:27017/')
    db = client['artist']
    collection = db['MidiFile']

    # find one document in collection by filename
    document = collection.find_one({"filename": filename})

    download_url = f"/midi/download/{document['filename']}"
    delete_url = f"/midi/delete/{document['filename']}"
    document['download_url'] = download_url
    document['delete_url'] = delete_url
    return document