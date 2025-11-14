<script setup lang="ts">
import Menu from '@/components/Menu.vue';
import PizzaItem from '@/components/PizzaItem.vue';
import type { Pizza } from '@/types/Pizza';
import { ref } from 'vue';

const pizzas = ref<Pizza[]>([
    {
        id: 1,
        nome: 'Calabresa',
        preco: 19.9,
        imagem: 'imagem',
        promocao: false,
        vegana: false,
        doce: false
    },
    {
        id: 2,
        nome: 'Banana Nevada',
        preco: 39.9,
        imagem: 'imagem',
        promocao: false,
        vegana: false,
        doce: true
    }
])

const pizzasExibidas = ref<Pizza[]>(pizzas.value)

function selecionarCategoria(categoria: string) {
    console.log(categoria)
    if (categoria == 'Promoções') {
        pizzasExibidas.value = pizzas.value.filter(pizza => pizza.promocao);
    } else if (categoria == 'Doces') {
        pizzasExibidas.value = pizzas.value.filter(pizza => pizza.doce);
    } else if (categoria == 'Vegetarianas') {
        pizzasExibidas.value = pizzas.value.filter(pizza => pizza.vegana);
    } else {
        pizzasExibidas.value = pizzas.value
    }
}

</script>

<template>
    <div class="body">
        <Menu @selecionarCategoria="selecionarCategoria" />
        <div class="container py-4">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
                <PizzaItem
                    v-for="pizza in pizzasExibidas"
                    :key="pizza.id"
                    :pizza="pizza"
                />
            </div>
        </div>
    </div>
</template>

<style scoped>

</style>
