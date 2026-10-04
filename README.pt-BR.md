[English](README.md) · **Português (Brasil)**

# serp-dominant-type

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`serp-dominant-type` é uma ferramenta de linha de comando gratuita e de código aberto que propõe o tipo de página dominante no top 10 orgânico de uma busca: serviço, post, guia longo, glossário, lista ou comparativo, ferramenta, diretório ou marketplace, página local. Lê arquivos JSON no formato do Serper. O resultado é uma proposta para conferir à mão.

## Sumário

- [O que a ferramenta verifica](#o-que-a-ferramenta-verifica)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Perguntas frequentes](#perguntas-frequentes)
- [Limitações](#limitações)
- [Como contribuir](#como-contribuir)
- [Autor](#autor)
- [Licença](#licença)

## O que a ferramenta verifica

Cada um dos 10 resultados é classificado por URL e título. As faixas são convenção minha, sem fonte externa: 6 ou mais do mesmo tipo é consenso, 4 ou 5 é misto, 3 ou menos é fragmentado. Resultado que não encaixa em nenhum tipo fica como "n/d" e não entra na conta.

## Requisitos

Python 3.9 ou superior. Só biblioteca padrão.

## Instalação

```bash
git clone https://github.com/LucasFerrazSEO/serp-dominant-type.git
cd serp-dominant-type
```

## Uso

```bash
python serp_dominant_type.py examples/serp-posts.json examples/serp-mista.json
```

O código de saída é 2 quando um arquivo não pode ser lido. Os arquivos de `examples/` são inventados.

## Perguntas frequentes

**É gratuita mesmo?**
Sim. É código aberto sob a licença MIT.

**Por que usar o tipo dominante?**
Quando a maior parte do top 10 é de um tipo de página, uma página de outro tipo tem pouca chance naquela busca. A ferramenta mostra o tipo, e a decisão continua com você.

## Limitações

A classificação é uma heurística sobre URL e título: uma página de serviço dentro de um caminho `/blog/` é lida como post. As listas de diretórios e de cidades brasileiras não são exaustivas. Ler as páginas é a única conferência confiável, então confirme à mão antes de decidir qualquer coisa.

## Como contribuir

Relatos de erro e sugestões são bem-vindos pelas [Issues do GitHub](https://github.com/LucasFerrazSEO/serp-dominant-type/issues).

## Autor

[Lucas Ferraz](https://lucasferraz.com) é especialista em SEO, criação de sites e Generative Engine Optimization e fundador da [Lucas Ferraz SEO](https://lucasferrazseo.com).

## Licença

MIT. Veja [LICENSE](LICENSE).
