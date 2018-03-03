import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'y0u-wi11-n3v3r-gu3$$'
