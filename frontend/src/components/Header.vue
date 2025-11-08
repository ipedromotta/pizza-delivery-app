<script setup>
import { useRouter } from 'vue-router';

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

                <RouterLink to="/login" class="text-dark">
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

</style>