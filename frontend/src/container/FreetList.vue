<template>
    <div>
        <template v-if="viewOnly">
            <ViewOnlyFreet v-for="freet in freets" v-bind:key="freet.id" v-bind:freet="freet"></ViewOnlyFreet>
        </template>
        <template v-else>
            <Freet v-for="freet in freets" v-bind:key="freet.id" v-bind:freet="freet"></Freet>
        </template>
    </div>
</template>
        

<script>
import Freet from "../components/Freet";
import ViewOnlyFreet from "../components/ViewOnlyFreet";

export default {
    name: "FreetList",
    props: ["freets", "viewOnly"],
    components: {
        Freet,
        ViewOnlyFreet
    }
};
</script>

<style scoped>
</style>
