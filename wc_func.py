from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import urllib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import requests
import base64
from io import BytesIO


def get_text(url= 'alice'):
    if url == 'alice':
        url = 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt'
    if url == 'tale':
        url = 'https://raw.githubusercontent.com/GITenberg/A-Tale-of-Two-Cities_98/master/98-0.txt'

    file = urllib.request.urlopen(url)
    alice = ''
    for line in file:
        alice += line.decode("utf-8")
    return alice

def wc_function(text, stop_words = None, mask= 'rect.jpg', size = (400,400),
                replace_word = ['',''], gradient = None, bg_color= '#E7E7EC'):
    image = Image.open('shapes/' + mask).resize(size)
    mask =np.array(image)

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color= bg_color, max_words=1000, mask = mask,
               stopwords=stopwords)

    text = get_text(text)
    text = text.replace(replace_word[0], replace_word[1])
    wc.generate(text)   # generate word cloud
    # color code
    gradient= str(gradient)
    if gradient != 'None':
        colors = Image.open('color/' + gradient).resize(size)
        color_array = np.array(colors)
        image_colors = ImageColorGenerator(color_array)
        wc.recolor(color_func=image_colors)
    # color code ends
    font_color= {'#E7E7EC': '#2F2D2D', '#2F2D2D':'#E7E7EC'}
    img = Image.fromarray(np.array(wc))
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype(r'static/fonts/GIL_____.TTF')
    d1.text((5, img.size[0]-15), "https://wordcloud-shzr.herokuapp.com/",
            font= myFont, fill= font_color.get(bg_color))
    
    return img

def temp_img(wc_image):
    im = wc_image
    tmpfile = BytesIO()
    im = im.save(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    image_tag= 'data:image/png;base64,'+ encoded
    
    return image_tag

# wc_function(text= 'tale', mask = 'lady.jpg', replace_word = ['Alice','Name']).show()
