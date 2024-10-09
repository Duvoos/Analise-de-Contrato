# Analise de Contrato de Partnership

Bem-vindo ao projeto de Análise de Contrato de Partnership! 🎉

Este projeto foi criado com o objetivo de automatizar a extração de dados de um contrato de sociedade (partnership). Ele identifica os nomes dos sócios e a quantidade de cotas que cada um possui, e gera um arquivo `.docx` organizado com essas informações em formato de tabela.

## Como Funciona?

O script faz o seguinte:

1. Lê o conteúdo de um arquivo `.docx` que contém o contrato de partnership.
2. Identifica os sócios e a quantidade de cotas que cada um possui.
3. Gera um novo arquivo `.docx` contendo uma tabela com o nome de cada sócio e suas cotas.

No final, você terá um documento pronto com o quadro societário formatado e organizado!

---

## Requisitos

Antes de começar, você precisa garantir que tem o Python instalado em seu computador. Este projeto também usa algumas bibliotecas específicas que você precisará instalar.

### Bibliotecas necessárias:

- `python-docx`: Para manipular arquivos do Word (`.docx`).

---

## Instruções de Instalação

Siga estes passos simples para configurar e rodar o projeto no seu computador:

1. **Clone este repositório ou baixe os arquivos para o seu diretório de trabalho.**

2. **Instale as dependências**: Abra o terminal (ou PowerShell) e, dentro da pasta do projeto, execute o seguinte comando para instalar a biblioteca necessária:

   pip install python-docx


## Comando para executar o codigo principal 

   python extrair_socios.py

## Comando para executar o teste de automação

   python -m unittest tests.py
