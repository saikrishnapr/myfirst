FROM python:3.11-alpine
LABEL maintainer="lorenz.vanthillo@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 3306
ENTRYPOINT ["python"]
CMD ["main.py"]
