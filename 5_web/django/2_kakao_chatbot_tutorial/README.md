# Kakaotalk Massenger App Chatbot Tutorial

Refrence : <http://codeac.tistory.com/entry/Python으로-카카오톡-플러스친구-만들기-5?category=731564>


### 1장

장고 프로젝트 시작하기

- `$ virtualenv -p python3 .`

- `$ source bin/activate`

- `$ django-admin startproject <project_name>.`

- `/chatbot_tutorial$ python3 manage.py startapp <app_name>`

- `/chatbot_tutorial/chatbot_tutorials/settings.py`에서
  - `INSTALLED_APPS`에 새로운 생성한 앱 추가
  - 날짜, 시간대 변경

<br>

### 2장

- `/chatbot_tutorial/chatbot_tutorials/urls.py`에서
  - `from chatbot_app import views`추가

- `/chatbot_tutorial/chatbot_app/views.py`에서 키보드 반응 내용 추가하기

- `/chatbot_tutorial/chatbot_tutorials/urls.py`에서 keyboard추가하기

- `$ python3 manage.py runserver`을 통해
  - http://127.0.0.1:8000/keyboard 에서 해당 내용이 잘 나오는지 확인

<br>

#### 2장 + a

- AWS EC2에 동일 프로젝트 생성
- AWS Elastic IP (탄력적 IP 생성)
  - 사용하고자 하는 EC2 Instance 연결
  - Inbound 포트 개방
    - 8000, 8080
- `$ python3 manage.py runserver 0:8000` 실행
- [카카오 플러스친구 관리자 센터](https://center-pf.kakao.com)
  - 계정 생성
  - 스마트 채팅
    - API형
    - APP URL 에서 http://내서버:8000 API 테스트 반응하는지 확인
    - API형 시작하기
  - 관리페이지 --> 공개 설정
  - 카카오톡에서 검색 후 제대로 검색 및 실행하는지 확인

### 3장

@csrf_exempt는 카카오톡에서 message를 내 서버로 전송할 때 데이터를 post값으로 전송하기 때문에 Django에서 post 값으로 데이터를 전송 할 때 오류를 방지.

- message 함수 구현
- message 함수까지 카카오톡 API에 구현
