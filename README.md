**English** · [Português (Brasil)](README.pt-BR.md)

# serp-dominant-type

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)

`serp-dominant-type` is a free, open source command-line tool that proposes the dominant page type in the organic top 10 of a search: service, post, long guide, glossary, list or comparison, tool, directory or marketplace, local page. It reads JSON files in the Serper format and prints the report in Brazilian Portuguese. The result is a proposal to be checked by hand.

## Contents

- [What it checks](#what-it-checks)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [FAQ](#faq)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## What it checks

Each of the 10 results is classified by URL and title. The bands are my own convention, with no external source: 6 or more of the same type is consensus, 4 or 5 is mixed, 3 or fewer is fragmented. Results that fit no type stay as "n/d" and are not counted.

## Requirements

Python 3.9 or newer. Standard library only.

## Installation

```bash
git clone https://github.com/LucasFerrazSEO/serp-dominant-type.git
cd serp-dominant-type
```

## Usage

```bash
python serp_dominant_type.py examples/serp-posts.json examples/serp-mista.json
```

Real output on the invented files in `examples/`:

```
serp-mista: serviço 3/10 (fragmentado) | serviço 3, post 2, glossário 1, lista ou comparativo 1
serp-posts: post 7/10 (consenso) | post 7, diretório ou marketplace 1, ferramenta 1 | n/d 1 (classificar à mão)
```

The exit code is 2 when a file cannot be read.

## FAQ

**Is it really free?**
Yes. It is open source under the MIT license.

**Why use the dominant type?**
When most of the top 10 is one type of page, a page of another type has little chance for that search. The tool shows the type, and the decision stays with you.

## Limitations

The classification is a heuristic over URL and title: a service page inside a `/blog/` path is read as a post. The lists of directories and Brazilian cities are not exhaustive. Reading the pages is the only reliable check, so confirm by hand before deciding anything.

## Contributing

Bug reports and suggestions are welcome through [GitHub Issues](https://github.com/LucasFerrazSEO/serp-dominant-type/issues).

## Author

[Lucas Ferraz](https://lucasferraz.com) is an SEO, website development and Generative Engine Optimization specialist and the founder of [Lucas Ferraz SEO](https://lucasferrazseo.com).

## License

MIT. See [LICENSE](LICENSE).
