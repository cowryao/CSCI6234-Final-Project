# User guide
our project is a maven project.

## intellij
To develop our project we need to install intelliJ, intelliJ contains Tomcat as local sever, so we don't need to install tomcat
Version: 2019.3.1
Build: 193.5662.53
[This is the Link to download intellij](https://www.jetbrains.com/idea/download/#section=windows)

## JDK
search java jdk in google to download jdk
[This is the Link TO download JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html)
for windows download jdk-13.0.2_windows-x64_bin.exe
for mac OS download jdk-13.0.2_osx-x64_bin.dmg
version: Java SE Development Kit 13.0.2

<strong>after install JDK:</strong> according to [this website](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) open environment window
new system variables names <strong>JAVA_HOME</strong>, path is the path of jdk, for instance C:\Program Files\Java\jdk-13.0.2

install this project and use intelliJ to open the project. Let maven install required packages.


After open the project <strong> Check in intelliJ !!!</strong> 

1. File-> Settings-> Java Compiler -> Project bytecode version == 13 

2. File-> Settings-> Java Compiler -> Module-> Target bytecode version == 13

3. File-> Project Structure -> Project -> Project SDK == 13 (or your installed JDK, find the location and choose it)

4. File-> Project Structure -> Project -> Project Language Level == 13 - new language features

5. Edit configurations -> Spring Boot WatchAMovieTogetherApplication(1) -> Environment -> Jre == path of your JDK

## Run app
hit run button (green triangle) on the top left, to check if the project can run

open browser type  localhost:8080/greeting?name=Your_Name  to test if the web run correctly 
