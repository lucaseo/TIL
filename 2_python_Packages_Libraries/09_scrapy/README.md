# Scrapy

<br>

## **1**.

### 1. 1. Install Scrapy

`$ pip3 install scrapy`

### 1. 2. Initiate Scrapy

`$ scrapy startproject <project name>`

### 1. 3. Tree Structure

```
$ tree
.
└── <project name>
    ├── <project name>
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── items.py
    │   ├── middlewares.py
    │   ├── pipelines.py
    │   ├── settings.py
    │   └── spiders
    │       ├── __init__.py

    │       └── __pycache__
    └── scrapy.cfg

5 directories, 7 files
```

#### 1. 3. 1.

- `item.py`
원하는 부분의 스크랩해서 데이터를 저장할 때 사용하는 사용자가 정의한 자료구조 클래스

- `pipelines.py`  
스크랩한 데이터를 이를 자유롭게 후처리 가공하거나 다양한 파일 형태로 저장할 수 있도록 하는 클래스 (filtering, database input ...)

- `setting.py`  
`spider`나 `pipeline`의 세부적인 사   설정.

- `spiders`폴더  
스크랩할 내용의 코드

<br>

## 2. Preparation_1

### 2. 1. `item.py`

- 가져올 내용에 대한 변수 선언

### 2. 2.

- `spiders` 디렉토리 내 spider파일 생성
- class와 함수 선언

### 3. Shell에서 추출하기

#### 3. 1. Scrapy Shell 실행

`$ scrapy shell "<url>"`

#### 3. 2. Scrapy Shell command

- (ex) 설렉터를 사용하여 데이터 추출  
`response.xpath('//a/text()').extract()`


### 4. Spider에서 추출하기

- 저장
`$ scrapy crawl dmoz -o item.json` --> item.json으로 저장
