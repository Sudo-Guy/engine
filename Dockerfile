FROM python:latest
WORKDIR /app
COPY ./ /app/
RUN python setup.py install
RUN pip install --upgrade pip
RUN python -m pip install --upgrade cython
RUN pip install eval7
ENTRYPOINT [ "python engine.py" ]