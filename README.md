# ROS-phone-network
ROS communication between Android Phone and Jetson Nano

# 목차
[1. 코드 설명](#코드-설명)

[2. 실행 방법](#실행-방법)
  
## 코드 설명
#### publisher.py
Publish하는 코드, 여기에서는 ROS Mobile이 Publisher가 되므로 굳이 필요 없음
#### subscriber.py
Subscribe하는 코드, 버튼의 상태에 따라 토픽의 내용을 모두 기록하거나 중지함
  
## 실행방법
1. Terminal 1에서 ROS의 Master를 구동해준다.
```
$ roscore
```
2. Terminal 2에서 Subscriber 코드를 구동.
```
$ rosrun [패키지이름] subscriber
```
3. 만약 ROS에서 어떤 토픽이 구동 중인지 확인하기 위해서는 다음 코드로 확인
```
$ rostopic echo list
```
