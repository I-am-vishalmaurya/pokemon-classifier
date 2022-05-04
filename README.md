
# Pokemon Classifier

PyTorch and FastAI implementation of pokemon classifier with over 150 different classes with the error rate of 6%.


## Demo

The demo for the application is available at [Pokemon Classifier](https://pokemonclassifier.pythonicnerds.me)






## Screenshots

![](https://github.com/I-am-vishalmaurya/pokemon-classifier/blob/master/static/Screenshot%202022-05-04%20at%209.37.15%20AM.png?raw=true "https://github.com/I-am-vishalmaurya/pokemon-classifier/")

![](https://github.com/I-am-vishalmaurya/pokemon-classifier/blob/master/static/Screenshot%202022-05-04%20at%209.37.32%20AM.png?raw=true)

![](https://github.com/I-am-vishalmaurya/pokemon-classifier/blob/master/static/Screenshot%202022-05-04%20at%209.37.40%20AM.png?raw=true)


## Installation

Create a virtual environement with python 3.7+

```bash
  python -m pip install virualenv
  python -m virtualenv venv
```
Activate the virtual environement
```bash
    source venv/bin/activate
```
Install the requirements from the application.
```bash
    pip install -r requirements.txt
```
Download and place the `export.pkl` file inside the root directory of the project.
The `model` is avilable at [export.pkl](https://github.com/I-am-vishalmaurya/pokemon-classifier/releases/download/model/export.pkl)

After placing the `export.pkl` inside the project run the flask server with these command
```bash
    python app.py
```
It will start development server at `http://127.0.0.1:5000`

