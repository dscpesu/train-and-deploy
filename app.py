from flask import Flask, request, jsonify, render_template
import joblib
import traceback
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
logreg = joblib.load('model.pkl')
print("Model loaded successfully")
model_columns = joblib.load('columns.pkl')

@app.route('/', methods=['GET'])
def root():
	return render_template('index.html', message = "Flask")

@app.route('/predict',methods=['POST'])
def predict():
	if logreg:
		try:
			json = request.json
			print(json)
			query = pd.get_dummies(pd.DataFrame(json))
			query = query.reindex(columns=model_columns,fill_value=0)
			prediction = list(logreg.predict(query))
			return jsonify({'prediction':str(prediction)})
		except:
			return jsonify({'trace':traceback.format_exc()})
	else:
		print('Train model first')
		return('No trained model available')

if __name__ == "__main__":
	port=5000
	logreg = joblib.load('model.pkl')
	print("Model loaded successfully")
	model_columns = joblib.load('columns.pkl')
	print('Columns loaded')
	
	app.run(port=port,debug=True)
