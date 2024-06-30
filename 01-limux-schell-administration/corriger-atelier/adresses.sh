#!/bin/bash 
 #echo "les num de tel avec x ou X"
 #grep -i x[0-9][0-9][0-9][0-9]$  $1
 #echo "lignes commenecent par 3 chiffre suivies par -"
 #grep -E "^[0-9]{3}-" $1 
#echo ou bien 
#grep ^[0-9]'\{3\}'- $1 

#echo les lignes qui commencent par s
#grep ^S $1
cligne=1
cnom=3
cnum=4
while  read -r ligne;
do
        echo line $cligne est $ligne
        if [ $cligne -eq $cnom ]; then
                echo $ligne >> pers.txt
                cnom=$(($cnom+5))
        fi
        if [ $cligne -eq $cnum ]; then
        echo $ligne >> pers.txt
        cnum=$(($cnum+5))
         fi
cligne=$(($cligne+1))
done    < $1
