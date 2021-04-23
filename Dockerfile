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
    numpy \
    pandas \
    pylint \
    pylint-fail-under \
    pytest-cov \
    pytest==5.0.1
