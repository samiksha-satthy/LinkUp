<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Log In</h1>
        <p class="mb-6 text-gray-500">this is to log into the application</p>
        <p class="font-bold">
          don't have an account?
          <RouterLink to="/signup" class="underline">Click here</RouterLink> to
          Sign Up!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div>
            <label>Email</label><br />
            <input
              type="email"
              v-model="form.email"
              placeholder="Enter your email"
              class="w-full py-4 p-2 border border-gray-300 rounded-md"
              required
            />
          </div>

          <div>
            <label>Password</label>
            <input
              type="password"
              v-model="form.password"
              placeholder="Enter your password"
              class="w-full py-4 p-2 border border-gray-300 rounded-md"
              required
            />
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </template>

          <div
            v-if="userStore.isVisible"
            class="fixed top-4 right-4 p-4 rounded-lg"
            :class="userStore.classes"
          >
            {{ userStore.message }}
          </div>

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
              Log In
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },

  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];

      if (this.form.email === "") {
        this.errors.push("Your e-mail is missing");
      }

      if (this.form.password === "") {
        this.errors.push("Your password is missing");
      }

      if (this.errors.length === 0) {
        await axios
          .post("/api/login/", this.form)
          .then((response) => {
            this.userStore.setToken(response.data);

            console.log(response.data.access);

            axios.defaults.headers.common["Authorization"] =
              "Bearer " + response.data.access;
          })
          .catch((error) => {
            console.log("error", error);
          });

        await axios
          .get("/api/me/")
          .then((response) => {
            this.userStore.setUserInfo(response.data);

            this.$router.push("/feed");
          })
          .catch((error) => {
            console.log("error", error);
          });
      }
    },
  },
};
</script>
