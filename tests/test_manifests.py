from pathlib import Path
import json
import struct
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "python-modern-extensions-pack": ("FEMADOX Python Modern Extensions Pack", 9),
    "django-full-extensions-pack": ("FEMADOX Django Full Extensions Pack", 5),
    "react-nextjs-modern-pack": ("FEMADOX React / Next.js Modern Pack", 22),
}

class ManifestTests(unittest.TestCase):
    def test_manifests_icons_and_readmes(self):
        seen = set()
        publishers = set()
        for name, (title, count) in EXPECTED.items():
            with self.subTest(pack=name):
                folder = ROOT / "packs" / name
                p = json.loads((folder / "package.json").read_text(encoding="utf-8"))
                self.assertEqual((p["name"], p["displayName"]), (name, title))
                self.assertEqual(p["version"], "1.0.0")
                self.assertEqual(p["publisher"], "FEMADOX")
                self.assertEqual(p["categories"], ["Extension Packs"])
                self.assertEqual(p["license"], "SEE LICENSE IN LICENSE.txt")
                self.assertNotIn("private", p)
                self.assertEqual(p["repository"]["directory"], "packs/" + name)
                self.assertEqual(p["repository"]["url"], "https://github.com/FEMADOX/vscode-extension-packs.git")
                self.assertEqual(len(p["extensionPack"]), count)
                self.assertEqual(len(set(p["extensionPack"])), count)
                self.assertFalse(seen.intersection(p["extensionPack"]))
                seen.update(p["extensionPack"])
                publishers.add(p["publisher"])
                icon = (folder / p["icon"]).read_bytes()
                self.assertEqual(icon[:8], b"\x89PNG\r\n\x1a\n")
                width, height = struct.unpack(">II", icon[16:24])
                self.assertEqual(width, height)
                self.assertGreaterEqual(width, 256)
                readme = (folder / "README.md").read_text(encoding="utf-8")
                self.assertTrue(readme.startswith("# " + title))
                self.assertTrue(all(i in readme for i in p["extensionPack"]))
                self.assertIn("Permission is hereby granted", (folder / "LICENSE.txt").read_text())
        self.assertEqual(len(seen), 36)
        self.assertEqual(len(publishers), 1)

    def test_duplicate_roles_removed(self):
        packs = {n: json.loads((ROOT / "packs" / n / "package.json").read_text()) for n in EXPECTED}
        django = set(packs["django-full-extensions-pack"]["extensionPack"])
        frontend = set(packs["react-nextjs-modern-pack"]["extensionPack"])
        self.assertEqual(django, {"batisteo.vscode-django", "bibhasdn.django-snippets",
                                  "samuelcolvin.jinjahtml", "monosans.djlint",
                                  "shamanu4.django-intellisense"})
        self.assertTrue({"dbaeumer.vscode-eslint", "biomejs.biome", "oxc.oxc-vscode",
                         "vitest.explorer", "dsznajder.es7-react-js-snippets",
                         "ritwickdey.liveserver"} <= frontend)
        self.assertFalse({"burkeholland.simple-react-snippets", "ijs.reactnextjssnippets",
                          "ms-vscode.live-server", "voidzero.vite-plus-extension-pack",
                          "samuelcolvin.jinjahtml", "wholroyd.jinja", "monosans.djlint"} & frontend)

if __name__ == "__main__":
    unittest.main()
