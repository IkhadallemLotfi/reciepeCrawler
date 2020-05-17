require('./bootstrap');


import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import GridLoader from 'vue-spinner/src/GridLoader.vue'
Vue.component('grid-loader',GridLoader);

require('vue2-animate/dist/vue2-animate.min.css')

import { VLazyImagePlugin } from "v-lazy-image";
Vue.use(VLazyImagePlugin);


import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

window.Vue = require('vue');

import user from './components/user.vue';
import listeRecipes from './components/listeRecipes.vue';
import foot from './components/footer.vue';



const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'listeRecipes',
            component: listeRecipes,
        },
    ]
});

const app = new Vue({
    el: '#app',
    components : {
        user,
    },
    router
});


const footcompo = new Vue({
    el: '#footer',
    components : {
        foot,
    },
    router
});