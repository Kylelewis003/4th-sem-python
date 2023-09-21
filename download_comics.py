
import requests
import os
import bs4

start_url = 'https://xkcd.com'
download_directory = 'xkcd'
os.makedirs(download_directory, exist_ok=True)
    
while True:
    
    print("Downloading the page: " + start_url)

    response = requests.get(start_url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'lxml')
            
    comic_element = soup.select('#comic img')
    if not comic_element:
            print("No comic image found.")
    else:
        comic_image_url = 'https:' + comic_element[0].get('src')
        print("Downloading the image: " + comic_image_url)
        response = requests.get(comic_image_url)
        response.raise_for_status()
        with open(os.path.join(download_directory, os.path.basename(comic_image_url)), 'wb') as file:
            for i in response.iter_content(100000):
                file.write(i)
                
    prev_link = soup.select('a[rel="prev"]')[0]
    start_url = 'https://xkcd.com' + prev_link.get('href')
        
    print("Done")
