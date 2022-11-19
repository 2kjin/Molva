<template>
  <div>
    <div v-for="review in reviews" :key="review.id" style="padding-left: 10px;">
      {{review?.username}} | 
      <v-rating
      style="display:inline-block; margin-bottom: 5px;"
      class="rating"
      background-color="amber"
      :value="review.vote"
      color="amber"
      dense
      half-increments
      readonly
      size="15"
    ></v-rating>
    <span style="margin-left: 10px; font-size: 12px;">[ {{review.vote}} / 5 ]</span>
    <div>{{review?.content}}</div>
    <hr>
    </div>
  </div>
</template>

<script>
export default {
  name:'DetailReviewList',
  props:{
    reviews:Array
  },
}
</script>

<style>

</style>