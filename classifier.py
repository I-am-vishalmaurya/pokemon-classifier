from fastai.vision.all import *


learner = load_learner('./export.pkl')
pred = learner.predict("abra.jpg")
print(pred)
