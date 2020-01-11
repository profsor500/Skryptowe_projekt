import sys

def DecToAny(num,syst):
    mod=[]
    while num!=0:
        mod.append(num%syst)
        num=int((num-(num%syst))/syst)
    mod.reverse()
    return "".join(str(x) for x in mod)

def szyfrowanie(str):
    tab=[]
    syst=2
    for i in range(len(str)):
        tab.append(DecToAny(ord(str[i]),syst))
        syst=(ord(str[i])%8)+2
    return " ".join(tab)
def pelne_szyfrowanie(path_input, path_output):
    f_in=open(path_input,"r")
    f_out=open(path_output,"w")
    for l in f_in:
        f_out.write(szyfrowanie(l.rstrip())+'\n')
    f_in.close()
    f_out.close()
pelne_szyfrowanie(sys.argv[1],sys.argv[2])
