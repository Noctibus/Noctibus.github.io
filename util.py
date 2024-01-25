from pprint import pprint


def cut_text(text:str):
    result = {}
    run = True
    i = 1
    i_begin = 0
    i_end = 0
    while run:
        text_begin = "%s. " % i
        text_end = "%s. " % (i+1)
        i_begin = text.find(text_begin)
        i_end = text.find(text_end)
        t = text[i_begin+3:i_end]
        result["Claim %s " % i] = {t}
        i += 1
        if i_end == -1:
            run = False
    return result




# def assemble(text)





if __name__ == "__main__":
    with open("test.txt", "r") as f:
        text = f.read()
    # text = "1. hello world. 2. hello. 3. world."
    result = cut_text(text)
    # for t in result:
    #     print(result[t])
    pprint(result)