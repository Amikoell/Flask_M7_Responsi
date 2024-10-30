module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.css",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    colors: {
      // ...
      "purple-heart": {
        50: "#f4f0ff",
        100: "#ece4ff",
        200: "#dacdff",
        300: "#c0a5ff",
        400: "#a372ff",
        500: "#8a3aff",
        600: "#8012ff",
        700: "#7301ff",
        800: "#6700e6",
        900: "#5002b0",
        950: "#2f0078",
      },

      // ...
    },
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
