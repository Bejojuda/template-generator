import os
import pathlib

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def check_emails(email):
    """
    Access online Google Sheet to check company's employees emails. If the email is present, a True value is returned
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # add credentials to the account
    path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'google_credentials.json')
    creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)

    # authorize the clientsheet
    client = gspread.authorize(creds)

    sheet = client.open('Empleados')
    sheet_instance = sheet.get_worksheet(0)
    emails = [record['E-mail'] for record in sheet_instance.get_all_records()]
    if email in emails:
        return True
    else:
        return False