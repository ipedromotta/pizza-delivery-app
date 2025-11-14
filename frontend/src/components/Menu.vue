<script setup lang="ts">
import { ref } from 'vue';

const categorias = [
  'Todas',
  'Promoções',
  'Doces',
  'Vegetarianas'
];

const emit = defineEmits(['selecionarCategoria']);
const categoriaSelecionada = ref('Todas');

function selecionarCategoria(categoria: string) {
  emit('selecionarCategoria', categoria)
  categoriaSelecionada.value = categoria
}


</script>

<template>
    <div class="categoria-menu d-flex align-items-center">
        <button 
            v-for="cat in categorias" 
            :key="cat"
            :class="['categoria-item', categoriaSelecionada === cat ? 'active' : '']"
            @click="selecionarCategoria(cat)"
        >
            {{ cat }}
        </button>
    </div>
</template>

<style scoped>
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
