from pprint import pprint


def cut_text(text:str):
    result = []
    run = True
    i = 1
    i_begin = 0
    i_end = 0
    while run:
        text_begin = "%s. " % i
        text_end = "%s. " % (i+1)
        i_begin = text.find(text_begin)
        i_end = text.find(text_end)
        result.append(text[i_begin+3:i_end])
        i += 1
        if i_end == -1:
            run = False
    return result




# def assemble(text)