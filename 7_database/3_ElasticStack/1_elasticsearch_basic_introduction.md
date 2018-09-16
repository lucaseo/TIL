---
layout: "post"
title: "[Elastic Stack] Basic Introduction"
date: "2018-08-16 13:28:56"
category:
  - "Database"
  - "ELK"
tags:
  - "Elastic Stack"
---

# Elastic Stack이란

`Elastic Stack` 이란 모든 유형의 데이터(특히 _비정형 데이터_)를 저장, 실시간으로 검색, 분석 및 시각화 할 수 있도록 도와주는 Elastic의 오픈소스 서비스 제품이다.
기존에 `Elasticsearch`, `Logstash`, `Kibana`를 같이 묶어 `ELK` 라는 서비스명으로 제공하기 시작했고, 현재 `Beats`가 포함되어 `Elastic Stack` 혹은 `ELK Stack`이란 이름으로 서비스가 제공되고 있다.

### Elastic Stack의 구성

![](/images/20180816/image1.png)


|      종류       |           기능          |                                    특이점                                   |
|---------------|-------------------------|-----------------------------------------------------------------------------|
| Elasticsearch | 데이터 검색, 분석, 저장 |                                                                             |
| Logstash      | 데이터 수집, 변환, 운송 | 데이터 처리 파이프라인. <br> 특히 로그를 운반하는 역할.                                                   |
| Kibana        | 데이터 시각화, 분석     |                                                                             |
| Beats         | 데이터 수집, 운송       | Logstash와 비슷하나, <br> 변환 기능이 제외되어 있음. <br> 보다 가볍게 사용할 수 있음. |



이외에 **Elastic Cloud**와 **X-pack**이 추가로 있으며, 기업을 대상으로 한 Enterprise 솔루션도 확대되고 있는 추세다.

- X-pack의 경우 유료이며, 보안을 강화하여 유저에게 권한까지 부여 가능하다.
- X-pack의 머신러닝 기능은 현재로서는 데이터의 이상징후를 탐지하는 수준이다.

<br>
<br>

### Elastic, 어떻게 좋은가?

- **Near Realtime**
    - 데이터 색인 후 약 1초 후 Refresh 시점부터 **거의 실시간**으로 검색결과에 반영됨 
<br>
<br>
- **Fast**
    - 기본적으로 모든 Field에 대해 Indexing(색인) 처리를 하기 때문에 **검색 처리 시간이 짧다**
<br>
<br>
- **Horizontal Scalability**
    - Elastic Cluster에 Elasticsearch Node를 1개씩 추가하며 **수평적으로 확장하기에 용이**하다
<br>
<br>
- **Distributed Operation**
    - 데이터를 조각(shard)로 세분화 하여 분산 저장하기 때문에 **처리 속도가 향상**된다.
<br>
<br>
- **Replica Shard**
    - 데이터 조각을 복제하여 다른 Node에도 저장하기 때문에, 특정 Node가 다운되거나 **손실이 생겨도 데이터 유실 없이 운영할** 수 있다.


<br>
<br>

### Elastic Stack에서의 용어 비교


| RDBMS    | Excel      | Elastic  |                                                                                                                                                                       |
|----------|------------|----------|------------------------------------------------------------------------------------------------------------------------------|
| Database | Excel File | Index    | 최상위 데이터 계층 <br> Document의 덩어리.                                                                                                                            |
| Table    | Sheet      | Type     | Document들을 담고 있는 컨테이너.|
| Row      | Row        | Document | 데이터 검색을 위한 최소의 단위. (\*)                                                                                                                                      |
| Column   | Column     | Field    | JSON으로 이루어진 데이터의 Property.                                                                                                                                  |
| Schema   | 없음       | Mapping  | Index / Type / Document의 <br> 저장 규칙을 정의한다.                                                                                                                       |

\* RDBMS, Excel과는 달리 엘라스틱에서는 1 Index에 1개의 Type만 할당되어 사실상 의미가 사라진 상태이며, 7.0버전으로 업그레이드 시 Type이란 개념은 폐지 될 예정이다.

<br>
<br>

### Elastic의 Work Flow

![](/images/20180816/image3.png)

0. Elasticsearch
    - Mapping 설정
<br>
<br>
1. Logstash
    - 데이터 전처리 & 전송
<br>
<br>
2. Elasticsearch
    - 데이터 저장
<br>
<br>
3. Kibana
    - Index 등록
    - EDA
    - 차트 선택
    - Aggregation 선택
    - 데이터 시각화
    - 대시보드 생성
