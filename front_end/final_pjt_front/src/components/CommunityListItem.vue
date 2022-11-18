<template>
  <div>
    <h5>{{ community.id }}</h5>
    <p>작성자 : {{ community.username }}</p>
    <p>{{ community.title }}</p>
    <router-link :to="{ name: 'DetailPage', params: { id: community.id } }">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommunityListItem',
  props: {
    community: Object,
  }
}
</script>

<style>

</style>
