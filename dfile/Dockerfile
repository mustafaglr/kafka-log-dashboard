FROM python:3.6

WORKDIR .

ADD ./requirements.txt ./

ADD ./kafka_2.12-2.2.0 ./

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN mkdir /usr/java

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk
RUN apt-get install -y openjdk-8-jre
RUN update-alternatives --config java
RUN update-alternatives --config javac

ENV JAVA_HOME /usr

ADD . .

EXPOSE 8050

CMD ["sh" ,"script.sh"]

