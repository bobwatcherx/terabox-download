import requests, os
from tqdm import tqdm
def down(url, name):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    with open("videos/"+name, 'wb') as file:
            with tqdm(desc="> Downloading", total=total_size, unit="B", unit_scale=True) as pbar:
                for data in response.iter_content(block_size):
                    file.write(data)
                    pbar.update(len(data))
    print(f"> File Saved: videos/{name}")
def download(link, op):
    ses = requests.Session()
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://ytshorts.savetube.me',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'url': link,
    }
    resp = ses.post('https://ytshorts.savetube.me/api/v1/terabox-downloader',headers=headers,json=json_data).json()["response"]
    for key in resp:
        print(f"> TITLE : {key['title']}")
        print("-----------------------------------")
        videos = key['resolutions']
        if op=="a":
            down(videos['Fast Download'], key['title'])
        elif op=="b":
            down(videos['HD Video'], key['title'])
        else:
            down(videos['Fast Download'], key['title'])
def main():
    try:
        os.system("mkdir videos")
    except:
        pass
    os.system("xdg-open https://t.me/peaky_xd")
    os.system("clear")
    logo = """
-----------------------------------
| Coded by : @x_spoilt            |
| Team : @peaky_xd                |
| Tool : Terabox Video Downloader |
-----------------------------------
"""
    print(logo)
    link = input("> ENTER VIDEO LINK : ")
    print(f"> [A] - [FAST DOWNLOAD]")
    print("> [B] - [HD VIDEO]")
    print("-----------------------------------")
    op = input("> SELECT : ")
    if op.lower() == "a":
        download(link, op="a")
    elif op.lower() == "b":
        download(link, op="b")
    else:
        download(link, op="a")
main()