
FROM python:3.9


WORKDIR /NIRFRankPredictor


COPY ./requirements.txt /NIRFRankPredictor/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /NIRFRankPredictor/requirements.txt

 
COPY ./app /NIRFRankPredictor/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]