import os
import shutil

def suffix_archive(folder1, folder2, sfx):
    os.makedirs(folder2, exist_ok=True)

    for c_w, sub_dir, files in os.walk(folder1):
        for file in files:
            if any(file.endswith(ext) for ext in sfx):
                f1 = os.path.join(c_w, file)
                f2 = os.path.join(folder2, file)
                with open(f1, 'rb') as src_file, open(f2, 'wb') as dest_file:
                    dest_file.write(src_file.read())
                print(f"{f1}から{f2}へ移動.")

a,b,c = input('[検索ディレクトリ],[[移動先ディレクトリ],[拡張子]\n').split(',')
suffix_archive(a, b, c)
