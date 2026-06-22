FROM python:3.12-slim

# Install Java
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean

# Set Java Home
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]