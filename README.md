# Pipeline de Dados com Python e Pandas (ETL)

## Descrição do Projeto

Este projeto consiste na construção de um pipeline de dados (ETL) utilizando Python e Pandas, simulando um cenário real de integração de dados provenientes de múltiplas empresas, cada uma com formatos e padrões distintos.

O desenvolvimento foi realizado em ambiente Linux (WSL), reforçando práticas comuns em contextos profissionais de engenharia de dados e contribuindo para maior familiaridade com ferramentas de linha de comando, organização de projetos e versionamento de código.

---

## Problema Simulado

As empresas **Empresa A** e **Empresa B** fornecem dados de produtos com:

- Formatos diferentes (JSON e CSV)
- Nomes de colunas inconsistentes
- Estruturas distintas entre os datasets

Esses dados precisam ser padronizados, consolidados e exportados para consumo analítico.

---

## Objetivos do Projeto

- Construir um pipeline ETL em Python
- Ler dados de múltiplas fontes
- Padronizar schemas e nomes de colunas
- Unificar datasets heterogêneos
- Gerar um dataset final consistente
- Aplicar boas práticas de organização, versionamento e reutilização de código

---

## Tecnologias Utilizadas

- Python 3
- Pandas
- Linux (WSL)
- Git e GitHub para versionamento
- Ambiente virtual (venv)
- VS Code

---

## Estrutura do Projeto

```
pipeline_dados/
│
├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
│
├── data_processed/
│   └── df_processed.csv
│
├── scripts/
│   └── fusao_dfs.py
│
├── .venv/
├── README.md
└── requirements.txt
```

---

## Etapas do Pipeline (ETL)

### Extração
- Leitura de arquivos JSON e CSV utilizando Pandas
- Identificação do tipo de dado por parâmetro
- Execução dos processos em ambiente Linux (WSL)

### Transformação
- Padronização dos nomes das colunas
- Ajuste de diferenças de schema entre datasets
- Uso de funções e classes para reutilização de código
- União de múltiplos DataFrames com `pd.concat`

### Carga
- Exportação do DataFrame final para CSV
- Dataset preparado para análises ou ingestão em banco de dados



---

## Aprendizados

- Desenvolvimento de pipelines de dados em Python
- Uso do Pandas para leitura, transformação e consolidação de dados
- Organização de projetos em ambiente Linux (WSL)
- Versionamento de código com Git e GitHub
- Aplicação de orientação a objetos (classes e métodos)
- Boas práticas de estruturação e reutilização de código

---

## Próximos Passos

- Validação automática de schema
- Implementação de logs e monitoramento
- Tratamento avançado de erros
- Persistência dos dados em banco de dados
- Automatização do pipeline

---

## Autor

**Danilo Kofugi**  
Projeto desenvolvido para fins de estudo e portfólio em Engenharia de Dados.