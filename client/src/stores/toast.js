import { defineStore } from "pinia";

export const useToastStore = defineStore("toast", {
  id: "toast",

  state: () => ({
    ms: 0,
    message: "",
    classes: "",
    isVisible: false,
  }),

  actions: {
    showToast(ms, message, classes = "bg-green-500 text-white px-4 py-2 rounded shadow-lg transition-transform duration-500 ease-in-out") {
      this.ms = parseInt(ms);
      this.message = message;
      this.classes = classes;
      this.isVisible = true;

      // Small delay to allow Vue to update `isVisible`
      setTimeout(() => {
        this.classes += " translate-y-0 opacity-100";
      }, 10); // Apply the animation

      // Remove animation before hiding
      setTimeout(() => {
        this.classes = this.classes.replace(" translate-y-0 opacity-100", " opacity-0");
      }, this.ms - 500);

      // Hide the toast completely after animation
      setTimeout(() => {
        this.isVisible = false;
      }, this.ms);
    },
  },
});
