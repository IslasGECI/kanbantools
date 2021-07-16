FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    ipykernel \
    mutmut \
    pylint \
    pylint-fail-under \
    pytest \
    pytest-cov
