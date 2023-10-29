# Usa un'immagine di base basata su una distribuzione Linux
FROM ubuntu:latest

# Aggiorna il sistema e installa Apache2
RUN apt-get update && apt-get install -y apache2 procps
COPY entrypoint.sh /entrypoint.sh

# Esponi la porta 80 per il traffico HTTP
EXPOSE 80

# Crea una directory "results"
RUN mkdir /results && chmod +x entrypoint.sh

# Definisci l'entrypoint per il contenitore
ENTRYPOINT ["/entrypoint.sh"]
