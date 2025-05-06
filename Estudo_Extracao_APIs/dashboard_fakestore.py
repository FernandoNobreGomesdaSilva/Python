import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Título do Dashboard
st.title("📊 Dashboard de Produtos - FakeStore API")

# Fetch data from API
@st.cache_data  # Cache para evitar múltiplas requisições
def load_data():
    response = requests.get("https://fakestoreapi.com/products")
    return pd.DataFrame(response.json())

df = load_data()

# Sidebar com filtros
st.sidebar.header("Filtros")
category = st.sidebar.selectbox(
    "Selecione a Categoria",
    options=df['category'].unique()
)

# Filtrar dados
filtered_df = df[df['category'] == category]

# Mostrar tabela
st.subheader(f"Produtos da Categoria: {category}")
st.dataframe(filtered_df[['title', 'price', 'rating']])

# Gráfico de preços
st.subheader("📈 Distribuição de Preços")
fig, ax = plt.subplots()
ax.hist(filtered_df['price'], bins=10, color='skyblue', edgecolor='black')
st.pyplot(fig)

# Métricas resumidas
col1, col2 = st.columns(2)
with col1:
    st.metric("Número de Produtos", len(filtered_df))
with col2:
    st.metric("Preço Médio", f"${filtered_df['price'].mean():.2f}")