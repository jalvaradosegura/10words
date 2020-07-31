import os
from pathlib import Path

from utils.send_gmail import send_email
from utils.scraper import scrape
from utils.environment_variables import set_environment_variables

BASE_DIR = Path(__file__).parent.absolute()
ENVIRONMENT_FILE = os.path.join(BASE_DIR, '.env')

if __name__ == '__main__':
    set_environment_variables(
        os.path.join(BASE_DIR, '.env')
    )
    output_file = scrape()
    with open(output_file) as email_body:
        send_email(email_body.read())
