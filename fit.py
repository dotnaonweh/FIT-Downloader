import requests
import re,os
import random
from colorama import init, Fore, Back, Style
init()

fr  =   Fore.RED                                                                                     
fw  =   Fore.WHITE                                          
fg  =   Fore.GREEN

def facebook():
    print("in progress a")

def instagram():
    try:
        os.mkdir('Instagram')
    except:
        pass
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    print("\n========Instagram Downloader========")
    pilih = print("[-] 1.Video ")
    pilih = print("[-] 2.Photo ")
    choose = input("Mau apa => ")

    if choose == '1':
        url = input("[-] Masukkan Link Post => ")
        if 'agram.com/p/' in url:
            print("[-] Downloading....\n[-] This may take several minutes")
            req_url = requests.post(url, headers=headers).text
            rex = re.findall('<meta property="og:video" content="(.*?)"', req_url)
            name = random.randrange(0,10000)
            for i in rex:
                req_url = requests.get(i, headers=headers)
                with open("Instagram/video-"+str(name)+".mp4", 'wb') as fl:
                    fl.write(req_url.content)
                    fl.close()
                print(fg+"[-] Download Success => Instagram/video-"+str(name)+".mp4")
        else:
            print("{}\n[#] NOT FOUND OR THE LINK YOU ENTERED IS WRONG [#]".format(fr))

    elif choose == '2':
        url = input("[-] Masukkan Link Post => ")
        if 'agram.com/p/' in url:
            print("[-] Downloading....")
            req = requests.post(url, headers=headers).text
            rex = re.findall('<meta property="og:image" content="(.*?)"', req)
            name = random.randrange(0,10000)
            for i in rex:
                req2 = requests.get(i, headers=headers)
                with open("Instagram/foto-"+str(name)+".jpg", 'wb') as fl:
                    fl.write(req2.content)
                    fl.close()
                print(fg+"[-] Download Success => Instagram/foto-"+str(name)+".jpg")
        else:
            print("{}\n[#] NOT FOUND OR THE LINK YOU ENTERED IS WRONG [#]".format(fr))
    else:
        print("{}\n[#] PILIHAN TIDAK TERSEDIA [#]".format(fr))

def tiktok():
    try:
        os.mkdir('Tiktok')
    except:
        pass
    headers = {
        'authority': 'www.tiktok.com',
        'referer' : 'https://www.tiktok.com/',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'tt_webid_v2=6982415427130033666; tt_webid=6982415427130033666',
    }

    print("\n========Tiktok Downloader========")
    url = input("[-] Masukkan Link Video => ")
    if 'vt.tiktok.com' in url:
        name = random.randrange(0,10000)
        print("[-] Downloading the video....")
        req_url = requests.get(url, headers=headers).text
        rex = re.findall('og:url" content="(.*?)"', req_url)
        for i in rex:
            replacing = i.replace("?_r=1", "")
            req_video = requests.get(replacing, headers=headers).text
            rex2 = re.findall('"og:video" content="(.*?)"', req_video)
            for i in rex2:
                replacing = i.replace("&amp;", "&")
                req_video = requests.get(replacing, headers=headers)
                with open("Tiktok/tiktok-"+str(name)+".mp4", 'wb') as fl:
                    fl.write(req_video.content)
                    fl.close()
                print(fg+"[-] Download success => Tiktok/tiktok-"+str(name)+".mp4")
    elif 'tiktok.com/@' in url:    
        name = random.randrange(0,10000)
        print("[-] Downloading the video....")
        req_url = requests.get(url, headers=headers).text
        rex = re.findall('"og:video" content="(.*?)"', req_url)
        for i in rex:
            replacing = i.replace("&amp;", "&")
            req_video = requests.get(replacing, headers=headers)
            with open("Tiktok/tiktok-"+str(name)+".mp4", 'wb') as fl:
                fl.write(req_video.content)
                fl.close()
            print(fg+"[-] Download success => Tiktok/tiktok-"+str(name)+".mp4")
    else:
        print("{}\n[#] Video not found or the link you entered is wrong [#]".format(fr))

def banner():

    print("""{}

                                ███████╗██╗████████╗  
                                ██╔════╝██║╚══██╔══╝  
                                █████╗░░██║░░░██║░░░  
                                ██╔══╝░░██║░░░██║░░░  
                                ██║░░░░░██║░░░██║░░░  
                                ╚═╝░░░░░╚═╝░░░╚═╝░░░  

██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
    """.format(fr))

    pil = print("{}[#] 1. Facebook Video Downloader\n[#] 2. Instagram Pic/Vid Downloader\n[#] 3. Tiktok Downloader".format(fw))

    choose = input("\nMau apa => ")
    if choose == '1':
        facebook()
    elif choose == '2':
        instagram()
    elif choose == '3':
        tiktok()
    else:
        print("\n{}Pilihan Tidak Tersedia".format(fr))

if __name__ == "__main__":
    banner()