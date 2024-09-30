# Use a imagem oficial do Ubuntu como base
FROM ubuntu:latest

# Instale o servidor ssh
RUN apt-get update && apt-get install -y ssh

# Cria o diretorio base do ssh
RUN mkdir /var/run/sshd

# Adicionar o usuario aluno e senha 123456
RUN useradd -m -s /bin/bash aluno && echo 'aluno:123456' | chpasswd

# Exponha a porta TCP 22
EXPOSE 22

# Inicialize o servidor SSH quando o contêiner for iniciado
CMD ["/usr/sbin/sshd", "-D"]
