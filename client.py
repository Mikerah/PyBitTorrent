import argparse
import tracker
import random
import datetime
import torrent
import tracker

class Client():
    """
    Implementation of bittorent client
    """
    
    def __init__(self,torrent_file):
        self.torrent_file = torrent_file
        random.seed(datetime.datetime.now())
        self.peer_id = "".join([str(random.randint(0,9)) for i in range(20)])
        self.torrent = torrent.Torrent(self.torrent_file, self.peer_id)
        self.event = "started"
        self.tracker = tracker.Tracker(self.torrent, 6881, self.event)
        self.tracker.results()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="My Implementation of BitTorrent Client")
    parser.add_argument("-D", "--download", help="Downloads")
    args = parser.parse_args()
    
    client = Client(args.download)