<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ community?.id }}</p>
    <p>제목 : {{ community?.title }}</p>
    <p>내용 : {{ community?.content }}</p>
    <p>작성시간 : {{ community?.created_at }}</p>
    <p>수정시간 : {{ community?.updated_at }}</p>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailPage',
  data() {
    return {
      community: null,
    }
  },
  created() {
    this.getCommunityDetail()
  },
  methods: {
    getCommunityDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/communities/${this.$route.params.id}`
      })
        .then((res) => {
          console.log(res)
          this.community = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
