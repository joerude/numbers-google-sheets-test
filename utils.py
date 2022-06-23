def exchange_rate_usdrub_today():
    """
    Получение курса доллара в рублях
    по курсу ЦБ РФ на текущий день.
    https://www.cbr.ru/development/SXML/
    """
    import requests
    import xml.etree.ElementTree as ET
    from datetime import date

    today = date.today()
    day = today.day
    month = today.month
    year = today.year

    if int(day) < 10:
        day = '0%s' % day

    if int(month) < 10:
        month = '0%s' % month

    request_url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' \
                  f'{day}/{month}/{year}'

    # Выполняем запрос к API.
    usdrub_xml = requests.get(request_url)

    structure = ET.fromstring(usdrub_xml.content)

    dollar = structure.find("./*[@ID='R01235']/Value")
    dollar = dollar.text.replace(',', '.')
    usdrub = float(dollar.replace(',', ''))

    return usdrub


def gsheet2df(spreadsheet_name, sheet_num):
    import pandas as pd
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials as sac

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials_path = 'creds.json'

    credentials = sac.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(credentials)

    sheet = client.open(spreadsheet_name).get_worksheet(sheet_num).get_all_records()
    df = pd.DataFrame.from_dict(sheet)

    return df
