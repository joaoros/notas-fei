# Notas FEI

Este projeto é um script Python que, através de webscraping, realiza login no portal da FEI, acessa a página de notas, calcula e exibe as médias por semestre e a média geral do aluno.

## Como usar?

1. Baixe o repositório

```bash
$ git clone https://github.com/joaoros/notas-fei
$ cd notas-fei
```

2. Instale as dependências

```
$ pip3 install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz do seu projeto e configure as credenciais de acesso ao portal da FEI. Há um arquivo `.env.example`, no qual você pode se basear.

```bash
USUARIO=seu_usuario
SENHA=sua_senha
```

4. Entre no diretório ```src``` e execute o script:

```bash
cd src; python3 main.py
```

O script exibirá as notas por semestre a média geral no terminal

## Estrutura do projeto

```bash
├── .env                
├── .gitignore         
├── README.md         
├── requirements.txt
└── src/
    └── main.py
```

## Depedências

- Python 3.9
- As dependências do projeto estão listadas no arquivo requirements.txt

## Observações

- Certifique-se de que as credenciais fornecidas no arquivo .env estão corretas.
- O script depende da estrutura HTML do portal da FEI. **Caso o portal seja atualizado, o script pode precisar de ajustes.**
