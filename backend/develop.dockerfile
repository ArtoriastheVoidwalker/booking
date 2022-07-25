FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8


ENV PYTHONPATH=/app
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app/

COPY requirements.txt /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 9000
EXPOSE 5432

CMD ["/bin/bash", "-c", "./scripts.sh upgrade && uvicorn app.main:app --host 0.0.0.0 --port 9000"]