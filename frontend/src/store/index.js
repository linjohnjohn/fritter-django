import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

import router from '../router';

const axiosInstance = axios;
let errorTimer;
Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        userId: '',
        username: '',
        following: {},
        allFreets: [],
        followingFreets: [],
        errorMessage: ''
    },
    getters: {
        userId(state) {
            return state.userId;
        },
        username(state) {
            return state.username;
        },
        allFreets(state) {
            return state.allFreets;
        },
        followingFreets(state) {
            return state.allFreets.filter(f => f.owner in state.following)
        },
        errorMessage(state) {
            return state.errorMessage; 
        },
        following(state) {
            return state.following;
        }
    },
    mutations: {
        setUserId(state, userId) {
            state.userId = userId;
            router.push({ name: 'Main Page' })
        },
        setUsername(state, username) {
            state.username = username;
        },
        setToken(state, token) {
            state.token = token;
            if (token) {
                localStorage.setItem('token', token);
                axios.defaults.headers.common['Authorization'] = `Token ${token}`;
            } else {
                localStorage.removeItem('token');
                delete axios.defaults.headers.common['Authorization'];
            }
        },
        clearUserDetail(state) {
            state.userId = '';
            state.username = '';
        },
        setFollowing(state, profile) {
            const { following } = profile;
            const followingUsernameMap = following.reduce((prev, u) => {
                prev[u.username] = true;
                return prev;
            }, {})
            state.following = followingUsernameMap;
        },
        addFreet(state, freet) {
            const freets = [...state.allFreets];
            freets.push(freet);
            state.allFreets = freets;
        },
        updateFreet(state, freet) {
            const freets = [...state.allFreets];
            const i = freets.findIndex(f => f.id === freet.id);
            if (i !== -1) {
                freets[i] = freet;
            }
            state.allFreets = freets;
        },
        removeFreet(state, id) {
            const freets = [...state.allFreets];
            const i = freets.findIndex(f => f.id === id);
            freets.splice(i, 1);
            state.allFreets = freets;
        },
        setAllFreets(state, freets) {
            state.allFreets = freets;
        },
        setFollowingFreets(state, freets) {
            state.followingFreets = freets;
        },
        setErrorMessage(state, errorMessage) {
            state.errorMessage = errorMessage;
        }
    },
    actions: {
        loginToken: (state) => {
            const token = localStorage.getItem('token');
            if (token) {
                state.commit('setToken', token);
                return axiosInstance.get('/api/user/').then(response => {
                        const { username, id } = response.data;
                    state.commit('setUserId', id);
                    state.commit('setUsername', username);
                }).catch(err => {
                    state.commit('setToken', null)
                    window.e = err
                    console.log(err)
                });
            }
        },
        login(state, { username, password }) {
            const body = { username, password };
            return axiosInstance.post('/api/auth/login/', body)
                .then(response => {
                    const { user: { id, username }, token } = response.data;
                    state.commit('setUserId', id);
                    state.commit('setUsername', username);
                    state.commit('setToken', token);
                    // router.push({ name: 'Main Page' });
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        getFollowing(state) {
            return axiosInstance.get('api/user/following/')
                .then(response => {
                    state.commit('setFollowing', response.data);
                }).catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                })
        },
        signup(state, { username, password }) {
            const body = { username, password };
            axiosInstance.post('/api/auth/register/', body)
                .then(response => {
                    const { user: { id, username }, token } = response.data;
                    state.commit('setUserId', id);
                    state.commit('setUsername', username);
                    state.commit('setToken', token);
                    router.push({ name: 'Main Page' });
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        logout(state) {
            axiosInstance.post('/api/auth/logout/')
                .then(() => {
                    state.commit('setToken', null);
                    state.commit('clearUserDetail');
                    // router.push({ name: 'Log In' });
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        changeUsername(state, newUsername) {
            const body = { username: newUsername };
            return axiosInstance.put('/api/user/username/', body)
                .then(response => {
                    state.commit('setUsername', response.data.username);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        changePassword(state, newPassword) {
            const body = { password: newPassword };
            return axiosInstance.put('/api/user/password/', body)
                .then(response => {
                    // eslint-disable-next-line
                    console.log(response);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        follow(state, username) {
            axiosInstance.post(`/api/user/${username}/follow/`)
                .then(response => {
                    state.commit('setFollowing', response.data);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        unfollow(state, username) {
            axiosInstance.post(`/api/user/${username}/unfollow/`)
                .then(response => {
                    state.commit('setFollowing', response.data);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        deleteUser(state) {
            return axios.delete('/api/user')
                .then(() => {
                    state.commit('clearUserDetail');
                    router.push({ name: 'Log In' });
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        fetchAllFreets(state) {
            return axiosInstance.get('api/freets/')
                .then(response => {
                    state.commit('setAllFreets', response.data);
                }).catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        fetchFollowingFreets: async (state) => {
            await state.dispatch('fetchAllFreets')
            await state.dispatch('getFollowing')
        },
        createFreet(state, { content }) {
            const body = { content };
            axiosInstance.post('/api/freets/', body)
                .then(response => {
                    state.commit('addFreet', response.data);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        editFreet(state, { id, content }) {
            const body = { content };
            axiosInstance.put(`/api/freets/${id}/`, body)
                .then(response => {
                    state.commit('updateFreet', response.data);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        deleteFreet(state, { id }) {
            axiosInstance.delete(`/api/freets/${id}/`)
                .then(response => {
                    state.commit('removeFreet', id)
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err.response.data);
                });
        },
        upvoteFreet(state, { id }) {
            axiosInstance.post(`/api/freets/${id}/like/`)
                .then(response => {
                    state.commit('updateFreet', response.data);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        unvoteFreet(state, { id }) {
            axiosInstance.post(`/api/freets/${id}/unlike/`)
                .then(response => {
                    state.commit('updateFreet', response.data);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        refreet(state, { id }) {
            axiosInstance.post(`/api/freets/${id}/refreet/`)
                .then(response => {
                    state.commit('addFreet', response.data);
                })
                .catch(err => {
                    state.dispatch('setErrorMessage', err.response.data);
                    // eslint-disable-next-line
                    console.log(err);
                });
        },
        setErrorMessage(state, errorMessage) {
            if (errorTimer) {
                clearTimeout(errorTimer);
            }
            state.commit('setErrorMessage', errorMessage);
            errorTimer = setTimeout(() => {
                state.commit('setErrorMessage', '');
            }, 5000)
        }
    },
});

export default store;