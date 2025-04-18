# Deploying Docusaurus to GitHub Pages with GitHub Actions

To successfully deploy a **Docusaurus** site to **GitHub Pages**, a **GitHub Action** workflow must be implemented.

## GitHub Actions Workflow Configuration

The workflow should be defined in the following file:

```plaintext
.github/workflows/deploy-page.yml
```

### Example Workflow File

Below is an example configuration for `deploy-page.yml` that automates the deployment process:

```yaml
name: Deploy Docusaurus to GitHub Pages

on:
   push:
      branches:
         - main

jobs:
   deploy:
      runs-on: ubuntu-latest
      steps:
         - name: Checkout repository
           uses: actions/checkout@v3
           with:
              fetch-depth: 0

         - name: Set up Node.js
           uses: actions/setup-node@v3
           with:
              node-version: 18

         - name: Install dependencies
           run: npm install
           working-directory: ./my-docs

         - name: Build Docusaurus site
           run: npm run build
           working-directory: ./my-docs

         - name: Configure Git user (Optional, but recommended)
           run: |
              git config --global user.name "github-actions[bot]"
              git config --global user.email "github-actions[bot]@users.noreply.github.com"

         - name: Deploy to GitHub Pages
           env:
              GIT_PASS: ${{ secrets.GITHUB_TOKEN }}
           run: GIT_USER="****" GIT_PASS=${{ secrets.GITHUB_TOKEN }} npm run deploy
           working-directory: ./my-docs
```

**Note**: Ensure that the Docusaurus directory is my-docs. If your project uses a different directory, update the working-directory paths accordingly.
