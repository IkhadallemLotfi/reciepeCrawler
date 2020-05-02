require('./bootstrap');


import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

import GridLoader from 'vue-spinner/src/GridLoader.vue'
Vue.component('grid-loader',GridLoader);

require('vue2-animate/dist/vue2-animate.min.css')

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

window.Vue = require('vue');

import user from './components/user.vue';
import listeRecipes from './components/listeRecipes.vue';


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
