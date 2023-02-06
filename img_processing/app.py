from flask import Flask, request, jsonify

app = Flask(__name__)

# route returns the size of the image 
@app.route('/img_size', methods=['POST'])
def img_size():
    file = request.files['image']

    # read image
    img = Image.open(file.stream)
    return jsonify({'msg': 'success', 'size': [img.width, img.height]})

# route rotates image 
@app.route('/img_rotate', methods=['POST'])
def img_rotate():
    file = request.files['image']

    # read image
    img = Image.open(file)
    img = img.rotate(-1*90)
    return send_file(img, mimetype='image/jpg')

# route resizes image
@app.route('/img_resize', methods=['POST'])
def img_resize():
    file = request.files['image']

    # read image
    img = Image.open(file)
    width, height = img.size

    # Setting the points for cropped image
    left = 4
    top = height / 5
    right = 154
    bottom = 3 * height / 5

    im1 = im.crop((left, top, right, bottom))
    newsize = (300, 300)
    im1 = im1.resize(newsize)

    return send_file(im1, mimetype='image/jpg')

@app.route('/', methods=['GET', 'POST'])
def some_work():
    return 'Home route\n'

if __name__ == "__main__":
    app.run(debug=True)