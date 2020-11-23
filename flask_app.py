from flask import Flask, render_template, request
from wc_func import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    shape_data= 'rect.jpg'; colour_data= 'None'; size_data_tuple= (400,400);
    to_replace = ''; replace_with = '';
    text_data = 'alice';
    if request.method == 'POST':
        shape_data= request.form.get('shape_name')
        colour_data= request.form.get('colour_name')
        size_data= request.form.get('size_name')
        size_data_tuple = (int(size_data), int(size_data))
        to_replace = request.form.get('to_replace')
        replace_with = request.form.get('replace_with')
        text_data= request.form.get('text_name')

    bg_data= request.form.get('bg')
    if to_replace== None:
        to_replace= ''
    if replace_with== None:
        replace_with= ''

    image_location= temp_img(wc_function(text= text_data,
                                        mask= str(shape_data), gradient = colour_data,
                                        bg_color= bg_data, size= size_data_tuple,
                                        replace_word=[to_replace, replace_with],))

    return render_template('index.html', user_image= image_location)


if __name__ == "__main__":
    app.run(debug=True)
#     app.run()
