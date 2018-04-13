# Scrapy

<br>

## 1.

### 1. 1. Install Scrapy

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
긁어올 데이터를 클래스 형태로 지정한다.

- `pipelines.py`
긁어온 데이터를 후처리 하기 위한 동작 (filtering, database input ...)

- `setting.py`
`spider`의 설정.

- `spider`폴더
스크랩할 내용의 코드

#### 1. 3. 2. ``
