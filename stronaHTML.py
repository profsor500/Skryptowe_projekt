import sys as s
import os
def HTML_table_creator(file_1, file_2):
    
    table="<table class='table-fill'><tr><td class='text-left'>Zaszyfrowany tekst</td><td class='text-left'>odszyfrowany tekst</td></tr>\n"
    for l, k in zip(file_1, file_2):
        table = table+"<tr><td class='text-left'>",l,"</td><td class='text-left'>",k,"</td></tr>\n"
    table=table+"</table>"
    return table
    
def HTML_table(data_file1, data_file2,w_file):
    f_szyfr = open(data_file1,"r")
    f_deszyfr = open(data_file2,"r")
    open(w_file,"w").close()
    f_zapis = open(w_file,"w")
    f_zapis.write("<title>Wyniki</title>")
    f_zapis.write("<div class='table-title'>")
    f_zapis.write("<h3>Wyniki szyfrowania i deszyfrowania</h3>")
    f_zapis.write("</div>")
    f_zapis.write("<meta name='viewport' content='initial-scale=1.0; maximum-scale=1.0; width=device-width;'>\n")
    f_zapis.write("<link rel='stylesheet' type='text/css' href='style.css'>\n")
    f_zapis.write("<table class='table-fill'><tr><th class='text-left'>Zaszyfrowany tekst</th><th class='text-left'>Odszyfrowany tekst</th></tr>\n")
    for l, k in zip(f_szyfr, f_deszyfr):
        f_zapis.write("<tr><td class='text-left'>"+l+"</td><td class='text-left'>"+k+"</td></tr>\n")
    f_zapis.write("</table>")
    f_zapis.close()
    f_szyfr.close()
    f_deszyfr.close()
    
HTML_table(s.argv[1],s.argv[2],os.path.splitext(s.argv[3])[0]+'.html')
