<script setup>

defineProps({
  nome: String,
  preco: Number,
  imagem: String
}) 
</script>

<template>
    <div class="col">
        <div class="card p-3 text-center mb-3">
            <img :src="imagem" class="img-fluid mb-2" />
            <h5>{{ nome }}</h5>
            <p>{{ preco }} R$</p>
            <button class="btn btn-danger">
                <i class="bi bi-bag-plus-fill"></i>
                Comprar
            </button>
        </div>
    </div>
</template>

