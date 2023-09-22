FROM ubuntu:latest
LABEL version="0.1"
RUN ln -fs /usr/share/zoneinfo/America/Cuiaba /etc/localtime
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y samba
COPY script.sh /script.sh
RUN chmod +x /script.sh
ENTRYPOINT ["/script.sh"]
