<script setup>
// import axios from 'axios';
import { ref } from 'vue';


const errors = ref('')
const success = ref('')
const form = ref({
  email: ''
})

function onSubmit() {
  errors.value = ''
  success.value = ''
//   axios.post('/api/v1/users/reset_password/', form.value)
//     .then((res) => {
//       if (res.status === 204) {
//         errors.value = 'Não existe conta com esse email'
//       }
//       // Um e-mail com um código de verificação acaba de ser enviado para email@exemplo.com
//     })
//     .catch((error) => {
//       if ( error.response ) {
//         for (const property in error.response.data) {
//           // errors.value += `${error.response.data[property]}\n`
//         }

//       } else if ( error.message ) {
//         errors.value = 'Algo deu errado. Por favor tente novamente.'

//         console.log(JSON.stringify(error))
//       }
//     })
}

</script>

<template>
  <div class="text-center body">
    <form @submit.prevent="onSubmit" class="form-password">
      <img class="mb-4" src="@/assets/logo.svg" alt="" width="150">
      <h1 class="h3 mb-3 fw-normal">Recuperação de conta</h1>
      <p>Digite o endereço de e-mail verificado da sua conta de usuário e nós lhe enviaremos um link de redefinição de senha</p>
      <div class="form-floating mb-2">
        <input @input="errors=''" v-model="form.email" required type="email" maxlength="50" class="form-control" id="floatingEmail" placeholder="email@exemplo.com">
        <label for="floatingEmail">Email</label>
      </div>
      
      <div class="alert alert-danger" role="alert" v-if="errors.length">
        <span v-for="error, index in errors" :key="index">{{ error }}</span>
      </div>

      <div class="alert alert-success" role="alert" v-if="success.length">
        <span v-for="msg, index in success" :key="index">{{ msg }}</span>
      </div>

      <button :class="`w-100 btn btn-lg btn-danger ${errors.length || success.length ?'mt-0': 'mt-5'}`" type="submit">Enviar email de redefinição de senha</button>

      <p class="mt-5">
        Ou <RouterLink to="/login" class="text-danger fw-bold link">clique aqui</RouterLink> para logar
      </p>
    </form>
  </div>
</template>

<style scoped>
.body {
  display: flex;
  align-items: center;
  margin-top: 10vh;
}
.form-password {
  width: 100%;
  max-width: 400px;
  padding: 15px;
  margin: auto;
}
</style>