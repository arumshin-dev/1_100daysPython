import requests
from bs4 import BeautifulSoup

# berlinstartupjobs.com 웹사이트용 스크래퍼를 만듭니다.
# 스크래퍼는 다음 URL을 스크랩할 수 있어야 합니다:
# https://berlinstartupjobs.com/engineering/
site = 'https://berlinstartupjobs.com/engineering/'
# https://berlinstartupjobs.com/skill-areas/python/
# https://berlinstartupjobs.com/skill-areas/typescript/
# https://berlinstartupjobs.com/skill-areas/javascript/
# 첫 번째 URL에는 페이지가 있으므로 pagination 을 처리해야 합니다.
# 나머지 URL은 특정 스킬에 대한 것입니다. URL의 구조에 스킬 이름이 있으므로 모든 스킬을 스크래핑할 수 있는 스크래퍼를 만드세요.
# 회사 이름, 직무 제목, 설명 및 직무 링크를 추출하세요.
r = requests.get(site, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})

print(r.status_code)#접근 가능200 확인

all_jobs = []#리스트 생성

#페이징 페이지가 있으므로 스크랩 기능을 함수로 만들어서 사용
def scrape_page(url, arr):

  #response = requests.get(url)#페이지 요청
  response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})

  #print(response.content)#해당 페이지 html 찍음

  soup = BeautifulSoup(response.content, 'html.parser')#html 파싱
  jobs = soup.find("ul", class_="jobs-list-items").find_all("li")[0:]

  for job in jobs:
    #회사이름
    company = job.find("a", class_="bjs-jlid__b").text
    #직무제목
    title = job.find("h4", class_="bjs-jlid__h").find("a").text
    #설명 bjs-jlid__description div
    desc = job.find("div", class_="bjs-jlid__description").text 
    #직무링크 bjs-jlid__h 안에 a태그 href 속성
    url = job.find("h4", class_="bjs-jlid__h").find("a")["href"]#링크

    job_data = {
      'title': title,
      'company': company,
      'desc': desc,
      'url': url
    }
    #all_jobs.append(job_data)#리스트에 저장
    arr.append(job_data)#리스트에 저장

#페이징 개수를 가져오는 함수
def get_pages(url):
  #response = requests.get(url)#페이지 요청
  response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"})
  soup = BeautifulSoup(response.content, "html.parser",)#html 파싱
  return len(soup.find("ul", class_= "bsj-nav").find_all("a"))#페이지 개수를 리턴

total_pages = get_pages(site)#페이지 개수를 가져오는 함수를 호출
print(f"🎈{site}:{total_pages}")
#페이지 개수를 가져와 스크랩 함수에 개수를 넣어 반복 호출
for x in range(total_pages):
  url = f"{site}page/{x+1}"#페이지를 가져오는 url
  print("💧", url)
  scrape_page(url,all_jobs)#페이지를 스크랩하는 함수를 호출


print("total",len(all_jobs))#모든 정보를 가져왔으므로 개수를 출력
print(all_jobs)
print("😃페이지 스크랩 끝😃")