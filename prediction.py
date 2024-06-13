import joblib


class PredictionPipeline:
    def __init__(self):
        self.preprocessor = joblib.load('preprocessor.joblib')
        self.model = joblib.load('model.joblib')
    
    def predict(self, data):
        data = self.preprocessor.transform(data)
        prediction = self.model.predict(data)

        return prediction