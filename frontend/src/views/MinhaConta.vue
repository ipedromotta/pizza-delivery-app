<template>
    <div class="container text-center mx-auto mt-5">
        <h1>Detalhes da conta</h1> 

        <form class="row g-3 w-50 mx-auto mt-3">
            <div class="col-md-6">
                <label for="inputName" class="form-label">Nome</label>
                <input v-model="usernameSets.name" type="text" max="15" class="form-control" :disabled="disableForm" id="inputName" placeholder="Seu nome">
            </div>
            <div class="col-md-6">
                <label for="inputUser" class="form-label">Usuario</label>
                <input v-model="usernameSets.username" type="text" max="15" class="form-control" id="inputUser" :disabled="disableForm" placeholder="Seu usuario">
            </div>
            <div class="col-12">
                <label for="inputEmail" class="form-label">Email</label>
                <input v-model="usernameSets.email" :disabled="disableForm" type="email" class="form-control" id="inputEmail" placeholder="seuemail@exemplo.com">
            </div>

            <div class="col-12 mt-3" v-if="disableForm">
                <button @click="enableForm" type="button" class="btn btn-dark">Alterar dados</button>
            </div>
            <div class="col-12 mt-3" v-else>
                <div class="btn-group" role="group">
                <button @click="enableForm" type="button" class="btn btn-secondary">Cancelar</button>
                <button type="button" class="btn btn-dark" @click="validateForm">Salvar Alterações</button>
                </div>
            </div>

            <div v-if="errors.length" class="alert alert-danger col-12 mt-3" role="alert">
                {{ errors }}
            </div>
            <div v-if="success.length" class="alert alert-success col-12 mt-3" role="alert">
                {{ success }}
            </div>
        </form>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { Modal } from 'bootstrap'

const authStore = useAuthStore()
const router = useRouter()

const disableForm = ref(true)
const success = ref('')
const errors = ref('')

const deletePassword = ref({ current_password: '' })
const usernameSets = ref({ username: '', email: '', name: '', current_password: '' })
const passwordSets = ref({ new_password: '', re_new_password: '', current_password: '' })

// MODAL REFS
const changeModalRef = ref(null)
const deleteModalRef = ref(null)
const passwordModalRef = ref(null)

function enableForm() {
  disableForm.value = !disableForm.value
  setForm()
}

function setForm() {
  usernameSets.value.username = authStore.user.username
  usernameSets.value.email = authStore.user.email
  usernameSets.value.name = authStore.user.name
  usernameSets.value.current_password = ''
}

function validateForm() {
  if (!usernameSets.value.username || !usernameSets.value.name || !usernameSets.value.email) {
    errors.value = "Preencha todos os campos"
    setTimeout(() => (errors.value = ''), 2500)
    return
  }

  const modal = new Modal(changeModalRef.value)
  modal.show()
}

function updateUser() {
  if (!usernameSets.value.current_password) {
    errors.value = 'Coloque sua senha'
    return
  }

  axios
    .post(`/api/v1/update/`, usernameSets.value)
    .then((res) => {
      if (res.data.status === 200) {
        const modal = Modal.getInstance(changeModalRef.value)
        if (modal) modal.hide()

        success.value = res.data.response
        authStore.initializeStore()
        usernameSets.value.current_password = ''
      } else {
        errors.value = res.data.response
      }
    })
    .catch(() => {
      errors.value = "Algo deu errado!"
    })

  setTimeout(() => {
    errors.value = ''
    success.value = ''
  }, 2500)

  disableForm.value = true
}

function updatePassword() {
  if (passwordSets.value.new_password !== passwordSets.value.re_new_password) {
    errors.value = 'Senhas não correspondem'
    return
  }
  if (!passwordSets.value.new_password || !passwordSets.value.re_new_password || !passwordSets.value.current_password) {
    errors.value = 'Preencha todos os campos'
    return
  }

  axios
    .post('/api/v1/users/set_password/', passwordSets.value)
    .then(() => {
      const modal = Modal.getInstance(passwordModalRef.value)
      if (modal) modal.hide()

      success.value = 'Senha alterada com sucesso'
      setTimeout(() => (success.value = ''), 2500)
    })
    .catch((error) => {
      if (error.response) {
        for (const property in error.response.data) {
          errors.value = `${error.response.data[property]}`
        }
      } else {
        errors.value = 'Algo deu errado. Por favor tente novamente'
      }
    })
}

function deleteUser() {
  if (!deletePassword.value.current_password.length) {
    errors.value = 'Digite sua senha'
    return
  }

  axios
    .delete('/api/v1/users/me/', { data: deletePassword.value })
    .then(() => {
      const modal = Modal.getInstance(deleteModalRef.value)
      if (modal) modal.hide()
      router.go()
    })
    .catch((error) => {
      if (error.response) {
        for (const property in error.response.data) {
          errors.value = `${error.response.data[property]}`
        }
      } else {
        errors.value = 'Algo deu errado. Tente novamente'
      }
    })
}

function setDeleteForm() {
  errors.value = ''
  deletePassword.value.current_password = ''
}

function setPasswordForm() {
  passwordSets.value = { new_password: '', re_new_password: '', current_password: '' }
  errors.value = ''
}

onMounted(() => {
  setForm()
})
</script>
