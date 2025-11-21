# 🖥️ Execução Local

Siga os passos abaixo para rodar o frontend em sua máquina:

## 1. Instalar Dependências

No diretório `frontend`, execute:

```sh
npm install
```

## 2. Iniciar a Aplicação

### ▶️ Ambiente de Desenvolvimento (Hot Reload)

```sh
npm run dev
```

A aplicação estará acessível em:
**[http://localhost:5173/](http://localhost:5173/)**

### 📦 Build para Produção

```sh
npm run build
```

Este comando realiza:

* Checagem de tipos (via `vue-tsc`)
* Compilação e minificação para produção

---

# 🧪 Testes, Lint e Outras Rotinas

## 🔍 Testes Unitários com Vitest

```sh
npm run test:unit
```

## 🧼 Lint com ESLint

```sh
npm run lint
```

---

# 📁 Resumo dos Comandos Principais

| Ação                     | Comando             |
| ------------------------ | ------------------- |
| Instalar dependências    | `npm install`       |
| Rodar em desenvolvimento | `npm run dev`       |
| Build de produção        | `npm run build`     |
| Testes unitários         | `npm run test:unit` |
| Lint                     | `npm run lint`      |

---
