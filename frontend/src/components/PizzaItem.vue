<script setup lang="ts">
import { useCarrinhoStore } from '@/stores/carrinho';
import type { Pizza } from '@/types/Pizza';
import { formatarMoeda } from '@/utils/helpers';


const props = defineProps<{
  pizza: Pizza
}>()

const headerStore = useCarrinhoStore();

</script>

<template>
    <div class="col">
        <div class="card p-3 text-center mb-3">
            <img :src="pizza.imagem" class="img-fluid mb-2" />
            <h5>{{ pizza.nome }}</h5>
            <p>{{ formatarMoeda(pizza.preco) }}</p>
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

