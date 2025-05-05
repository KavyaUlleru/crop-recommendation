from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load or train model
MODEL_PATH = 'model.pkl'
DATA_PATH = 'crop_recommendation.csv'

if not os.path.exists(MODEL_PATH):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split

    df = pd.read_csv(DATA_PATH)
    X = df.drop('label', axis=1)
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
else:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[x]) for x in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        prediction = model.predict([np.array(features)])
        return render_template('index.html', prediction_text=f'Recommended Crop: {prediction[0]}')
    except:
        return render_template('index.html', prediction_text='Error: Invalid input.')

if __name__ == '__main__':
    app.run(debug=True)
