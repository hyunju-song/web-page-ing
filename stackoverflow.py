import requests
from bs4 import BeautifulSoup

#1. get the page
URL = f"https://stackoverflow.com/jobs?q=python&sort=i"
#2. make the requests
#3. extract the info


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    #가장 마지막 페이지는 next이고 실제로 그 앞의 가장 마지막 페이지 숫자를 받기 위해서 -2 인덱스입
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)


def extract_job(html):
    title = html.find("h2", {"class":"fs-body3"}).string
    company = html.find("h3", {"class": "fc-black-700"}).find("span")
    location = html.find("h3", {"class": "fc-black-700"}).find("span", {"class": "fc-black-500"}).string
    job_id = html['data-jobid']
    return ({
        'title': title,
        'company': company,
        'location': location,
        'apply_link': f"https://stackoverflow.com/jobs/{job_id}"
    })


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs




def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return []