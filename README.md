# Executive Sales & Retention Intelligence
**Framework de Análise de Performance Financeira e Comportamento de Base**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

Este repositório contém uma solução de Business Intelligence desenvolvida para a extração de insights estratégicos a partir de dados transacionais de e-commerce. O foco do projeto é a decodificação do Ciclo de Vida do Cliente (LTV) e a otimização de estoque baseada em demanda real.

---

## <img src="https://cdn-icons-png.flaticon.com/512/2103/2103633.png" width="25"> Arquitetura do Projeto

O sistema processa volumes de dados históricos para identificar anomalias, sazonalidades e padrões de retenção, estruturando a visualização em quatro pilares fundamentais:

### 1. Monitoramento de KPIs Financeiros
*   **Gross Revenue:** Rastreamento do faturamento bruto consolidado.
*   **Average Order Value (AOV):** Monitoramento do ticket médio por transação.
*   **Customer Base:** Mensuração da expansão da base de clientes únicos.

### 2. Análise de Tendência e Sazonalidade
*   Identificação de picos de faturamento (Q4 - Novembro).
*   Mapeamento de vales operacionais para planejamento de ações de ativação.

### 3. Inteligência de Inventário
*   Ranking dinâmico de performance de SKUs (Top 5).
*   Análise de giro de estoque para mitigação de ruptura e excesso de capital imobilizado.

### 4. Segmentação RFM e Cohort
*   **RFM Analysis:** Classificação técnica da base em perfis (Champions, Loyal, At Risk, Hibernating).
*   **Retention Cohort:** Identificação do ponto crítico de churn entre o 3º e 4º mês de relacionamento.

---

## <img src="https://cdn-icons-png.flaticon.com/512/1085/1085469.png" width="25"> Stack Tecnológica

| Componente | Tecnologia |
| :--- | :--- |
| **Engine** | Python 3.9+ |
| **Interface** | Streamlit |
| **Data Processing** | Pandas / NumPy |
| **Visualization** | Plotly / Matplotlib |
| **Metodologias** | RFM Segmenting / Cohort Analysis |

---

## <img src="https://cdn-icons-png.flaticon.com/512/1155/1155050.png" width="25"> Diagnóstico Estratégico

Com base nos dados processados, as seguintes diretrizes foram estabelecidas:

1.  **Otimização de Retenção:** Implementação de réguas de relacionamento preditivas ao final do 2º mês para estender o LTV.
2.  **Recuperação de Receita:** Estratégia de win-back direcionada aos 29.3% de clientes em estado de hibernação.
3.  **Planejamento de Demanda:** Ajuste de compras baseado na tração acelerada observada a partir de Agosto.

---


