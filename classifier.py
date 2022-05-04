from fastai.vision.all import *


learner = load_learner('./export.pkl')
pred = learner.predict("abra.jpg")
print("Classname:", pred[0])
index = int(pred[1])
prob = pred[2][index]
print("Probability:", round(float(prob), 2) * 100, "%")
