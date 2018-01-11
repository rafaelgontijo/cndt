#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import argparse
from selenium import webdriver
from splinter import Browser
from utils import transcript_mp3


def download_cndt(cpf_cnpj, path):
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "profile.default_content_settings.popups": 0,
        'download.default_directory': path
    }
    chrome_options.add_experimental_option("prefs", prefs)
    with Browser('chrome', options=chrome_options, incognito=True) as browser:
        url = "http://aplicacao.jt.jus.br/cndtCertidao/inicio.faces"
        browser.visit(url)
        button = browser.find_by_value('Emitir Certidão')
        button.click()
        button = browser.find_by_id('idUrlServletSoundCaptcha')
        button.click()
        browser.fill('gerarCertidaoForm:cpfCnpj', cpf_cnpj)
        time.sleep(1)
        cookies = browser.cookies.all()
        browser.fill('gerarCertidaoForm:textoAudioCaptcha', transcript_mp3(cookies))
        button = browser.find_by_id("gerarCertidaoForm:btnEmitirCertidao")
        button.click()
        time.sleep(3)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
        Download do CNDT (Certidão Negativa de Débitos Trabalhistas)''')
    parser.add_argument(
      "--cpf",
      type=str,
      help="Digite o cpf somente os numeros"
    )
    parser.add_argument(
      "--cnpj",
      type=str,
      help="Digite o cnpj somente os numeros"
    )
    parser.add_argument(
      "--path",
      type=str,
      help="Digite o caminho para salvar a certidão"
    )
    args = parser.parse_args()
    if args.cpf:
        cpf_cnpj = args.cpf
    else:
        cpf_cnpj = args.cnpj
    download_cndt(cpf_cnpj, args.path)
