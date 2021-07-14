```
docker kill $(docker ps -aq) && docker rm $(docker ps -aq)
export SECRET_KEY=$(python WebApp/utils/generate_secret_key.py)
docker-compose up -d --build
```
