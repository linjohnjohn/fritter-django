import Vue from 'vue';
import Vuex from 'vuex';
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(Vuex);

import App from './App.vue'
import router from './router';
import store from './store';

export const eventBus = new Vue();

Vue.config.productionTip = false

Vue.use(VueMaterial)

new Vue({
    render: h => h(App),
    router,
    store,
    created() {
        this.$store.dispatch('loginToken').then(() => {
            this.$store.commit('setErrorMessage', '');
            this.$store.dispatch('fetchAllFreets');
        });
    }
}).$mount('#app')
