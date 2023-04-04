import gspread


def write():
    gc = gspread.service_account(filename="./rational-mote-381601-8fee208ca571.json")
    sh = gc.open("initial 앱 지표").worksheet("Form Responses 1")
    print(sh.get('A1'))
    sel = 'A3'

    sh.update_acell(sel, "python input")
    print(sh.get(sel))


if __name__ == '__main__':
    write()
