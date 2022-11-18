<template>
  <div class="community-list">
    <h3>Community List</h3>
    <CommunityListItem
      v-for="community in communities"
      :key="community.id"
      :community="community"
    />
  </div>
</template>

<script>
import CommunityListItem from '@/components/CommunityListItem'

export default {
  name: 'CommunityList',
  components: {
    CommunityListItem
  },
  computed: {
    communities() {
      return this.$store.state.communities
    }
  }
}
</script>

<style>
.community-list {
  text-align: start;
}
</style>
