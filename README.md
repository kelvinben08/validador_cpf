# ✅ Validador de CPF (Python)
- Programa em Python que valida CPFs informados pelo usuário.  
- Aceita entradas com ou sem pontuação e realiza validação matemática completa.

---

### 📌 Funcionalidades
- Aceita CPF com ou sem pontuação (ex: `123.456.789-00` ou `12345678900`)
- Sanitiza a entrada removendo `.`, `-` e espaços
- Verifica caracteres permitidos (somente números e separadores)
- Valida se o CPF possui exatamente 11 dígitos
- Rejeita CPFs com todos os dígitos iguais (ex: `11111111111`)
- Validação matemática completa (dígitos verificadores)

---

### 🧠 Conceitos aplicados
- Funções com responsabilidade única
- Sanitização e validação de dados (pipeline)
- Boas práticas (PEP8)
- Docstrings
- Early return para fluxo mais legível

---

### 🚀 Versão
- v1.2:
  - Validação matemática dos dígitos verificadores (10º e 11º)
  - Rejeição de CPFs com todos os dígitos iguais
  - Sanitização com separadores reutilizáveis 
  - Refatoração do main com early return e mensagens claras


- v1.1:
  - Sanitização de CPF (remoção de pontuação)
  - Verificação de caracteres permitidos 
  - Mensagens de erro mais claras


- v1.0:
  - Validação básica de formato (11 dígitos numéricos)
