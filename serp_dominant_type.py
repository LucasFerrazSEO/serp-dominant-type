#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""serp-dominant-type: propoe o tipo de pagina dominante no top 10 de uma busca.

Entrada: um ou mais JSON no formato do Serper ({"organic": [{"link": ..., "title": ...}]}).

    python serp_dominant_type.py busca.json [outra.json ...]

Classifica cada resultado, por URL e titulo, em: diretório ou marketplace, lista ou
comparativo, ferramenta, glossário, guia longo, post, página local, serviço. O que nao
encaixa fica "n/d". Faixas (convencao do autor, sem fonte externa): 6 ou mais = consenso,
4 ou 5 = misto, 3 ou menos = fragmentado.

E HEURISTICA por URL e titulo: confira a mao antes de decidir qualquer coisa.
Biblioteca padrao apenas, Python 3.9+.
"""
import argparse
import collections
import json
import os
import re
import sys

DIRETORIOS = ("clutch.co", "getninjas", "workana", "99freelas", "sortlist", "goodfirms",
              "reclameaqui", "apontador", "yelp", "guiamais", "telelistas", "econodata", "cnpj.",
              "linkedin.com", "facebook.com", "instagram.com", "google.com/maps", "doctoralia",
              "jusbrasil", "solutudo", "empresaqui", "casadosdados")
CIDADES = ("belo-horizonte", "belo horizonte", "sao-paulo", "são paulo", "rio-de-janeiro",
           "rio de janeiro", "curitiba", "porto-alegre", "porto alegre", "brasilia", "brasília",
           "salvador", "fortaleza", "recife", "goiania", "goiânia", "campinas", "manaus",
           "florianopolis", "florianópolis", "vitoria", "vitória")
# Serviço: raiz do site ou caminho com palavra comercial generica (nada de nicho).
SERVICO = r"(servico|servicos|services?|solucoes|solutions|planos|precos|pricing|orcamento|contato|agencia|agency|consultoria|consulting)"


def classificar(link, titulo):
    u = (link or "").lower()
    t = (titulo or "").lower()
    caminho = re.sub(r"^https?://[^/]+", "", u).split("?")[0].strip("/")
    if any(x in u for x in DIRETORIOS):
        return "diretório ou marketplace"
    if re.search(r"\b(\d+|top)\s+(melhores|maiores|principais)\b|\bmelhores\b|\branking\b|\bvs\.?\b| x |compar", t):
        return "lista ou comparativo"
    if re.search(r"/(ferramenta|ferramentas|tools?|gerador|calculadora|checker)\b", u) or \
       re.search(r"\b(gerador|calculadora|checker|ferramenta grátis|ferramenta gratuita|online grátis)\b", t):
        return "ferramenta"
    if "wikipedia.org" in u or re.search(r"/(glossario|dicionario|significado|definicao)\b", u) or \
       re.search(r"^o que (é|e) |: o que (é|e)|significado", t):
        return "glossário"
    if re.search(r"guia (completo|definitivo|prático|pratico)|passo a passo", t):
        return "guia longo"
    if re.search(r"/(blog|artigos?|noticias?|news|conteudos?)/", "/" + caminho + "/") or re.search(r"/20\d\d/", u):
        return "post"
    if any(c in u or c in t for c in CIDADES):
        return "página local"
    if caminho == "" or re.search(SERVICO, caminho):
        return "serviço"
    return "n/d"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("arquivos", nargs="+")
    a = ap.parse_args()
    for f in a.arquivos:
        try:
            with open(f, encoding="utf-8") as fh:
                org = json.load(fh).get("organic", [])[:10]
        except (OSError, ValueError, AttributeError) as e:
            print(f"ERRO {f}: {e}", file=sys.stderr)
            sys.exit(2)
        tipos = [classificar(o.get("link"), o.get("title")) for o in org if isinstance(o, dict)]
        cont = collections.Counter(t for t in tipos if t != "n/d")
        nome = os.path.splitext(os.path.basename(f))[0]
        if not cont:
            print(f"{nome}: sem classificação possível ({len(tipos)} resultados)")
            continue
        tipo, n = cont.most_common(1)[0]
        banda = "consenso" if n >= 6 else "misto" if n >= 4 else "fragmentado"
        detalhe = ", ".join(f"{t} {c}" for t, c in cont.most_common())
        nd = tipos.count("n/d")
        print(f"{nome}: {tipo} {n}/10 ({banda}) | {detalhe}" + (f" | n/d {nd} (classificar à mão)" if nd else ""))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    main()
