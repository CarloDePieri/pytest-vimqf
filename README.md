[![PyPI](https://img.shields.io/pypi/v/pytest-vimqf)](https://pypi.python.org/pypi/pytest-vimqf)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-vimqf)](https://pypi.python.org/pypi/pytest-vimqf)
[![Build system: poetry](https://img.shields.io/badge/build%20system-poetry-blue)](https://github.com/python-poetry/poetry)

A simple pytest plugin that will shrink pytest output when specified, to fit vim
quickfix window.

## The problem

The vim quickfix window prepends `||` to commands output lines, to differentiate
from its actual fix elements. This behaviour is intended and not configurable.

Pytest default terminal reporter calculates the available terminal width and
organize its layout accordingly, often printing characters to the far right of
the screen.

When running pytest in vim (for example using [vim-dispatch](https://github.com/tpope/vim-dispatch)),
its output in the quickfix window will result in a broken layout (since there
actually are less columns available to pytest).

## The solution

Pytest-vimqf simply trick pytest's terminal reporter in thinking the terminal is
slightly smaller. This will allows it to fit nicely in the vim quickfix window.

## Installation

Install using pip:

```bash
pip install pytest-vimqf
```

## Usage

The plugin is disabled by default, allowing pytest to use the whole terminal when
called normally.

From inside vim, simply add the flag `--vim-quickfix` to pytest. For example:

```vim
:Dispatch pytest --vim-quickfix
```
