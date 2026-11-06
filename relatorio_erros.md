# Relatório de erros — Aula 13: Sintaxe JSON

**Atividade:** Construção de Backend — IESB  
**Validação:** execução local com Python e a biblioteca padrão `json`.

## Cenário A — JSON com erros de sintaxe

### Código original

```text
{
  'nome': "Carlos Lima",
  "matricula": "2024002",
  "aprovado": False,
}
```

### Erros identificados

1. **Erro de sintaxe — aspas simples:** chaves JSON precisam de aspas duplas.
2. **Erro de sintaxe — `False`:** JSON usa `false` minúsculo, não a grafia booleana do Python.
3. **Erro de sintaxe — vírgula final:** JSON não permite vírgula após o último membro do objeto.

O decodificador para no primeiro problema do trecho original. As três mensagens abaixo vêm de testes separados com `json.loads()`; cada trecho isola um dos problemas:

| Demonstração | Mensagem real observada |
|---|---|
| Trecho original completo | `Expecting property name enclosed in double quotes: line 2 column 3 (char 4)` |
| Aspas simples isoladas | `Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` |
| Booleano Python isolado | `Expecting value: line 1 column 14 (char 13)` |
| Vírgula final isolada | `Illegal trailing comma before end of object: line 1 column 23 (char 22)` |

### Código corrigido

```json
{
  "nome": "Carlos Lima",
  "matricula": "2024002",
  "aprovado": false
}
```

### Resultado

A versão corrigida foi carregada com sucesso por `json.load()`. O objeto resultante contém `nome`, `matricula` e `aprovado: false`.

## Cenário B — aninhamento confuso

### Código original

```text
{
  "turma": "9º Ano A",
  "alunos": "Ana Souza", "Carlos Lima"
}
```

### Erro identificado

**Erro de sintaxe:** depois do valor `"Ana Souza"`, o parser encontra outro texto sem uma nova chave. `alunos` só pode receber um valor; para agrupar vários nomes, esse valor deve ser um array.

**Mensagem real observada:** `Expecting ':' delimiter: line 4 column 1 (char 64)`.

### Código corrigido

```json
{
  "turma": "9º Ano A",
  "alunos": ["Ana Souza", "Carlos Lima"]
}
```

### Resultado

A versão corrigida foi carregada com sucesso por `json.load()` e produziu uma lista com os dois nomes em `alunos`.

## Validação dos arquivos de exemplo

Os oito arquivos `.json` foram carregados localmente pelo programa, sem erros:

- `aluno.json`
- `aluno_camel_case.json`
- `aluno_com_turma.json`
- `aluno_snake_case.json`
- `aninhamento_corrigido.json`
- `json_corrigido.json`
- `payload_complexo.json`
- `turma_alunos.json`

Os arquivos `json_incorreto.txt` e `aninhamento_incorreto.txt` continuam inválidos intencionalmente e foram testados com `json.loads()`. As três falhas isoladas do Cenário A também foram capturadas. Não foi feita validação externa pelo JSONLint.

## Conclusão

JSON tem regras próprias, diferentes da sintaxe de literais Python. A validação local capturou as mensagens do parser; as correções seguem a sintaxe JSON. O resultado geral foi 8/8 arquivos `.json` aprovados. Não foi feita validação externa pelo JSONLint.
