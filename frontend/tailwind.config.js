/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'norsk-blue': '#003f7f',
        'norsk-red': '#ef2b2d',
        'norsk-light': '#f8fafc',
      }
    },
  },
  plugins: [],
}