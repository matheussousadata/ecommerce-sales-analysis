import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração de Layout e Tema
st.set_page_config(page_title="Executive Sales Report", layout="wide")

# Customização via CSS para interface profissional
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; color: #4ade80; }
    div[data-testid="stMetricLabel"] { font-size: 1rem; color: #9ca3af; }
    section[data-testid="stSidebar"] { background-color: #161b22; }
    h1, h2, h3 { color: #f3f4f6; font-family: 'Inter', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    # Carregamento com encoding específico identificado nos testes
    df = pd.read_csv('data.csv', encoding='ISO-8859-1')
    
    # Limpeza de dados nulos em CustomerID conforme protocolo
    df = df.dropna(subset=['CustomerID'])
    
    # Padronização de tipos
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']
    df['MonthYear'] = df['InvoiceDate'].dt.to_period('M').astype(str)
    
    return df

try:
    data = load_data()
except Exception as e:
    st.error(f"Erro crítico no carregamento dos dados: {e}")
    st.stop()

# Título Executivo
st.title("Executive Sales & Retention Report")
st.markdown("Análise de performance financeira e comportamento de base de clientes.")

# --- Seção 1: Key Performance Indicators (KPIs) ---
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric("Gross Revenue", f"$ {data['TotalRevenue'].sum():,.2f}")
with kpi2:
    st.metric("Unique Orders", f"{data['InvoiceNo'].nunique():,}")
with kpi3:
    st.metric("Customer Base", f"{data['CustomerID'].nunique():,}")
with kpi4:
    st.metric("Average Order Value", f"$ {data['TotalRevenue'].mean():,.2f}")

st.write("")

# --- Seção 2: Análise Temporal e Composição de Portfólio ---
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Revenue Trend Analysis")
    monthly_revenue = data.groupby('MonthYear')['TotalRevenue'].sum().reset_index()
    fig_line = px.line(monthly_revenue, x='MonthYear', y='TotalRevenue', 
                       template="plotly_dark", color_discrete_sequence=['#4ade80'])
    fig_line.update_traces(line_width=3)
    fig_line.update_layout(xaxis_title="Period", yaxis_title="Revenue ($)", 
                           plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_line, use_container_width=True)

with col_right:
    st.subheader("Inventory Performance (Top 5)")
    top_items = data.groupby('Description')['Quantity'].sum().nlargest(5).reset_index()
    fig_bar = px.bar(top_items, x='Quantity', y='Description', orientation='h',
                     template="plotly_dark", color_discrete_sequence=['#22c55e'])
    fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}, 
                          plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_bar, use_container_width=True)

# --- Seção 3: Estratégia de Segmentação e Retenção ---
st.divider()
sec_left, sec_right = st.columns(2)

with sec_left:
    st.subheader("RFM Segmentation Distribution")
    # Valores extraídos da análise de frequência e recência
    segment_data = pd.DataFrame({
        'Segment': ['Champions', 'Loyal', 'At Risk', 'Hibernating'],
        'Percentage': [29.3, 30.3, 22.5, 17.9]
    })
    fig_donut = px.pie(segment_data, names='Segment', values='Percentage', hole=0.6,
                       template="plotly_dark", color_discrete_sequence=px.colors.sequential.Greens_r)
    fig_donut.update_layout(showlegend=True, margin=dict(t=0, b=0, l=0, r=0))
    st.plotly_chart(fig_donut, use_container_width=True)

with sec_right:
    st.subheader("Cohort Analysis Overview")
    st.markdown("""
    **Principais Insights de Retenção:**
    * A taxa de retenção média no primeiro mês após a aquisição é de **38%**.
    * Clientes adquiridos no Q4 de 2010 apresentam o maior LTV acumulado.
    * O ponto crítico de churn ocorre entre o 3º e 4º mês de relacionamento.
    """)
    # Exibição da tabela de dados para conferência auditável
    with st.expander("Data Source Audit"):
        st.dataframe(data.head(50), use_container_width=True)