import argparse
import sys


from pyDcCrypto.crypto import PyDcCrypto


def main():
    """Main function"""
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', '--encrypt', action="store_true",
                        required=False, help='encrypt', default=False)
    parser.add_argument('-d', '--decrypt', action="store_true",
                        required=False, help='decrypt', default=False)
    parser.add_argument('-k', '--key',
                        required=True, help='master Key')
    parser.add_argument('-m', '--msg',
                        required=True, help='message to encrypt or decrypt')

    args = parser.parse_args()

    client = PyDcCrypto(args.key)

    if args.encrypt:
        print(client.encrypt(args.msg))
    elif args.decrypt:
        print(client.decrypt(args.msg))
    else:
        print("no action set")


if __name__ == '__main__':
    sys.exit(main())

