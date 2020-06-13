<template>
    <div id="app" class="main-frame">
        <nav class="main-navigation">
            <router-link class="fritter-logo" to="/">Fritter</router-link>
            <nav v-if="hasLoggedIn">
                <router-link to="/">All Freets</router-link>
                <router-link to="/following">Following Freet</router-link>
                <router-link v-bind:to="`/user/${username}`">{{username}}</router-link>
                <router-link v-on:click.native="$store.dispatch('logout')" to="/login">Sign Out</router-link>
            </nav>
            <nav v-else>
                <router-link to="/login">Login</router-link>
                <router-link to="/login/signup">Signup</router-link>
            </nav>
        </nav>
        <div v-if="errorMessage" class="error" v-on:click.prevent="clearError">{{ errorMessage }}</div>
        <div class="scroller">
            <div class="main-body">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "app",
    data() {
        return {};
    },
    computed: {
        userId() {
            return this.$store.getters.userId;
        },
        username() {
            return this.$store.getters.username;
        },
        hasLoggedIn() {
            return this.userId.length !== 0;
        },
        errorMessage() {
            return this.$store.getters.errorMessage;
        }
    },
    methods: {
        clearError() {
            this.$store.commit('setErrorMessage', '');
        }
    }
};
</script>

<!-- global styles -->
<style>
* {
    --fritter-blue: #66e0ff;
    --fritter-black: black;
    --fritter-white: white;
    --fritter-green: #92d36e;
    --fritter-red: #ff5d55;
    --fritter-background-grey: #ebebeb;
    --fritter-grey: #aaaaaa;
    --fritter-font-family: Arial, Helvetica, sans-serif;
}

body {
    margin: 0;
    overflow: hidden;
    height: 100vh;
    font-size: 16px;
}

input {
    display: block;
    margin: 1em auto;
    font-size: 0.9em;
    padding: 0.5em;
    border-radius: 0.25em;
    border: 1px solid black;
    width: 95%;
    box-sizing: border-box;
}

button {
    border-radius: 0.25em;
    padding: 0.6em;
    border: none;
    background-color: var(--fritter-green);
    font-weight: bold;
    font-size: 1em;
    transition:  all 200ms;
}

button:hover {
    transform: scale(1.1)
}

.icon {
    transition: transform 200ms;
    opacity: .6;
}

.icon:hover {
    transform: scale(1.2)
}

.icon.icon-active {
    opacity: 1;
}

button.btn-green {
    background-color: var(--fritter-green);

}
button.btn-red {
    background-color: var(--fritter-red);

}
textarea {
    font-size: .9em;
    width: 95%;
    padding: 0.5em;
    box-sizing: border-box;
    border-radius: 0.25em;
    border: 1px solid black;
}
</style>

<style scoped>
.main-frame {
    display: flex;
    flex-direction: column;
    height: 100%;
    font-family: var(--fritter-font-family);
}

div.error {
    border: 1px solid red;
    background-color: var(--fritter-red);
    border-radius: 0.25em;
    text-align: center;
    font-size: 1.5em;
}

.scroller {
    overflow-y: auto;
}
.main-body {
    text-align: center;
    margin: 0 auto;
    width: 300px;
}

.main-navigation {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background-color: var(--fritter-blue);
}

.main-navigation a {
    padding: 1em;
    color: var(--fritter-white);
    font-family: var(--fritter-font-family);
    text-decoration: none;
}

.main-navigation .fritter-logo {
    font-size: 1.5em;
}
</style>
