def DecToAny(num, sys):
    mod=[]
    while num!=0:
        mod.append(int(num % sys))
        num=int((num-(num % sys))/sys
    mod.reverse()
    return("".join(str(x) for x in mod))

def szyfrowanie(str):
    tab=[]
    sys = 2
    for i in range(len(str)):
        tab.append(DecToAny(ord(str[i]), sys))
        sys = (ord(str[i]) % 8) + 2
    print(" ".join(tab))
    return(" ".join(tab))

def pelne_szyfrowanie(path_to_input, path_to_output):
    f_in = open(path_to_input,"r")
    open(path_to_output, 'w').close() #czyści plik przed zapisem, aby zapisać na czysto nowy tekst
    f_out = open(path_to_output,"a")
    for l in f_in:
        f_out.write(szyfrowanie(l.rstrip())+'\n')
    f_in.close()
    f_out.close()

pelne_szyfrowanie("Input/tekst.txt","Output/Szyfr.txt")