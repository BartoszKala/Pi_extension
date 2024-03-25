@echo off
chcp 1250 > nul
setlocal enabledelayedexpansion

echo Kolorowe Pi- Bartosz Kala
:menu
echo.
echo        Menu
echo 1. Uruchom Program
echo 2. Opis programu
echo 3. Kopia wejscia, wyniku i raportu
echo 4. Zakoncz
echo.

set /p choice=Dokonaj wyboru: (1 - 4): 

if !choice! equ 1 goto opcja1
if !choice! equ 2 goto opcja2
if !choice! equ 3 goto opcja3
if !choice! equ 4 goto exit
echo wybiez numer 1-4
echo.
goto menu

:opcja1
cls
IF EXIST raport.html DEL raport.html
echo ^<HTML^> >> raport.html
IF EXIST wyniki DEL /Q wyniki

call python Kolorowe_Pi.py
call python Raport.py
goto menu

:opcja2
cls
echo Program   ma  za  zadanie  wygenerowac  tablice   n   x  n,
echo gdzie n to  liczba  naturalna,  skladajaca sie  z kolejnych
echo rozszerzen dziesietnych liczbi pi.  Dodatkowo ma obliczac i
echo wyswietlac sumy "przekatnych" tej tablicy.
goto menu

:opcja3
cls
IF NOT EXIST kopia mkdir kopia

:: Użyj zmiennej "name" do uzyskania unikalnej nazwy katalogu
set "name=!date:/=-!-!TIME:~0,2!-!TIME:~3,2!-!TIME:~6,2!"

IF EXIST raport.html mkdir kopia\!name!
C:\Windows\System32\Robocopy.exe wejscie kopia\!name!\wejscie
C:\Windows\System32\Robocopy.exe wyniki kopia\!name!\wyniki
copy raport.html kopia\!name!\raport.html

goto menu


:exit
