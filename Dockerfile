FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy
RUN pip install waitress

COPY ["predict.py", "model1.bin", "dv.bin", "./"]

EXPOSE 8080

ENTRYPOINT ["python", "-m", "waitress", "--host=0.0.0.0", "--port=8080", "predict:app"]