#!/bin/sh
echo "Iniciando servicos"
#/usr/sbin/apachectl start
service smbd start
service nmbd start


echo "Script senhas"
while IFS=',' read -r a b; do
 useradd -m "$a"
 (echo "$b"; echo "$b") | smbpasswd -s -a "$a"
done < dados.csv

echo "Ajustando permissao dos diretórios"
chmod 777 /dados -R

# Pegando o IP e mostrando
IP=$(hostname -I)
echo "Seu ip : $IP"
tail -f /var/log/samba/log.nmbd

