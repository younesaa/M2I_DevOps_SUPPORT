#!/bin/bash
echo -e "mon nom de connexion est $LOGNAME \n"
echo -e "nom du script est $0 \n"
echo -e "la date est"
date
echo -e "\n le calendrier est" `cal 04 2024`
echo -e "\n le nom de la machine $HOSTNAME"
echo  -e "\n le nom du système est" 
uname -a
echo -e "la liste des fichiers \n"
ls ..
echo -e "\n *************la liste des var env*************"
echo $TERM
echo $PATH 
echo $HOME
echo -e "\n au revoir et merci"
date +%T
