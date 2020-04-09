import argparse
from flask import Flask

from app import routes

app = Flask(__name__,template_folder='app/templates', static_folder='app/static')

def main():
    arg_parser = argparse.ArgumentParser(description='Process Daily Orders')
    args = arg_parser.parse_args()

    routes.start()

if __name__ == '__main__':
    main()
