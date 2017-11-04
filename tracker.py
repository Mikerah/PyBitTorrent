import hashlib
import requests 
import torrent
from bencoder import encode, decode

class Tracker():
    """
    Implementation of Tracker
    """
    
    def __init__(self, torrent, port, event):
        self.torrent = torrent
        self.port = port
        self.event = event
        self.params = dict()
        
    def set_params(self):
        self.params['info_hash'] = self.torrent.get_info_hash()
        self.params['peer_id'] = self.torrent.get_peer_id()
        self.params['port'] = self.port
        self.params['uploaded'] = 0
        self.params['downloaded'] = 0
        self.params['left'] = self.torrent.get_length_of_torrent()
        self.params['compact'] = 1
        self.params['event'] = self.event
       
    def results(self):
        self.set_params()
        announce_url = self.torrent.get_announce_url()
        try:
            response = requests.get(announce_url, params=self.params, timeout=3)
            print(response.text)
        except:
            pass

        
        