# python_loops
Selle ülesandega õpime tsükleid.
Pythonis kasutatakse kaht tsüklit. For tsükkel (For loop) ja while tsükkel (while loop).

Enne ülesande lahendamist soovitan lugeda mõlema tsükli kohta Pydoci.
For tsükkel: https://ained.ttu.ee/pydoc/loop.html#for-tsukkel
While tsükkel: https://ained.ttu.ee/pydoc/loop.html#while

`def check_tea_temp(temp)`
Teed ei saa juua kui tee on liiga kuum (üle 90 kraadi), aga tee ei tohi olla ka liiga külm (alla 50 kraadi). 
Check_tea_temp kontrollib tee jahtumist ja annab teada kui tee on joomiseks piisavalt kuum. 

Sisend temp on ühe tassi tee temperatuur.

`def sort_drinkable_teas(teas, temp)`
Funktsioon tagastab listi nendest tassidest, kus temperatuur on väiksem või võrdne antud temperatuuriga.
Tasside sorteerimisel ei muuda funktsioon tassi temperatuuri (st. check_tea_temp funktsiooni sorteerimisel kasutama ei 
pea). 

Sisend teas on list tee temperatuuridest ja temp on nõutud tee temperatuur.
