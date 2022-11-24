<template>
  <div>
    <MovieText :text="'이한빈 같은 영화'"></MovieText>
    <MovieLists :movieList="similar"></MovieLists>
    <!-- {{ similar }} -->
  </div>
</template>

<script>
import { movieApi } from "../utils/axios";
import MovieLists from "../components/MovieLists";
import MovieText from "../components/MovieText";

export default {
  name: 'DetailViewSimilar',
  data() {
    return {
      similar: {},
    }
  },
  components: {
    MovieText,
    MovieLists,
  },
  props: {
    sendId: String 
  },
  async mounted() {
      // vuex를 통해서 로딩을 없애준다.
      // console.log(this.sendId)
      // const { id } = this.$route.params.id;
      const { data } = await movieApi.similar(this.sendId);
      // console.log(data.results);
      this.similar = data.results;
      console.log(this.similar)
  },
}
</script>

<style>

</style>