# Análise de condições agrícolas e previsão de culturas

Projeto acadêmico da FIAP — Fase 3, Capítulo 2.

## 1. Objetivo

Organizar e analisar dados relacionados às condições de solo e clima, comparar perfis de culturas agrícolas e utilizar modelos de classificação para identificar a cultura associada a um conjunto de condições informado. O projeto também prevê armazenamento estruturado no Oracle e consultas SQL para apoiar a análise dos dados.

> **Limite de interpretação:** a base atual permite analisar associações entre nutrientes, temperatura, umidade, pH, precipitação e cultura. Ela não contém, por si só, dados de produtividade, custos, safra, região ou manejo. Portanto, não apresente as análises como previsão de produtividade nem como recomendação agronômica definitiva.

## 2. Dados utilizados e origem

### 2.1 Base de condições agrícolas

Arquivo esperado: `produtos_agricolas.csv`.

| Coluna | Significado |
|---|---|
| `N` | Nitrogênio informado na base |
| `P` | Fósforo informado na base |
| `K` | Potássio informado na base |
| `temperature` | Temperatura |
| `humidity` | Umidade |
| `ph` | pH |
| `rainfall` | Precipitação |
| `label` | Cultura agrícola associada ao registro |

**Origem:** preencher com a fonte exata indicada pela FIAP ou utilizada pelo grupo (URL, instituição/autor e data de acesso, quando aplicável). Não atribua uma fonte sem confirmação.

### 2.2 Dados das Fases 1 e 2

O projeto anterior menciona um protótipo agrícola com ESP32/Wokwi e variáveis relacionadas a umidade, pH, nutrientes e acionamento de bomba. Antes da entrega, confirme quais arquivos e leituras foram efetivamente produzidos, os campos e unidades utilizados e a origem/data da coleta.

**Importante:** o script fornecido neste pacote carrega o CSV `produtos_agricolas.csv`. A tabela `LEITURAS_SENSORES` é apenas um modelo para acomodar o histórico das Fases 1 e 2; ajuste-a aos dados reais antes de afirmar que esses dados foram importados.

## 3. Tecnologias

- Python 3, Jupyter Notebook e VS Code
- Pandas e NumPy
- Matplotlib e Seaborn
- scikit-learn
- Oracle Database e python-oracledb

## 4. Instalação e execução da análise

1. Instale Python.
2. Abra a pasta do projeto no VS Code.
3. Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

4. Coloque `produtos_agricolas.csv` na mesma pasta do notebook.
5. Abra `PedroVictorPires_RM575181_fase3_cap2.ipynb`.
6. Selecione o kernel Python que contém as dependências.
7. Execute as células em ordem; ao final, confira e salve as saídas, tabelas e gráficos.

## 5. Banco Oracle

Execute `sql/01_estrutura_oracle.sql` no schema destinado ao projeto. Ele cria:

- `CULTURAS_AGRICOLAS`: registros do CSV;
- `LEITURAS_SENSORES`: modelo para leituras do protótipo, sujeito à conferência dos arquivos das Fases 1 e 2.

As consultas estão em `sql/02_consultas_gestao.sql`.

## 6. Carga repetível com Python

Configure as variáveis de ambiente com os dados do Oracle. Exemplo no PowerShell:

```powershell
$env:ORACLE_USER="seu_usuario"
$env:ORACLE_PASSWORD="sua_senha"
$env:ORACLE_DSN="localhost:1521/XEPDB1"
```

Execute:

```bash
py scripts/carregar_culturas_oracle.py
```

O script substitui o conteúdo atual de `CULTURAS_AGRICOLAS` pelo conteúdo válido do CSV, dentro de uma transação. **Use somente na tabela de trabalho deste projeto**, pois os registros anteriores dessa tabela serão substituídos. A tabela deve existir antes da execução.

## 7. Consultas de gestão

As consultas respondem, entre outras, às perguntas: volume total de registros; amostras por cultura; médias de nutrientes e condições climáticas por cultura; limites observados; cultura com maior média de precipitação; correlações entre variáveis; evolução temporal e estado da bomba nas leituras do protótipo (após integração dos dados históricos).

Execute as consultas no Oracle e registre resultados reais como evidência. Não inclua números estimados ou inventados.

## 8. Vídeo demonstrativo

Link do YouTube (não listado): **PREENCHER APÓS PUBLICAÇÃO**.

O vídeo deve ter até 4 minutos e demonstrar o tratamento dos dados, indicadores e gráficos, criação das tabelas Oracle, carga por Python e consultas SQL com resultados.

## 9. Entrega

- Repositório GitHub privado, organizado conforme o modelo da coordenação.
- Adicione `fiap-tutoria` como colaborador, conforme orientação da FIAP.
- Preencha `ENTREGA.txt` com o link do repositório e o link do vídeo.
- Confira o prazo e não altere o repositório após a entrega, conforme o critério informado.