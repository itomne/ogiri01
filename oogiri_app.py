import streamlit as st
import requests
from io import BytesIO
import google.generativeai as genai

# gemini api のためのモジュール
# Google Generative AI（Gemini API）のAPIキー設定
genai.configure(api_key="GEMINI_API_KEY")

# Geminiモデルの設定
model = genai.GenerativeModel('gemini-1.5-pro-preview-0409')

# アプリのタイトル
st.title("大喜利Webアプリ")

# 画像のアップロード
uploaded_file = st.file_uploader("画像をアップロードしてください", type=["jpg", "jpeg", "png"])

# APIキーの設定


# キャプションを生成する関数
def generate_caption(image, api_key):
    url = "https://your_actual_endpoint_here"  # 実際のエンドポイントを使用してください
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    files = {
        "image": image
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        return response.json().get("caption", "キャプションが生成できませんでした。")
    else:
        return "エラーが発生しました。"

# 画像がアップロードされた場合
if uploaded_file is not None:
    st.image(uploaded_file, caption='アップロードされた画像', use_column_width=True)
    
    caption = generate_caption(uploaded_file, api_key)
    st.write(f"生成されたキャプション: {caption}")
else:
    st.warning("画像をアップロードしてください。")
