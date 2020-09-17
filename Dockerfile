FROM python:3.8.5-alpine3.12

WORKDIR /opt
RUN pip install flask
COPY app.py /opt

EXPOSE 8080
CMD ["/usr/local/bin/python", "/opt/app.py"]
