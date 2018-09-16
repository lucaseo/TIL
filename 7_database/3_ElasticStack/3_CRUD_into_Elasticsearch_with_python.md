---
layout: "post"
title: "[Elastic Stack] How to CRUD to Elasticsearch with Python"
date: "2018-09-13 20:26:29"
category:
  - "Database"
  - "ELK"
tags:
  - "elastic"
  - "elastic stack"
  - "elasticsearch"
  - "kibana"
  - "python"
---


# 파이썬으로 엘라스틱서치에 데이터 CRUD 하기

ELK Stack 중에서 **Logstash**는  데이터를 수집, 변환하여 Elasticsearch로 운송하는 기능을 한다. 하지만 Logstash는 지속적인 로그를 수집 할 때는 강력한 기능을 하는 것 같지만, 개인적으로 사용법을 익히기에는 어려움을 느꼈다. 단순히 Kibana를 활용하여 토이데이터를 시각화하는 용도로 다른 방법을 찾아보던 중, 역시나 파이썬에도 관련 패키지가 있음을 알게 되었다. 파이썬을 사용해서 당장에 필요한 가상데이터를 Elasticsearch에 넣어보자.

<br>

### 1. elasticsearch 파이썬 패키지 설치

```
$ pip3 install elasticsearch
```
<br>

### 2. 기본 Snippet

```
# 패키지 불러오기
from elasticsearch import Elasticsearch

# 클라우드 연결 객체 생성
es = Elasticsearch([{'host': '<your cloud server public IP>', 'port': '9200'}])
```

**2.1. 테스트로 Index를 생성해보자 (Create)** 

참고로 ELK Stack에서의 Index는 RDBMS에서의 Database와 같은 개념을 지니고 있다. 용어가 다르니, 차이점은 [엘라스틱스택 소개](https://lucaseo.github.io/2018/08/16/reviewNote-20180816/) 포스팅을 참고하시면 된다.

```
# Index 생성하기
es.indices.create(
    index='test_python_to_elastic', 
    body={
        "mappings" : {
            "type1" : {
                "properties" : {
                    "field1" : { 
                        "type" : "text" 
                      }
                  }
              }
          }
      }
  )
```

다음과 같은 결과가 리턴되어 성공적으로 Index가 등록 되었다.

```
# 리턴되는 결과
{'acknowledged': True,
 'shards_acknowledged': True,
 'index': 'test_python_to_elastic'}
```

Kibana 브라우저에 접속해서 등록된 Index를 확인해보자

- Kibaba 브라우저 접속 (http://"your cloud server public IP":5601)

![](/images/20180913/to_kibana_1.png)

- Management 클릭

![](/images/20180913/to_kibana_2.png)

- Elasticsearch - Index Management 클릭

![](/images/20180913/to_kibana_3.png)

![](/images/20180913/to_kibana_4.png)

Index가 등록된 것을 확인할 수 있다.


**2.2. Index를 읽어보자 (Read)**

```
es.search(
    index='test_python_to_elastic',
    body={ 
          "query": {
              "match_all" : {
                }
           }
      }
 )
```

```
# 리턴되는 결과
{'took': 0,
 'timed_out': False,
 '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0},
 'hits': {'total': 0, 'max_score': None, 'hits': []}}
```

**2.3. 데이터를 넣어보자 (Update)**


```
es.create(
    index='test_python_to_elastic', 
    doc_type='type1', 
    body= {
        "doc" : {
            "field1" : "inserting data"
         }
     },
     id = 'data1'
)
```

성공적으로 데이터를 업데이트했다.

```
# 리턴되는 결과
{'_index': 'test_python_to_elastic',
 '_type': 'type1',
 '_id': 'data1',
 '_version': 1,
 'result': 'created',
 '_shards': {'total': 2, 'successful': 1, 'failed': 0},
 '_seq_no': 0,
 '_primary_term': 1}
```


**2.4. 데이터를 삭제해보자 (Delete)**

```
es.indices.delete(index='test_python_to_elastic')
```

성공적으로 삭제되었다.

```
# 리턴되는 결과
{'acknowledged': True}
```

<br>

### 3. csv형태 데이터프레임 한꺼번에 삽입하기

실제 환경에서 데이터를 하나씩 일일이 업데이트 할 일은 거의 없을 것이다. 패키지의 **Bulk API**를 사용하면 csv나 excel 포맷의 테이블 형태의 데이터를 한꺼번에 Elasticsearh에 넣을 수 있다.


**3.1. 데이터셋 준비**

테스트를 하기 위해서 Kaggle에서 입문용 데이터로 사용되는 [_**Boston House Price**_](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) 데이터셋을 준비했다.

```
import pandas as pd

df = pd.read_csv('../../dataset/bostonHousePrice/train.csv')
print(df.info())
print(df.head())
```

데이터셋의 형태는 다음과 같다.

```
# 리턴되는 결과
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 1460 entries, 0 to 1459  
Data columns (total 81 columns):  
Id               1460 non-null int64  
MSSubClass       1460 non-null int64  
MSZoning         1460 non-null object  
...  
MoSold           1460 non-null int64  
YrSold           1460 non-null int64  
SaleType         1460 non-null object  
SaleCondition    1460 non-null object   
SalePrice        1460 non-null int64  
dtypes: float64(3), int64(35), object(43)  
memory usage: 924.0+ KB
```

![](/images/20180913/dataset.png)


**3.2. Index 생성**

다음과 같이 매핑 없이 Index만 생성할 수도 있다. (데이터셋 칼럼이 81개가 되어, 매핑은 생략.)

```
es.indices.create(index='boston_house_price')
```

```
# 리턴되는 결과
{'acknowledged': True,
 'shards_acknowledged': True,
 'index': 'boston_house_price'}
```


_**Mapping의 설정은 꼭 필요할까?**_

Mapping을 설정하지 않아도 error가 발생하지는 않는다. 그리고 ES가 데이터를 감지하고 자동으로 Mapping을 한다. **하지만** 사용자가 원하는 data type으로 데이터가 저장된다는 보장이 없다. 예를 들어 `2017-01-31 13:34:93` (YYYY-MM-DD HH:MM:SS)의 형태로 이루어진 datetype 데이터를 삽입할 때 mapping을 설정하지 않는다면, ES는 해당 데이터를 그냥 String type으로 저장하는 경우도 있는 것이다. 그러므로 Index(database or table)의 Field(column)들이 특정 type으로 저장되는지의 여부가 중요하다면, Mapping을 설정해야한다. 데이터가 색인(index)되기 전에 Mapping을 미리 설정하는 것이 권장된다.



**3.2. Dataframe을 Dictionary 형태로 변환**

```
documents = df.to_dict(orient='records')
print(documents)
```

```
# 리턴되는 결과
[{'Id': 1,
  'MSSubClass': 60,
  'MSZoning': 'RL',
  'LotFrontage': 65.0,
  'LotArea': 8450,
  'Street': 'Pave',
  'Alley': 0,
  'LotShape': 'Reg',
  'LandContour': 'Lvl',
  'Utilities': 'AllPub',
  'LotConfig': 'Inside',
  'LandSlope': 'Gtl',
	.
	.
	.
```

**3.3. 변환한 Dictionary를 Bulk API를 사용하여 Elasticsearch에 입력**

```
from elasticsearch.helpers import bulk

bulk(es, documents, index='boston_house_price',doc_type='boston_house_price', raise_on_error=True)
```

성공적으로 Update 되었다.

```
# 리턴되는 결과
(1460, [])
```

Kibana에서 확인해보자 ! 

![](/images/20180913/to_kibana_5.png)

![](/images/20180913/to_kibana_6.png)

![](/images/20180913/to_kibana_7.png)

![](/images/20180913/to_kibana_8.png)


**3.4.시계열 데이터 등록하기**

Elastic Stack은 시계열 특성이 있는 데이터를 다룰 때 강력함을 자랑한다. 추후 시계열 데이터를 분석하기 위해, 또 다른 입문용 [_**Bike Sharing Demand**_](https://www.kaggle.com/c/bike-sharing-demand) 데이터셋을 추가했다.

```
df = pd.read_csv('../../dataset/bikeSharingDemand/train.csv')
print(df.info())
print(df.head())
```

```
# 결과값
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10886 entries, 0 to 10885
Data columns (total 12 columns):
datetime      10886 non-null object
season        10886 non-null object
holiday       10886 non-null int64
workingday    10886 non-null int64
weather       10886 non-null int64
temp          10886 non-null float64
atemp         10886 non-null float64
humidity      10886 non-null int64
windspeed     10886 non-null float64
casual        10886 non-null int64
registered    10886 non-null int64
count         10886 non-null int64
dtypes: float64(3), int64(7), object(2)
memory usage: 1020.6+ KB
```

![](/images/20180913/dataset2.png)

Kibana에서 시계열 데이터를 분석하기 위해서는, Index의 기준이 되는 **시간**을 명시해야 한다. 현재 `datetime` 컬럼은 단순히 `object` 타입의 데이터로 이루어져 있으니, date형식으로 변환한 후 업데이트를 해주자.

```
df['datetime'] = pd.to_datetime(df['datetime'])

print(df.dtypes)
```

아래와 같이 변경된 것을 확인할 수 있다.

```
# 결과값
datetime      datetime64[ns]
season                object
holiday                int64
workingday             int64
weather                int64
temp                 float64
atemp                float64
humidity               int64
windspeed            float64
casual                 int64
registered             int64
count                  int64
dtype: object
```

이제 앞서 **Boston House Price** 데이터셋의 케이스와 동일한 방법으로 Elasticsearch에 업데이트해보자.

```
es.indices.create(index='bike_sharing_demand')
```

```
# 결과값
{'acknowledged': True,
 'shards_acknowledged': True,
 'index': 'bike_sharing_demand'}
```

```
documents = df.to_dict(orient='records')

bulk(es, documents, index='bike_sharing_demand',doc_type='bike_sharing_demand', raise_on_error=True)
```

정상적으로 업데이트 됐다. 
```
# 결과값
(10886, [])
```

정상적으로 업데이트 된 결과를 Kibana에서도 확인할 수 있다.

![](/images/20180913/to_kibana_9.png)




<br>
<br>

* * * *

Reference

- [https://m.blog.naver.com/nomadgee/220867517835](https://m.blog.naver.com/nomadgee/220867517835)
- [https://creativedata.atlassian.net/wiki/spaces/SAP/pages/130252820/Python+-+Index+Search+documents+in+ElasticSearch](https://creativedata.atlassian.net/wiki/spaces/SAP/pages/130252820/Python+-+Index+Search+documents+in+ElasticSearch)

