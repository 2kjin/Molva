<template>
  <div>
    <h1>Profile</h1>
    <GenreMovie/>
  </div>
</template>
<script>
// @ is an alias to /src
import GenreMovie from '@/components/GenreMovie'
export default {
  name: 'ProfileView',
  components: {
    GenreMovie
  }
}
</script>
