import time
def Schoenheit():
    name = input('Bitte Vornamen eingeben:').lower()
    if name == 'morten':
        print('Sie sind super schoen!')
    elif name == 'jorge':
        print('Sie sind ausgesprochen haesslich.')
    else:
        yn = input('Das weiss ich nicht. Wollen wir vielleicht Morten fragen? y/n').lower()
        if yn not in ['y', 'n']:
            print('Bitte nur mit y/n antworten.')
            time.sleep(4)
            print('Ahhh verdammt, jetzt habe ich den Namen wieder vergessen..')
            Schoenheit()
        else:
            if yn == 'n':
                print('Dann halt nochmal..')
                Schoenheit()
            else:
                print('Fragen wir Morten..')
                time.sleep(3)
                if name == 'marlene':
                    print('Dein Freund ist ausgesprochen haesslich.')
                else:
                    print('Du bist haesslich')