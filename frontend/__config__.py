SIDO_LIST = ['', '경기', '인천', '서울', '충북', '강원', '전북', '경남', '경북', '부산', '대구', '울산', '대전', '충남', '전남', '광주', '세종특별자치시', '제주특별자치도']

def set_front_url(host, port):
    return f"http://{host}:{port}/random-recommendations/?sido="