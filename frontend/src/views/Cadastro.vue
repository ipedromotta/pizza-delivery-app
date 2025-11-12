<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const errors = ref('')
const form = ref({
  first_name: '',
  email: '',
  username: '',
  password: '',
  password_confirm: '',
})

async function onSubmit() {
  errors.value = ''

  if (form.value.password !== form.value.password_confirm) {
    errors.value = 'As senhas não são iguais. Tente novamente'
  }

  if (!errors.value.length) {
    await axios.post('/api/v1/users/', form.value)
    .then((res) => {
      router.push('/login')
    })
    .catch((error) => {
      if ( error.response ) {
        for (const property in error.response.data) {
          errors.value += `${error.response.data[property]}\n`
        }

        console.log(JSON.stringify(error.response.data))
      } else if ( error.message ) {
        errors.value = 'Algo deu errado. Por favor tente novamente.'

        console.log(JSON.stringify(error))
      }
    })
  }
}

</script>

<template>
  <div class="text-center body">
    <main class="form-signup">
      <form class="space-between" @submit.prevent="onSubmit">
        <img class="mb-4" src="@/assets/logo.svg" alt="" width="150">
        <h1 class="h3 mb-3 fw-normal">Cadastre-se</h1>

        <div class="form-floating mb-2">
          <input v-model="form.first_name" required type="text" maxlength="15" class="form-control" id="floatingName" placeholder="Seu Nome">
        </div>

        <div class="form-floating mb-2">
          <input v-model="form.email" required type="email" maxlength="50" class="form-control" id="floatingEmail" placeholder="email@exemplo.com">
        </div>

        <div class="form-floating mb-2">
          <input v-model="form.username" required type="text" maxlength="15" class="form-control" id="floatingInput" placeholder="Seu Usuário">
        </div>

        <div class="form-floating mb-2">
          <input v-model="form.password" required type="password" class="form-control" id="floatingPassword" placeholder="Senha">
        </div>

        <div class="form-floating">
          <input v-model="form.password_confirm" required type="password" class="form-control" id="floatingPassword2" placeholder="Confirme sua senha">
        </div>

        <div class="alert alert-danger" role="alert" v-if="errors.length">
          <span v-for="error, index in errors" :key="index">{{ error }}</span>
        </div>

        <button :class="`w-100 btn btn-lg btn-danger ${errors.length?'mt-0': 'mt-5'}`" type="submit">Cadastrar</button>
        
        <div>
          <p class="mt-5">
            Ou <RouterLink to="/login" class="text-danger fw-bold link">clique aqui</RouterLink> para logar
          </p>
        </div>
      </form>
    </main>
  </div>
</template>

<style scoped>
.body {
  display: flex;
  align-items: center;
  margin-top: 10vh;
}

.form-signup {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.link {
  text-decoration: none;
}
.link:hover{
  cursor: pointer;
  color: #aaaaaa!important;
  transition: ease-in 0.2s;
}
</style>