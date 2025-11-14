<script setup lang="ts">
import { useHeaderStore } from '@/stores/header';
import type { Pizza } from '@/types/Pizza';


const props = defineProps<{
  pizza: Pizza
}>()

const headerStore = useHeaderStore();

</script>

<template>
    <div class="col">
        <div class="card p-3 text-center mb-3">
            <img :src="pizza.imagem" class="img-fluid mb-2" />
            <h5>{{ pizza.nome }}</h5>
            <p>{{ pizza.preco }} R$</p>
            <button
                class="btn btn-danger"
                @click="headerStore.adicionarPizza(pizza)"
            >
                <i class="bi bi-bag-plus-fill"></i>
                Comprar
            </button>
        </div>
    </div>
</template>

