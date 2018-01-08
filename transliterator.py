d = dict()
d["a"] = 'अ'
d["b"] = 'ब'
d["c"] = 'क'
d["d"] = 'द'
d["e"] = 'ए'
d["f"] = 'फ'
d["g"] = 'ग'
d["h"] = 'ह'
d["i"] = 'इ'
d["j"] = 'ज'
d["k"] = 'क'
d["l"] = 'ल'
d["m"] = 'म'
d["n"] = 'न'
d["o"] = 'ओ'
d["p"] = 'प'
d["q"] = 'क'
d["r"] = 'र'
d["s"] = 'स'
d["t"] = 'त'
d["u"] = 'उ'
d["v"] = 'भ'
d["w"] = 'व'
d["x"] = 'क्ष'
d["y"] = 'य'
d["z"] = 'ज'

d['ka'] = 'क'
d['kha'] = 'ख'
d['ga'] = 'ग'
d['gha'] = 'घ'
d['nga'] = 'ङ'
d['ch'] = 'च'
d['cha'] = 'छ'
d['ja'] = 'ज'
d['jha'] = 'झ'
d['Yna'] = 'ञ'
d['Ta'] = 'ट'
d['Tha'] = 'ठ'
d['Da'] = 'ड'
d['da'] = 'द'
d['Na'] = 'ण'
d['ta'] = 'त'
d['tha'] = 'थ'
d['Dha'] = 'ढ'
d['dha'] = 'घ'
d['na'] = 'न'
d['pa'] = 'प'
d['fa'] = 'फ'
d['ba'] = 'ब'
d['bha'] = 'भ'
d['ma'] = 'म'
d['ya'] = 'य'
d['ra'] = 'र'
d['la'] = 'ल'
d['wa'] = 'व'
d['sha'] = 'श'
d['Sha'] = 'ष'
d['sa'] = 'स'
d['ha'] = 'ह'
d['ksh'] = 'क्ष'
d['tra'] = 'त'
d['gya'] = 'ज्ञ'
d['gy'] = 'ज्ञ'
d['tr'] = 'त'


def tokenize(word):
    word += " "
    temp = ""
    i = 0
    while i < len(word):
        temp2 = temp
        temp += word[i]
        if temp is " ":
            break
        if temp not in d:
            print("{0} {1}".format(i, temp2))
            temp = ""
            i -= 1
        i += 1


tokenize("shirish")
