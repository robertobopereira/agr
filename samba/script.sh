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

lista=$(grep "path" /etc/samba/smb.conf)

echo "$lista" | while IFS= read -r linha; do
    valor=$(echo "$linha" | grep -oP 'path\s*=\s*\K[^[:space:]]+')
    if [ ! -d "$valor" ]; then
       echo "Criando diretório: $valor"
       mkdir -p $valor
    fi
done
chmod 777 /dados -R

# Pegando o IP e mostrando
IP=$(hostname -I)
echo "Seu ip : $IP"
tail -f /var/log/samba/log.nmbd

