LIMITE_DESCONTO = 1000
FATOR_DESCONTO = 0.90


def processar_pedido(dados_produto: dict, enviar_email: bool) -> dict:
    """
    Processa os dados de um produto e calcula o valor total do pedido.

    Parâmetros:
        dados_produto (dict): Dicionário contendo código, nome, preço
            unitário e quantidade do produto.
        enviar_email (bool): Indica se deve exibir a mensagem de
            confirmação de envio do e-mail.

    Retorna:
        dict: Dados do produto processado e o valor total calculado.

    Exceções:
        ValueError: Caso algum valor do produto seja inválido.
        KeyError: Caso alguma chave obrigatória não exista no dicionário.
    """

    if dados_produto is None:
        raise ValueError("Os dados do produto não foram informados.")

    try:
        nome_produto = dados_produto["nome"]
        preco_unitario = dados_produto["preco_unitario"]
        quantidade = dados_produto["quantidade"]
        codigo_produto = int(dados_produto["codigo"])
    except KeyError as erro:
        raise KeyError(f"Campo obrigatório não encontrado: {erro}") from erro
    except ValueError as erro:
        raise ValueError("O código do produto deve ser um número inteiro.") from erro

    if nome_produto == "":
        raise ValueError("O nome do produto não pode estar vazio.")

    if preco_unitario <= 0:
        raise ValueError("O preço do produto deve ser maior que zero.")

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    total_pedido = preco_unitario * quantidade

    if total_pedido > LIMITE_DESCONTO:
        total_pedido = total_pedido * FATOR_DESCONTO

    if enviar_email:
        print("Enviando e-mail de confirmacao para o pedido...")

    return {
        "codigo": codigo_produto,
        "nome": nome_produto,
        "preco_unitario": preco_unitario,
        "quantidade": quantidade,
        "total_calculado": total_pedido
    }


try:
    dados_produto = {
        "codigo": "101",
        "nome": "Teclado Mecânico",
        "preco_unitario": 150.0,
        "quantidade": 8
    }

    resultado = processar_pedido(dados_produto, True)

except (ValueError, KeyError) as erro:
    print(f"Erro ao processar o pedido: {erro}")

else:
    print("Resultado:", resultado)

finally:
    print("Processamento do pedido finalizado.")
