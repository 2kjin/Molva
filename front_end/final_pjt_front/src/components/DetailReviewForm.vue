<template>
  <form id="reviewForm">
    <h4 style="display:inline-block; margin-right: 20px;">{{movie.title}}</h4>

    <!-- RATINGS -->
    <span class="star">
      ★★★★★
      <span>★★★★★</span>
      <input type="range" @input="drawStar" value="0" step="1" min="0" max="10">
    </span>
    
    <textarea cols="30" rows="10" placeholder="Write your review !"></textarea>
    
    <input type="submit" value="write" class="review-btn"
    style="padding: 2px 7px; margin: 10px">
  </form>
</template>

<script>
export default {
  name:'DetailReviewForm',
  props:{
    movie:Object
  },
  methods:{
    drawStar(event) {
      document.querySelector('.star span').style.width = `${event.target.value * 15}px`;
      // console.log(document.querySelector('.star input').value)
  }
  }
}
</script>

<style>
#reviewForm{
  margin: 0 auto;
  width: 830px;
  min-width: 500px;
  border-radius: 10px;
  border: 0.5px solid #F8F9FA;
  padding: 20px 40px;
}
textarea{
  color:#F8F9FA;
  width:650px;
  min-width: 300px; 
  max-height:60px; 
  font-size:17px; 
  padding: 10px; 
  margin: 20px;
  margin-right: 30px;
  border:0;
  resize: none;
}
textarea:hover{
  border-bottom: solid 1px #F8F9FA;
}
textarea:focus{
  outline: none;
  caret-color: #F8F9FA;
}
textarea::-webkit-scrollbar {
    width: 10px;
}
textarea::-webkit-scrollbar-corner{
  display:none;
}
textarea::-webkit-scrollbar-thumb {
  background-color:#e0d598;
  border-radius: 10px;
  background-clip: padding-box;
  border: 2px solid transparent;
  box-shadow: inset 0 0 2px #c3ddecc5;
}
.star {
    position: relative;
    font-size: 30px;
    color: #ddd;
  }
  
.star input {
  width: 160px;
  height: 100%;
  padding: 15px 0;
  position: absolute;
  top: 0.5px;
  left: 0;
  cursor: pointer;
  opacity: 0;
}
.star span {
  width: 0;
  position: absolute; 
  left: 7px;
  color: rgb(255, 188, 4);
  overflow: hidden;
  pointer-events: none;
}
.review-btn,
.form-btn{
  border: 1px solid #F8F9FA; 
  transition: transform 0.3;
  border-radius: 10px; 
}
.review-btn:hover,
.form-btn:hover{
  cursor: pointer;
  transform: scale(1.05);
}
.review-btn:active,
.form-btn:active{
  transform: translateY(4px);
}
.form-btn{
  padding: 7px; 
  font-size: 13px; 
  display:inline-block;
}
</style>