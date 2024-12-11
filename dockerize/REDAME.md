# 도커 실행

- 단독 실행
```bash
docker build -t your_image_name -f dockerize/Dockerfile-{back or front} .
docker run -d -p {host port}:{container port} -v {log volume folder}:/app/{back or front}/logs your_image_name
```

