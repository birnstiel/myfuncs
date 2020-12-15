"""here we have an example shell command"""
import pathlib


def main():
    print('hello from ' + str(pathlib.Path().absolute()))


if __name__ == '__main__':
    main()
