import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_format =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=json_format, headers=header) 
    formatted_response = json.loads(response.text) 

    if response.status_code == 200:
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion =  max(emotion_dict, key=emotion_dict.get)
    
    elif response.status_code == 400:
        emotion_dict = {
                        "anger": None, 
                        "disgust": None, 
                        "fear": None, 
                        "joy": None, 
                        "sadness": None,
        }
        dominant_emotion = None
                        
    
    return {**emotion_dict, 'dominant_emotion': dominant_emotion}