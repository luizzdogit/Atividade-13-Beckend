"""Demonstrações da atividade sobre sintaxe JSON."""

import json
from pathlib import Path


PASTA_ATIVIDADE = Path(__file__).resolve().parent
PASTA_EXEMPLOS = PASTA_ATIVIDADE / "exemplos"


def demonstrar_erro(titulo, trecho, causa):
    """Exibe um JSON inválido e captura o erro real do decodificador."""
    print(f"\n{titulo}")
    print("Código incorreto:")
    print(trecho)
    print(f"Erro identificado: {causa}")
    try:
        json.loads(trecho)
    except json.JSONDecodeError as erro:
        print(f"Erro real do Python: {erro}")
        return str(erro)
    raise AssertionError("O trecho deveria ser JSON inválido.")


def validar_arquivo(caminho):
    """Carrega um arquivo JSON e informa o resultado da validação."""
    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def demonstrar_cenario_a():
    original = (PASTA_EXEMPLOS / "json_incorreto.txt").read_text(
        encoding="utf-8"
    )
    demonstrar_erro(
        "Cenário A — trecho original",
        original,
        "aspas simples, booleano escrito como em Python e vírgula final.",
    )

    erros_isolados = [
        (
            "Erro isolado 1 — aspas simples na chave",
            """{'nome': "Carlos Lima"}""",
            "JSON exige aspas duplas nas chaves.",
        ),
        (
            "Erro isolado 2 — booleano Python",
            '{"aprovado": False}',
            "JSON usa true/false em minúsculas.",
        ),
        (
            "Erro isolado 3 — vírgula final",
            '{"nome": "Carlos Lima",}',
            "JSON não permite vírgula após o último elemento.",
        ),
    ]
    for titulo, trecho, causa in erros_isolados:
        demonstrar_erro(titulo, trecho, causa)

    corrigido = PASTA_EXEMPLOS / "json_corrigido.json"
    dados = validar_arquivo(corrigido)
    print("\nCódigo corrigido:")
    print(corrigido.read_text(encoding="utf-8"))
    print(f"Resultado da validação: aprovado ({dados})")


def demonstrar_cenario_b():
    original = (PASTA_EXEMPLOS / "aninhamento_incorreto.txt").read_text(
        encoding="utf-8"
    )
    demonstrar_erro(
        "Cenário B — aninhamento confuso",
        original,
        "dois valores foram escritos para alunos sem formar um array.",
    )
    corrigido = PASTA_EXEMPLOS / "aninhamento_corrigido.json"
    dados = validar_arquivo(corrigido)
    print("\nCódigo corrigido:")
    print(corrigido.read_text(encoding="utf-8"))
    print(f"Resultado da validação: aprovado ({dados})")
    print("Um array agrupa os dois nomes em uma única chave alunos.")


def validar_exemplos():
    """Valida todos os arquivos .json da pasta de exemplos."""
    print("\nPARTE 4 — Validação dos exemplos")
    arquivos = sorted(PASTA_EXEMPLOS.glob("*.json"))
    falhas = []
    for caminho in arquivos:
        try:
            validar_arquivo(caminho)
            print(f"APROVADO: exemplos/{caminho.name}")
        except (json.JSONDecodeError, OSError) as erro:
            falhas.append(caminho.name)
            print(f"FALHOU: exemplos/{caminho.name}: {erro}")
    print(f"Arquivos JSON aprovados: {len(arquivos) - len(falhas)}/{len(arquivos)}")
    if falhas:
        raise SystemExit(1)


def main():
    print("PARTE 1 — Questões teóricas: respostas disponíveis no README.md.")
    print("PARTE 2 — Comandos JSON: respostas disponíveis no README.md.")
    print("\nPARTE 3 — Encontre o erro")
    demonstrar_cenario_a()
    demonstrar_cenario_b()
    validar_exemplos()
    print("\nPARTE 5 — Desafio extra: resposta disponível no README.md.")


if __name__ == "__main__":
    main()
