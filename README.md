# 여행 로그 기반 여행지 추천 사이트 (웹 프론트/백엔드)

## [front/](./front/)
- 프론트엔드 코드
- 역할
    - 로그 데이터 입력 데모 사이트
    - 추천 여행지 결과 출력
- 포트 번호 : 80

## [data-api/](./data-api/)
- 백엔드(1) 코드
- 역할
    - 데이터 저장/조회
    - Data Lake로의 데이터 송신
    - Data Warehouse로의 데이터 수신
- 포트 번호 : 5000

## [recommend-api/](./recommend-api/)
- 백엔드(2) 코드
- 역할
    - 추천시스템 알고리즘 코드 (여행지 반환)
- 포트 번호 : 5100

## 작업 방법
- 작업별 다른 branch 이용 및 merge 요청
- branch 명은 폴더명으로 할 것

## To Do
- [ ] `dockerize/` 폴더에 전체 docker container build 테스트 코드 작성