# 여행 로그 데이터 기반 장소 추천 알고리즘

> 2024. 10. 24. 최초 작성
> 서버 아키텍처 구축 프로젝트 01 - psudo version

## 실행
`sh start_api.sh`
- 백그라운드 실행 `nohup sh start_api.sh > api.log &`

[참고] 백그라운드 프로세스 찾기 및 중단 
1. ps -fu {유저이름:root} | grep {검색어:start_demo}
2. 해당 프로세스 번호 pid 를 찾기
3. kill {pid} (강제종료 kill -9 {pid})