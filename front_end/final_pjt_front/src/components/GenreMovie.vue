<template>
  <div>
    <h1>Genre</h1>
    {{ genre_lst }}
    <GenreMovieItem
      :genre-list="genre_lst"
    />
  </div>
</template>
<script>
import GenreMovieItem from '@/components/GenreMovieItem'
// @ is an alias to /src

export default {
  name: 'GenreMovie',
  data () {
    return {
      genre_lst: null
    }
  },
  components: {
    GenreMovieItem,
  },
  methods: {
    getGenreMenu() {
      this.$store.dispatch('getGenreMenu')
      this.genre_lst = this.$store.state.genre_menu
    },
  },
  created() {
    this.getGenreMenu()
  },
}
</script>
