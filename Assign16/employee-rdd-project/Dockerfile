FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y default-jdk wget && \
    apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/employee_rdd.py"]