FROM debian:buster-slim
MAINTAINER Eric Régnier <utopman@gmail.com>

WORKDIR /app
RUN apt update && apt install -y wget gdebi python3 python3-pip
RUN wget -O /tmp/wkhtmltopdf.deb https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb
RUN apt install -y libfontenc1 xfonts-75dpi xfonts-base xfonts-encodings xfonts-utils
RUN dpkg -i /tmp/wkhtmltopdf.deb

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache-dir -r /tmp/requirements.txt


COPY . .

ENTRYPOINT [ "/app/entrypoint" ]