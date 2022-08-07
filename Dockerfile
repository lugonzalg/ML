FROM python:3

RUN apt-get update

RUN pip3 install \
    matplotlib \
    NumPy \
    SciPy \
    Pandas


