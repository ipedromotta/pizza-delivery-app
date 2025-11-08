<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const categorias = [
  'Todas',
  'Promoções',
  'Doces',
  'Vegetarianas'
];

const categoriaSelecionada = ref('Todas');

const router = useRouter()


</script>

<template>

    <nav class="navbar navbar-light bg-light shadow-sm py-2">
        <div class="container d-flex align-items-center justify-content-between">

            <!-- LOGO -->
            <RouterLink to="/" class="d-flex align-items-center">
            <img src="@/assets/logo.svg" alt="logo" class="logo">
            </RouterLink>

            <!-- SEARCH (Só aparece no Desktop) -->
            <div class="search-box d-none d-md-flex align-items-center">
            <i class="bi bi-search search-icon"></i>
            <input type="text" class="search-input" placeholder="Pesquisar pizzas, promoções...">
            </div>

            <!-- ICONES -->
            <div class="d-flex align-items-center ms-3 gap-3">
                <RouterLink to="/carrinho" class="text-dark">
                    <i class="bi bi-cart2 icones"></i>
                </RouterLink>

                <RouterLink to="/minha-conta" class="text-dark">
                    <i class="bi bi-person icones"></i>
                </RouterLink>
            </div>

        </div>

        <!-- SEARCH NO MOBILE -->
        <div class="container d-flex d-md-none mt-2">
            <div class="search-box w-100 d-flex align-items-center">
            <i class="bi bi-search search-icon"></i>
            <input type="text" class="search-input" placeholder="Buscar pizzas...">
            </div>
        </div>
    </nav>

    <div class="categoria-menu d-flex align-items-center">
        <button 
            v-for="cat in categorias" 
            :key="cat"
            :class="['categoria-item', categoriaSelecionada === cat ? 'active' : '']"
            @click="categoriaSelecionada = cat"
        >
            {{ cat }}
        </button>
    </div>


</template>


<style scoped>

.logo {
  height: 50px; /* Ajuste fácil */
}

.icones {
  font-size: 1.9rem; /* Aumenta ícones */
  cursor: pointer;
  margin-left: 12px;
}

.search-box {
  background: #fff;
  border-radius: 25px;
  padding: 6px 14px;
  border: 1px solid #ddd;
  max-width: 400px; /* Limita o tamanho */
  width: 100%;
}

.search-input {
  border: none;
  outline: none;
  width: 100%;
  font-size: 1rem;
  margin-left: 8px;
  background: transparent;
}

.search-icon {
  font-size: 1.2rem;
  color: #555;
}

.search-input:focus {
  box-shadow: none;
}

.categoria-menu {
  overflow-x: auto;
  white-space: nowrap;
  border-bottom: 1px solid #eee;
  padding: 0.5rem 1rem;
  background: #fff;
  justify-content: center;
}

.categoria-item {
  background: none;
  border: none;
  padding: 0.6rem 1rem;
  margin-right: 1rem;
  font-size: 1rem;
  color: #555;
  cursor: pointer;
  border-bottom: 2px solid transparent;
}

.categoria-item.active {
  color: #d93025; /* vermelho estilo pizzaria */
  border-bottom-color: #d93025;
  font-weight: 600;
}

/* remove barra de scroll feia no mobile */
.categoria-menu::-webkit-scrollbar {
  display: none;
}



</style>