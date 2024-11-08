# Termo

Este é um projeto didático que sugere palavras para jogar no Termo e variantes. A ordem das palavras sugeridas é pensada para a versão em português do jogo.

## Heurística usada

A ordenação das palavras usadas é baseada em duas heurísticas:

- Palavras com mais letras diferentes vem antes
- Palavras com mais vogais diferentes vem antes
- Ordem alfabética normal

## Editando as palavras

Para adicionar/remover uma palavra do arquivo de texto basta adicionar a palavra, respeitando a regra de uma palavra por linha. Em seguida é necessário ordenar o arquivo já na ordem de prioridades, para isso basta executar o comando a baixo:

```shell
python3 sort_txt.py
```