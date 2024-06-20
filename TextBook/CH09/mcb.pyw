import shelve, sys
import pyperclip as p

mcb,arg = shelve.open('mcb'),sys.argv

if len(arg) == 3 and arg[1] == 'save':
    mcb[arg[2]] = p.paste()
elif len(arg) == 2 and arg[1] == 'list':
    p.copy(str(list(mcb.keys())))
elif len(arg) == 2 and arg[1] in mcb:
    p.copy(mcb[arg[1]])

mcb.close()
