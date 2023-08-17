NONBREAKSPACE = u'\xa0'
NONBREAKTAB1 = u'\u300013'
NONBREAKTAB2 = u'\u3000IO'
NONBREAKTAB3 = u'\u3000DX'
NONBREAKTAB4 = u'\u3000'
NONBREAKTAB5 = u'\u3000Em'
NONSHARP = u'#'
NEWLINE = u'\n'


def convert_text(text):
    if(NONBREAKSPACE in text):
        text = text.replace(NONBREAKSPACE, ' ')

    if(NONBREAKTAB1 in text):
        text = text.replace(NONBREAKTAB1, '     ')

    if(NONBREAKTAB2 in text):
        text = text.replace(NONBREAKTAB2, '     ')
    
    if(NONBREAKTAB3 in text):
        text = text.replace(NONBREAKTAB2, '     ')
    
    if(NONBREAKTAB4 in text):
        text = text.replace(NONBREAKTAB2, '     ')
    
    if(NONBREAKTAB5 in text):
        text = text.replace(NONBREAKTAB2, '     ')

    if(NONSHARP in text):
        text = text.replace(NONSHARP, '')

    if(NEWLINE in text):
        text = text.replace(NEWLINE, '')

    text = text.strip()
    return text
