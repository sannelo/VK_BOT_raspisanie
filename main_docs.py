import io
import re
import ssl
import urllib.request

DOCUMENT_ID = '1IbsUkef6m0U8qwMnYOIBdKpm34cc0qubyTDs2l6Rz0U'

def getFile(DOC_ID, format='txt'):
    url = f'https://docs.google.com/document/d/{DOC_ID}/export?format={format}'

    context = ssl._create_unverified_context()

    response = urllib.request.urlopen(url, context=context)


    with io.TextIOWrapper(response, encoding='utf-8') as f:
        text = f.read()
    
    return text

# Formating the text, removing tabs and empty line, and making it lowercase, remove all lines up to "1ур"
def getNewLessons(id="1IbsUkef6m0U8qwMnYOIBdKpm34cc0qubyTDs2l6Rz0U"):
    text = getFile(id)
    text = text.replace('\t', '')
    text = text.replace('\n\n', '')
    text = text.replace('+\n', '')
    text = text.lower()


    new_text = text[:text.find('1ур')]
    for line in new_text.split('\n'):
        line = line.replace(' ', '')

        if line.find('м-20') != -1:
            line = line.replace('м-20', '')
            
            line = line.replace('-', '')

            new_lessons = {}

            for less in range(10):
                new_lessons[less] = line
            
            return new_lessons

    text = text[text.find('1ур'):]
    text = re.split('([+-]?\d+)ур', text)

    # print(text)

            
    # For each in the text n increments of 1.
    # If the line is empty, skip it.
    # If the line is not empty, print the line.

    for i in text:
        if i is None:
            text.remove(i)
        elif len(i) == 0:
            text.remove(i)
        elif re.fullmatch('[+-]?\d+', i) is not None:
            text.remove(i)

    text.pop(0)
    text.pop(-1)

    # print(text)

    # for lesson in text:
    #     print(lesson, end='\n\n')

    party = "м-20"

    new_lessons = {}

    for l_num, lessons in enumerate(text):
        for i, lesson in enumerate(lessons.split('\n')):
            if party == lesson:
                nlesson = lessons.split('\n')[i+2]
                new_lessons[l_num] = nlesson
                continue
    return new_lessons
