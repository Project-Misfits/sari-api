FROM ubuntu:20.04 as base-image

ENV TZ=UTC
ENV DEBIAN_FRONTEND=nointeractive
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install build-essential wget make libxt6 libdbus-1-3 libdbus-1-dev \
    unzip curl python3 python3-pip \
    libssl-dev libffi-dev libpq-dev gcc git -y

# Download + Install Miniconda
RUN wget -P /tmp https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh
RUN bash /tmp/Miniconda3-py38_4.12.0-Linux-x86_64.sh -b -p /home/sari-api/miniconda

ENV PATH="/home/sari-api/miniconda/bin:$PATH"

RUN conda update -n base -c defaults conda

RUN conda config --set auto_activate_base true

FROM base-image as builder

ENV PATH="$PATH:/home/sari-api/miniconda/envs/base/bin"

FROM builder as deps

WORKDIR /app

COPY requirements.txt /app/requirements.txt

WORKDIR /app
# Installing dependencies

RUN pip3 install gunicorn

RUN pip3 install -r requirements.txt

RUN pip install gunicorn

RUN pip install -r requirements.txt

FROM deps as final

COPY . /app

RUN chmod +x /app/.deploy/entrypoint.sh

CMD ["sh", "/app/.deploy/entrypoint.sh"]