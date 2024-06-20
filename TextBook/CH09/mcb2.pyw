import shelve,sys
import pyperclip as p

mcb_s = shelve.open('mcb')
arg = sys.argv

if len(arg) == 3 and arg[1] == 'save':
    mcb_s[arg[2]] = p.paste()
elif len(arg) == 2 and arg[1] == 'list':
    p.copy(str(list(mcb_s.keys())))
elif len(arg) == 2 and arg[1] in mcb_s:
    p.copy(mcb_s[arg[1]])
elif len(arg) == 3 and arg[1] == 'delete':
    if arg[2] == 'all':
        mcb_s.clear()
    elif arg[2] in mcb_s:
        del mcb_s[arg[2]]
    else:
        print(f"'{arg[2]}' は存在しないキーです")
else:
    print("無効なコマンド")

mcb_s.close()
