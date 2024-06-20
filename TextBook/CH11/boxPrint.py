def box(s, w, h):
    if len(s) != 1 or w < 2 or h < 2:
        raise Exception('文字は１文字、幅は２以上、高さは２以上でなければなりません') 
    print('\n'.join([s * w if i in {0, h-1} else s + ' ' * (w - 2) + s for i in range(h)]))


s, w, h = input("[文字] [幅] [高さ]\n").split()
w, h = int(w), int(h)

try:
    box(s, w, h)
except Exception as err:
    print("エラー発生:" + str(err))
