import requests, json
def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json={ "raw_document": { "text": text_to_analyze } }
    response=requests.post(URL,headers=Headers,json=Input_json)
    r=json.loads(response.text)
    anger_score=r["emotionPredictions"][0]['emotion']['anger']
    disgust_score=r["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score=r["emotionPredictions"][0]["emotion"]["fear"]
    joy_score=r["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score=r["emotionPredictions"][0]["emotion"]["sadness"]
    scores={}
    scores['anger']=anger_score
    scores['disgust']=disgust_score
    scores['fear']=fear_score
    scores['sadness']=sadness_score

    dominant_emotion=max(scores,key=scores.get)
    scores['dominant_emotion']=dominant_emotion
    return scores