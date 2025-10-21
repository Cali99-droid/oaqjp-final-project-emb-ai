import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    try: 
            response = requests.post(url, headers=header, json=obj)

            if response.status_code == 400:
                return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }

            response_data = response.json()

            emotions = response_data['emotionPredictions'][0]['emotion']
            emotion_scores = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0)
            }
            emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)
            return  emotion_scores
    except requests.exceptions.RequestException as e:
        print(f"Error ao conectar ao Watson NLP API: {e}")
        return None

        