import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


download_web_image("https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/17759651_1606418126076468_7138459390352376287_n.jpg?oh=d1ff9dcb24dd2ef8777de43910f66e5f&oe=59C14090")