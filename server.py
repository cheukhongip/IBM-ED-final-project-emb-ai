"""
This module defines the Flask server for Emotion Detection
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Get the text from user
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant = response['dominant_emotion']

    if dominant is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {anger_score},
    'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}.
    The dominant emotion is {dominant}."""

@app.route("/")
def render_index_page():
    """
    Front page access
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    