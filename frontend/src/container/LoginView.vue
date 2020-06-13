<template>
    <div>
        <div class="login">
            <template v-if="isSignupMode">
                <h1>Signup</h1>
                <form v-on:submit.prevent="handleSignup">
                    <input type="text" placeholder="Username" v-model="username" />
                    <input type="text" placeholder="Password" v-model="password" />
                    <button>Sign Up</button>
                    <a class="subtext" v-on:click.prevent="toggleLoginMode">Already Have an Account</a>
                </form>
            </template>
            <template v-else>
                <h1>Login</h1>
                <form v-on:submit.prevent="handleLogin">
                    <input type="text" placeholder="Username" v-model="username" />
                    <input type="text" placeholder="Password" v-model="password" />
                    <button>Log In</button>
                    <a class="subtext" v-on:click.prevent="toggleLoginMode">Create an Account</a>
                </form>
            </template>
        </div>
        <FreetList v-bind:freets="$store.getters.allFreets"></FreetList>
    </div>
</template>
        

<script>
import FreetList from "./FreetList";

export default {
    name: "LoginView",
    props: ["signupMode"],
    components: {
        FreetList
    },
    data() {
        return {
            username: "",
            password: "",
            isSignupMode: this.signupMode === "signup"
        };
    },
    watch: {
        signupMode() {
            this.isSignupMode = this.signupMode === "signup";
            this.clearCredentials();
        }
    },
    methods: {
        handleLogin() {
            this.$store.dispatch("login", {
                username: this.username,
                password: this.password
            });
        },
        handleSignup() {
            this.$store.dispatch("signup", {
                username: this.username,
                password: this.password
            });
        },
        toggleLoginMode() {
            this.isSignupMode = !this.isSignupMode;
            this.clearCredentials();
        },
        clearCredentials() {
            this.username = "";
            this.password = "";
        }
    }
};
</script>

<style scoped>


a.subtext {
    margin: 0.5em 0;
    font-size: 0.8em;
    font-weight: bold;
    display: block;
    text-decoration: underline;
}

div.login {
    background-color: var(--fritter-background-grey);
    padding: 0.5em;
    border-radius: 0.25em;
    margin: 1em 0;
}
</style>
