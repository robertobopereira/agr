#!/bin/sh
echo "Iniciando servicos"
#/usr/sbin/apachectl start
service smbd start
service nmbd start

echo "Adicionando usuario"
#adduser aluno
#passwd -d aluno
#smbpasswd -a aluno -s 123456

# Pegando o IP e mostrando
IP=$(hostname -I)
echo "Seu ip : $IP"
tail -f /var/log/samba/log.nmbd

