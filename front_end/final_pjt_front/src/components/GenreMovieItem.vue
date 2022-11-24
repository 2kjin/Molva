<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'GenreMovieItem',
  props: {
    genreList : Array,
  },
  methods: {
    getGenreMovie() {
      this.$store.dispatch('getGenreMovie')
      this.genre_lst = this.$store.state.genre_menu
    },
  },
  created() {
    this.getGenreMovie()
  },
}
</script>

<style>

</style>