import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from dotenv import load_dotenv
import os

def realizar_login(session, url_login, usuario, senha):
    """Realiza o login no portal e retorna a sessão autenticada."""

    res = session.get(url_login)
    soup = BeautifulSoup(res.text, "html.parser")

    token_tag = soup.find("input", {"name": "__RequestVerificationToken"})
    token = token_tag["value"] if token_tag else None

    payload = {
        "__RequestVerificationToken": token,
        "Usuario": usuario,
        "Senha": senha
    }

    res_post = session.post(url_login, data=payload)

    if res_post.status_code != 200:
        print(f"Erro no acesso: {res_post.status_code}")
        exit()

    return session


def acessar_pagina_notas(session, notas_url):
    """Acessa a página de notas e retorna o conteúdo HTML."""

    notas_response = session.get(notas_url)

    if notas_response.status_code != 200:
        print("Não foi possível acessar a página de notas.")
        exit()

    return notas_response.text


def calcular_medias(soup):
    """Calcula as médias por semestre e a média geral."""

    ciclos = soup.find_all("div", class_="panel panel-default")
    tabela = PrettyTable(["Ciclo", "Média Semestre"])
    soma_notas_geral = 0
    total_disciplinas_geral = 0

    for ciclo in ciclos:
        ciclo_titulo = ciclo.find("a", class_="col-sm-12 tabela-notas")
        if ciclo_titulo:
            ciclo_nome = ciclo_titulo.text.strip()
            tabela_notas = ciclo.find("table", class_="table table-striped no-more-tables")
            if tabela_notas:
                linhas = tabela_notas.find("tbody").find_all("tr")
                soma_notas = 0
                total_disciplinas = 0

                for linha in linhas:
                    colunas = linha.find_all("td")
                    if len(colunas) >= 4:
                        try:
                            media_final = float(colunas[3].text.strip().replace(",", "."))
                            soma_notas += media_final
                            soma_notas_geral += media_final
                            total_disciplinas += 1
                            total_disciplinas_geral += 1
                        except ValueError:
                            continue

                if total_disciplinas > 0:
                    media_semestre = soma_notas / total_disciplinas
                    tabela.add_row([ciclo_nome, f"{media_semestre:.2f}"])

    media_geral = soma_notas_geral / total_disciplinas_geral if total_disciplinas_geral > 0 else 0
    return tabela, media_geral


def main():
    load_dotenv()

    url_login = "https://interage.fei.org.br/secureserver/portal/"
    notas_url = "https://interage.fei.org.br/secureserver/portal/graduacao/secretaria/consultas/notas"

    usuario = os.getenv("USUARIO")
    senha = os.getenv("SENHA")

    if not usuario or not senha:
        print("\nCredenciais não configuradas.")
        exit()

    session = requests.Session()
    session = realizar_login(session, url_login, usuario, senha)

    html_notas = acessar_pagina_notas(session, notas_url)
    soup = BeautifulSoup(html_notas, "html.parser")
    
    tabela, media_geral = calcular_medias(soup)

    print("\nNotas do usuário: " + usuario + "\n")
    print(tabela)
    print(f"\nMédia Geral: {media_geral:.2f}")

if __name__ == "__main__":
    main()