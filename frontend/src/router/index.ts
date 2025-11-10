import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Carrinho from '@/views/Carrinho.vue'
import EsqueceuSenha from '@/views/EsqueceuSenha.vue'
import Cadastro from '@/views/Cadastro.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      alias: '/inicio',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        isLogin: true
      }
    },
    {
      path: '/esqueceu-senha',
      name: 'esqueceu-senha',
      component: EsqueceuSenha,
      meta: {
        isLogin: true
      }
    },
    {
      path: '/cadastrar',
      name: 'cadastrar',
      component: Cadastro,
      meta: {
        isLogin: true
      }
    },
    {
      path: '/carrinho',
      alias: '/carrinho',
      name: 'carrinho',
      component: Carrinho,
      meta: {
        requireLogin: true
      }
    },
  ],
})

export default router
