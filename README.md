# 📖 Documentação Completa do Projeto

## 🚦 Preditor de Interrupção Temporária em Caso de Acidente

Este projeto é um sistema de predição que utiliza machine learning para estimar se ocorrerá uma interrupção temporária em situações de acidente. Ele é composto por uma API desenvolvida em Flask, um modelo de machine learning treinado, e uma interface web para consulta.

---

## 📂 Estrutura do Projeto

```
.gitignore
README.md
requirements.txt
app/
    run.bat
    server.py
data/
    base_dados_limpa.csv
    base_dados_ml.csv
    base_dados.csv
dataviz/
    grafico-interrupcao_anualXcausa_direta.png
    grafico-interrupcaoXnatureza.png
    grafico-ocorrencias_anuaisXmes.png
    grafico-ocorrenciasXcausa.png
    grafico-vitimasXnatureza.png
documentation/
    abstracao-dados.pdf
    navegador-requisicao.mp4
    requisição-postman.png
frontend/
    css/
    img/
    js/
    pages/
models/
    modelo_treinado.pkl
notebooks/
    ...
```

---

## 📦 Instalação

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Execução do Projeto

### Backend (API Flask)
1. Navegue até a pasta `/app`:
   ```bash
   cd app
   ```
2. Execute o arquivo `run.bat` para iniciar a API:
   ```bash
   run.bat
   ```

### Frontend
1. Abra o arquivo `/frontend/pages/home.html` com a extensão **Live Server** no VSCode:
   - Clique com o botão direito no arquivo `home.html`.
   - Selecione **Open with Live Server**.
   - Acesse o projeto pelo navegador através do link gerado pelo Live Server.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do backend e do modelo de machine learning.
- **Flask**: Framework para criação da API.
- **Flask-CORS**: Para habilitar o compartilhamento de recursos entre o frontend e o backend.
- **scikit-learn**: Para treinamento e uso do modelo de machine learning.
- **pandas** e **numpy**: Para manipulação e análise de dados.
- **matplotlib** e **seaborn**: Para visualização de dados.
- **HTML, CSS e JavaScript**: Para o desenvolvimento do frontend.

---

## 📊 Dados e Visualizações

### Bases de Dados
- `base_dados.csv`: Base de dados original.
- `base_dados_limpa.csv`: Base de dados após limpeza.
- `base_dados_ml.csv`: Base de dados preparada para o treinamento do modelo.

### Visualizações
Os gráficos gerados estão disponíveis na pasta `dataviz/`:
- **Interrupção Anual x Causa Direta**: `grafico-interrupcao_anualXcausa_direta.png`
- **Interrupção x Natureza**: `grafico-interrupcaoXnatureza.png`
- **Ocorrências Anuais x Mês**: `grafico-ocorrencias_anuaisXmes.png`
- **Ocorrências x Causa**: `grafico-ocorrenciasXcausa.png`
- **Vítimas x Natureza**: `grafico-vitimasXnatureza.png`

---

## 🌐 API Endpoints

### `/prever` (POST)
- **Descrição**: Recebe os dados do acidente e retorna a previsão de interrupção.
- **Exemplo de Requisição**:
  ```json
  {
    "Causa_Direta": "Colisão",
    "Natureza": "Grave",
    "Hora": 14
  }
  ```
- **Exemplo de Resposta**:
  ```json
  {
    "interrupcao_prevista_h": 2.5
  }
  ```

---

## 🖥️ Frontend

### Páginas
- **Home**: Página inicial com informações sobre o projeto.
- **Predição**: Formulário para envio de dados e exibição do resultado da previsão.

### Scripts
O arquivo `frontend/js/script.js` gerencia a interação com a API, enviando os dados do formulário e exibindo o resultado.

---

## 📑 Requisitos

- Python 3.x
- VSCode com a extensão **Live Server**

---

## 📚 Referências e Recursos Adicionais

- [Abstração dos Dados](documentation/abstracao-dados.pdf)
- [Demonstração de Requisição no Navegador](documentation/navegador-requisicao.mp4)
- [Exemplo de Requisição no Postman](documentation/requisição-postman.png)

---

## 👥 Colaboradores

- João Vinicius Alves - 559369
- Juan Pablo - 560445
- Matheus Mariotto - 560276
