import requests, bs4, webbrowser

a = input('キワードを空白区切りで入力して:\n').split()
print('pythonパッケージを検索しています...')
res = requests.get(f'https://pypi.org/search/?q={" ".join(a)}')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.package-snippet')

num_open = min(5, len(link_elems))
for i in range(num_open):
    url = 'https://pypi.org' + link_elems[i].get('href')
    print(f'URL: {url}')
    webbrowser.open(url)

