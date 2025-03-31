<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Sign Up</h1>
        <p class="mb-6 text-gray-500">this is to sign into the application</p>
        <p class="font-bold">
          already have an account?
          <RouterLink to="/login" class="underline">Click here</RouterLink> to
          Log in!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div>
            <label>Name</label><br />
            <input
              type="text"
              v-model="form.name"
              placeholder="Enter your full name"
              class="w-full py-4 p-2 border border-gray-300 rounded-md"
              required
            />
          </div>

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
              v-model="form.password1"
              placeholder="Enter your password"
              class="w-full py-4 p-2 border border-gray-300 rounded-md"
              required
            />
          </div>

          <div>
            <label>Repeat Password</label>
            <input
              type="password"
              v-model="form.password2"
              placeholder="Repeat your password"
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
            v-if="toastStore.isVisible"
            class="fixed top-4 right-4 p-4 rounded-lg"
            :class="toastStore.classes"
          >
            {{ toastStore.message }}
          </div>

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
              Sign Up
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useToastStore } from "@/stores/toast";

export default {
  setup() {
    const toastStore = useToastStore();

    return {
      toastStore,
    };
  },

  data() {
    return {
      form: {
        email: "",
        name: "",
        password1: "",
        password2: "",
      },
      errors: [],
    };
  },

  methods: {
    submitForm() {
      this.errors = [];

      if (this.form.name === "") {
        this.errors.push("Name is required");
      }

      if (this.form.email === "") {
        this.errors.push("Email is required");
      }

      if (this.form.password1 === "") {
        this.errors.push("Password is required");
      }

      if (this.form.password1 !== this.form.password2) {
        this.errors.push("Passwords do not matchhh");
      }

      if (this.errors.length === 0) {
        console.log("Form is valid, submitting...");
        axios
          .post("/api/signup/", this.form)
          .then((response) => {
            console.log("response", response.data);
            if (response.data.status === "success") {
              console.log("Success response received");
              this.toastStore.showToast(
                5000,
                "user successfully registered. please log in"
              );
              console.log("Toast triggered");
              this.form.email = "";
              this.form.name = "";
              this.form.password1 = "";
              this.form.password2 = "";
            } else {
              this.toastStore.showToast(
                5000,
                "something went wrong. please try again",
                "bg-red-300"
              );
            }
          })
          .catch((error) => {
            console.log("error", error);
          });
      }
    },
  },
};
</script>
