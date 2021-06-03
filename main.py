import requests
from flask import Flask, render_template
import numpy as np
from PIL import Image, ImageStat

app = Flask(__name__)
Dict_image = {}


# This code checks any wrong url
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/health', methods=['GET'])
def func_start():
    return render_template('health.html'), 200


@app.route('/stats/<IMAGE_NAME>/<FUNC_NAME>', methods=['GET'])
def get_result(IMAGE_NAME, FUNC_NAME):
    # get the picture
    url = 'https://storage.googleapis.com/seetree-demo-open/' + IMAGE_NAME
    r = requests.get(url, stream=True).raw
    try:
        img = Image.open(r)
    except Exception:  #if the image doesn't exists
        return render_template('img-page-404.html'), 404
    stat = ImageStat.Stat(img)
    if IMAGE_NAME in Dict_image.keys() and FUNC_NAME in Dict_image[IMAGE_NAME].keys():
        value = Dict_image[IMAGE_NAME][FUNC_NAME]["value"]
        return render_template("statshow.html", IMG_NAME=IMAGE_NAME, value=Dict_image[IMAGE_NAME][FUNC_NAME]['value'],
                               text=Dict_image[IMAGE_NAME][FUNC_NAME]["text"])
    if FUNC_NAME == 'min':
        minimum = [x[0] for x in stat.extrema]
        value = minimum
        return render_template("statshow.html", IMG_NAME=IMAGE_NAME, value=minimum,
                               text="This function calculates the Min value ")
    elif FUNC_NAME == 'max':
        maximum = [x[1] for x in stat.extrema]
        value = maximum

        return render_template("statshow.html", IMG_NAME=IMAGE_NAME, value=maximum,
                               text="This function calculates the Max value ")
    elif FUNC_NAME == 'mean':
        mean = stat.mean
        value = mean

        return render_template("statshow.html", IMG_NAME=IMAGE_NAME, value=mean,
                               text="This function calculates the Mean value ")

    elif FUNC_NAME == 'median':
        median = stat.median
        value = median

        return render_template("statshow.html", IMG_NAME=IMAGE_NAME, value=median,
                               text="This function calculates the Median value ")
    elif FUNC_NAME[0] == 'p' and FUNC_NAME[1:].isnumeric():
        if 0 <= int(FUNC_NAME[1:]) <= 100:
            pixels = list(img.getdata())
            percentile = np.percentile(pixels, int(FUNC_NAME[1:]))
            value = percentile

            return render_template("statshow.html", IMG_NAME=IMAGE_NAME, value=percentile,
                                   text="This function calculates the Percentile value ")
        else:    # the percentile is NOT between 0..100
            return render_template('function_page404.html'), 404

    else:        #if the function doesn't exists
        return render_template('function_page404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
