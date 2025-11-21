<script setup lang="ts">
import Menu from '@/components/Menu.vue';
import PizzaItem from '@/components/PizzaItem.vue';
import type { Pizza } from '@/types/Pizza';
import { useBuscaStore } from '@/stores/busca';
import { ref, computed } from 'vue';


const pizzas = ref<Pizza[]>([
    { id: 1, nome: 'Calabresa', preco: 29.9, imagem: 'imagem', promocao: false, vegana: false, doce: false },
    { id: 2, nome: 'Banana Nevada', preco: 39.9, imagem: 'imagem', promocao: false, vegana: false, doce: true },
    { id: 3, nome: 'Portuguesa', preco: 29.9, imagem: 'imagem', promocao: false, vegana: false, doce: false },
    { id: 4, nome: 'Frango Catupiry', preco: 19.9, imagem: 'imagem', promocao: true, vegana: false, doce: false },
    { id: 5, nome: 'Brocollis', preco: 24.95, imagem: 'imagem', promocao: true, vegana: true, doce: false },
])


const buscaStore = useBuscaStore();
const categoriaSelecionada = ref('')

const pizzasExibidas = computed(() => {
    return pizzas.value
        .filter(pizza => {
            if (categoriaSelecionada.value === 'Promoções') return pizza.promocao
            if (categoriaSelecionada.value === 'Doces') return pizza.doce
            if (categoriaSelecionada.value === 'Vegetarianas') return pizza.vegana
            return true
        })
        .filter(pizza =>
            pizza.nome.toLowerCase().includes(buscaStore.termoBusca.toLowerCase())
        )
})

</script>

<template>
    <div class="body">
        <Menu @selecionarCategoria="categoriaSelecionada = $event" />
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
