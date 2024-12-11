'''
지역 기반 랜덤 여행지 추천 함수
'''
import pandas as pd
from fastapi import FastAPI
from typing import List
import argparse
import logging
from datetime import datetime

# 로그 설정
logging.basicConfig(
    filename='demo.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 명령행 인수 파서 생성
parser = argparse.ArgumentParser(description='여행지 추천 API 서버')
parser.add_argument('--host', type=str, default='0.0.0.0', help='서버 호스트 주소')
parser.add_argument('--port', type=int, default=8000, help='서버 포트 번호')

# 명령행 인수 파싱
args = parser.parse_args()
app = FastAPI()

df_path = 'src/dataset.csv'
df = pd.read_csv(df_path)

@app.get("/random-recommendations/")
async def get_random_recommendations(sido: str, n: int = 5) -> List[dict]:
    logger.info(f"추천 API 호출 - 시도: {sido}, 추천 개수: {n}, 시간: {datetime.now()}")
    # 점수가 4점 이상인 결과만 필터링
    high_rated = df[df['rating'] >= 4]
    # SIDO 컬럼에서 sido와 일치하는 항목만 필터링
    high_rated = high_rated[high_rated['SIDO'] == sido]
    # 결과가 5개 미만이면 가능한 모든 결과 반환
    if len(high_rated) <= n:
        result = high_rated
    else:
        # 랜덤하게 5개 선택
        result = high_rated.sample(n=n)
    
    logger.info(f"추천 결과 반환 완료 - 추천 개수: {len(result)}, 시간: {datetime.now()}")
    return result.to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=args.host, port=args.port)
