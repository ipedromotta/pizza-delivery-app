import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useAuthStore = defineStore('auth', () => {
  const isAuthenticated = ref(false)
  const token = ref<string>('')
  const user = ref({
    name: '',
    email: '',
    username: '',
    cart: [],
  })

  const router = useRouter()

  function initializeStore() {
    if (localStorage.getItem('token')) {
      token.value = localStorage.getItem('token') || ''

      axios.defaults.headers.common["Authorization"] = `Token ${token.value}`

      axios.get('/api/v1/users/me/')
        .then((res) => {
          user.value.name = res.data.first_name
          user.value.username = res.data.username
          user.value.email = res.data.email
        })
        .catch((err) => {
          router.push('/login')
          removeToken()
          localStorage.removeItem('token')
        })
      setToken(token.value)
    } else {
      removeToken()
    }
  }

  function setToken(tokenValue: string | '') {
    token.value = tokenValue
    isAuthenticated.value = true
  }

  function removeToken() {
    token.value = ''
    isAuthenticated.value = false
  }

  return { user, initializeStore, isAuthenticated, setToken, removeToken }
})