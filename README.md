# Mars Rover Data Collector

Este repositório contém um script Python desenvolvido para coletar e processar dados e imagens do rover Perseverance, que está atualmente explorando Marte. Utilizando a API pública da NASA disponível em [api.nasa.gov](https://api.nasa.gov/), o script coleta informações detalhadas sobre as fotos capturadas pelo rover, armazena os dados em formato tabular, salva em um arquivo CSV e organiza as imagens em diretórios de forma sistemática.

## Objetivo do Script

O objetivo deste script é facilitar a coleta automatizada e o processamento de dados de imagens do rover Perseverance, permitindo uma análise aprofundada e armazenamento eficiente. Este projeto exemplifica a utilização prática de APIs para a obtenção de dados espaciais, contribuindo para estudos de dados, visualizações e projetos de exploração espacial.

## Estrutura do Projeto

- **Script principal**: Realiza a coleta de dados da API, tratamento dos dados em formato JSON para tabular, armazenamento em CSV e download das imagens.
- **Organização dos arquivos**: As imagens são organizadas em pastas nomeadas de acordo com a data de captura, no formato `YYYYMMDD`.

## Etapas do Processo

1. **Coleta dos dados**: Utiliza a API da NASA para obter informações e imagens do rover Perseverance.
2. **Tratamento dos dados JSON**: Converte a resposta JSON da API para um formato tabular usando o Pandas.
3. **Armazenamento em CSV**: Salva os dados tabulares em um arquivo CSV para futuras análises.
4. **Coleta de dados de um mês**: Reúne dados do primeiro dia do mês atual até D-2 (dois dias atrás).
5. **Download das imagens**: Baixa as fotos disponíveis e as salva localmente.
6. **Organização das imagens**: Cria diretórios específicos por data para armazenar as fotos de forma ordenada.
