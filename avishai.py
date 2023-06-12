import requests
from bs4 import BeautifulSoup



import requests

cookies = {
    '_ga': 'GA1.3.795721787.1646653868',
    '_hjSessionUser_707580': 'eyJpZCI6ImVjN2RhMzI3LWZjNDgtNThlMS05ODY1LTVmMDhlNWY4MWM1NyIsImNyZWF0ZWQiOjE2NDY2NTM4Njc2NTksImV4aXN0aW5nIjp0cnVlfQ==',
    '__RequestVerificationToken': 'SfXnvWCBMlXBaEC7u5QPTwUOGI2mP1OM7FRT7VIT08g4N0DTtWj6canhnoJXKvvwD5m2RxUVVCk6K4gMQX5ceESfh0gPc_vDoDuOsuvMQ701',
    '.AspNet.ApplicationCookie': 'KAl_jMF1k_AiZsPqLVvov3KC4A3x9tF729Jm6JB8CEiNJHgGPvln3ZB5qQRFo37E-qvn1w6xkVCEt8r2N7gxRP4EF48cLe9x5CLXkn7ofXl8jZ7HFONODjsfWz0hspBrhhqW8Lex0CLJaV6ZkCyVDG7ynDhacxsbA5HXOSvb-rv5NUjkR1bmVEG_8_iWUubz5vH6BOXXdCcRi95Y5oKDcWDMXDyUo2A2ro9S9gVPDRRaGpskTpaQpfVgYAkKXxHyNBD7U3J5LJxYNTwbsMYU_-EJrfyAGPsluQyJ7RE4NPJHA-JWI4x51e3dUp5HEbVUQyGtJx_9FQ3vVcloZG-8UzALFf9s817DmFKHoDXli3n_Q4aBTY9GNfN3GQd7pmyT5P8gM1nRCU5603ZbEo5XnhxfzhvOTxH5n1laIOUK7u1qTldWRmnrqVLXr28eZKQ_K_6u-Y_2by1t3_YmHXzwSwzJXpaOVjDEgUxdFCVz8v2eMd4XGUsn4rqC76vCBloV',
    'qproject': 'projID=54&projName=×××¨××× ××××&DatabaseName=boazqualish_GeneralTenders&ExpDate=09/24/2022 13:39:56',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Alt-Used': 'qm.govo.co.il',
    'Connection': 'keep-alive',
    'Referer': 'https://qm.govo.co.il/',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ga=GA1.3.795721787.1646653868; _hjSessionUser_707580=eyJpZCI6ImVjN2RhMzI3LWZjNDgtNThlMS05ODY1LTVmMDhlNWY4MWM1NyIsImNyZWF0ZWQiOjE2NDY2NTM4Njc2NTksImV4aXN0aW5nIjp0cnVlfQ==; __RequestVerificationToken=SfXnvWCBMlXBaEC7u5QPTwUOGI2mP1OM7FRT7VIT08g4N0DTtWj6canhnoJXKvvwD5m2RxUVVCk6K4gMQX5ceESfh0gPc_vDoDuOsuvMQ701; .AspNet.ApplicationCookie=KAl_jMF1k_AiZsPqLVvov3KC4A3x9tF729Jm6JB8CEiNJHgGPvln3ZB5qQRFo37E-qvn1w6xkVCEt8r2N7gxRP4EF48cLe9x5CLXkn7ofXl8jZ7HFONODjsfWz0hspBrhhqW8Lex0CLJaV6ZkCyVDG7ynDhacxsbA5HXOSvb-rv5NUjkR1bmVEG_8_iWUubz5vH6BOXXdCcRi95Y5oKDcWDMXDyUo2A2ro9S9gVPDRRaGpskTpaQpfVgYAkKXxHyNBD7U3J5LJxYNTwbsMYU_-EJrfyAGPsluQyJ7RE4NPJHA-JWI4x51e3dUp5HEbVUQyGtJx_9FQ3vVcloZG-8UzALFf9s817DmFKHoDXli3n_Q4aBTY9GNfN3GQd7pmyT5P8gM1nRCU5603ZbEo5XnhxfzhvOTxH5n1laIOUK7u1qTldWRmnrqVLXr28eZKQ_K_6u-Y_2by1t3_YmHXzwSwzJXpaOVjDEgUxdFCVz8v2eMd4XGUsn4rqC76vCBloV; qproject=projID=54&projName=×××¨××× ××××&DatabaseName=boazqualish_GeneralTenders&ExpDate=09/24/2022 13:39:56',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
}

response = requests.get('https://qm.govo.co.il/CarBids', cookies=cookies, headers=headers)



soup = BeautifulSoup(response.content, 'lxml')

cars = soup.find_all('tr')


b=5