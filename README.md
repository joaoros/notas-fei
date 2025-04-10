# Notas FEI

Este projeto é um script Python que, através de webscraping, realiza login no portal da FEI, acessa a página de notas, calcula e exibe as médias por semestre e a média geral do aluno.

## Configuração

- Crie um arquivo `.env` na raiz do seu projeto e configure as credenciais de acesso ao portal da FEI:

```bash
USUARIO=seu_usuario
SENHA=sua_senha
```

Há um arquivo `.env.example`, no qual você pode se basear.

## Como usar?

1. Entre no diretório ```src``` e execute o script principal:

```bash
python3 main.py
```

2. O script exibirá as notas por semestre a média geral no terminal

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

## Licença
n/a
