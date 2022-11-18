<template>
  <div class="col">
    <div class="card border-light border-opacity-50 mb-3 bg-dark text-white img_size">
      <img :src='movieImg(movieProps.poster_path)' class="card-img-top" alt="">
      <div class="card-body">
        <h5 class="card-title txt_title">
        {{ movieProps.title }}
        </h5>
        <p class="card-text txt_post">
        {{ movieProps.overview }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movieProps : Object,
  },
  methods: {
    movieImg(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`
    }
  }
}
</script>

<style>

</style>