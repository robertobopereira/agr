# Use a imagem oficial do Ubuntu como base
FROM ubuntu:latest

# Configura o localtime
RUN ln -fs /usr/share/zoneinfo/America/Cuiaba /etc/localtime

# Instale o servidor NTP (NTPd) da ISC
RUN apt-get update && apt-get install -y ntp

# Exponha a porta UDP 123 utilizada pelo NTP
EXPOSE 123/udp

# Inicialize o servidor NTP quando o contêiner for iniciado
CMD ["ntpd", "-n", "-u", "ntp:ntp", "-p", "/var/run/ntpd.pid", "-g", "-4"]
