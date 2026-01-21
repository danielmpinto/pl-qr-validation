FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libzbar0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    opencv-python-headless \
    pyzbar \
    pycryptodome

RUN mkdir -p /grade/tests /grade/student /grade/results /grade/serverFilesCourse

WORKDIR /grade