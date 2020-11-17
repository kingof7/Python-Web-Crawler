# 크롤러 : 웹에서 정보를 수집하는 프로그램
# 예시 : 공연 예매, 수강신청, 구글&네이버
"""
1. 원하는 정보가 있는 웹페이지에 접속
2. 페이지 로딩
3. 페이지에서 원하는 정보를 눈으로 찾아서 본다. ***
4.
"""
'''
selector: 통(정보가담겨있는)을 찾는 것
HTML : 내용과 전체적인 구조를 담당 
CSS : 각 요소들의 속성(크기,색상,위치 등..) - 크롤러 생성과 무관
JS : 화면의 움직임, 추가 데이터 가져오는 로직 담당(알람,반복,요청 등등)

- request, beautifulsoup (가장 기본 크롤러)
+ 모듈 사용법 
+ 셀렉터 만드는 법

- scrapy : 다중 페이지 수집 
- selenium - 더 깔끔하게 (고급 크롤러) JS를 가지고 추가내용을 불러오느 경우 - 예매 자동화 등...)
+ 셀레늄의 모듈 사용법 학습

'''