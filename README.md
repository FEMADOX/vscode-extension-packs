# FEMADOX VS Code Extension Packs

Three curated, code-free collections for Python, Django and React/Next.js.

| Pack | Extensions | Source |
| --- | ---: | --- |
| FEMADOX Python Modern Extensions Pack | 9 | [Manifest and guide](packs/python-modern-extensions-pack) |
| FEMADOX Django Full Extensions Pack | 5 | [Manifest and guide](packs/django-full-extensions-pack) |
| FEMADOX React / Next.js Modern Pack | 22 | [Manifest and guide](packs/react-nextjs-modern-pack) |

## Curation

Django uses one Django grammar, one Jinja grammar and djLint. React/Next.js uses one React snippet collection and one static preview server. Oxc and Vitest are referenced directly. Python's complementary tools are preserved.

ESLint, Biome and Oxc are project-specific choices. Read the [tooling guide](docs/tooling.md) before configuring save actions. The packs do not change settings.

## Build and checks

Run python -m unittest discover -s tests -v. Build each pack from its folder with npx --yes @vscode/vsce@4.1.0 package --no-dependencies. See [publishing](PUBLISHING.md) for publisher binding and release steps.

## License

MIT covers the manifests and documentation. Referenced extensions retain their own licenses. AI-generated icons identify the relevant projects without endorsement.
