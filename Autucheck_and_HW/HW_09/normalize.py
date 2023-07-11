CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "y",
    "",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
)
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


replace_simb = "!@#$%&'№()*+,-/.:;<=>?-\\]^{|}\""


def normalize(name_object: str) -> str:
    trans_name = name_object.translate(TRANS)

    for symbol in trans_name:
        if symbol in replace_simb:
            replace_name = trans_name.replace(symbol, "_")
            trans_name = replace_name

    return trans_name


if __name__ == "__main__":
    normalize()
