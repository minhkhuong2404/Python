import pyperclip
import sys

PASSWORDS = {'facebook':'Khuong2804',
                'google':'24041999',
                }
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] #first comemnt argy is account name
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+ account + ' copied to clipboard' )
else:
    print('There is no account named ' + account)
