import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

print('Enter URL: ')
url=input()

page = requests.get(url)

soupped = BeautifulSoup(page.content,"html.parser")
#print(soupped)
imgs = soupped.find_all("img")
#print(imgs)

for img in tqdm(imgs):
    imglink=img.attrs.get("src")
    #print(imglink)
    image=requests.get(imglink).content
    file_name = r"images"+imglink[imglink.rfind("/"):]
    with open(file_name,"wb") as file:
        file.write(image)