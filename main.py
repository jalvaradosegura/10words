import os
from pathlib import Path

from utils.email_utils import EmailSender
from utils.scraper import CustomScraper
from utils.environment_variables import set_environment_variables

BASE_DIR = Path(__file__).parent.absolute()
ENVIRONMENT_FILE = os.path.join(BASE_DIR, '.env')

if __name__ == '__main__':

    set_environment_variables(
        os.path.join(BASE_DIR, '.env')
    )

    scraper = CustomScraper(os.environ.get('URL_TO_SCRAPE'))
    output_file = scraper.scrape()

    with open(output_file) as email_body:
        email_sender = EmailSender(
            user=os.environ.get('EMAIL_USER'),
            password=os.environ.get('EMAIL_PASSWORD')
        )
        email_sender.create_email(
            receivers=os.environ.get('EMAIL_RECEIVERS'),
            subject=os.environ.get('EMAIL_SUBJECT'),
            body=email_body.read(),
        )
        email_sender.send_email()
