import streamlit as st
import requests
import argparse
import logging
from datetime import datetime
from __config__ import SIDO_LIST, set_front_url

# 로그 설정
logging.basicConfig(
    filename='logs/demo.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='여행지 추천 데모 애플리케이션')
parser.add_argument('front_host', type=str, help='프론트엔드 호스트 IP')
parser.add_argument('front_port', type=int, help='프론트엔드 포트 번호')

args = parser.parse_args()
FRONT_URL = set_front_url(args.front_host, args.front_port)

# 페이지 로드 시간 로깅
logger.info(f"페이지 로드 시작: {datetime.now()}")

# streamlit setting
st.set_page_config(page_title="여행지 추천 데모 사이트",
                   page_icon="🏕️",
                   layout="wide")
st.title('여행지 추천')

# layout
input_container = st.container()
st.divider()
output_container = st.container()

# Input 
left_col, right_col = input_container.columns([7,3])
img_file = left_col.file_uploader("여행지 이미지 첨부", ["png", "jpg"], disabled=True)
sido = right_col.selectbox("시도", SIDO_LIST)

if (img_file is not None):
    input_container.image(img_file, caption='업로드된 여행지 이미지', use_column_width=True)
    if (sido == ''):
        right_col.write('<div style="text-align: center;">시도를 선택해주세요.</div>', unsafe_allow_html=True)
    else:
        rec_btn = right_col.button('추천 받기', use_container_width=True)

else:
    # input_container.write('<div style="text-align: center;">이미지를 업로드해주세요.</div>', unsafe_allow_html=True)
    rec_btn = False
    if (sido == ''):
        right_col.write('<div style="text-align: center;">시도를 선택해주세요.</div>', unsafe_allow_html=True)
    else:
        rec_btn = right_col.button('추천 받기', use_container_width=True)

# Output
rec_img_con, rec_result_con = output_container.columns([3, 7])

if rec_btn:
    logger.info(f"추천 버튼 클릭 시간: {datetime.now()}")
    output_container.markdown("### 추천 결과")
    data = requests.get(f"{FRONT_URL}{sido}").json()
    output_container.dataframe(data)
    logger.info(f"추천 결과 로드 완료 시간: {datetime.now()}")
