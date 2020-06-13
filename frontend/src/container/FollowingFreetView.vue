<template>
    <div>
        <h1>View Only Following Freets</h1>
        <FreetList v-bind:freets="followingFreets" v-bind:viewOnly="true"></FreetList>
    </div>
</template>

<script>
// eslint-disable-next-line
import FreetList from "./FreetList";

export default {
    name: "FollowingFreetView",
    components: {
        FreetList
    },
    mounted() {
        if (this.$store.getters.userId.length === 0) {
            this.$router.push({ name: "Log In" });
        } else {
            this.$store.dispatch("fetchFollowingFreets");
        }
    },
    computed: {
        followingFreets() {
            return this.$store.getters.followingFreets || [];
        }
    }
};
</script>

<style scoped>
</style>
