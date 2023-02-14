import unittest
import parser


class TestMethods(unittest.TestCase):

    def test_header(self):
        museScore = parser.get_musescore("msmodel_examples/test_header.mscx")
        parser.get_header(museScore)


if __name__ == '__main__':
    unittest.main()
