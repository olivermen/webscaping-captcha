# Import external libraries
import requests
from bs4 import BeautifulSoup
 # Create a request and fetch the content from the target website
url = 'https://www.behance.net/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
resp = requests.get(url, headers=headers)
 # Parse the html and create a BeautifulSoup object so we can access and parse the content
soup = BeautifulSoup(resp.text, 'lxml')
 # Loop through the content and find all elements with the class 'captcha'
captchas = soup.find_all('div', class_='captcha')
 # Loop through the captchas and add the URL of each captcha to a list
captcha_urls = []
for captcha in captchas:
    captcha_url = captcha.find('img')['src']
    captcha_urls.append(captcha_url)
 # Now loop through the captcha urls and download each captcha image
for captcha_url in captcha_urls:
    response = requests.get(captcha_url)
    file_name = captcha_url.split('/')[-1]
    open(file_name, 'wb').write(response.content)