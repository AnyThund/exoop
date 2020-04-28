import argparse
import os
import pprint
import re
import shutil
import zipfile

from . import __version__
from .constant import DESKTOP, SCOOP_CACHE, pattern_app


def main():
    parser = argparse.ArgumentParser(prog='exoop', description='Portable for your scoop.')
    parser.add_argument('-n', '--name', dest='name', help='Name of export file', default='apps')
    parser.add_argument('-d', '--dst', dest='destination', help='Where the manifest export', default=DESKTOP)
    parser.add_argument('-z', '--zip', help='Whether to export Zip of apks', action='store_true')
    parser.add_argument('--uninstalled', help='List all uninstalled apps', action='store_true')
    parser.add_argument('-v', '--version', help='Version of %(prog)s', action='version', version='%(prog)s {}'.format(__version__))

    pp = pprint.PrettyPrinter(indent=4)

    args = parser.parse_args()

    filename = args.name
    dst_dir = args.destination

    os.chdir(dst_dir)

    os.system(f"scoop export > {filename}.txt")

    if args.zip:
        appZip = zipfile.ZipFile(f'{filename}.zip', 'w')

        def zip_app(ZipFile, app_name):
            for file in os.listdir(SCOOP_CACHE):
                if app_name in file:
                    ZipFile.write(os.path.join(SCOOP_CACHE, file))

        with open(f'{filename}.txt', 'rt') as f:
            for line in f:
                match_app = pattern_app.match(line)
                app_name = '#'.join(match_app.group(1,2))
                print(app_name)
                zip_app(appZip, app_name)
            appZip.close()
    
    if args.uninstalled:
        all_app_list = ['#'.join(x.split('#')[:2]) for x in os.listdir(SCOOP_CACHE)]
        uninstalled_list = [x for x in all_app_list]
        with open(f'{filename}.txt', 'rt') as f:
            for line in f:
                match_app = pattern_app.match(line)
                app_name = '#'.join(match_app.group(1,2))
                for file in all_app_list:
                    if app_name in file:
                        uninstalled_list.remove(file)
        print("\n---uninstalled apps---\n")
        pp.pprint(uninstalled_list)
