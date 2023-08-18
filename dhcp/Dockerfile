FROM ubuntu:latest
RUN apt-get update && apt-get install -y isc-dhcp-server
RUN touch /var/lib/dhcp/dhcpd.leases
COPY dhcpd.conf /etc/dhcp/dhcpd.conf
CMD ["dhcpd","-f","-d","--no-pid"]
