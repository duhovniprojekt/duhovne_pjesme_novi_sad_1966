import unittest
from parser import *


class TestMethods(unittest.TestCase):

    def test_header(self):
        musescore = get_musescore("msmodel_examples/test_header.mscx")
        get_header(musescore)

    def test_time_signature(self):
        musescore = get_musescore("msmodel_examples/test_time_signature.mscx")
        for i in range(get_measure_count(musescore)):
            print(get_time_signature(get_measure(musescore, i)))

if __name__ == '__main__':
    unittest.main()
