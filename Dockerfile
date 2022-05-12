FROM openjdk:11


COPY target/*.jar       myapp.jar

CMD ["java" , "-jar" , "myapp.jar"]
