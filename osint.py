from spray import spray
from linktr import linktr
from argparse import ArgumentParser

__author__ = 'Game K'
__version__ = "v0.1"

logo = '''
 ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███     
███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄ 
███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██ 
███    ███   ███ Game K ███▌ ███   ███     ███   ▀ 
███    ███ ▀███████████ ███▌ ███   ███     ███     
███    ███          ███ ███  ███   ███     ███     
███    ███    ▄█    ███ ███  ███   ███     ███     
 ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀   

'''
print(logo)

parser = ArgumentParser(prog='osint.py', description='OSINT search ' + str(__version__) + ' by ' + str(__author__))
parser.add_argument('name', metavar='name', type=str, nargs='+', help='Name of person')
parser.add_argument("-s", "--spray", action="store_true", default=False, help="Take search on all similar name")
parser.add_argument("--linktr", action="store_true", default=False, help="Search on 'linktr' website")
args = parser.parse_args()

name = [' '.join(args.name)]

if args.spray:
    name = spray(name[0]).run()

if args.linktr:
    for n in name:
        print(linktr(n))
