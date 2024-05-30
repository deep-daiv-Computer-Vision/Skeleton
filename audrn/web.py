import streamlit as st
import yt_dlp

st.title('YouTube 동영상 다운로더')

# 사용자로부터 YouTube URL 입력받기
video_url = st.text_input('YouTube URL을 입력해주세요.')

# 동영상 다운로드 버튼
if st.button('동영상 다운로드'):
    if not video_url:
        st.error('URL을 입력해주세요.')
    else:
        # youtube-dl 옵션 설정
        ydl_opts = {
            'format': 'best[height=720]/best',
            'outtmpl': 'videos/downloaded_video.mkv',  # 다운로드 파일 이름
        }
        
        # 동영상 다운로드 시도
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([video_url])
                st.success('다운로드 완료!')
                st.video('videos/downloaded_video.mkv')
            except Exception as e:
                st.error('다운로드 중 오류 발생: {}'.format(e))
