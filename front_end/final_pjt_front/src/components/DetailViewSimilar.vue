<template lang="pug">
  .container

    .slide-button(
      @click="right"
      class="slide-button--right"
    )
      i(class="fa fa-chevron-right fa-2x" aria-hidden="true" )
    .slide-button(
      @click="left"
      class="slide-button--left"
      v-if="infinityLoop"
    )
      i(class="fa fa-chevron-left fa-2x" aria-hidden="true")

    .showcase(
      ref="showcase"
      v-on:mouseout="hideShowcase"
      :class="{expand:expandShowcase}"
      )

    .slider-wrapper(ref="wrapper")
      transition-group(tag="div" class="slider" name="list")
        .slide-container(
          v-for="(container,slideContainerIndex) in slideContainer"
          :key="container"
          :class="[slideContainerIndex%3 === 1 ? 'middle' : '']"
          v-on:transitionend="containerTransition"
          )
          .slide(
            v-for="(content ,contentIndex) in contentContainer[container]"
            ref="slides"
            v-mouse:mouseover="{position: slideContainerIndex % 3,handler:selectSlide}"
            v-mouse:mouseout="{position: slideContainerIndex % 3,handler:unselectSlide}"
            :id="'slide-'+container+'-'+contentIndex"
            :data-container-index="slideContainerIndex"
            :data-content-index="contentIndex"
          )
            .slider-movie-backdrop_path
              img(
                :src="imgFnc(`${content.backdrop_path}`)"
                @click="goDetail(`${content.movie_id}`)"
              )
            .slider-movie-box
              div
              .slider-movie-title
                h6 {{ content.title }}

</template>


<script>
import _ from 'lodash';
import { movieApi } from "../utils/axios";
// import MovieLists from "../components/MovieLists";
// import MovieText from "../components/MovieText";

export default {
  name: 'DetailViewSimilar',
  directives: {
    mouse: {
      bind(el, binding) {
        if (binding.value.position === 1) {
          el.addEventListener(binding.arg, binding.value.handler);
        }
      },
      update(el, binding) {
        if (binding.value.position === 1) {
          el.addEventListener(binding.arg, binding.value.handler);
        } else {
          el.removeEventListener(binding.arg, binding.value.handler);
        }
      },
    },
  },
  props: {
    ottMovie : Array,
    sendId: String,
  },  
 data() {
    return {
      bodyMarginLeft: document.body.getBoundingClientRect().left,
      expandShowcase: false,
      timeoutID: '',
      ratio: 1.6,
      selectedSlidePos: {},
      isSliding: false,
      slideContainer: [-1, 0, 1],
      contentContainer: [],
      contentContainerSize: 6,
      infinityLoop: false,
      similar: {},
    };
  },
  methods: {
    imgFnc(img) {
      return `https://image.tmdb.org/t/p/w300/${img}`
    },
    left: _.debounce(function slideLeft() {
      if (!this.expandShowcase) {
        this.isSliding = true;
        // Infinity loop
        if (this.slideContainer[0] === 0) {
          const page = this.contentContainer.length - 1;
          this.slideContainer.unshift(page);
        } else {
          this.slideContainer.unshift(this.slideContainer[0] - 1);
        }
        this.slideContainer.pop();
      }
    }, 500),
    right: _.debounce(function slideRight() {
      if (!this.expandShowcase && _.last(this.slideContainer) < this.contentContainer.length) {
        this.isSliding = true;
        this.infinityLoop = true;
        // Infinity loop
        if (_.last(this.slideContainer) === this.contentContainer.length - 1) {
          const page = (this.contentContainer.length - _.last(this.slideContainer)) - 1;
          this.slideContainer.push(page);
        } else {
          this.slideContainer.push(_.last(this.slideContainer) + 1);
        }
        this.slideContainer.shift();
      }
    }, 500),
    selectSlide(event) {
      this.timeoutID = setTimeout(() => {
        if (!this.isSliding && !this.expandShowcase) {
          const selectedSlide = event.target;
          this.selectedSlidePos = this.slideIsFirstOrLast(selectedSlide);
          const transitionDistance = this.transitionDistance(selectedSlide);
          const selectedContainer = this.containerIndex(selectedSlide);
          this.popShowcase(selectedSlide);
          const animationCallback = (currentSlide) => {
            if (currentSlide !== selectedSlide) {
              const currentContainer = this.containerIndex(currentSlide);
              let direction = 0;
              if (this.selectedSlidePos.isFirst) {
                if (currentContainer >= 1) {
                  direction = 1;
                }
              } else if (this.selectedSlidePos.isLast) {
                if (currentContainer <= 1) {
                  direction = -1;
                }
              } else if (currentContainer === selectedContainer) {
                direction =
                this.contentIndex(currentSlide) < this.contentIndex(selectedSlide) ? 1 : -1;
              } else {
                direction = currentContainer < 1 ? 1 : -1;
              }
              this.setStyleProperty(currentSlide, { transform: `translateX(${transitionDistance * direction}px)` });
            }
          };
          this.animateSlideTransition(animationCallback);
        }
      }, 500);
    },
    unselectSlide() {
      clearTimeout(this.timeoutID);
    },
    containerIndex(element) {
      return element.dataset.containerIndex * 1;
    },
    contentIndex(element) {
      return element.dataset.contentIndex * 1;
    },
    slideIsFirstOrLast(element) {
      return {
        isFirst: this.slideIsFirst(element),
        isLast: this.slideIsLast(element),
      };
    },
    slideIsFirst(element) {
      return this.contentIndex(element) === 0;
    },
    slideIsLast(element) {
      const containerIndex = this.containerIndex(element);
      return this.contentIndex(element) === this.contentContainer[containerIndex].length - 1;
    },
    transitionDistance(element) {
      if (this.selectedSlidePos.isFirst || this.selectedSlidePos.isLast) {
        return element.clientWidth * (this.ratio - 1);
      }
      return element.clientWidth * ((this.ratio - 1) / -2);
    },
    animateSlideTransition(callback) {
      this.$refs.slides.forEach((slide) => {
        callback(slide);
      });
    },
    containerTransition() {
      // Triggered by 'transitionend' event from slider container
      this.isSliding = false;
    },
    popShowcase(selectedSlide) {
      const selectedRect = selectedSlide.getBoundingClientRect();
      const showcaseWidth = selectedRect.left - this.bodyMarginLeft;
      const showcaseStyle = {
        left: `${showcaseWidth}px`,
        width: `${selectedRect.width}px`,
        height: `${selectedRect.height}px`,
        'background-color': `${selectedSlide.style.backgroundColor}`,
      };
      let transformOrigin = 'center center';
      if (this.selectedSlidePos.isFirst) {
        transformOrigin = 'center left';
      } else if (this.selectedSlidePos.isLast) {
        transformOrigin = 'center right';
      }
      Object.assign(showcaseStyle, { 'transform-origin': transformOrigin });
      this.setStyleProperty(this.$refs.showcase, showcaseStyle);
      this.expandShowcase = true;
    },
    hideShowcase(event) {
      if (event.currentTarget.classList.contains('expand')) {
        this.expandShowcase = false;
        this.animateSlideTransition((currentSlide) => {
          this.setStyleProperty(currentSlide, { transform: '' });
        });
      }
    },
    resetContentContainer() {
      this.setContentContainer();
    },
    setContentContainer() {
      if (window.matchMedia('(max-width: 480px)').matches) {
        this.contentContainerSize = 2;
      } else if (window.matchMedia('(max-width: 768px)').matches) {
        this.contentContainerSize = 3;
      } else if (window.matchMedia('(max-width:1024px)').matches) {
        this.contentContainerSize = 4;
      } else {
        this.contentContainerSize = 6;
      }
      this.contentContainer = _.chunk(this.similar, this.contentContainerSize);
    },
    setStyleProperty(element, styles) {
      Object.assign(element.style, styles);
    },
    goDetail(id){
      this.$router.push(`${id}`);
    },
  },
  async mounted() {
    // vuex를 통해서 로딩을 없애준다.
    // console.log(this.sendId)
    // const { id } = this.$route.params.id;
    const { data } = await movieApi.similar(this.sendId);
    // console.log(data.results);
    this.similar = data.results;
    console.log(this.similar)
    console.logG(111111111111111111111111111111111)
    this.$el.style.setProperty('--ratio', `${this.ratio}`);
    window.addEventListener('resize', _.debounce(this.resetContentContainer, 150));
  },
  destroyed() {
    window.removeEventListener('resize', _.debounce(this.resetContentContainer, 150));
  },
  created() {
    this.setContentContainer();
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

$button-width: 5vw;
$slider-container-width:90vw;
$slider-width: $slider-container-width *3;
/* Medium Devices, Desktops */
@mixin md-screen {
  @media only screen and (max-width : 1024px) {
    @content;
  }
}
/* Small Devices, Tablets */
@mixin sm-screen {
  @media only screen and (max-width : 768px) {
    @content;
  }
}
/* Extra small devices */
@mixin xs-screen {
  @media only screen and (max-width : 480px) {
    @content;
  }
}

@function slide-width($numOfSlides) {
  @return $slider-container-width / $numOfSlides;
}

@function slide-height($width) {
  @return $width * 0.6;
}

.container {
  --duration: 0.4s;
  --cubic-bezier: cubic-bezier( 0.5 , 0, 0.1 ,1);
  position: relative;
}
.container * {
  box-sizing: border-box;
}

/* Slider buttoms */
.slide-button {
  width: $button-width;
  height: slide-height(slide-width(6));
  background-color: black;
  opacity: 0.6;
  position: absolute;
  z-index: 10;
}
.slide-button > .fa {
  color:grey;
  position: absolute;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
}
.slide-button.slide-button--left {
  left: 0;
}
.slide-button.slide-button--right {
  right: 0;
}

/* Showcase */
.showcase {
  position: absolute;
  visibility: hidden;
  transition: transform var(--duration) var(--cubic-bezier),visibility 0s calc(var(--duration));
  will-change: transform, visibility;
  z-index: 10;
}
.showcase.expand {
  transform: scale( var(--ratio) , var(--ratio));
  visibility: visible;
  transition: transform var(--duration) var(--cubic-bezier) ;
}

/* Slider */

.slider-movie-box {
  color: #fff;
  position: absolute; left: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  width: 100%;
  padding: 11px;
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.35s ease-in-out;
}
.slider-movie-box:hover {
  opacity: 1;
}
.slider-movie-title {
  font-size: 24px;
  // padding-bottom: 0.4em;
  overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
  justify-content: center;
  text-align: center;
  
}

.slider-movie-backdrop_path {
    width: 100%;
    vertical-align: middle;
    border-radius: 10px;
    border:none;

    box-shadow: 0 10px 15px 0 #000000;
}
.slider-wrapper {
  overflow: hidden;
}
.slider {
  display: flex;
  width: $slider-width;
  transform: translateX(-($slider-container-width - $button-width));
}
.slide-container {
  display: flex;
  flex: 0 0 $slider-container-width;
  will-change: transform;
}
.slide-container.middle {
  z-index: 1;
}
.slide {
  width:slide-width(6);
  height: slide-height(slide-width(6));
  transition: transform var(--duration) var(--cubic-bezier);
  will-change: transform;
  // box-sizing: border-box;
}

/* Slider Transition*/
.list-enter,
.list-leave-to {
  opacity: 0;
}
.list-leave-active{
  display: none;
  position: absolute;
}
.list-move {
  transition: all 1s;
}
/* Responsilbe Web */
@include md-screen {
  .slide {
    width:slide-width(4);
    height: slide-height(slide-width(4));
  }
  .slide-button {
    height:slide-height(slide-width(4));
  }
}
@include sm-screen {
  .slide {
    width:slide-width(3);
    height: slide-height(slide-width(3));
  }
  .slide-button {
    height:slide-height(slide-width(3));
  }
}
@include xs-screen {
  .slide {
    width:slide-width(2);
    height: slide-height(slide-width(2));
  }
  .slide-button {
    height:slide-height(slide-width(2));
  }
}
</style>