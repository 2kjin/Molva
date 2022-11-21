<template>
  <div>
    <img src="@/assets/f_molva.png" alt="logo" id="Indexlogo" @click="goToHome"/>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'IndexPage',
  components: {
  },
  methods: {
    goToHome() {
      this.$router.push({name: 'home'})
    },
  }
}
</script>
<style>
#Indexlogo{
  width: 60%;
  margin: auto;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>