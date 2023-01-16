#! python

# https://docs.python.org/3/library/argparse.html

import argparse

if __name__ == '__main__':

    # We create a parser
    parser = argparse.ArgumentParser(
        prog='VirusTotal scanner',
        description='The program allows to check a url with VT API',
        epilog='Text at the bottom of help')

    # define arguments so it will know how to parse
    parser.add_argument('url', help="URL to scan")  # positional argument
    parser.add_argument('-k', '--apikey')  # option that takes a value
    parser.add_argument('-s', '--scan', action='store_true')  # on/off flag

    # perform the parse
    args = parser.parse_args()
    print(args.url, args.apikey, args.scan)

    # here will come the call for actual logic
