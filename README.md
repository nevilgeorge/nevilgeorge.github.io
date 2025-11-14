SvelteKit-powered personal website/blog.

> Deployed via GitHub Actions to GitHub Pages.

# Development

### Start serving locally:
```bash
npm run dev
```

### Build for production:
```bash
npm run build
```

### Preview production build:
```bash
npm run preview
```

### Deploy to GitHub Pages:

1. Push your code to GitHub
2. Go to your repository Settings → Pages
3. Under "Source", select "GitHub Actions"
4. The workflow will automatically deploy on every push to `main`

# Project Structure

- `src/routes/` - Page routes (SvelteKit file-based routing)
- `src/lib/components/` - Reusable Svelte components
- `src/lib/data/` - TypeScript data files
- `src/lib/styles/` - Global CSS styles
- `static/` - Static assets (CSS, images, etc.)
