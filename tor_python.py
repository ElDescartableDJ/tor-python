"""
setup:
    pip install requests
    pip install requests[socks]

super helpful:
    - http://packetforger.wordpress.com/2013/08/27/pythons-requests-module-with-socks-support-requesocks/
    - http://docs.python-requests.org/en/master/user/advanced/#proxies

1- Tor Should be Installed
sudo apt install tor
2- Tor Service must be opened
sudo service tor start
3- install requirements
pip install requests
pip install requests[socks]
4 - change the port in the tool from 9150 to 9050
5 - RUN :)

"""
import requests


proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}


def main():
    url = 'http://ifconfig.me/ip'

    response = requests.get(url)
    print('ip: {}'.format(response.text.strip()))

    response = requests.get(url, proxies=proxies)
    print('tor ip: {}'.format(response.text.strip()))


if __name__ == '__main__':
    main()
