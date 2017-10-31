import unittest
import bencode

class TestDecodingForBencode(unittest.TestCase):
    
    def test_str(self):
        bencoded_str1= "4:spam"
        decoded_str1 = "spam"
        self.assertEqual(bencode.decode(bencoded_str1), decoded_str1)
        
        bencode_str2 = "0:"
        decoded_str2 = ""
        self.assertEqual(bencode.decode(bencoded_str2), decoded_str2)
        
    
    def test_int(self):
        bencoded_int1 = "i3e"
        decoded_int1 = 3
        self.assertEqual(bencode.decode(bencoded_int1), decoded_int1)
        
        bencoded_int2 = "i-3e"
        decoded_int2 = -3
        self.assertEqual(bencode.decode(bencoded_int2), decoded_int2)
        
    def test_list(self):
        bencoded_list1 = "l4:spam4:eggse"
        decoded_list1 = ["spam", "eggs"]
        self.assertEqual(bencode.decode(bencoded_list1), decoded_list1)
        
        bencoded_list2 = "le"
        decoded_list2 = []
        self.assertEqual(bencode.decode(bencode_list2), decoded_list2)
        
    def test_dictionary(self):
        bencoded_dict1 = "d3:cow3:moo4:spam4:eggse"
        decoded_dict1 = {"cow": "moo", "spam": "eggs"}
        self.assertEqual(bencode.decode(bencoded_dict1), decoded_dict1)
        
        bencoded_dict2 = "d4:spaml1:a1:bee"
        decoded_dict2 = {"spam":["a","b"]}
        self.assertEqual(bencode.decode(bencoded_dict2), decoded_dict2)
        
if __name__ == '__main__':
    unittest.main()