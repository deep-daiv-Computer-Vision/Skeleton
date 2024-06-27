import streamlit as st
import youtube
import upload
from pytube import YouTube
import re
from datetime import datetime
import os # 경로 탐색
from datetime import datetime
import requests

st.title('Upload') #제목
st.write('1. youtube 영상 가져오기') #내용

url = st.text_input('The URL link')

btn = st.button("download youtube")
if btn:
    if not url:
        st.write("error: Missing 'url' parameter in the request body.")

    if not youtube.is_valid_youtube_url(url):
        st.write("error: Invalid YouTube URL.")

    resolution = "720p"
    success, error_message = youtube.download_video(url, resolution)

    if success:
        st.write("message Video with downloaded successfully.")
    else:
        st.write("error")


st.write('2. 직접 영상 가져오기') #내용

video_file = st.file_uploader('영상을 업로드 하세요.', type=['mov', 'mp4', 'mkv'])
if video_file is not None: # 파일이 없는 경우는 실행 하지 않음
    print(type(video_file))
    print(video_file.name)
    print(video_file.size)
    print(video_file.type)

    # 유저가 올린 파일을,
    # 서버에서 처리하기 위해서(유니크하게) s
    # 파일명을 현재 시간 조합으로 만든다. 
    current_time = datetime.now()
    print(current_time)
    print(current_time.isoformat().replace(':', "_") + '.jpg') #문자열로 만들어 달라
    # 파일 명에 특정 특수문자가 들어가면 만들수 없다.
    filename = current_time.isoformat().replace(':', "_") + '.jpg'
    video_file.name = filename

    upload.save_uploaded_file('video', video_file)

    st.video(f'video/{video_file.name}')

st.title('분석 요청')
# flask api 분석요청
# GET 요청 버튼 
if st.button('flask api'):
    # Flask 서버로 GET 요청 보내기
    response = requests.get('http://localhost:5000/test')
    
    if response.status_code == 200:
        st.success('Response received: ' + response.text)
    else:
        st.error('Failed to receive response')