import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import type { Pizza } from '@/types/Pizza'


export const useCarrinhoStore = defineStore('carrinho', () => {
    const pizzasNoCarrinho = ref<Pizza[]>([])

    const valorTotal = computed(() => {
        return pizzasNoCarrinho.value.reduce((total, pizza) => {
            return total + pizza.preco
        }, 0)
    })

    function adicionarPizza(pizza: Pizza) {
        pizzasNoCarrinho.value.push(pizza)
    }

    function removerPizza(index: number) {
        if (index >= -1) {
            pizzasNoCarrinho.value.splice(index, 1)
        }
    }

    function removerTodasPizzas(){
        pizzasNoCarrinho.value = []
    }

    return { pizzasNoCarrinho, adicionarPizza, removerPizza, removerTodasPizzas, valorTotal }
})