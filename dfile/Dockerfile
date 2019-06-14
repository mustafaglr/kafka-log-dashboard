FROM python:3.6

WORKDIR .

ADD ./requirements.txt ./

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN mkdir /usr/java

RUN apt-get update \
    && apt-get install -y openjdk-8-jdk \
    && apt-get install -y openjdk-8-jre \
    && update-alternatives --config java \
    && update-alternatives --config javac

ENV JAVA_HOME /usr

ADD . .

EXPOSE 8050

CMD ["sh" ,"script.sh"]

