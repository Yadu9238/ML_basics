import numpy as np 
from flask import Flask, request, jsonify, render_template 
import pickle 

app = Flask(__name__)

model = pickle.load(open('gb_model2.pkl','rb'))

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
	
	dataList = request.form.to_dict()
	print("DAta = ",dataList)
	dataList = list(dataList.values())

	dataList = np.array(list(map(float, dataList)))
	print(type(dataList))
	print(dataList)
	if sum(dataList) == 0:
		return render_template('home.html', prediction = "Since all the entered values are zero, there is no concrete")
	
	res = model.predict(dataList.reshape(1,-1))
	if res[0] > 24:
		return render_template('home.html', prediction = "The Predicted strength is {0:.2f} MPa \n and concrete is at the least strong enough for slabs".format(res[0]))
	else:
		return render_template('home.html', prediction = "The Predicted strength is {0:.2f} MPa \nwhich might not be enough for certain usecases".format(res[0]))
	

if __name__ == "__main__":
	app.run(debug = True)