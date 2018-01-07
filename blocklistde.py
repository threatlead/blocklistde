import requests
from ipaddress import IPv4Address, AddressValueError


class BlocklistDe:
    """
    Blocklist.de website scraper
    """
    base_url = 'https://lists.blocklist.de'
    lists_url = '{0}/lists'.format(base_url)

    @staticmethod
    def validate(ipv4):
        try:
            ip = IPv4Address(ipv4)
        except AddressValueError:
            return False
        else:
            return True

    @classmethod
    def get_ip_list(cls, list_name):
        url = '{0}/{1}'.format(cls.lists_url, list_name)
        response = requests.get(url=url)
        if not response.status_code == requests.codes.ok:
            raise Exception('Unable to fetch list:{0} from Blocklistde'.format(list_name))
        # --
        return [ip.decode('ascii') for ip in response.content.splitlines() if BlocklistDe.validate(ipv4=ip.decode('ascii'))]

    @classmethod
    def ssh(cls, ):
        return [(ip, 'ssh') for ip in cls.get_ip_list('ssh.txt')]

    @classmethod
    def mail(cls, ):
        return [(ip, 'mail') for ip in cls.get_ip_list('mail.txt')]

    @classmethod
    def apache(cls, ):
        return [(ip, 'apache') for ip in cls.get_ip_list('apache.txt')]

    @classmethod
    def imap(cls, ):
        return [(ip, 'imap') for ip in cls.get_ip_list('imap.txt')]

    @classmethod
    def ftp(cls, ):
        return [(ip, 'ftp') for ip in cls.get_ip_list('ftp.txt')]

    @classmethod
    def sip(cls, ):
        return [(ip, 'sip') for ip in cls.get_ip_list('sip.txt')]

    @classmethod
    def bots(cls, ):
        return [(ip, 'bots') for ip in cls.get_ip_list('bots.txt')]

    @classmethod
    def strongips(cls, ):
        return [(ip, 'strongips') for ip in cls.get_ip_list('strongips.txt')]

    @classmethod
    def ircbot(cls, ):
        return [(ip, 'ircbot') for ip in cls.get_ip_list('ircbot.txt')]

    @classmethod
    def bruteforcelogin(cls, ):
        return [(ip, 'bruteforcelogin') for ip in cls.get_ip_list('bruteforcelogin.txt')]

    @classmethod
    def get_all(cls, ):
        return cls.ssh() + cls.mail() + cls.apache() + cls.imap() + cls.ftp() + cls.sip()\
               + cls.bots() + cls.strongips() + cls.ircbot() + cls.ircbot()
