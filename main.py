import datetime
import os

from googleapiclient import discovery
from google.oauth2 import service_account

from main_docs import *
from site_parser import *

def getOldArray(spreadsheet_id="1rRovBbunOEocsxxvFCy6crunAmH63pnHxhvAId_EsXo"):
    try:
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
        ]
        secret_file = os.path.join(os.getcwd(), "annelo-uschqd-a99efe061391.json")

        # spreadsheet_id = "1rRovBbunOEocsxxvFCy6crunAmH63pnHxhvAId_EsXo"
        range_name = 'AA6:AA65'

        credentials = service_account.Credentials.from_service_account_file(
            secret_file, scopes=scopes
        )

        service = discovery.build("sheets", "v4", credentials=credentials)


        values=service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name,
        ).execute()


        

        return values.get('values')

    except OSError as e:
        print(e)
        return None
    
def getAllOldLessons(id="1rRovBbunOEocsxxvFCy6crunAmH63pnHxhvAId_EsXo"):
    oldLessons = getOldArray(id)

    # print(oldLessons)

    FAllOldLessons = ""

    for lesson in oldLessons:
        if len(lesson) == 0:
            FAllOldLessons += '\n'
        else:
            # print(lesson)
            FAllOldLessons += lesson[0] + '\n'
    # print(FAllOldLessons)
    return FAllOldLessons

def NewLessons():

    id_0, id_1 = get_id()

    GAOL = getAllOldLessons(id_1).split('\n\n\n\n\n')
    print(GAOL)

    IOfWeek = datetime.datetime.today().isoweekday() - 1

    if datetime.datetime.today().hour > 15:
        IOfWeek += 1

    if IOfWeek > 4:
        IOfWeek = 0
    


    GAOL = GAOL[IOfWeek].split('\n')

    # print(GAOL)

    NewLesson = getNewLessons(id_0)

    # print(NewLesson)
    
    NEW_GAOL = ""

    lesson_number = 1

    for i in range(len(GAOL)):
        # lesson_number = i
        if GAOL[i] == "" or GAOL[i] == "\n":
            lesson_number -= 1
            continue
        elif i in NewLesson:
            NEW_GAOL += f"{lesson_number}ур. " + NewLesson[i] + " (Замена)\n"
        else:
            NEW_GAOL += f"{lesson_number}ур. " + GAOL[i] + "\n"
        lesson_number += 1
    
    return NEW_GAOL 

if __name__ == "__main__":
    print(NewLessons())


