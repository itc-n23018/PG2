import requests, bs4, re, os

a = input("画像のキーワードを入力してください:\n")
img_dir = 'images'
os.makedirs(img_dir,exist_ok=True)


res = requests.get(f'https://flickr.com/search/?text={a}')

soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgs = soup.select('.photo-list-photo-view img')

for i in range(min(10,len(imgs))):
        url = imgs[i].get('src')
        print(f'https:{url}')
        img_res = requests.get(f'https:{url}')
        img_file = open(os.path.join(img_dir,os.path.basename(url)), 'wb')
        for chunk in img_res.iter_content(100000):
            img_file.write(chunk)
        img_file.close()
