# Use a base image do BIND9
FROM ubuntu

# Instale o BIND9
RUN apt-get update && \
    apt-get install -y bind9 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copie os arquivos de configuração
COPY named.conf /etc/bind/named.conf
#COPY db.roberto.ic.ufmt.br /etc/bind/zones/db.roberto.ic.ufmt.br

# Abra a porta 53/udp para consultas DNS
EXPOSE 53/udp
EXPOSE 53/TCP

# Comando para iniciar o BIND9
CMD ["/usr/sbin/named", "-g"]
