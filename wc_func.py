from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import urllib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import requests

url = 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt'
file = urllib.request.urlopen(url)
alice = ''
for line in file:
    alice += line.decode("utf-8")

def wc_function(text = alice, stop_words = None, mask= 'rect.jpg', size = (400,400),
                replace_word = ['',''], gradient = None, bg_color= "white"):
    image = Image.open('shapes/' + mask).resize(size)
    mask =np.array(image)

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color= bg_color, max_words=1000, mask = mask,
               stopwords=stopwords)

    text = text.replace(replace_word[0], replace_word[1])
    wc.generate(text)   # generate word cloud
    # color code
    if gradient != None:
        colors = Image.open('color/' + gradient).resize(size)
        color_array = np.array(colors)
        image_colors = ImageColorGenerator(color_array)
        wc.recolor(color_func=image_colors)
    # color code ends
    return np.array(wc)

# Image.fromarray(wc_function(mask = 'lady.jpg', replace_word = ['Alice','Name'])).show()

