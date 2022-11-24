<template>
  <div class="modalDiv">
    <div class="overlay" @click="$emit('close-modal')"></div>
    <div class="modal-card">
      <slot/>

    </div>
  </div>
</template>

<script>
export default {
  name:'ModalView',
  components: {
  }
}
</script>

<style>
.modalDiv{
  display:block;
}
.modal,
.overlay {
  width: 100%;
  height: 100%;
  position: fixed;
}
.overlay {
  opacity: 0.5;
  background-color: black;
}
.modal-card{
  border-radius: 10px;
  min-height: 500px;
  position: relative;
  min-width: 800px;
  margin: 100px 25vw;
  background-color: #5a5a5a;
  z-index:10;
  /* opacity: 3; */
}
</style>