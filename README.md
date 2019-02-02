## Trailer Filmes

Este é o projeto de estudo "Site de trailers de filmes" do curso de Desenvolvedor Web Full-Stack do módulo 1 do curso da Udacity.

O projeto consiste em uma página Web que exibe um conjunto de filmes e que permite uma rápida visualização de seus trailers, embarcados na própria página.

A página web é estática e é gerada a partir da execução do script python 'entertainment_center.py', conforme mostrado abaixo:

| python entertainment_center.py

# Pré-execução

O script faz uso da API do site themoviedb.org. Caso queira usar o site fazendo uso da API é necessário editar o arquivo
entertainment_center.py e na function get_movies_from_tmdb() substituir o texto < MY_API_KEY > pela sua chave gerada no site do projeto da API.

# Execução

Se uma API_KEY é fornecida o script fará uso da API para coleta dos dados dos filmes, caso contrário o script carrega um arquivo no formato '.yaml'
que contém as informações relacionados à filmes pré-definidos.
Após os dados dos filmes serem coletados, o script 'fresh_tomatoes.py' recebe esse conjunto de informações, é executado e dele é gerado o arquivo de entrada do projeto, o fresh_tomatoes.html.

# Pré-requisitos do projeto:

- Versão do Python: 2.7.9
- É necessário a instalação da lib pyyaml: 3.13
- É necessário a instalação da lib tmdbsimple: 2.2.0
- É necessário possuir uma API_KEY para acesso à API do themoviedb.org(que pode ser gerada no próprio site https: // www.themoviedb.org/).

# Fontes consultadas:

- https://pyyaml.org/wiki/PyYAMLDocumentation
- https://www.themoviedb.org/
- https://developers.themoviedb.org/3/getting-started/introduction
- https://github.com/celiao/tmdbsimple
- https://pypi.org/project/tmdbsimple/
- https://www.pydoc.io/pypi/tmdbsimple-1.8.0/index.html
- https://www.pythonforbeginners.com/error-handling/python-try-and-except
- https://code.visualstudio.com/docs/python/linting
