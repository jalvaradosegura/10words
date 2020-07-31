from utils.send_gmail import send_email
from utils.scraper import scrape

if __name__ == '__main__':
    output_file = scrape()
    with open(output_file) as email_body:
        send_email(email_body.read())
