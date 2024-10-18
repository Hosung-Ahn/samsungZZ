import folium
import requests
from collections import deque
from .models import SubwayStationLatLng

class StationMap :
    def __init__(self, api_key = "4408c2262908b5c0a96f61beee8e80f2") :
        self.edges = [{'연천역': ['전곡역'],
            '전곡역': ['청산역'],
            '청산역': ['소요산역'],
            '소요산역': ['동두천역'],
            '동두천역': ['보산역'],
            '보산역': ['동두천중앙역'],
            '동두천중앙역': ['지행역'],
            '지행역': ['덕정역'],
            '덕정역': ['덕계역'],
            '덕계역': ['양주역'],
            '양주역': ['녹양역'],
            '녹양역': ['가능역'],
            '가능역': ['의정부역'],
            '의정부역': ['회룡역'],
            '회룡역': ['망월사역'],
            '망월사역': ['도봉산역'],
            '도봉산역': ['도봉역'],
            '도봉역': ['방학역'],
            '방학역': ['창동역'],
            '창동역': ['녹천역'],
            '녹천역': ['월계역'],
            '월계역': ['광운대역'],
            '광운대역': ['석계역'],
            '석계역': ['신이문역'],
            '신이문역': ['외대앞역'],
            '외대앞역': ['회기역'],
            '회기역': ['청량리역'],
            '청량리역': ['제기동역'],
            '제기동역': ['신설동역'],
            '신설동역': ['동묘앞역'],
            '동묘앞역': ['동대문역'],
            '동대문역': ['종로5가역'],
            '종로5가역': ['종로3가역'],
            '종로3가역': ['종각역'],
            '종각역': ['시청역'],
            '시청역': ['서울역역'],
            '서울역역': ['남영역'],
            '남영역': ['용산역'],
            '용산역': ['노량진역'],
            '노량진역': ['대방역'],
            '대방역': ['신길역'],
            '신길역': ['영등포역'],
            '영등포역': ['신도림역'],
            '신도림역': ['구로역'],
            '구로역': ['구일역', '가산디지털단지역'],
            '구일역': ['개봉역'],
            '가산디지털단지역': ['독산역'],
            '개봉역': ['오류동역'],
            '독산역': ['금천구청역'],
            '오류동역': ['온수역'],
            '금천구청역': ['석수역', '광명역'],
            '온수역': ['역곡역'],
            '석수역': ['관악역'],
            '광명역': [],
            '역곡역': ['소사역'],
            '관악역': ['안양역'],
            '소사역': ['부천역'],
            '안양역': ['명학역'],
            '부천역': ['중동역'],
            '명학역': ['금정역'],
            '중동역': ['송내역'],
            '금정역': ['군포역'],
            '송내역': ['부개역'],
            '군포역': ['당정역'],
            '부개역': ['부평역'],
            '당정역': ['의왕역'],
            '부평역': ['백운역'],
            '의왕역': ['성균관대역'],
            '백운역': ['동암역'],
            '성균관대역': ['화서역'],
            '동암역': ['간석역'],
            '화서역': ['수원역'],
            '간석역': ['주안역'],
            '수원역': ['세류역'],
            '주안역': ['도화역'],
            '세류역': ['병점역'],
            '도화역': ['제물포역'],
            '병점역': ['세마역', '서동탄역'],
            '제물포역': ['도원역'],
            '세마역': ['오산대역'],
            '서동탄역': [],
            '도원역': ['동인천역'],
            '오산대역': ['오산역'],
            '동인천역': ['인천역'],
            '오산역': ['진위역'],
            '인천역': [],
            '진위역': ['송탄역'],
            '송탄역': ['서정리역'],
            '서정리역': ['평택지제역'],
            '평택지제역': ['평택역'],
            '평택역': ['성환역'],
            '성환역': ['직산역'],
            '직산역': ['두정역'],
            '두정역': ['천안역'],
            '천안역': ['봉명역'],
            '봉명역': ['쌍용역'],
            '쌍용역': ['아산역'],
            '아산역': ['탕정역'],
            '탕정역': ['배방역'],
            '배방역': ['온양온천역'],
            '온양온천역': ['신창역'],
            '신창역': []},
            {'신설동역': ['용두역'],
            '용두역': ['신답역'],
            '신답역': ['용답역'],
            '용답역': ['성수역'],
            '성수역': ['건대입구역'],
            '건대입구역': ['구의역'],
            '구의역': ['강변역'],
            '강변역': ['잠실나루역'],
            '잠실나루역': ['잠실역'],
            '잠실역': ['잠실새내역'],
            '잠실새내역': ['종합운동장역'],
            '종합운동장역': ['삼성역'],
            '삼성역': ['선릉역'],
            '선릉역': ['역삼역'],
            '역삼역': ['강남역'],
            '강남역': ['교대역'],
            '교대역': ['서초역'],
            '서초역': ['방배역'],
            '방배역': ['사당역'],
            '사당역': ['낙성대역'],
            '낙성대역': ['서울대입구역'],
            '서울대입구역': ['봉천역'],
            '봉천역': ['신림역'],
            '신림역': ['신대방역'],
            '신대방역': ['구로디지털단지역'],
            '구로디지털단지역': ['대림역'],
            '대림역': ['신도림역'],
            '신도림역': ['문래역', '도림천역'],
            '문래역': ['영등포구청역'],
            '도림천역': ['양천구청역'],
            '영등포구청역': ['당산역'],
            '양천구청역': ['신정네거리역'],
            '당산역': ['합정역'],
            '신정네거리역': ['까치산역'],
            '합정역': ['홍대입구역'],
            '까치산역': [],
            '홍대입구역': ['신촌역'],
            '신촌역': ['이대역'],
            '이대역': ['아현역'],
            '아현역': ['충정로역'],
            '충정로역': ['시청역'],
            '시청역': ['을지로입구역'],
            '을지로입구역': ['을지로3가역'],
            '을지로3가역': ['을지로4가역'],
            '을지로4가역': ['동대문역사문화공원역'],
            '동대문역사문화공원역': ['신당역'],
            '신당역': ['상왕십리역'],
            '상왕십리역': ['왕십리역'],
            '왕십리역': ['한양대역'],
            '한양대역': ['뚝섬역'],
            '뚝섬역': ['성수역']},
            {'대화역': ['주엽역'],
            '주엽역': ['정발산역'],
            '정발산역': ['마두역'],
            '마두역': ['백석역'],
            '백석역': ['대곡역'],
            '대곡역': ['화정역'],
            '화정역': ['원당역'],
            '원당역': ['원흥역'],
            '원흥역': ['삼송역'],
            '삼송역': ['지축역'],
            '지축역': ['구파발역'],
            '구파발역': ['연신내역'],
            '연신내역': ['불광역'],
            '불광역': ['녹번역'],
            '녹번역': ['홍제역'],
            '홍제역': ['무악재역'],
            '무악재역': ['독립문역'],
            '독립문역': ['경복궁역'],
            '경복궁역': ['안국역'],
            '안국역': ['종로3가역'],
            '종로3가역': ['을지로3가역'],
            '을지로3가역': ['충무로역'],
            '충무로역': ['동대입구역'],
            '동대입구역': ['약수역'],
            '약수역': ['금호역'],
            '금호역': ['옥수역'],
            '옥수역': ['압구정역'],
            '압구정역': ['신사역'],
            '신사역': ['잠원역'],
            '잠원역': ['고속터미널역'],
            '고속터미널역': ['교대역'],
            '교대역': ['남부터미널역'],
            '남부터미널역': ['양재역'],
            '양재역': ['매봉역'],
            '매봉역': ['도곡역'],
            '도곡역': ['대치역'],
            '대치역': ['학여울역'],
            '학여울역': ['대청역'],
            '대청역': ['일원역'],
            '일원역': ['수서역'],
            '수서역': ['가락시장역'],
            '가락시장역': ['경찰병원역'],
            '경찰병원역': ['오금역'],
            '오금역': []},
            {'진접역': ['오남역'],
            '오남역': ['별내별가람역'],
            '별내별가람역': ['당고개역'],
            '당고개역': ['상계역'],
            '상계역': ['노원역'],
            '노원역': ['창동역'],
            '창동역': ['쌍문역'],
            '쌍문역': ['수유역'],
            '수유역': ['미아역'],
            '미아역': ['미아사거리역'],
            '미아사거리역': ['길음역'],
            '길음역': ['성신여대입구역'],
            '성신여대입구역': ['한성대입구역'],
            '한성대입구역': ['혜화역'],
            '혜화역': ['동대문역'],
            '동대문역': ['동대문역사문화공원역'],
            '동대문역사문화공원역': ['충무로역'],
            '충무로역': ['명동역'],
            '명동역': ['회현역'],
            '회현역': ['서울역역'],
            '서울역역': ['숙대입구역'],
            '숙대입구역': ['삼각지역'],
            '삼각지역': ['신용산역'],
            '신용산역': ['이촌역'],
            '이촌역': ['동작역'],
            '동작역': ['총신대입구 (이수)역'],
            '총신대입구 (이수)역': ['사당역'],
            '사당역': ['남태령역'],
            '남태령역': ['선바위역'],
            '선바위역': ['경마공원역'],
            '경마공원역': ['대공원역'],
            '대공원역': ['과천역'],
            '과천역': ['정부과천청사역'],
            '정부과천청사역': ['인덕원역'],
            '인덕원역': ['평촌역'],
            '평촌역': ['범계역'],
            '범계역': ['금정역'],
            '금정역': ['산본역'],
            '산본역': ['수리산역'],
            '수리산역': ['대야미역'],
            '대야미역': ['반월역'],
            '반월역': ['상록수역'],
            '상록수역': ['한대앞역'],
            '한대앞역': ['중앙역'],
            '중앙역': ['고잔역'],
            '고잔역': ['초지역'],
            '초지역': ['안산역'],
            '안산역': ['신길온천역'],
            '신길온천역': ['정왕역'],
            '정왕역': ['오이도역'],
            '오이도역': []},
            {'방화역': ['개화산역'],
            '개화산역': ['김포공항역'],
            '김포공항역': ['송정역'],
            '송정역': ['마곡역'],
            '마곡역': ['발산역'],
            '발산역': ['우장산역'],
            '우장산역': ['화곡역'],
            '화곡역': ['까치산역'],
            '까치산역': ['신정역'],
            '신정역': ['목동역'],
            '목동역': ['오목교역'],
            '오목교역': ['양평역'],
            '양평역': ['영등포구청역'],
            '영등포구청역': ['영등포시장역'],
            '영등포시장역': ['신길역'],
            '신길역': ['여의도역'],
            '여의도역': ['여의나루역'],
            '여의나루역': ['마포역'],
            '마포역': ['공덕역'],
            '공덕역': ['애오개역'],
            '애오개역': ['충정로역'],
            '충정로역': ['서대문역'],
            '서대문역': ['광화문역'],
            '광화문역': ['종로3가역'],
            '종로3가역': ['을지로4가역'],
            '을지로4가역': ['동대문역사문화공원역'],
            '동대문역사문화공원역': ['청구역'],
            '청구역': ['신금호역'],
            '신금호역': ['행당역'],
            '행당역': ['왕십리역'],
            '왕십리역': ['마장역'],
            '마장역': ['답십리역'],
            '답십리역': ['장한평역'],
            '장한평역': ['군자역'],
            '군자역': ['아차산역'],
            '아차산역': ['광나루역'],
            '광나루역': ['천호역'],
            '천호역': ['강동역'],
            '강동역': ['길동역', '둔촌동역'],
            '길동역': ['굽은다리역'],
            '둔촌동역': ['올림픽공원역'],
            '굽은다리역': ['명일역'],
            '올림픽공원역': ['방이역'],
            '명일역': ['고덕역'],
            '방이역': ['오금역'],
            '고덕역': ['상일동역'],
            '오금역': ['개롱역'],
            '상일동역': ['강일역'],
            '개롱역': ['거여역'],
            '강일역': ['미사역'],
            '거여역': ['마천역'],
            '미사역': ['하남풍산역'],
            '마천역': [],
            '하남풍산역': ['하남시청역'],
            '하남시청역': ['하남검단산역'],
            '하남검단산역': []},
            {'역촌역': ['불광역'],
            '불광역': ['독바위역'],
            '독바위역': ['연신내역'],
            '연신내역': ['구산역'],
            '구산역': ['응암역'],
            '응암역': ['새절역', '역촌역'],
            '새절역': ['증산역'],
            '증산역': ['디지털미디어시티역'],
            '디지털미디어시티역': ['월드컵경기장역'],
            '월드컵경기장역': ['마포구청역'],
            '마포구청역': ['망원역'],
            '망원역': ['합정역'],
            '합정역': ['상수역'],
            '상수역': ['광흥창역'],
            '광흥창역': ['대흥역'],
            '대흥역': ['공덕역'],
            '공덕역': ['효창공원앞역'],
            '효창공원앞역': ['삼각지역'],
            '삼각지역': ['녹사평역'],
            '녹사평역': ['이태원역'],
            '이태원역': ['한강진역'],
            '한강진역': ['버티고개역'],
            '버티고개역': ['약수역'],
            '약수역': ['청구역'],
            '청구역': ['신당역'],
            '신당역': ['동묘앞역'],
            '동묘앞역': ['창신역'],
            '창신역': ['보문역'],
            '보문역': ['안암역'],
            '안암역': ['고려대역'],
            '고려대역': ['월곡역'],
            '월곡역': ['상월곡역'],
            '상월곡역': ['돌곶이역'],
            '돌곶이역': ['석계역'],
            '석계역': ['태릉입구역'],
            '태릉입구역': ['화랑대역'],
            '화랑대역': ['봉화산역'],
            '봉화산역': ['신내역'],
            '신내역': []},
            {'장암역': ['도봉산역'],
            '도봉산역': ['수락산역'],
            '수락산역': ['마들역'],
            '마들역': ['노원역'],
            '노원역': ['중계역'],
            '중계역': ['하계역'],
            '하계역': ['공릉역'],
            '공릉역': ['태릉입구역'],
            '태릉입구역': ['먹골역'],
            '먹골역': ['중화역'],
            '중화역': ['상봉역'],
            '상봉역': ['면목역'],
            '면목역': ['사가정역'],
            '사가정역': ['용마산역'],
            '용마산역': ['중곡역'],
            '중곡역': ['군자역'],
            '군자역': ['어린이대공원역'],
            '어린이대공원역': ['건대입구역'],
            '건대입구역': ['자양역'],
            '자양역': ['청담역'],
            '청담역': ['강남구청역'],
            '강남구청역': ['학동역'],
            '학동역': ['논현역'],
            '논현역': ['반포역'],
            '반포역': ['고속터미널역'],
            '고속터미널역': ['내방역'],
            '내방역': ['이수역'],
            '이수역': ['남성역'],
            '남성역': ['숭실대입구역'],
            '숭실대입구역': ['상도역'],
            '상도역': ['장승배기역'],
            '장승배기역': ['신대방삼거리역'],
            '신대방삼거리역': ['보라매역'],
            '보라매역': ['신풍역'],
            '신풍역': ['대림역'],
            '대림역': ['남구로역'],
            '남구로역': ['가산디지털단지역'],
            '가산디지털단지역': ['철산역'],
            '철산역': ['광명사거리역'],
            '광명사거리역': ['천왕역'],
            '천왕역': ['온수역'],
            '온수역': ['까치울역'],
            '까치울역': ['부천종합운동장역'],
            '부천종합운동장역': ['춘의역'],
            '춘의역': ['신중동역'],
            '신중동역': ['부천시청역'],
            '부천시청역': ['상동역'],
            '상동역': ['삼산체육관역'],
            '삼산체육관역': ['굴포천역'],
            '굴포천역': ['부평구청역'],
            '부평구청역': ['산곡역'],
            '산곡역': ['석남역'],
            '석남역': []},
            {'별내역': ['다산역'],
            '다산역': ['동구릉역'],
            '동구릉역': ['구리역'],
            '구리역': ['장자호수공원역'],
            '장자호수공원역': ['암사역사공원역'],
            '암사역사공원역': ['암사역'],
            '암사역': ['천호역'],
            '천호역': ['강동구청역'],
            '강동구청역': ['몽촌토성역'],
            '몽촌토성역': ['잠실역'],
            '잠실역': ['석촌역'],
            '석촌역': ['송파역'],
            '송파역': ['가락시장역'],
            '가락시장역': ['문정역'],
            '문정역': ['장지역'],
            '장지역': ['복정역'],
            '복정역': ['남위례역'],
            '남위례역': ['산성역'],
            '산성역': ['남한산성입구역'],
            '남한산성입구역': ['단대오거리역'],
            '단대오거리역': ['신흥역'],
            '신흥역': ['수진역'],
            '수진역': ['모란역'],
            '모란역': []}]
        self.api_key = api_key
        self.start_station = ['연천역', '신설동역', '대화역', '진접역', '방화역', '역촌역', '장암역', '별내역']
                
    def get_map(self, n) :
        """
        n -> n 호선 지도를 출력합니다.
        """
        if n < 1 or n > 8 :
            raise ValueError("1~8호선만 가능합니다.")
        
        points = dict()
        for station in self.edges[n-1].keys() :
            points[station] = self.__get_lat_lon(station)
            
        map = folium.Map(location = self.__get_middle(points), zoom_start = 10)
        visited = set()
        
        q = deque([self.start_station[n-1]])

        while q :
            cur_station = q.popleft()
            if cur_station in visited :
                continue
            
            folium.Marker(points[cur_station], popup=cur_station).add_to(map)
            visited.add(cur_station)
            
            for nxt_station in self.edges[n-1][cur_station] :
                q.append(nxt_station)
                folium.PolyLine([points[cur_station], points[nxt_station]], color="blue", weight=2.5, opacity=1).add_to(map)
                
        return map
        
    
    def __get_middle(self, points) :
        sum_a = 0
        sum_b = 0
        for a,b in points.values() :
            sum_a += a
            sum_b += b
            
        return sum_a/len(points), sum_b/len(points)
    
    def __get_lat_lon(self, addr) :
        stations = SubwayStationLatLng.objects.filter(name=addr)
    
        if stations.exists():  # 존재 여부 확인
            # 첫 번째 지하철역의 위도와 경도를 반환
            return stations.first().latitude, stations.first().longitude
        else : 
            headers = {"Authorization": f'KakaoAK {self.api_key}'} #REST API 키(유효한 키)
            url = f'https://dapi.kakao.com/v2/local/search/keyword.json?query={addr}'
            result = requests.get(url, headers = headers).json()
            
            lat = float(result['documents'][0]['y'])
            lon = float(result['documents'][0]['x'])
            
            return lat, lon
        
        