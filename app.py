from flask import Flask, render_template, request, redirect, flash, url_for, session
from fastai.vision.all import *


app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


learner = load_learner('./export.pkl')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
            path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(path)
            pred = learner.predict(path)
            pokemon = str(pred[0])
            index = int(pred[1])
            prob = pred[2][index]
            probability = str(round(float(prob), 2) * 100) + "%"
            flash("The pokemon is: " + pokemon + " with a probability of " + probability, "success")
            return redirect(url_for('index'))
        else:
            flash("No file selected", "warning")
            return redirect(url_for('index'))

    else:
        flash('Please send post request only!', "danger")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
