import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import re

class MitreContentScraper:

    def __init__(self,url):

        self.url=url

        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        self.soup=None

    def fetch_page(self):

        response=requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        self.soup=BeautifulSoup(
            response.text,
            "html.parser"
        )

    def clean_text(self,text):

        if not text:
            return ""

        text=re.sub(r"\s+"," ",text)

        return text.strip()

    def get_title(self):

        title=self.soup.select_one(
            "div.container-fluid h1"
        )

        if title:
            return self.clean_text(
                title.get_text()
            )

        return "Unknown Technique"

    def get_technique_id(self):

        ttp=self.soup.select_one(
            "#card-id .pl-0"
        )

        if not ttp:
            return "UNKNOWN"

        text=self.clean_text(
            ttp.get_text()
        )

        if ":" in text:
            return text.split(":")[1].strip()

        return text

    def get_filename(self):

        filename=f"{self.get_technique_id()} - {self.get_title()}"

        filename=re.sub(
            r'[\\/*?:"<>|]',
            "-",
            filename
        )

        return filename+".md"

    def get_description(self):

        paragraphs=self.soup.select(
            "div.description-body p"
        )

        description=[]

        for p in paragraphs:

            text=self.clean_text(
                p.get_text(" ",strip=True)
            )

            if text:
                description.append(text)

        return "\n\n".join(description)

    def parse_table(self,section_id,section_title):

        heading=self.soup.find(
            "h2",
            id=section_id
        )

        if not heading:
            return ""

        wrapper=heading.find_next(
            "div",
            class_="tables-mobile"
        )

        if not wrapper:
            return ""

        table=wrapper.find("table")

        if not table:
            return ""

        markdown=f"## {section_title}\n\n"

        headers=[]

        for th in table.select("thead th"):

            headers.append(
                self.clean_text(
                    th.get_text()
                )
            )

        if headers:

            markdown+="| "+" | ".join(headers)+" |\n"
            markdown+="|"+"---|"*len(headers)+"\n"

        for tr in table.select("tbody tr"):

            row=[]

            for td in tr.find_all(["td","th"]):

                text=self.clean_text(
                    td.get_text(" ",strip=True)
                )

                row.append(text)

            if row:

                while len(row)<len(headers):
                    row.append("")

                markdown+="| "+" | ".join(row)+" |\n"

        markdown+="\n---\n\n"

        return markdown

    def get_references(self):

        refs=self.soup.select(
            "span.scite-citation-text a"
        )

        if not refs:
            return ""

        markdown="## References\n\n"

        for ref in refs:

            text=self.clean_text(
                ref.get_text()
            )

            href=ref.get("href","")

            if href:
                markdown+=f"- [{text}]({href})\n"

            else:
                markdown+=f"- {text}\n"

        markdown+="\n---\n"

        return markdown

    def build_markdown(self):

        markdown=f"# {self.get_title()}\n\n"

        description=self.get_description()

        if description:

            markdown+="## Description\n\n"
            markdown+=description
            markdown+="\n\n---\n\n"

        markdown+=self.parse_table(
            "examples",
            "Procedure Examples"
        )

        markdown+=self.parse_table(
            "mitigations",
            "Mitigations"
        )

        markdown+=self.parse_table(
            "detection",
            "Detection Strategy"
        )

        markdown+=self.get_references()

        return markdown

    def save_markdown(self):

        filename=self.get_filename()

        content=self.build_markdown()

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return filename

    def run(self):

        self.fetch_page()

        filename=self.save_markdown()

        return filename

# if __name__=="__main__":
#     url="https://attack.mitre.org/techniques/T1566/"
#     scraper=MitreScraper(url)
#     scraper.run()


## Scrape Single MITRE Technique
## 1) Remove Comments from above code using Ctrl K + Ctrl C. 
## 2) Remove or Comment Code After This Point using Ctrl K + Ctrl C to use this script for scraping a single MITRE Technique Data. 


class MitreLinkScraper:

    def __init__(self):

        self.url="https://attack.mitre.org/techniques/enterprise/"

        self.base_url="https://attack.mitre.org"

        self.headers={
            "User-Agent":"Mozilla/5.0"
        }

        self.links=[]

        self.soup=None

    def fetch_page(self):

        response=requests.get(
            self.url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        self.soup=BeautifulSoup(
            response.text,
            "html.parser"
        )

    def extract_links(self):

        for a in self.soup.select(
            ".table-techniques tbody tr a[href]"
        ):

            href=a["href"]

            if href.startswith("/techniques/"):

                full_url=self.base_url+href

                if full_url not in self.links:
                    self.links.append(full_url)

    def scrape_single(self,link):

        try:

            scraper=MitreContentScraper(link)

            filename=scraper.run()

            return f"[+] {filename}"

        except Exception as error:

            return f"[!] Failed: {link} -> {error}"

    def scrape_all(self):

        print(f"[+] Total Links Found: {len(self.links)}")

        max_threads=20

        with ThreadPoolExecutor(max_workers=max_threads) as executor:

            futures=[
                executor.submit(self.scrape_single,link)
                for link in self.links
            ]

            with tqdm(
                total=len(futures),
                desc="Scraping MITRE ATT&CK",
                unit="file"
            ) as progress_bar:

                for future in as_completed(futures):

                    result=future.result()

                    print(result)

                    progress_bar.update(1)

    def run(self):

        self.fetch_page()

        self.extract_links()

        self.scrape_all()


if __name__=="__main__":

    scraper=MitreLinkScraper()

    scraper.run()
