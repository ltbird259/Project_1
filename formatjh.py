def format(a = "-"):
    print(str(a) * 50)

def autoformat(string,a="-"):
    format(a)
    print(f'{string}')
    format(a)
# mana = "can't touch this"
# autoformat("Gotta get that boom, boom, BOOM!!","$")