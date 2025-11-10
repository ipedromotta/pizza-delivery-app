/// <reference types="vite/client" />

declare module "*.vue" {
  import type { DefineComponent } from "vue";
  const component: DefineComponent<{}, {}, any>;
  export default component;
}


/*
TypeScript não sabe automaticamente o tipo de arquivos .vue, então ele reclama dizendo que o componente tem tipo any.
Esse arquivo ensina o TypeScript a tratar arquivos .vue corretamente.
*/
