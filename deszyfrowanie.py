import sys as s

def deszyfrowanie(str):
    tab_str=str.split(" ")
    wynik=[]
    sys=2
    for i in range(len(tab_str)):
        suma=0
        dl=len(tab_str[i])
        for j in range(dl):
            suma+=int(tab_str[i][dl-1-j])*pow(sys,j)
        sys=(suma%8)+2
        wynik.append(chr(suma))
    return "".join(wynik)
    
def pelne_deszyfrowanie(path_to_input, path_to_output):
    f_in = open(path_to_input,"r")
    open(path_to_output, 'w').close()
    f_out = open(path_to_output,"a")
    for l in f_in:
        f_out.write(deszyfrowanie(l.rstrip())+'\n')
    f_in.close()
    f_out.close()
pelne_deszyfrowanie(s.argv[1],s.argv[2])
