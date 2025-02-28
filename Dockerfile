FROM debian:bookworm
SHELL ["/bin/bash", "-c"]
ENV TZ=UTC
ARG DEBIAN_FRONTEND=nointeractive
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && apt-get upgrade -y && apt-get install wget curl git gcc make unzip libssl-dev libffi-dev libpq-dev \
    -y

# install uv (https://docs.astral.sh/uv/) instead of conda
RUN curl --proto '=https' --tlsv1.2 -LsSf https://github.com/astral-sh/uv/releases/download/0.6.3/uv-installer.sh | sh
ENV PATH="/root/.local/bin/:$PATH"
RUN uv python install 3.12

WORKDIR /app
RUN uv venv /opt/venv
# Use the virtual environment automatically
ENV VIRTUAL_ENV=/opt/venv
# Place entry points in the environment at the front of the path
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /app/requirements.txt
RUN uv pip install -r requirements.txt

COPY . /app
RUN chmod +x /app/.deploy/entrypoint.sh
CMD ["bash", "/app/.deploy/entrypoint.sh"]
