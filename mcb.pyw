import shelve, pyperclip, sys
import logging

# logging.basicConfig(level=logging.DEBUG, format = ' %(acstime)s - %(levelname)s - &(message)s')
# logging.debug('Start of the program')
mcbShelf = shelve.open('mcb')

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

#Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcbShelf[sys.argv[2]] = pyperclip.copy(str(list.remove(mcbShelf.keys())))

elif len(sys.argv) == 2:
    #list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
 # add a delete option !!!
# logging.debug('End of the program')
