import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useBuscaStore = defineStore('busca', () => {
    const termoBusca = ref('')

    return { termoBusca }
})
