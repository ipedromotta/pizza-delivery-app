import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Carrinho from '@/views/Carrinho.vue'
import Cadastro from '@/views/Cadastro.vue'
import { useAuthStore } from '@/stores/auth'
import EsqueceuSenha from '@/views/EsqueceuSenha.vue'
import MinhaConta from '@/views/MinhaConta.vue'


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
      path: '/minha-conta',
      name: 'minha-conta',
      component: MinhaConta,
      meta: {
        requireLogin: true
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

router.beforeEach((to, from, next) => {
  const pageStore = useAuthStore()

  if (to.matched.some(record => record.meta.requireLogin) && !pageStore.isAuthenticated) {
    next({ name: 'login', query: { to: to.path }})
  } else if (to.matched.some(record => record.meta.isLogin) && pageStore.isAuthenticated) {
    next({ name: 'home', query: { to: to.path }})
  } else {
    next()
  }
})

export default router
