# samsungZZ

### open api 다루기
#### 로드
<ol>

<li>지하철 역별 시간대별 승하차인원 데이터 로드
<li>터미널에서 다음을 실행: <code>python manage.py fetch_subway_data</code>
<li>잘못된 데이터 삭제
<details>
    <summary>sql 쿼리</summary>
<pre><code>
delete from subway_monthly_time_slot_passenger_counts where line == "1호선" and sttn == "서빙고";
delete from subway_monthly_time_slot_passenger_counts where line == "1호선" and sttn == "한남";
delete from subway_monthly_time_slot_passenger_counts where line == "1호선" and sttn == "옥수";
delete from subway_monthly_time_slot_passenger_counts where line == "1호선" and sttn == "응봉";
delete from subway_monthly_time_slot_passenger_counts where line == "1호선" and sttn == "이촌(국립중앙박물관)";
delete from subway_monthly_time_slot_passenger_counts where line == "1호선" and sttn == "왕십리(성동구청)";
</code></pre>
</details>
</ol>


1. 지하철 역별 위도 경도 데이터 로드
2. 터미널에서 다음을 실행: `python manage.py fetch_subway_lat_lng_data`

#### 초기화
<ol>
<li>지하철 역별 시간대별 승하차인원 데이터 초기화
<li>터미널에서 <code>sqlite3 db.sqlite3</code>
<li><code>delete from subway_monthly_time_slot_passenger_counts</code>
</ol>

1. 지하철 역별 위도 경도 데이터 초기화
2. 터미널에서 `sqlite3 db.sqlite3`
3. `delete from subway_station_lat_lng`

### csv 파일 다루기
#### 로드
1. `data_collection/manage/load_csv.py`에서 로드하고 싶은 csv 파일 경로 입력
2. 터미널에서 다음을 실행 `python manage.py load_csv`
#### 초기화
1. 터미널에서 shell을 열어서 사용
2. 다음을 입력하고 실행 `{모델}.objects.all().delete()`

### 지하철 역별 승하차인원 및 편의시설 정보 확인

1. (DB 실행) 터미널에서 다음을 실행 
* `python manage.py load_csv`
* `python manage.py fetch_subway_data`
2. (서버 접속) 터미널에서 서버 실행
* `python manage.py runserver`
* http://127.0.0.1:8000/subway/station-information 으로 접속
* 예시 화면
![스크린샷 2024-10-21 222927](https://github.com/user-attachments/assets/6e7b8ae3-2bc4-4eb2-9268-8cce9751c99d)

* http://127.0.0.1:8000/data-collection/api/subway-daily-passenger-difference/날짜/호선/역명/시간대/ (예시. http://127.0.0.1:8000/data-collection/api/subway-daily-passenger-difference/2024-05-01/1호선/서울역/07시-08시/)
* 예시 화면
![image](https://github.com/user-attachments/assets/aa0c8b0a-19fe-4173-a251-f465ac99f796)


### 지하철 혼잡도 호선별 시각화
호선, 평일/주말, 시간대를 선택하면 그에 맞는 정보가 필터링되어 출력됩니다.

1. DB 모델 최신화를 꼭 해주세요!
* `python manage.py makemigrations`
* `python manage.py migrate`
2. 터미널에서 서버를 실행 후, 아래 링크로 접속해주세요.
* url: `/func1/congestion`
3. 그 외 주의 사항
* function: 세 가지 드롭 다운에 필요한 값을 모두 선택하면 출력됩니다.
* `혼잡도 등급`: 1~4까지 존재하며 순서대로 초록, 노랑, 주황, 빨강색으로 표시됩니다. 존재하지 않는 값은 회색으로 표시됩니다.
* 원 위에 커서를 대면 팝업창으로 해당 역에 대한 정보가 간소화되어 표시됩니다.
* 조회를 누른 후 시간이 조금 소요될 수 있으므로 양해 부탁드립니다!
* 예시 화면
![image](https://github.com/user-attachments/assets/5014937c-8862-4be7-8973-d25beb2065a9)
  
