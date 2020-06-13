import Vue from 'vue';
import Router from 'vue-router';

import LoginView from '../container/LoginView.vue';
import MainView from '../container/MainView.vue';
import UserView from '../container/UserView.vue';
import FollowingFreetView from '../container/FollowingFreetView.vue';

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/login',
            name: 'Log In',
            component: LoginView,
        },
        {
            path: '/login/:signupMode',
            name: 'Log In',
            component: LoginView,
            props: true
        },
        {
            path: '/',
            name: 'Main Page',
            component: MainView
        },
        {
            path: '/user/:username',
            name: 'User Page',
            component: UserView
        },
        {
            path: '/following',
            name: 'Following Freets',
            component: FollowingFreetView
        }
    ]
})