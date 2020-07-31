import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from .environment_variables import set_environment_variables


def scrape():
    set_environment_variables()
    source = requests.get(
        'https://www.palabrasaleatorias.com/?fs=10&fs2=0&Submit=Nueva+palabra'
    ).content

    soup = BeautifulSoup(source, 'html5lib')

    main_container = soup.find('td')
    divs_with_words = main_container.find_all('div')

    current_date = datetime.now().strftime('%Y%m%d_%H_%M_%S')
    output_file = os.environ.get('OUTPUT_FILE_ROUTE').format(
        current_date=current_date
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        for i, word in enumerate(divs_with_words):
            if i >= 10:
                break
            word_cleaned = word.text.strip().replace('\n', '')
            word = f'{i + 1}) {word_cleaned}\n'
            f.write(str(word))

    return output_file
