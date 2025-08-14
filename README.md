# 📦 Sistema de Gestão de Estoque

> De um exercício simples de SQL a um mini-sistema completo — e a importância do planejamento desde o início.

## 💡 Contexto

O projeto começou como um exercício para praticar operações básicas de CRUD em banco de dados, mas acabou evoluindo para um **mini-sistema de gestão de estoque** com interface gráfica e funcionalidades adicionais.

---

## 🛠 Funcionalidades

- 📝 **CRUD de produtos** — cadastro, edição, exclusão e consulta individual  
- 📦 **Controle de estoque** — entrada e saída de produtos  
- 📥 **Importação via CSV** — carga rápida de dados  
- 📋 **Sistema de logs versionado** — histórico detalhado de alterações no estoque

---

## ⚙️ Arquitetura do Projeto

- 🧩 **Classe `GerenciarEstoque`**  
  - Manipulação direta de SQL  
  - Registro e versionamento de logs  
- 🔗 **Módulo `Application`**  
  - Atua como “API interna”  
  - Recebe inputs e organiza a lógica de execução  
- 🖥 **Interface Gráfica**  
  - Desenvolvida em **Tkinter/CustomTkinter**  
  - Primeiro contato com a biblioteca, trazendo desafios de layout e usabilidade

---

## 🚩 Aprendizado

Começar sem planejamento resultou em código difícil de manter à medida que novas funcionalidades surgiam, exigindo adaptações pouco elegantes.  
A principal lição: **arquitetura e boas práticas devem estar presentes desde o início, mesmo em pequenos projetos**.
