@echo off
@chcp 1250
attr 0F
:menu
cls
echo ------------------------
echo 	MENU
echo ------------------------
echo.
echo 1) start programu
echo  1.1) tylko szyfruj
echo  1.2) tylko deszyfruj
echo  1.3) tylko tworz strone
echo 2) otworz strone.html z wynikiem
echo 3) informacje 
echo 4) backup danych
echo 5) wyjdź 
echo.
set /p opcja=wybierz i wpisz odpowiedni nr, np: 1 lub 1.2:
if %opcja%==1 goto start
if %opcja%==1.1 goto szyfrowanie
if %opcja%==1.2 goto deszyfrowanie
if %opcja%==1.3 goto strona
if %opcja%==2 goto wyniki
if %opcja%==3 goto info
if %opcja%==4 goto backup
if %opcja%==5 exit
goto error

:start
cls 
python szyfrowanie.exe
echo zaszyfrowano dane z Input/Tekst.txt do Output/Szyfr.txt
python deszyfrowanie.exe
echo zdeszyfrowano dane z Output/Szyfr.txt do Output/Deszyfrowane.txt
python stronaHTML.exe
echo utworzono strone HTML z wynikami powyzszych polecen (stronaHTML/index.html)
pause >null
goto backup

:szyfrowanie
python szyfrowanie.exe
echo zaszyfrowano dane z Input/Tekst.txt do Output/Szyfr.txt
pause >null
goto backup

:deszyfrowanie
python deszyfrowanie.exe
echo zdeszyfrowano dane z Output/Szyfr.txt do Output/Deszyfrowane.txt
pause >null
goto backup

:strona
python stronaHTML.exe
echo utworzono strone HTML z wynikami powyzszych polecen (stronaHTML/index.html)
pause >null
goto backup

:wyniki
start stronaHTML/index.html
goto menu
:info
cls
type info.txt
pause >null
goto menu

:backup
cls
if not exist backup md backup
set datestr=%date:~-4,4%.%date:~-7,2%.%date:~-10,2%_%time:~0,2%.%time:~3,2%.%time:~6,2%
md backup/%datestr%
robocopy ..\projekt_sem .\backup/%datestr% /S /XD backup
cls
echo stworzono kopie plikow w folderze backup/%datestr%
pause >nul
goto menu

:error
echo wpisano nieprawidłowe dane, wybierz sposrod: {1, 1.1, 1.2, 1.3, 2, 3 ,4}
pause >null
goto menu