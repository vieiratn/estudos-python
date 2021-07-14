# Script Diagnóstico de Covid-19

Script criado em Python e que ajuda no diagnóstico da **Covid-19**.

Muitas pessoas possuem sintomas leves e não querem ou não podem sair de casa e ir até um ponto de saúde com medo de realmente contrair o vírus e outros problemas de saúde.

Visando resolver esse problema e ajudar as pessoas com informações válidas, pensei em desenvolver esse Script com o objetivo de praticar e aprofundar meus conhecimentos na linguagem Python.

## Imagens do Script

![Coleta de Dados](https://i.imgur.com/8lDM9dO.png)

![Apresentação do Relatório](https://i.imgur.com/gcYPGsJ.png)

## Funcionamento do Script

O Script é formado por três arquivos:

* aplicação_principal
* modulo_execucao
* modulo_mensagens
* conexao_db


### Aplicação Principal

É o script que contém a lógica de programação básica com a ordem de execução dos comandos, basicamente, o esqueleto que irá executar todos os demais Scripts.

Para excutar com mas facilidade em sistemas linux:
Dê permissão de execução ao script -> "sudo chmod +x aplicacao_principal.py"
Rode o script ./aplicação_principal.py

### Módulo de Execução

É o *coração do sistema*, neste Script eu vou coletar e processar a análise de todos os dados fornecidos pelo usuário, dessa forma, podendo personalizar o seu diagnóstico como se fosse uma *mini-consulta* com um médico.


### Módulo de Mensagens

É onde personalizo todas as mensagens que serão utilizadas no sistema com cores e formatação. Dessa forma, a facilidade para prover manutenção ao código é mais ágil de acordo com novas informações fornecidas pelos órgãos de saúde.

### Modulo conexão

Este modulo foi desenvolvido com a ideia de salvar os dados em um banco de dados hospedado em um servidor, o intuito da criação do banco é que posteriormente possamos fazer algumas consultas mais avançadas. 
Foi criado um banco no servidor do site http://freesqldatabase.com, todos os dados para conexão esta no modulo conexao. Todas as infomações estão em "texto plano". Pedimos que seja levado em consideração que este script foi desenvolvido apenas para estudo, não tendo informações valiosas salvas no banco. Lembre-se que todos os dados são ficticios e esta sistema pode servir para outras pessoas estudarem e aprender. Tenha conciência e não mude a senha ou algo do tipo.

Para o funcionamento do sistema é necessário a instalação de um mysql_connector. Você pode baixar no link abaixo o connector equivalente ao seu sistema operacional.
https://dev.mysql.com/downloads/connector/python/

## imagem
![Concector_python](https://i.imgur.com/xRmtDls.png)

Para sistemas linux após baixar o arquivo nome_arquivo.deb,navegue ate a pasta que foi salvo o arquivo e use o comando -> sudo dpkg -i nome_arquivo.deb 

## Considerações Finais

No momento, não tenho qualquer pretensão de disponibilizar ao público a aplicação, até por não ter experiência em outras linguagens e pacotes, porém, pretendo apresentar melhorias e fornecer manutenção ao código com o intuito de melhorar e aprofundar meus conhecimentos sobre programação.

**Sinta-se completamente à vontade para sugerir melhorias e estudar os códigos.**

## Observação Importante:

> Sou um pequeno gafanhoto e comecei a aprender sobre programação durante a quarentena em 2020, portanto, pense antes de criticar de forma não-construtiva.

## Notas de Manutenção:

> **Primeira Melhoria**: Ajuste no Script para não aceitar idades em valores zero ou negativos. (Melhoria feita);

> **Segunda Melhoria**: Ajuste no Script e criação do arquivo de log de erros para acompanhar a usabilidade e implementar melhorias baseadas nos erros apresentados durante uso. 

> **Terceira Melhoria**: Ajuste no Script para não aceitar números e caracteres especiais no campo nome. (Melhoria feita, inclusive aceita o nome completo do usuário!)

============================================================================================================

> **Quarta Melhoria**: Melhorar o banco de dados para salvar todas as informações pertinentes ao "paciante".
> **Quinta Melhoria**: Incluir sexo e estado do user afim de melhorar as consultas mais complexas do banco de dados.
> **Sexta Melhoria**: Normalização do banco de dados.
> **Sétima Melhoria**: Criação de uma interface para o script.
> **Oitava Melhoria**: caso o resultado seja 'positivo para covid', coletar o email do user, contar 14 dias e enviar um email para ele refazer a pesquisa.

============================================================================================================= 