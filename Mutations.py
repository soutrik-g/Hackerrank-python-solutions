def mutate_string(string, position, character):
    nlist = list(string)
    nlist[position] = character
    nstring = ''.join(nlist)
    return nstring
