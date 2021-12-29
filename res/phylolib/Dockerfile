FROM openjdk:13-jdk-alpine

COPY PhyloLib-1.0-SNAPSHOT.jar app.jar

RUN apk update && apk add bash
RUN apk add --no-cache bash

ENTRYPOINT ["java","-jar","/app.jar"]
