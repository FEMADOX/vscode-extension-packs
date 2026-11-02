# Django Full Extensions Pack

Django and Jinja language support, Python-side Django snippets, autocomplete and djLint.

## One tool per role

- Django grammar and template snippets: Django by Batisteo.
- Python-side Django scaffolding: Django Snippets by Bibhas.
- Jinja grammar: Better Jinja.
- Template formatter/linter: djLint.
- Dynamic-property completion: django-intellisense.

Competing Django grammars, the second Jinja grammar and the second template
formatter were removed. Djaneiro's extra forms/URLs snippets are not included.
Choose Django or Jinja language mode according to the template engine in your
project. The upstream django-intellisense documentation says Windows is
untested; package installation checks do not establish its runtime compatibility.
Combine this pack with Python Modern Extensions Pack for Python language/debugger support.

## Included extensions (5)

| Extension | Marketplace ID |
| --- | --- |
| Django | [batisteo.vscode-django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) |
| Django Snippets | [bibhasdn.django-snippets](https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-snippets) |
| djLint | [monosans.djlint](https://marketplace.visualstudio.com/items?itemName=monosans.djlint) |
| Better Jinja | [samuelcolvin.jinjahtml](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml) |
| django-intellisense | [shamanu4.django-intellisense](https://marketplace.visualstudio.com/items?itemName=shamanu4.django-intellisense) |

## Installation and scope

Install through VS Code's Extensions view or Install from VSIX. This pack installs extension references, not their binaries. It does not pin versions, install project dependencies or change editor settings. Nested packs can add their own members. A new machine needs access to the Marketplace.

This is an unofficial community collection, independent of the projects and extension publishers named above.

## License and support

MIT covers the pack manifests and documentation. Referenced extensions keep their own licenses. Icons were generated with AI for this collection; project names and marks belong to their owners and do not imply endorsement.

Report collection issues in the [source repository](https://github.com/FEMADOX/vscode-extension-packs/issues). Report extension-specific runtime bugs to the relevant upstream project.
