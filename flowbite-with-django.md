- Follow the link: [flowbite with django](https://flowbite.com/docs/getting-started/django/)
- Flowbite is a tailwind component library
- I don't know about the steps involving installing django compressor but I can just use tailwind with django normally without all that.

# Setting Up Tailwind
- ```
  npm install -D tailwindcss
  npx tailwindcss init
  ```

- In your `tailwind.config.js` file
  ```javascript
    /** @type {import('tailwindcss').Config} */
  module.exports = {
    content: ["./src/**/*.{html,js}"],
    theme: {
      extend: {},
    },
    plugins: [],
  }
  ```
  
- In your `input.css` file
  ```css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  ```

- to compile tailwind use
  ```
  npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
  ```
  notice the syntax: `npx tailwindcss -i <input-file-location> -o <output-file-location> --watch`

- Start using tailwind
  ```html
    <!doctype html>
    <html>
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="./output.css" rel="stylesheet">
    </head>
    <body>
      <h1 class="text-3xl font-bold underline">
        Hello world!
      </h1>
    </body>
    </html>
  ```

# Additional libraries
So to use additional libraries just do `npm install <whatever>` and just add it as required to the project. 
