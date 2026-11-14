# food-picture-01 — smash burger

Entry for make.fun's `food-picture-01` bounty: the best-looking food picture.

- `main.py` — the entrypoint (Python 3.13, standard library only). It copies
  the shipped photograph to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
  `/output`). A pure byte copy, so every run writes identical output.
- `entry.png` — the photograph itself (JPEG bytes, as the rules allow):
  a photorealistic smash burger — glossy brioche bun, molten cheddar
  dripping down the sides, seared beef patty, tomato and lettuce, a wisp of
  steam, warm side light on dark slate. Generated in the build session.
- `LICENSE` — MIT.

Run it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
