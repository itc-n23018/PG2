import os,re,shutil

def find_file(folder, prefix, rename=False):
    pattern = re.compile(f'^{prefix}(\d+)(.*)')
    files = {int(mo.group(1)): mo.group(0) for filename in os.listdir(folder) if (mo := pattern.search(filename))}
    if not files:
        return

    max_digit_len = len(str(max(files)))
    start, end = min(files), max(files)
    for n in range(start, end + 1):
        if n not in files:
            print('Missing', f'{prefix}{n:0{max_digit_len}}{mo.group(2)}')

    if rename:
        for n, ind in enumerate(sorted(files)):
            new_filename = f'{prefix}{start + n:0{max_digit_len}}{mo.group(2)}'
            if new_filename != files[ind]:
                print('Rename', os.path.join(folder, files[ind]), '->', os.path.join(folder, new_filename))
                shutil.move(os.path.join(folder, files[ind]), os.path.join(folder, new_filename))

find_file('seqfiles', 'spam')
find_file('seqfiles', 'spam', True)
