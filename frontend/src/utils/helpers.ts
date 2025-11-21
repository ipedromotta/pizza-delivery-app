export function formatarMoeda(valor: number) {
  // Intl.NumberFormat foi utilizado pois é mais performático, mais padronizado e evita comportamentos diferentes
  return new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  }).format(valor)
}
