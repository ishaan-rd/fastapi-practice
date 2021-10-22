FROM python:3.9

ARG PROXY
ARG APP_DIR /usr/src/app

WORKDIR $APP_DIR
COPY requirements.txt $APP_DIR/requirements.txt
RUN pip install --proxy $PROXY -r requirements.txt

COPY . $APP_DIR

ENTRYPOINT ["uvicorn", "main:my_app", "--reload", "--reload-dir", "/usr/src/app"]