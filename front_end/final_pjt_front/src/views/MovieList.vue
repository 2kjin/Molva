<template>
  <div>
    <h1>MovieList</h1>
    <MovieCard/>
  </div>
</template>
<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
  },
}
</script>
