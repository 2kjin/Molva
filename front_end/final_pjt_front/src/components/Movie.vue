<template>
  <div>
    <div id="head">
      <h1>Movie</h1>
      <nav>
        <div
          @click="isClicked('popular')"
          :class="{ selected: popularClicked }"
        >
          Popular
        </div>
        <div @click="isClicked('recent')" :class="{ selected: recentClicked }">
          Recent
        </div>
      </nav>
    </div>

    <div>
      <movie-popular v-if="popularClicked" />
      <movie-recent v-if="recentClicked" />
    </div>
  </div>
</template>

<script>
import MoviePopular from "./MoviePopular.vue"
import MovieRecent from "./MovieRecent.vue"
export default {
  name: "MovieContent",
  data() {
    return {
      popularClicked: true,
      recentClicked: false,
    }
  },
  components: {
    MoviePopular,
    MovieRecent,
  },
  methods: {
    isClicked(data) {
      if (data === "popular") {
        this.popularClicked = true
        this.recentClicked = false
      } else {
        this.recentClicked = true
        this.popularClicked = false
      }
    },
  },
}
</script>

<style scoped>
.selected {
  border-bottom: 3px solid #e0d598;
}
#head {
  margin: 20px 0;
  padding-right: 70px;
  padding-left: 30px;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
nav {
  display: flex;
}
nav div {
  padding: 5px 0;
  font-size: 20px;
  margin: 0 20px;
  transition: transform 0.2s linear;
}
nav div:hover {
  cursor: pointer;
  transform: scale(1.05);
}
</style>