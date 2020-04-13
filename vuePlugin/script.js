import Vue from './node_modules.vue/dist/vue'
import VuePlugin from './VueMathPlugin.js'


Vue.use(VuePlugin)


new Vue({
    el:'#app',
    data:{
        item:20
    }
})
