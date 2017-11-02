from bencoder import decode, encode
import hashlib


class Torrent():
    """
    Implementation of a torrent
    """
    
    
    def __init__(self, path_to_torrent):
        
        # Read torrent file
        with open(path_to_torrent, 'rb') as torrent_file:
            torrent_contents = torrent_file.read()
        
        # Decode torrent file
        self.metainfo = decode(torrent_contents)
        
        # Get info dictionary
        self.info_dict = self.metainfo[b'info']
        
        # Create SHA1 hash of info dictionary
        hash_sha1 = hashlib.sha1()
        self.info_hash = hashlib.sha1(self.info_dict).hexdigest()
        
        # Get announce url
        self.announce_url = self.metainfo[b'announce']
        
        # Get pieces and pieces length 
        self.piece_length = self.info_dict[b'piece_length']
        self.pieces = self.info_dict[b'pieces']
        
        # Get name of the torrent
        self.torrent_name = self.info_dict[b'name']
        
        # Get the length of the torrent
        if "files" in self.info_hash.keys():
            total_length = 0
            for i in self.info_hash[b'files']:
                total_length += decode(i)[b'length']
            self.torrent_length = total_length
        else:
            self.torrent_length = self.info_hash[b'length']
        
    def get_info_dict(self):
        """
        Retrieves the info dictionary, a dictionary that describes the file(s) of a torrent
        """
        return self.info_dict
        
    def get_announce_url(self):
        """
        Retrieves the announce URL of the tracker
        """
        return self.announce_url
        
    def get_info_hash(self):
        """
        Returns a SHA1 hash of the info dictionary
        """
        return self.info_hash
        
    def get_length_of_torrent(self):
        """
        Retrieves total length of the torrent
        """
        return self.torrent_length
        
    def get_torrent_name(self):
        """
        Retrieves name of the torrent
        """
        return self.torrent_name
        
    def get_piece_length(self):
        """
        Retrieves the number of bytes in each piece
        """
        return self.piece_length
    
    def get_pieces(self):
        """
        Retrieves string consisting of the concatenation of all 20-byte
        SHA1 hash values, one per piece
        """
        return self.pieces
        
        
        