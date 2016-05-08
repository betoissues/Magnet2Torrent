#!/usr/bin/python
import urllib2
import requests
import argparse
import wget

def main():
    parser = argparse.ArgumentParser(description='Conversion de enlace Magnet a archivo .torrent');
    parser.add_argument('-m', '--magnet', help='Enlace magnet', required=True);

    args = parser.parse_args();

    magnet = uToUTF(args.magnet);
    torrent = toTorrent(magnet);

    file = wget.download(torrent);

def uToUTF(url):
    utfStr = urllib2.quote(url.encode("utf8"));
    return utfStr;


def toTorrent(magnetURL):
    r = requests.get('http://magnet-to-torrent.com/magnet2torrent.php?magnet=' + magnetURL);
    
    torrentUrl = r.json();
    return torrentUrl['url'];

if __name__ == '__main__':
    main()
