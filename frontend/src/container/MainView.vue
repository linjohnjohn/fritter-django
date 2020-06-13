<template>
    <div>
        <div class="post">
            <textarea rows="10" v-model="content" placeholder="What's on your mind?"></textarea>
            <button v-on:click="createFreet">Post Freet</button>
        </div>
        <FreetList v-bind:freets="$store.getters.allFreets"></FreetList>
    </div>
</template>

<script>
import FreetList from "./FreetList.vue";

export default {
    name: "MainView",
    components: { FreetList },
    created() {
        if (this.$store.getters.userId.length === 0) {
            this.$router.push({name: 'Log In'})
        }
        this.$store.dispatch('fetchAllFreets')
    },
    data() {
        return {
            content: ""
        };
    },
    methods: {
        createFreet() {
            this.$store.dispatch('createFreet', { content: this.content });
            this.content = '';
        }
    }
};
</script>

<style scoped>
div.post {
    background-color: var(--fritter-background-grey);
    padding: 0.5em;
    border-radius: 0.25em;
    margin: 1em 0;
}
</style>
