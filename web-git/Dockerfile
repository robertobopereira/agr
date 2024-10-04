FROM ubuntu:latest
RUN apt-get update && apt-get install -y apache2 git
RUN rm /var/www/html/index.html
RUN git clone https://github.com/robertobopereira/teste.git /var/www/html/
EXPOSE 80
CMD ["apachectl","-D","FOREGROUND"]
