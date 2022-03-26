# Aqua-parser

## Description

...

## How to use

...

## System Requirements

To start the service, the following software must be installed on your working machine:

* the "make" utility

## Technologies used

* service - python 3.10.2

## Unique features of the service

...

## Start service

```bash
make run
```

## Pyproject config

```toml
# Раздел системы сборки
[build-system]
requires = ["flit"]
build-backend = "flit.buildapi"

[tool.flit.module]
# Имя проекта для строчки import ... если имя проетка для pip install отличается от имени для import
name = "pdfparser"

[project]
# Имя проекта на PyPI
name = "pdfparser"
authors = [
    {name = "Vladimir Puzakov", email = "vppuzakov@rambler.ru"},
]
classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Operating System :: OS Independent',
    "Topic :: Internet",
    "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development",
    "Typing :: Typed",
]
# зависимости (список используемых пакетов)
dependencies = [
    "flask >=2,<3",
]
# Требования к версии python
requires-python = ">=3.7.0"
dynamic = ["version", "description"]

# Ссылка на проект
[project.urls]
Source = "https://github.com/org/project/"
Issues = "https://github.com/org/project/issues"

# Необязательные-зависимости проекта
[project.optional-dependencies]
# Раздел для зависимостей тестов
test = [
    "faker>=9.8,<10.0",
    "pytest>=6.2,<7.0",
    "pytest-clarity>=1.0,<2",
    "pytest-cov>=3.0,<4",
    "pytest-dotenv>=0.5.2,<1",
    "pytest-mock>=3.6,<4",
    "pytest-testdox>=2,<3",
]
# Раздел для зависимостей связанных с разработкой
dev = [
    "mypy>=0.910,<1",
    "wemake_python_styleguide>=0.15.3,<1",
]

[tool.mypy]
follow_imports = "silent"
warn_redundant_casts = true
warn_unused_ignores = true
disallow_any_generics = true
check_untyped_defs = true
no_implicit_reexport = true

[[tool.mypy.overrides]]
module = "notebook.*"
ignore_missing_imports = true
```
