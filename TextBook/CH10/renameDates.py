import os,re,shutil

for file in os.listdir():
    new_file = re.sub(r'((0|1)\d)-((0|1|2|3)\d)-(\d{4})', r'\2-\1-\3', file)
    if new_file != file:
        print(f"{file}ファイルを{new_file}に置き換え(※処理はコメントアウトしてます.)")

            # shutil.move(file, new_file)
