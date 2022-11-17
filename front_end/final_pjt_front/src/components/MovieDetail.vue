<template>
  <div>
    <h1>Detail</h1>
    <MovieCard/>
    <p>예고편list</p>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: "MovieDetail",
  components: {
    MovieCard,
  },
}
</script>

<style>

</style>