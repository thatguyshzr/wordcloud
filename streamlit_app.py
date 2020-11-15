import streamlit as st
import wc_func
import numpy as np

st.write('''# Wordcloud''')
st.text('Made by Shzr')

# mask ----------------------------------------------------------------
mask_shape = st.sidebar.selectbox(
    "Shape",
    ("Default", "Lady", "Apple", 'White Rabbit')
)
mask = {"Default":'rect.jpg', "Lady":'lady.jpg', "Apple":'apple.png', 'White Rabbit':'rabbit.jpg'}

# text gradient -------------------------------------------------------
color_select = st.sidebar.selectbox("Color",
        ("Default", 'Black Beacon', 'Blue Bird', 'Orange Oscillator',
        'Pink Paranoia', "Purple Play", 'White Whim')
    )
color = {"Default": None, 'Black Beacon': 'black.jpg', 'Blue Bird': 'gradient2.jpg',
        'Orange Oscillator': 'gradient1.jpg', 'Pink Paranoia' : 'gradient3.jpg',
        "Purple Play":'gradient.jpg',
        'White Whim':'white.jpg',
        }

# background color ----------------------------------------------------
# bg_color_picker = st.sidebar.color_picker('Backcolor', '#ffffff')
bg_color_radio = st.sidebar.radio('Background Color', ('Light', 'Dark'))
if bg_color_radio == 'Light':
    bg_color = '#E7E7EC'
elif bg_color_radio == 'Dark' :
    bg_color = '#2F2D2D'
# black: #2F2D2D, white: #E7E7EC

# size ----------------------------------------------------------------
size_markdown = st.sidebar.selectbox(
    "Size (pixels)",
    ("400x400", "600x600", "800x800", '1000x1000')
)
size = {"400x400":(400,400), "600x600":(600,600), "800x800": (800,800), "1000x1000": (1000,1000)}

# replace word --------------------------------------------------------
to_replace = st.sidebar.text_input('Replace')
to_replace_with = st.sidebar.text_input('with')

if to_replace == '' or len(to_replace) <= 2:
    to_replace_with_text = ''
    to_replace_text = ''
else:
    to_replace_with_text = to_replace_with
    to_replace_text = to_replace

# ---------------------------------------------------------------------
st.image(wc_func.wc_function(mask = mask.get(mask_shape),
                            gradient = color.get(color_select),
                            size = size.get(size_markdown),
                            replace_word= [to_replace_text, to_replace_with_text],
                            bg_color= bg_color),
        caption = '')

suggest = '<a href="mailto:shzr&#64;protonmail.com?subject=Wordcloud%20suggestion" target="_blank">Got a suggestion? Click here.</a>'
st.markdown(suggest, unsafe_allow_html=True)
link = '[GitHub](http://github.com/thatguyshzr)<br />[Instagram](http://instagram.com/thatguyshzr)'
st.markdown(link, unsafe_allow_html=True)
