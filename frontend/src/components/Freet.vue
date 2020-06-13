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
      <div v-if="isOwner">
        <span v-on:click="toggleEdit">
          <md-icon v-bind:class="editIconClasses">edit</md-icon>
        </span>
        <span v-on:click="deleteFreet(id)">
          <md-icon class='icon'>delete</md-icon>
        </span>
      </div>
    </div>
    <template v-if="isEditing">
      <div class="body">
        <textarea name id cols="30" rows="10" v-model="newContent"></textarea>
      </div>
      <div class="footer">
        <button class="save" v-on:click="editFreet(id, newContent)">Save</button>
        <button class="cancel" v-on:click="toggleEdit">Cancel</button>
      </div>
    </template>
    <template v-else>
      <div class="body">
        <p>{{freet.content}}</p>
      </div>
      <div class="footer">
        <button v-if="hasUserUpvoted" class="unvote" v-on:click="unvoteFreet(id)">
          Unvote
          <span>{{upvotes}}</span>
        </button>
        <button v-else class="upvote" v-on:click="upvoteFreet(id)">
          Upvote
          <span>{{upvotes}}</span>
        </button>
        <button class="refreet" v-on:click="refreet(id)">Refreet</button>
      </div>
    </template>
  </div>
</template>
        

<script>
export default {
  name: "Freet",
  props: ["freet"],
  components: {},
  data() {
    return {
      id: this.$props.freet.id,
      owner: this.$props.freet.owner,
      isEditing: false,
      newContent: this.$props.freet.content,
      sourceId: this.$props.freet.source_freet
    };
  },
  computed: {
    upvotes() {
      return this.$props.freet.likes.length;
    },
    hasUserUpvoted() {
      return this.$props.freet.likes.includes(this.$store.getters.userId);
    },
    editIconClasses() {
      const classes = ["icon"];
      if (this.isEditing) {
        classes.push("icon-active");
      }
      return classes;
    },
    isOwner() {
      return this.$store.getters.username === this.owner;
    }
  },
  methods: {
    toggleEdit() {
      this.isEditing = !this.isEditing;
    },
    editFreet(id, newContent) {
      this.$store.dispatch("editFreet", { id, content: newContent });
      this.isEditing = false;
    },
    deleteFreet(id) {
      this.$store.dispatch("deleteFreet", { id });
    },
    upvoteFreet(id) {
      this.$store.dispatch("upvoteFreet", { id });
    },
    unvoteFreet(id) {
      this.$store.dispatch("unvoteFreet", { id });
    },
    refreet(id) {
      this.$store.dispatch("refreet", { id });
    }
  }
};
</script>

<style scoped>
p {
  margin: 0.5em;
}

a.username {
  color: var(--fritter-black);
}

button.unvote,
button.cancel {
  background-color: var(--fritter-red);
}

button.upvote,
button.save {
  background-color: var(--fritter-green);
}

button.refreet {
  background-color: var(--fritter-blue);
}

.icon {
  color: var(--fritter-grey);
}

.icon-active {
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
}

.main .footer {
  display: flex;
  justify-content: space-around;
  margin: 0.5em;
}
</style>
