<template>
    <div>
        <div class="user-card">
            <div v-if="isUser" class="action">
                <i v-bind:class="editIconClasses" v-on:click="toggleEdit">edit</i>
                <i class="material-icons icon" v-on:click="deleteUser">delete</i>
            </div>
            <h1>{{$route.params.username}}</h1>
            <template v-if="isEditing">
                <input type="text" placeholder="New Username" v-model="newUsername" />
                <button @click="changeUsername">Change Username</button>

                <input type="text" placeholder="New Password" v-model="newPassword" />
                <button @click="changePassword">Change Password</button>
            </template>
            <template v-else>
                <button class="btn-red" v-if="isFollowing" v-on:click="unfollowUser">Unfollow</button>
                <button class="btn-green" v-else v-on:click="followUser">Follow</button>
            </template>
        </div>
        <FreetList v-bind:freets="userFreets" v-bind:viewOnly="true"></FreetList>
    </div>
</template>

<script>
// eslint-disable-next-line
import axios from "axios";
import FreetList from "./FreetList";

export default {
    name: "UserView",
    components: {
        FreetList
    },
    mounted() {
        const { username } = this.$route.params;
        axios
            .get(`api/freets/?author=${username}`)
            .then(response => {
                this.userFreets = response.data;
            })
            .catch(err => {
                this.$store.commit("setErrorMessage", err.response.data);
            });
        this.$store.dispatch("getFollowing");
    },
    data() {
        return {
            newUsername: '',
            newPassword: '',
            userFreets: [],
            isEditing: false
        };
    },
    computed: {
        isUser() {
            return this.$route.params.username === this.$store.getters.username;
        },
        isFollowing() {
            return this.$route.params.username in this.$store.getters.following;
        },
        editIconClasses() {
            const classes = ["material-icons", "icon"];
            if (this.isEditing) {
                classes.push("icon-active");
            }
            return classes;
        }
    },
    methods: {
        toggleEdit() {
            this.isEditing = !this.isEditing;
        },
        changeUsername() {
            this.$store.dispatch("changeUsername", this.newUsername).then(() => {
                this.$router.push({ name: "Main Page"});
            });
        },
        changePassword() {
            this.$store.dispatch("changePassword", this.newPassword).then(() => {
                this.$router.push({ name: "Main Page"});
            });
        },
        deleteUser() {
            this.$store.dispatch("deleteUser").then(() => {
                this.$router.push({ name: "Main Page"})
            });
        },
        followUser() {
            this.$store.dispatch("follow", this.$route.params.username);
        },
        unfollowUser() {
            this.$store.dispatch("unfollow", this.$route.params.username);
        }
    }
};
</script>

<style scoped>
div.user-card {
    background-color: var(--fritter-background-grey);
    padding: 0.5em;
    border-radius: 0.25em;
    margin: 1em 0;
}

.icon {
    color: var(--fritter-grey);
}

.icon-active {
    color: var(--fritter-black);
}

div.action {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
}
</style>
