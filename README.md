# Script para automatizar o download da CNDT
Foram utilizado para isso as bibliotecas:
- [splinter](https://github.com/cobrateam/splinter)
Para simular a navegação.
- [google-cloud-speech](https://cloud.google.com/speech/?hl=pt-br)
Para quebrar o captcha, atravez do audio.

## Instalação
É necessario ter [chrome](https://www.google.com.br/chrome/browser/desktop/index.html) e [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) instalados.

Também é necessario ter uma chave de acesso da api do google para isso entre no link https://cloud.google.com/speech/docs/getting-started?hl=pt-br
clique em "SET UP A PROJECT", siga as instruções e baixe a chave.

Depois digite no terminal:
```
export GOOGLE_APPLICATION_CREDENTIALS="caminho/da/chave"
```

Instale as dependências:
```
sudo apt install python3-pip
sudo pip install -r requeriments.txt
chmod +x cndt.py
sudo ln -rs cndt.py /usr/bin/cndt
```

## Utilização
```
cndt --cpf cpfaqui --path caminho/a/ser/salvo
cndt --cnpj cnpjaqui --path caminho/a/ser/salvo
```
