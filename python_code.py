import requests, re, csv
from bs4 import BeautifulSoup


f = open("./csv_file.csv", "w+", encoding="utf-8")
temp_csv_file = csv.writer(f)
temp_csv_file.writerow(["Title", "Area", "Date", "Link"])

# List of filter words
job_list = [
    "^it",
    "it$",
    "it",
    "^network",
    "network$",
    "network",
    "^computer",
    "computer$",
    "computer",
]

# Seraching job posting dash board from 1 to 10
for i in range(1, 10):
    url = "https://radiokorea.com/bulletin/bbs/board.php?bo_table=c_jobs&page={}".format(i)

    # Create headers in case website block the scraping
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    items = soup.find_all("a", attrs={"class": "thumb"})

    for item in items:
        job_title = item.find("div", attrs={"class": "subject"})
        area = item.find("div", attrs={"class": "area"})
        date = item.find("div", attrs={"class": "date"})

        if job_title == None:
            continue
        else:
            for filter in job_list:
                if re.compile(filter).search(job_title.get_text().lower()):
                    temp_csv_file.writerow(
                        [
                            job_title.get_text(),
                            area.get_text(),
                            date.get_text(),
                            "https://radiokorea.com/bulletin" + item["href"][2:],
                        ]
                    )

f.close()