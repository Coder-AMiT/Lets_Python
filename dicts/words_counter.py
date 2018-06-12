para = """I'm tired of being what you want me to be
Feeling so faithless, lost under the surface
I don't know what you're expecting of me
Put under the pressure of walking in your shoes
Caught in the undertow, just caught in the undertow
Every step that I take is another mistake to you
Caught in the undertow, just caught in the undertow""".replace(',',' ').replace('\n',' ')


counter_dict = dict()

for word in para.split():
    if word in counter_dict:
        counter_dict[word] += 1
    else:
        counter_dict[word] = 1


for word, count in counter_dict.items():
    print(word, ':',count)