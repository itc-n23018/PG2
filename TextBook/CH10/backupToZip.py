import os,shutil,zipfile
from pathlib import Path

def backup(folder):
    i = 1
    while (backup_zip_path := Path.home() / f'backup{i}.zip').exists():
        i += 1

    temp_dir = Path.home() / f'temp_backup_{i}'
    shutil.rmtree(temp_dir, ignore_errors=True)
    shutil.copytree(folder, temp_dir)

    with zipfile.ZipFile(backup_zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        backup_zip.write(temp_dir, arcname='')
    
    shutil.rmtree(temp_dir)
    print(f'{backup_zip_path}にバックアップが作られました.')

folder = input('圧縮するフォルダを絶対パスで指定: ')
backup(folder)
