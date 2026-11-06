# Aula 13 — Sintaxe JSON

Atividade de Construção de Backend — IESB.

## Parte 1 — Questões teóricas

1. **O que é JSON e por que é usado na web?**  
   JSON é um formato leve de texto para representar e trocar dados. É simples de ler e escrever, e muitas linguagens conseguem processá-lo.

2. **Três diferenças entre dicionário Python e objeto JSON:**  
   Em JSON, chaves e textos usam aspas duplas; booleanos são `true` e `false` em minúsculas; ausência é representada por `null` (em Python, `None`).

3. **Chave com array de objetos:**  
   Significa que a chave aponta para uma lista cujos elementos são objetos. Exemplo: `{"alunos": [{"nome": "Ana"}, {"nome": "Carlos"}]}`.

4. **CamelCase e snake_case:**  
   CamelCase junta palavras e usa maiúscula no meio (`dataNascimento`); snake_case separa palavras com underline (`data_nascimento`).

5. **JSONLint:**  
   É uma ferramenta que verifica se o texto está sintaticamente correto como JSON. Conferir antes do envio ajuda a encontrar erros que fariam uma API rejeitar o payload.

## Parte 2 — Complete o comando

| Item | Resposta |
|---|---|
| a) Delimitador de objeto | `{}` |
| b) Delimitador de array | `[]` |
| c) Booleano verdadeiro | `true` |
| d) Ausência (equivalente a `None`) | `null` |
| e) Aspas das chaves | Aspas duplas (`"`) |
| f) Convenção de `dataNascimento` | camelCase |

## Parte 3 — Encontre o erro

Os arquivos `.txt` guardam os trechos originais inválidos. O programa usa `json.loads()` e captura as exceções reais, inclusive demonstrações isoladas para cada erro do Cenário A. As correções ficam nos arquivos `.json` correspondentes. O registro das mensagens observadas está em [relatorio_erros.md](./relatorio_erros.md).

No Cenário B, um array é necessário porque a chave `alunos` deve associar-se a um único valor que contenha os dois nomes. A lista em JSON (`[...]`) representa essa coleção.

## Parte 4 — Prática guiada

Os exemplos incluem objeto simples, objeto aninhado, array de objetos, as convenções snake_case/camelCase e um payload mais completo. O programa valida localmente todos os arquivos `.json` com a biblioteca padrão `json`; não foi feita validação externa pelo JSONLint.

Execute da pasta do projeto:

```powershell
python atividade_aula_13_json\atividade_json.py
```

## Parte 5 — Desafio extra

`application/json` é o MIME type que identifica conteúdo JSON.  
Ao enviar um corpo JSON em uma requisição HTTP, o cliente costuma informar `Content-Type: application/json`.  
Esse cabeçalho diz ao servidor como interpretar o corpo recebido.
