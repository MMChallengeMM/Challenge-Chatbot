# Chatbot para o Centro de Controle de Operações (CCO) - CCR

Este repositório contém o projeto de um chatbot desenvolvido para auxiliar o Centro de Controle de Operações (CCO) da CCR no monitoramento e controle de falhas, status de trens e estações. O chatbot foi projetado para facilitar o acesso a informações críticas em tempo real, otimizando as operações e aumentando a eficiência do CCO.

## 📋 Descrição do Projeto

O chatbot responde a consultas frequentes realizadas por operadores e administradores, como falhas ativas, status de trens, manutenções programadas e histórico de incidentes. A solução busca automatizar essas interações para reduzir a sobrecarga de trabalho manual e acelerar a resposta a problemas operacionais.

### Funcionalidades:
- **Consulta de falhas ativas**: Exibe as falhas operacionais em trens e estações.
- **Status de trens**: Permite ao usuário consultar o status atual de um trem específico.
- **Relatórios automáticos**: Gera relatórios de operação diários ou semanais.
- **Manutenções programadas**: Informa as manutenções agendadas para trens ou estações.

## 🧠 Estrutura do Projeto

O projeto foi organizado em diferentes componentes para garantir modularidade e facilidade de manutenção:

- **Intenções**: As diferentes ações ou perguntas que o chatbot é capaz de entender e responder.
- **Entidades**: Informações chave que o chatbot identifica nas interações, como trem, estação e falha.
- **Diagrama de Fluxo de Diálogo**: Representação gráfica do fluxo de interação entre o usuário e o chatbot (veja a imagem `Fluxo-Conversa-Chatbot.drawio.png`).

## 📂 Estrutura do Repositório

```bash
├── .gitignore
├── Challenge-Chatbot-2024.pdf   # Relatório completo do projeto
├── Fluxo-Conversa-Chatbot.drawio.png  # Diagrama de fluxo de conversa do chatbot
└── README.md
