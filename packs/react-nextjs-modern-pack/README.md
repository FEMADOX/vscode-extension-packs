# React / Next.js Modern Pack

React and Next.js tools for JavaScript, TypeScript, HTML and CSS, with project-specific linting choices.

## Snippets and previews

ES7+ React snippets is the single React snippet collection. The overlapping
Simple React and iJS React/Next collections were removed. React snippets work
with components; this pack does not add a framework or Next.js runtime behavior.

Live Server is the single static-page preview server. For React/Next applications,
use the development server configured by the project. HTML/Bootstrap snippets,
class completion, CSS navigation and SVG preview remain separate capabilities.

Oxc and Vitest are included directly; the redundant Vite+ wrapper was removed.
TypeScript 7 native preview is preview tooling, not a stable compiler guarantee.

## ESLint, Biome or Oxc?

| Tool | Choose it when |
| --- | --- |
| ESLint | The project uses ESLint configuration and ecosystem-specific plugins or rules. |
| Biome | The project is configured for Biome and its supported linting/formatting coverage. |
| Oxc | The project uses Oxlint/Oxfmt or delegates those tasks through Vite+. |

Follow repository configuration. Choose one formatter per language and one owner
per save-time fix action. Do not enable generic source.fixAll across all providers.
ESLint is not a universal formatter. Read the [workspace examples](https://github.com/FEMADOX/vscode-extension-packs/blob/main/docs/tooling.md).

## Included extensions (22)

| Extension | Marketplace ID |
| --- | --- |
| Bootstrap 5 Quick Snippets | [anbuselvanrocky.bootstrap5-vscode](https://marketplace.visualstudio.com/items?itemName=anbuselvanrocky.bootstrap5-vscode) |
| Tailwind Docs | [austenc.tailwind-docs](https://marketplace.visualstudio.com/items?itemName=austenc.tailwind-docs) |
| Biome | [biomejs.biome](https://marketplace.visualstudio.com/items?itemName=biomejs.biome) |
| Tailwind CSS IntelliSense | [bradlc.vscode-tailwindcss](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) |
| npm Intellisense | [christian-kohler.npm-intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense) |
| ESLint | [dbaeumer.vscode-eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) |
| ES7+ React/Redux/React-Native snippets | [dsznajder.es7-react-js-snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets) |
| HTML CSS Support | [ecmel.vscode-html-css](https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css) |
| Bootstrap IntelliSense | [hossaini.bootstrap-intellisense](https://marketplace.visualstudio.com/items?itemName=hossaini.bootstrap-intellisense) |
| Auto Barrel for VSCode | [imgildev.vscode-auto-barrel](https://marketplace.visualstudio.com/items?itemName=imgildev.vscode-auto-barrel) |
| Bun for Visual Studio Code | [oven.bun-vscode](https://marketplace.visualstudio.com/items?itemName=oven.bun-vscode) |
| Oxc | [oxc.oxc-vscode](https://marketplace.visualstudio.com/items?itemName=oxc.oxc-vscode) |
| TypeScript Importer | [pmneo.tsimporter](https://marketplace.visualstudio.com/items?itemName=pmneo.tsimporter) |
| CSS Peek | [pranaygp.vscode-css-peek](https://marketplace.visualstudio.com/items?itemName=pranaygp.vscode-css-peek) |
| Live Server | [ritwickdey.liveserver](https://marketplace.visualstudio.com/items?itemName=ritwickdey.liveserver) |
| Svg Preview | [simonsiefke.svg-preview](https://marketplace.visualstudio.com/items?itemName=simonsiefke.svg-preview) |
| Move TS - Move TypeScript files and update relative imports | [stringham.move-ts](https://marketplace.visualstudio.com/items?itemName=stringham.move-ts) |
| TypeScript 7 | [typescriptteam.native-preview](https://marketplace.visualstudio.com/items?itemName=typescriptteam.native-preview) |
| Vitest | [vitest.explorer](https://marketplace.visualstudio.com/items?itemName=vitest.explorer) |
| Console Ninja | [wallabyjs.console-ninja](https://marketplace.visualstudio.com/items?itemName=wallabyjs.console-ninja) |
| HTML/CSS/JavaScript Snippets | [wscats.html-snippets](https://marketplace.visualstudio.com/items?itemName=wscats.html-snippets) |
| Pretty TypeScript Errors | [yoavbls.pretty-ts-errors](https://marketplace.visualstudio.com/items?itemName=yoavbls.pretty-ts-errors) |

## Installation and scope

Install through VS Code's Extensions view or Install from VSIX. This pack installs extension references, not their binaries. It does not pin versions, install project dependencies or change editor settings. Nested packs can add their own members. A new machine needs access to the Marketplace.

This is an unofficial community collection, independent of the projects and extension publishers named above.

## License and support

MIT covers the pack manifests and documentation. Referenced extensions keep their own licenses. Icons were generated with AI for this collection; project names and marks belong to their owners and do not imply endorsement.

Report collection issues in the [source repository](https://github.com/FEMADOX/vscode-extension-packs/issues). Report extension-specific runtime bugs to the relevant upstream project.
