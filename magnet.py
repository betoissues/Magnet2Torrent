#!/usr/bin/python
import urllib2
import argparse
import wget
import json

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
    res = urllib2.urlopen('http://magnet-to-torrent.com/magnet2torrent.php?magnet=' + magnetURL);
    
    resJson = json.loads(res.read());
    print 'Response is: ' + res.read();
    return resJson['url'];

if __name__ == '__main__':
    main()
