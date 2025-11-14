<script setup>
import Menu from '@/components/Menu.vue';
import PizzaItem from '@/components/PizzaItem.vue';
import { ref } from 'vue';

const pizzas = ref([
    {
        id: 1,
        nome: 'Calabresa',
        preco: '19.90',
        imagem: 'imagem',
        promocao: false,
        vegana: false,
        doce: false
    },
    {
        id: 2,
        nome: 'Banana Nevada',
        preco: '39.90',
        imagem: 'imagem',
        promocao: false,
        vegana: false,
        doce: true
    }
])


</script>

<template>
    <div class="body">
        <Menu />
        <div class="container py-4">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-4">
                <PizzaItem
                    v-for="pizza in pizzas"
                    :key="pizza.id"
                    :nome="pizza.nome"
                    :preco="pizza.preco"
                    :imagem="pizza.imagem"
                />
            </div>
        </div>
    </div>
</template>

<style scoped>

</style>
