from flask import Flask, render_template, request
from EmotionDetection import emotion_detector
import json
app=Flask("Sentiment Analyzer")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    text=request.args.get("textToAnalyze")
    if request.args.get("status_code")==400:
        print("text_empty...")
    response=emotion_detector(text)
    d=response["dominant_emotion"]
    if 'dominant_emotion'in response:
        del response['dominant_emotion'] 
    t="For the given statement, the system response is " 
    j=  json.dumps(response).strip("{}")
    t+=j+f". The dominant emotion is {d}."
    return t

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)