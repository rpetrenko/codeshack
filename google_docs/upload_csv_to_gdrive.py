import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import click

"""
https://medium.com/craftsmenltd/from-csv-to-google-sheet-using-python-ef097cb014f9
"""
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]


@click.command()
@click.option('--secret_json', default="~/.secrets/client_secret.json")
@click.argument('spreadhsheet_name')
@click.argument('csv_file')
def upload_csv(secret_json, spreadhsheet_name, csv_file):
    print(f"{secret_json}, {spreadhsheet_name}, {csv_file}")
    client_secret_file = os.path.expanduser(secret_json)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(client_secret_file, scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadhsheet_name)

    data_file = os.path.expanduser(csv_file)
    with open(data_file, 'r') as file_obj:
        content = file_obj.read()
        client.import_csv(spreadsheet.id, data=content)


if __name__ == "__main__":
    upload_csv()
