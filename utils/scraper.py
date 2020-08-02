import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class CustomScraper:

    def __init__(self, url):
        self.url_to_scrape = url

    @property
    def output_file(self):
        current_date = datetime.now().strftime('%Y%m%d_%H_%M_%S')
        return os.environ.get('OUTPUT_FILE_ROUTE').format(
            current_date=current_date
        )

    def get_website_content(self):
        source = requests.get(
            self.url_to_scrape
        ).content

        soup = BeautifulSoup(source, 'html5lib')

        main_container = soup.find('td')
        return main_container.find_all('div')

    def write_content_to_file(self, content):
        output_file = self.output_file
        with open(output_file, 'w', encoding='utf-8') as f:
            for i, word in enumerate(content):
                if i >= 10:
                    break
                word_cleaned = word.text.strip().replace('\n', '')
                word = f'{i + 1}) {word_cleaned}\n'
                f.write(str(word))
        return output_file

    def scrape(self):
        website_content = self.get_website_content()
        output_file = self.write_content_to_file(website_content)
        return output_file
