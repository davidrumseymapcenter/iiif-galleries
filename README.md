# IIIF Galleries — David Rumsey Map Center

A curated collection of IIIF image galleries created by the David Rumsey Map Center at Stanford University Libraries. Each gallery is built with the [IIIF Gallery Builder](https://github.com/davidrumseymapcenter/set-builder) and can be opened directly in your browser.

**→ [Browse the Gallery Index](https://davidrumseymapcenter.github.io/iiif-galleries/)**

---

## Using the galleries

Each gallery in the index opens in presentation mode — a clean, full-screen view suitable for teaching and public display. You can also open any gallery in other modes by changing the filename in the URL:

| Mode | URL | Purpose |
|------|-----|---------|
| **Presentation** | `presentation.html?file=...` | Clean view, no notes, for classroom use |
| **Viewer** | `viewer.html?file=...` | Read-only with curator notes visible |
| **Builder** | `index.html?file=...` | Open and edit in the Gallery Builder |

---

## Adding a gallery

Galleries are stored as JSON files in the `galleries/` folder. Adding a new gallery is as simple as dropping a file in and pushing:

1. Build your gallery in the [IIIF Gallery Builder](https://davidrumseymapcenter.github.io/set-builder/)
2. Save it as a JSON file using the **💾 Save File** button
3. Add the file to the `galleries/` folder in this repo
4. Commit and push
5. A GitHub Action runs automatically, reads the gallery name from the JSON, and adds it to the index

The live index at `https://davidrumseymapcenter.github.io/iiif-galleries/` updates within a minute or two.

---

## How it works

A GitHub Action (`.github/workflows/generate-index.yml`) triggers on any push to the `galleries/` folder. It loops through all `.json` files, reads the `label` field from each one, and regenerates `index.md` as a simple linked list. GitHub Pages then rebuilds the site automatically.

The gallery JSON format is defined by the IIIF Gallery Builder. Each file is a IIIF Collection containing one or more manifests, with curator notes and page selections preserved.

---

## Forking this setup

If you'd like to create your own gallery index, you can fork this repo and the [IIIF Gallery Builder](https://github.com/davidrumseymapcenter/set-builder). You'll need to:

1. Enable GitHub Pages on your fork (Settings → Pages → Deploy from branch → main)
2. Update the gallery URLs in `generate-index.yml` to point to your repo and your instance of the Gallery Builder
3. Drop your own JSON files into `galleries/` and push

---

## Credits

Built at the [David Rumsey Map Center](https://library.stanford.edu/rumsey), Stanford University Libraries, with Claude Sonnet (Anthropic).

Questions or feedback: [rumseymapcenter@stanford.edu](mailto:rumseymapcenter@stanford.edu)
