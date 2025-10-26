from django.shortcuts import render
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
model = joblib.load(BASE_DIR / 'models' / 'model_pipeline.joblib')

def index(request):
    result = None

    if request.method == 'POST':
        data = {
            'Pclass': int(request.POST['Pclass']),
            'Sex': request.POST['Sex'],
            'Age': float(request.POST['Age']),
            'SibSp': int(request.POST['SibSp']),
            'Parch': int(request.POST['Parch']),
            'Fare': float(request.POST['Fare']),
            'Embarked': request.POST['Embarked']
        }
        df = pd.DataFrame([data])
        pred = int(model.predict(df)[0])
        proba = float(model.predict_proba(df)[0, 1])
        result = {'pred': pred, 'probability': proba}

    return render(request, 'index.html', {'result': result})
