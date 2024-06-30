#!/bin/bash 
png=0
for line in `ls /usr/share/pixmaps/*.png`
 do
         if [ ! -L $line ]; then
              # png=$(($png+1))
             #si non   let png=$png+1
             #si non 
             ((png++))
     fi
 done
echo le nombre png est $png 
# echo -e "\n la facon la plus simple le cas de jpg"

 find /usr/share/pixmaps -maxdepth 2 -name "*.jpg" -type f  | wc -l
#echo proposistion younes 
# ls -l /usr/share/pixmaps | grep ^-.*.png$ | wc -l 
