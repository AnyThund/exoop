import os
import re

HOMEPATH = os.path.join(os.environ['HOMEDRIVE'], os.environ['HOMEPATH'])
SCOOPPATH = os.environ['SCOOP']

DESKTOP = os.path.join(HOMEPATH, 'Desktop')
SCOOP_CACHE = os.path.join(SCOOPPATH, 'cache')

pattern_app = re.compile(r'([0-9A-Za-z\-]+)\s\(v:([0-9A-Za-z\.\-]*)\)\s*(\[[0-9A-Za-z\.:/\-]*\])*')

if __name__ == "__main__":
    print(pattern_app.match('nodejs-lts (v:12.16.1) [main]'))