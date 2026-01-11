# Coding Standards and Conventions

## General
- Follow the existing style of the landing page.
- Keep the site lightweight and fast-loading.

## CSS
- Use CSS Variables defined in `:root` for colors and spacing.
- Prefer Bootstrap utility classes where possible, but use `css/style.css` for custom components.
- Naming: Use descriptive kebab-case classes (e.g., `.feature-card`, `.hero-title-blue`).

## JavaScript
- Use Vanilla JS (No jQuery).
- Wrap logic in IIFEs (Immediately Invoked Function Expressions) to avoid global scope pollution.
- Use `IntersectionObserver` for scroll-triggered events.

## HTML
- Use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<footer>`).
- Maintain accessibility by using `aria-*` attributes where appropriate.
