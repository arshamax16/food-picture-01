"""food-picture-01 entry: write the shipped food photograph to the output dir.

The image (entry.png, JPEG bytes under a .png name, as the rules allow) is a
photorealistic smash-burger photograph generated in this session: a glossy
brioche bun, molten cheddar dripping, seared patty, tomato and lettuce, warm
side light on a dark slate surface. The program only copies bytes, so every
run writes the same output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly if the copy is ever incomplete, instead of shipping a
    # truncated image to the judge.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copy incomplete: %s" % dst)
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
