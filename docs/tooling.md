# Choosing ESLint, Biome, or Oxc in VS Code

Extension packs offer tools for different project configurations; they do not choose a formatter or change repository configuration. Follow the project's installed dependencies and configuration first. Put a choice in workspace settings (usually `.vscode/settings.json`), not global User settings. Choose one owner for each language and action. The examples below are alternatives: use only the one that matches the project and adjust its language scope. Do not combine them or enable generic `source.fixAll`, which can invoke overlapping providers.

A pack may include several related tools for different project configurations; that does not make them joint owners. Check package scripts and configuration file patterns to see which files each tool handles. A setting only runs when its extension is installed, enabled, and configured for that language.

Formatting and fixing are separate save actions. `editor.formatOnSave` calls the chosen default formatter; `source.fixAll.<tool>` asks that provider to apply rule fixes. If you use only code actions for save work, leave `editor.formatOnSave` off and select one fix provider.

| Tool | Use it when | VS Code role |
| --- | --- | --- |
| ESLint | The project has `eslint.config.*` and relies on ESLint rules or ecosystem plugins. | Linting and rule fixes through `source.fixAll.eslint`; not a universal formatter. |
| Biome | `biome.json` or `biome.jsonc` exists and its configured file coverage matches the project. | Formatting plus fixes through `source.fixAll.biome`. |
| Oxc | The project uses Oxlint or Oxfmt, directly or through Vite+, and assigns the relevant files to them. | Fixes through `source.fixAll.oxc`; formatting through `source.format.oxc` when Oxfmt owns those files. |

## ESLint

ESLint is the right fit when the repository already depends on it, especially for project-specific rules and plugins. Its save action applies ESLint fixes. Some projects use ESLint only as a linter and another formatter for source layout. Keep that formatter's existing scope; do not set ESLint as `editor.defaultFormatter` solely because ESLint is installed. This example runs fixes only:

```json
{
  "editor.formatOnSave": false,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.fixAll.biome": "never",
    "source.fixAll.oxc": "never"
  }
}
```

## Biome

Use the Biome extension when its configuration covers the files you want it to format and fix. Review its include/ignore patterns and formatter and linter settings before assigning files to the extension. This example assigns TypeScript formatting to Biome and runs its fixes on save. The language entry affects TypeScript only; add entries for other languages only when the project configures Biome to handle them.

```json
{
  "[typescript]": {
    "editor.defaultFormatter": "biomejs.biome",
    "editor.formatOnSave": true
  },
  "editor.codeActionsOnSave": {
    "source.fixAll.biome": "explicit",
    "source.fixAll.eslint": "never",
    "source.fixAll.oxc": "never"
  }
}
```

## Oxc

Use Oxc when the project has adopted Oxlint or Oxfmt for the files in question. Vite+ projects can also expose these tools through their configuration and scripts. Check which formatter is assigned to each language before adding save actions; Oxlint ownership alone does not mean Oxfmt should format the same files. This example runs Oxc formatting and fixes as explicit save actions while disabling competing fix providers. Enable `source.format.oxc` only when Oxfmt owns those files. If a repository delegates JavaScript or TypeScript style rules to Stylistic and excludes those files from Oxfmt, leave `source.format.oxc` disabled for those languages.

```json
{
  "editor.formatOnSave": false,
  "editor.codeActionsOnSave": {
    "source.format.oxc": "explicit",
    "source.fixAll.oxc": "explicit",
    "source.fixAll.eslint": "never",
    "source.fixAll.biome": "never"
  }
}
```

Check the extension and VS Code documentation for supported settings and actions: [ESLint](https://github.com/microsoft/vscode-eslint), [Biome](https://biomejs.dev/reference/vscode/), [Oxc](https://github.com/oxc-project/oxc-vscode/blob/main/README.md), and [VS Code code actions on save](https://code.visualstudio.com/docs/editing/refactoring#_code-actions-on-save).
