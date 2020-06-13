<template>
    <div class="main">
        <div class="header">
            <p>
                <router-link class="username" v-bind:to="`/user/${freet.owner}`">{{freet.owner}}</router-link>
                <span v-if="sourceId">
                    refreeted a
                    <router-link to="/">freet</router-link>
                </span>
            </p>
        </div>
            <div class="body">
                <p>{{freet.content}}</p>
            </div>
    </div>
</template>
        

<script>
export default {
    name: "ViewOnlyFreet",
    props: ["freet"],
    data() {
        return {
            id: this.$props.freet.id,
            ownerId: this.$props.freet.ownerId,
            sourceId: this.$props.freet.sourceFreet
        };
    },
};
</script>

<style scoped>
p {
    margin: 0.5em;
}

a.username {
    color: var(--fritter-black);
}

.main {
    background-color: var(--fritter-background-grey);
    border-radius: 0.25em;
    display: flex;
    flex-direction: column;
    margin: 1em 0;
}

.main .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.main .body p {
    font-size: 0.8em;
    margin: 3em 0;
}
</style>
