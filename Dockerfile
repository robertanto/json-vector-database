FROM python:3

WORKDIR /home 

ADD requirements.txt /home
RUN pip install --no-cache-dir -r requirements.txt

COPY src /home

CMD ["uvicorn","main:app","--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8081"]