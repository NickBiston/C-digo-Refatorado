# Refatoração de Código - Clean Code

Projeto de refatoração de um código em Python com o objetivo de aplicar princípios de Clean Code e boas práticas da PEP 8.

## Objetivo

Melhorar a legibilidade, organização e manutenção do código por meio de:

* Nomenclatura mais clara;
* Aplicação da PEP 8;
* Substituição de valores mágicos por constantes;
* Type Annotations;
* Docstrings;
* Remoção de comentários redundantes;
* Melhor tratamento de exceções.

## Principais alterações

### Nomenclatura

Os nomes abreviados foram substituídos por nomes mais descritivos.

| Original   | Refatorado         |
| ---------- | ------------------ |
| `proc_ped` | `processar_pedido` |
| `d`        | `dados_produto`    |
| `n`        | `nome_produto`     |
| `p`        | `preco_unitario`   |
| `q`        | `quantidade`       |
| `t`        | `total_pedido`     |
| `c`        | `codigo_produto`   |
| `res`      | `resultado`        |

Também foi utilizado `snake_case`, seguindo a PEP 8.

### Valores mágicos

Os valores `1000` e `0.90` foram transformados em constantes:

```python
LIMITE_DESCONTO = 1000
FATOR_DESCONTO = 0.90
```

### Type Annotations

A função passou a informar os tipos dos parâmetros e do retorno:

```python
def processar_pedido(
    dados_produto: dict,
    enviar_email: bool
) -> dict:
```

### Docstring

Foi adicionada uma Docstring para explicar a função, seus parâmetros, retorno e possíveis exceções.

### Comentários

Comentários que apenas descreviam o que o código já deixava claro foram removidos.

### Tratamento de exceções

Os retornos `None` e `False`, utilizados anteriormente para indicar erros, foram substituídos por exceções utilizando `raise`.

Também foram adicionados tratamentos específicos para:

* `KeyError`
* `ValueError`

### Estrutura de tratamento

O código passou a utilizar:

```python
try:
    ...
except (ValueError, KeyError) as erro:
    ...
else:
    ...
finally:
    ...
```

Cada bloco possui uma responsabilidade:

* `try`: executa o processamento;
* `except`: trata os erros;
* `else`: executa quando não ocorre erro;
* `finally`: executa sempre.

## Resultado

A refatoração tornou o código mais legível, previsível e organizado, seguindo os princípios de Clean Code e as convenções da PEP 8.
