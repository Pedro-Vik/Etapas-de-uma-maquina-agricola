# Levantamento de requisitos — Projeto agrícola

## 1. Objetivo

Definir informações necessárias e perguntas que podem ser respondidas por consultas SQL para apoiar a análise de condições agrícolas.

O escopo deve respeitar os campos disponíveis. A base `produtos_agricolas.csv` não contém produtividade, custos, safra ou localização; portanto, não permite concluir rendimento real, rentabilidade ou desempenho regional.

## 2. Perfis de usuário

- **Analista/estudante:** importa, trata e explora os dados.
- **Responsável pela operação:** acompanha leituras de sensores, caso o histórico das Fases 1 e 2 seja integrado.
- **Gestor:** consulta indicadores agregados para comparar grupos e identificar padrões que merecem investigação.

## 3. Requisitos funcionais

| ID | Requisito | Dados necessários | Validação |
|---|---|---|---|
| RF01 | Importar a base de culturas para Oracle por Python | N, P, K, temperatura, umidade, pH, precipitação e cultura | Comparar linhas válidas do CSV com linhas carregadas |
| RF02 | Repetir a carga de forma controlada | CSV e tabela de destino | Executar duas vezes e conferir a contagem final |
| RF03 | Consultar o volume total | Identificador dos registros | Consulta de contagem |
| RF04 | Contar amostras por cultura | Cultura (`label`) | Agrupamento por cultura |
| RF05 | Comparar condições médias por cultura | N, P, K, temperatura, umidade, pH e precipitação | Médias agrupadas |
| RF06 | Identificar limites observados | Variáveis numéricas | Mínimo e máximo |
| RF07 | Avaliar correlações lineares | Variáveis numéricas | Função `CORR` do Oracle |
| RF08 | Armazenar leituras do protótipo | Data/hora, umidade, pH, nutrientes e estado da bomba, se existirem | Conferir os dados reais das Fases 1 e 2 |
| RF09 | Consultar evolução temporal | Data/hora e medições | Agrupamento por dia/mês |
| RF10 | Contabilizar estado da bomba | Data/hora e estado da bomba | Contagem por estado |

## 4. Requisitos não funcionais

- **RNF01 — Integridade:** usar tipos numéricos para medições e restrições para valores categóricos.
- **RNF02 — Rastreabilidade:** documentar origem do arquivo e data de importação.
- **RNF03 — Repetibilidade:** permitir nova carga de forma controlada.
- **RNF04 — Segurança:** não versionar senhas ou credenciais do Oracle.
- **RNF05 — Clareza:** documentar significado e unidade de cada coluna.
- **RNF06 — Consistência:** validar colunas obrigatórias antes da importação.

## 5. Perguntas de gestão e consultas

| ID | Pergunta | Consulta |
|---|---|---|
| Q01 | Quantos registros da base foram carregados? | SQL 1 |
| Q02 | Quantas amostras existem por cultura? | SQL 2 |
| Q03 | Quais são as condições médias por cultura? | SQL 3 |
| Q04 | Quais são os valores mínimos e máximos observados? | SQL 4 |
| Q05 | Qual cultura apresenta maior média de precipitação na base? | SQL 5 |
| Q06 | Como as variáveis numéricas se correlacionam? | SQL 6 |
| Q07 | Quantas leituras de sensores existem por dia? | SQL 7 |
| Q08 | Quantas leituras registram bomba ligada/desligada? | SQL 8 |

## 6. Regras de interpretação

1. `label` é a cultura associada ao registro, não uma medida de produtividade.
2. Médias descrevem somente a base analisada; não são limites universais de cultivo.
3. Correlação não demonstra causalidade.
4. Q07 e Q08 só serão úteis após carregar as leituras reais das Fases 1 e 2.
5. A tabela de sensores é um modelo inicial. Ajuste nomes, unidades, escalas e formato de data/hora à fonte real antes de utilizá-la.

## 7. Evidências a registrar

- Captura das tabelas Oracle criadas.
- Saída do script Python com quantidade de linhas inseridas.
- Resultado de `SELECT COUNT(*)` após a carga.
- Resultados das consultas SQL.
- Evidência de uma segunda execução da carga, demonstrando repetibilidade.
