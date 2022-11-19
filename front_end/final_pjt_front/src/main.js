import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import Carousel3d from 'vue-carousel-3d'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Carousel3d)

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
