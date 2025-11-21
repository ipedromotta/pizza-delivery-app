<script setup>
import { useCarrinhoStore } from '@/stores/carrinho';
import { formatarMoeda } from '@/utils/helpers';


const carrinhoStore = useCarrinhoStore();

</script>

<template>
  <div class="container py-5 d-flex justify-content-center">
    <div class="carrinho-box">

      <!-- SE O CARRINHO ESTIVER VAZIO -->
      <div v-if="carrinhoStore.pizzasNoCarrinho.length === 0" class="carrinho-vazio">
        <i class="bi bi-bag-x fs-1"></i>
        <p class="mt-3 fs-4 text-muted">Seu carrinho está vazio 😢</p>
      </div>

      <!-- SE TIVER ITENS -->
      <div v-else>
        <h3 class="mb-4 text-center">Seu Pedido</h3>

        <div class="lista-itens">
          <div
            class="item"
            v-for="(pizza, index) in carrinhoStore.pizzasNoCarrinho"
            :key="index"
          >
            <div>
              <strong>{{ pizza.nome }}</strong>
              <p class="preco">{{ formatarMoeda(pizza.preco) }}</p>
            </div>

            <button
              class="btn btn-sm btn-outline-danger"
              @click="carrinhoStore.removerPizza(index)"
            >
              remover
            </button>
          </div>
        </div>

        <hr />

        <div class="total">
          <strong>Total:</strong>
          <span>{{ formatarMoeda(carrinhoStore.valorTotal) }}</span>
        </div>

        <div class="mt-4 d-flex gap-3 justify-content-center">
          <button class="btn btn-danger">Finalizar Pedido</button>
          <button class="btn btn-dark" @click="carrinhoStore.removerTodasPizzas">
            Limpar Carrinho
          </button>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.carrinho-box {
  background: #fff;
  padding: 30px;
  width: 450px;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.lista-itens {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 15px;
  border-radius: 10px;
  background: #f7f7f7;
}

.total {
  font-size: 1.3rem;
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
}

.carrinho-vazio {
  text-align: center;
  padding: 40px 0;
}
</style>