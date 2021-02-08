# 오늘 뭐 입지?

#### 👚매일 어떤 셔츠와 어떤 바지를 입을지 또 신발은 어떤 걸 신을지 고민하는 사람들을 위한 코디 추천 사이트



#### 👚 패션에 가장 중요한 요소 중 하나는 계절감!

#### 현재 온도를 기준으로 사용자의 성별, 선호 스타일, 목적에 맞는 상의, 하의, 신발을 동시에 추천 받아 옷을 고를 수 있습니다.



# 프로젝트 정보

## ◼ 팀원

### 이재환

------

* 팀장

* 데이터베이스 분석, 관리

* Django Back-End 기능 구현

  

### 여찬진

------

* Web Scrapping을 통한 데이터 수집
* Pandas, seaborn을 활용한 데이터 전 처리 및 시각화



### 유은서

------

* Django Front-End 페이지 제작
* Django Back-End 기능 구현



## ◼ 프로젝트 기간

2020.08.10 ~ 2020.09.03



## ◼ 개발 플랫폼

▪ Windows 10



## ◼ 개발 툴

▪ Pychram

▪ Jupyter Notebook



## ◼ 사용 기술

▪ Python

▪ Django

▪ jQuery

▪ HTML / CSS / JavaScript

▪ Bootstrap

▪ MongoDB



# 아키텍처

![image](https://user-images.githubusercontent.com/59273807/103452742-fa10f780-4d15-11eb-8749-690573765a4b.png)

![image](https://user-images.githubusercontent.com/59273807/103452766-2a589600-4d16-11eb-8fda-ce18c52e3db9.png)

# 데이터베이스 구조

![image](https://user-images.githubusercontent.com/59273807/103452753-1319a880-4d16-11eb-8365-78423d25f3c1.png)

# 스토리보드

![image](https://user-images.githubusercontent.com/59273807/103452868-5a546900-4d17-11eb-9c7e-5a4f87b3e148.png)



##### OpenWeather API를 이용하여 실시간 기온 정보에 따라 옷과 신발 데이터를 필터링하여 화면에 표시



------



![image](https://user-images.githubusercontent.com/59273807/103452876-693b1b80-4d17-11eb-986e-4d6ed758612e.png)



##### 주간, 월간별 좋아요를 많이 받은 순으로 데이터를 필터링하여 화면에 표시



------

![image](https://user-images.githubusercontent.com/59273807/103452887-79eb9180-4d17-11eb-8832-59b95628e24c.png)

##### 최신 트렌드 분석을 위한 의류 데이터에 포함되어 있는 “해시태그” 데이터 시각화



------



![image](https://user-images.githubusercontent.com/59273807/103452890-87a11700-4d17-11eb-80d3-6e82f9471d5b.png)



##### 메인 화면의 “코디네이션” 버튼 클릭 시 원하는 스타일과 어떤 장소에서의 옷을 추천받을지 선택



------

![image](https://user-images.githubusercontent.com/59273807/103452893-925bac00-4d17-11eb-980e-775e88d29881.png)



##### "코디네이션"을 통해 추천받은 목록에서 마음에 드는 상의, 하의, 신발을 조합하여 저장



------

![image](https://user-images.githubusercontent.com/59273807/103452896-9c7daa80-4d17-11eb-911d-ac450abc7767.png)



##### 메인 화면의 “내가 저장한 옷” 버튼 클릭 시 코디네이션에서 저장한 옷을 조회/삭제



# 제공 서비스

▪ 의류 쇼핑몰 스크래핑을 통해 데이터 수집

▪ 로그인 / 회원가입 (아이디, 비밀번호, 이름, 성별 ,선호 스타일)

▪ OpenWeather API를 이용하여 실시간 기온 정보에 따라 옷 필터링 (참조: 기온별 옷차림 픽토그램)

![image](https://user-images.githubusercontent.com/59273807/103452805-99ce8580-4d16-11eb-8d2a-d623f24008fd.png)

▪ 최신 트렌드 분석을 위한 의류 데이터에 포함되어 있는 해시태그 데이터 시각화

▪ 선호 스타일, 목적(데이트/출근/학교)을 사용자로부터 입력받아 매칭되는 상의, 하의, 신발을 각각 5개씩 리스트화. 사용자는 리스트 중 한 가지씩 선택하여 코디를 저장

▪ 좋아요 기능으로 많은 선택을 받은 의류들을 주간, 월간 베스트로 선정하여 표시