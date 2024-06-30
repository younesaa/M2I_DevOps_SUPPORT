#!/bin/bash 
read -p "donner votre nom" nom
read -p "donner votre age" age
voter() {
 if [ $age -ge 18 ];then
         echo $nom a le droit au vote
 else
        echo $nom vous etes mineur
 fi
}
voter $nom $age
