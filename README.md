# Web scraping

## 0. Overview
### Scraping job lists on Radiokorea website. Using AWS lambda, run the code regularly. Scraping data is saved in Amazon S3 Bucket.
### 라디오 코리아 게시판에 올라온 잡 리스팅 중에 원하는 항목만을 필터링하여 CSV로 아마존 S3에 저장하는 코드


## 1. Prerequisite
### 1. Code use libraries that Amazon lambda doesn't support natively, you must zip library (pip3 install datetime beautifulsoup4 requests -t ./custom_directory) and add layer to lambda fuctions.[tutorial](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
### 2. Creating schedule rule using Amazon CloudWatch and add to triger on lambda fuctions. 