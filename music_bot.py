import os
import torch
import numpy as np
import re
import underthesea
from transformers import AutoModel, AutoTokenizer
from sklearn.svm import SVC
from joblib import load
import json
import random
from predict_model import predict_sentiment

nhac = {
    "vui": {
        "Pop": ["Bài hát vui 1", "Bài hát vui 2", "Bài hát vui 3"],
        "Rock": ["Bài hát rock vui 1", "Bài hát rock vui 2"],
        "EDM": ["Bài hát EDM vui 1", "Bài hát EDM vui 2", "Bài hát EDM vui 3", "Bài hát EDM vui 4"]
    },
    "buồn": {
        "Pop": ["Bài hát buồn 1", "Bài hát buồn 2"],
        "Ballad": ["Bài hát ballad buồn 1", "Bài hát ballad buồn 2", "Bài hát ballad buồn 3"],
        "Indie": ["Bài hát indie buồn 1"]
    }
}


music_data=nhac

# Sentiment recommendation logic
def get_sentiment_recommendation(user_input):
    sentiment = predict_sentiment(user_input)
    return f"Mình thấy bạn đang {sentiment}. Bạn có muốn lắng nghe những giai điệu vui tươi hay buồn bã để hòa quyện cùng cảm xúc của mình không?"

# Music recommendation logic
def get_music_recommendation(user_input):
    # Predict sentiment
    sentiment = predict_sentiment(user_input)
    # print(sentiment)
    # Recommend music based on sentiment
    if sentiment in nhac.keys():
        genre = random.choice(list(music_data[sentiment].keys()))
        song = random.choice(music_data[sentiment][genre])
        responses = [
            f"Đây là bài hát mình tìm được, chúc bạn nghe nhạc vui vẻ: '{song}' thuộc thể loại {genre}!",
            f"Xin giới thiệu với bạn bài hát này: '{song}' thuộc thể loại {genre}!",
            f"Xin được giới thiệu bài hát này: '{song}' thuộc thể loại {genre}!",
            f"Sau khi tìm trong 14,000,605 bài hát, đây là bài phù hợp nhất dành cho bạn: '{song}' thuộc thể loại {genre}!"
        ]
        return random.choice(responses)

# Main function
def main():
    
    # with open(music_data_path, "r", encoding="utf-8") as f:
    #     music_data = json.load(f)

    # User interaction
    print("Chào mừng bạn đến với Music Bot! Hãy cho mình biết tâm trạng hoặc sở thích âm nhạc của bạn.")
    while True:
        user_input = input("Bạn đang cảm thấy thế nào? (hoặc gõ 'thoát' để dừng): ")
        if user_input.lower() == "thoát":
            print("Hẹn gặp lại bạn lần sau!")
            break

        recommendation = get_music_recommendation(user_input) # cho music_data = nhac
        print(recommendation)

if __name__ == "__main__":
    main()


