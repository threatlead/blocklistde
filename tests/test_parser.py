from .context import blocklistde
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_ip_list(self):
        ip = blocklistde.BlocklistDe.ssh()
        self.assertGreater(len(ip), 10, 'Found a total of {0} ipaddresses'.format(len(ip)))


if __name__ == '__main__':
    unittest.main()
