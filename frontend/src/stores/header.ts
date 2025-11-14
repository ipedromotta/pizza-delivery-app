import { ref } from 'vue'
import { defineStore } from 'pinia'
import type { Pizza } from '@/types/Pizza'


export const useHeaderStore = defineStore('header', () => {
    const pizzasNoCarrinho = ref<Pizza[]>([])

    function adicionarPizza(pizza: Pizza) {
        pizzasNoCarrinho.value.push(pizza)
    }

    return { pizzasNoCarrinho, adicionarPizza }
})