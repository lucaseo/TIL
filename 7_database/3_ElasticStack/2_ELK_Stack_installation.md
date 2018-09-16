---
layout: "post"
title: "[Elastic Stack] How to install Elastic Search & Kibana on AWS EC2 Instance"
date: "2018-09-12 23:04:22"
category:
  - "Database"
  - "ELK"
tags:
  - "elastic"
  - "elastic stack"
  - "elasticsearch"
  - "kibana"
---

# Elasticsearch & Kibana 설치하기

* 본 포스팅은 사용자가 클라우드 서버에 대한 기초적인 지식을 가지고, 1개 이상의 클라우드 서버를 운용 중이라는 전제 하에 진행됩니다.

* * * 

### 1. AWS EC2 접속

#### 1.1. AWS EC2 Ubuntu 서버에 접속

```
$ ssh -i <your aws pem key> ubuntu@<your ec2 public ip>
```



#### 1.3. Elastic Stack 설치를 위한 디렉토리를 생성

```
$ cd ~
$ mkdir elastic
$ cd elastic
```

<br>
<br>

### 2. Elasticsearch 설치파일 다운로드 및 설치


#### 2.1. Elasticsearch 설치파일 다운로드

현 시점에서 가장 최신 버전은 `6.4.0`이다. 아래 `wget` 에 이은 url에서 버전 정보만 바꾸어주면 다른 버전 설치도 가능하다.

```
$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.4.0.tar.gz
```

#### 2.2. Elasticsearch 설치파일 압축 해제

```
$ tar -xzvf elasticsearch-6.4.0.tar.gz
```

압축 해제 후 설치파일은 제거해준다

```
$ rm elasticsearch-6.4.0.tar.gz
```

<br>
<br>

### 3. Elasticsearch 환경설정

#### 3.1. max file dexcriptors 와 thread

**3.1.1. 작업 전**

```
$ ulimit -Hn
```

default값 `4096` 이 출력 되는 것을 확인한다.


**3.1.2. `limits.conf` 편집**

```
$sudo vi /etc/security/limits.conf
```

**3.1.3. 아래의 코드를 `limits.conf` 가장 아래 입력하고 ESC키 -> `:wq` -> ENTER키로 저장 후 빠져나온다.**

```
# max file descriptor
*        hard    nofile           65536
*        soft    nofile           65536

# thread
*        hard    nproc           65536
*        soft    nproc          65536
```

**3.1.4. ec2 를 재접속 한 후, 값이 65536으로 변경된 것을 확인한다.**

```
$ ulimit -Hn
```




#### 3.2. virtual memory areas 늘리기

**3.2.1. 작업 전 확인**

```
$ sudo sysctl -a | grep vm.max_map_count
```

default값 65530이 리턴 되는 것을 확인한다.

**3.2.2. `sysctl.conf` 편집**

```
$ sudo vi /etc/sysctl.conf
```

**3.2.3 아래의 코드를 `sysctl.conf` 가장 아래 입력하고 ESC키 -> `:wq` -> ENTER키로 저장 후 빠져나온다.**

```
vm.max_map_count=262144
```

**3.2.4. 시스템 재부팅 및 ec2 재접속한다.**

```
$ sudo reboot
```
**3.2.5. 변경된 값 확인**

```
$ sudo sysctl -a | grep vm.max_map_count
```


#### 3.3. JVM Heap Memory 설정

ELK 권장사항

- min size = max size 일치
- 일반적으로 서버 메모리의절반 정도 할당할 것을 권장
    - 반은 ES 할당 / 반은 Lucene 할당
- 최대 32GB를 넘지 않도록 한다. 
- Free Tier EC2 인스턴스라면 필수 !!
- 넉넉한 EC2 인스턴스를 사용 중이라면 꼭 하지 않아도 되는 작업이다.

<br>

**3.3.1. Elasticsearch config 디렉토리로 이동**

```
$ cd ~
$ cd elastic/elasticsearch-6.4.0/config
```

**3.3.2. JVM 설정 파일 편집**

```
$ vi jvm.options
```

**3.3.3 아래와 같이 Xms와 Xmx를 모두 128m 으로 변경 후, ESC키 -> `:wq` -> ENTER키로 저장 후 빠져나온다.**

```
-Xms128m
-Xmx128m
```


### 3.4. Network 설정

**3.4.1. elasticsearch config 디렉토리로 이동**

```
$ cd ~
$ cd elastic/elasticsearch-6.4.0/config
```

**3.4.2. `elasticsearch.yml` 파일 편집**

```
$ vi elasticsearch.yml
```

**3.4.3. network.host에 EC2 인스턴스의 public DNS 주소를 입력한 후, ESC키 -> `:wq` -> ENTER키로 저장 하고 빠져나온다.**

Public DNS 주소를 모른다면, AWS EC2 관리 웹페이지에서 참고할 수 있다. 

```
network.host: <your Public DNS>
```

<br>
<br>

### 4. Kibana 설치파일 다운로드 및 설치

#### 4.1. Kibana 설치파일 다운로드

키바나도 앞서 방법과 동일하게 설치할 수 있다.

```
$ wget https://artifacts.elastic.co/downloads/elasticsearch/kibana-6.4.0-linux-x86_64.tar.gz
```

#### 4.2. Kibana 설치파일 압축 해제

```
$ tar -xzvf kibana-6.4.0-linux-x86_64.tar.gz
```

압축 해제 후 설치파일은 제거해준다

```
$ rm kibana-6.4.0-linux-x86_64.tar.gz
```

<br>
<br>

### 5. Kibana 환경설정

**5.1.1. Kibana config 디렉토리로 이동**

```
$ cd ~ 
$ cd elastic/kibana-5.6.4-linux-x86_64/config
```

**5.1.2. `kibana.yml` 파일 편집**

```
$ vi kibana.yml
```

**5.1.3. searver.host와 elasticsearch.url 부분 수정**

Elasticsearch의 포트는 9200이다.
참고로 Kibana의 포트는 5602를 사용한다. 
AWS EC2 관리 페이지 security 탭을 통해 9200, 5601 포트를 미리 열어놓는 것을 권장한다.

```
server.host : "<your Public DNS>"
elasticsearch.url: "http://<your EC2 Public IP>:9200"
```

마찬가지로 ESC키 -> `:wq` -> ENTER키로 통해 저장 후 빠져나온다.

<br>
<br>

### 6. Elasticsearch & Kibana 실행

계속 띄워둔 상태로 작업을 할 것이므로, `nohup` 커맨드를 통해서 백그라운드에서도 계속 실행이 될 수 있도록 한다.

#### 6.1. Elasticsearch 실행

**6.1.1. Elasticsearch 백그라운드로 실행**

```
$ cd ~
$ cd elastic/elasticsearch-6.4.0
$ nohup bin/elasticsearch &
```

**6.1.2. 브라우저에서 `http://<your EC2 public IP>:9200` 에 접속해서 실행을 확인한다.**

![](/images/20180913/elastic_check.png)



#### 6.2. Kibana 실행

**6.2.1. Kibana 백그라운드 실행**

```
$ cd ~
$ cd elastic/kibana-6.4.0-linux-x86_64
$ nohup bin/kibana &
```

**6.2.2. 브라우저에서 `http://<your EC2 public IP>:5601`에 접속해서 키바나 실행을 확인한다. (프리티어 EC2 환경에서는 시간이 오래 걸릴 수 있다.)**

![](/images/20180913/kibana_check.png)



<br>
<br>

* * * *

Reference

[남지열님 Elastic Stack을 활용한 Dashboard 만들기 Github repository](https://github.com/higee/elastic/wiki/Elastic-Stack-설치-및-환경-설정.)