# Publishing

The manifests currently use publisher-pending. Do not upload these packages. Replace that value in all three package.json files with the registered publisher ID after verifying ownership in the Marketplace.

1. Register at https://marketplace.visualstudio.com/manage/publishers/ .
2. Set the registered publisher ID in each manifest and rerun tests.
3. Run npx --yes @vscode/vsce@4.1.0 package --no-dependencies from each pack folder.
4. Upload the VSIX files from the publisher management page.
5. Verify every listing's publisher ID, version and contents.

Source: https://github.com/FEMADOX/vscode-extension-packs . A local build or a source commit is not proof of Marketplace publication. No credentials or tokens belong in the repository. Future CI releases can use Marketplace Trusted Publishing with a narrow GitHub Actions policy.
