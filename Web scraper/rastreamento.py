def contar_covid():
    with open('noticias.txt', 'r', encoding='utf-8') as file:
        conteudo = file.read()
        palavras = conteudo.split()
        covid_count = palavras.count('COVID')
        return covid_count


covid_count = contar_covid()
print(f'A palavra COVID foi mencionada {
      covid_count} vezes nas manchetes das notícias.')
