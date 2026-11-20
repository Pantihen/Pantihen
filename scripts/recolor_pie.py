"""Recolor the language pie chart of github-profile-3d-contrib SVGs into the profile palette.

Usage: python3 scripts/recolor_pie.py <svg> <dark|light> [<svg> <dark|light> ...]

Languages keep their order (largest first); each one gets the next palette color.
"""
import re
import sys

PALETTES = {
    "dark": ["#E50914", "#FFFFFF", "#8A0F17", "#FF7A82", "#5A5A5A", "#3A3A3A"],
    "light": ["#E50914", "#0A0A0A", "#8A0F17", "#FF7A82", "#9E9E9E", "#CFCFCF"],
}

OTHER = "#444444"  # color the generator uses for "other"

LEGEND = re.compile(
    r'<rect x="0" y="[^"]+" width="[^"]+" height="[^"]+" fill="(#[0-9A-Fa-f]{3,6})" class="stroke-bg"'
)


def recolor(path, theme):
    palette = PALETTES[theme]
    svg = open(path, encoding="utf-8").read()

    order = []
    for color in LEGEND.findall(svg):
        if color.lower() not in (c.lower() for c in order):
            order.append(color)
    if not order:
        print(f"{path}: no language legend found, left unchanged")
        return

    # two-step swap so a language color that equals a palette color can't be recolored twice
    for i, color in enumerate(order):
        c = re.escape(color)
        svg = re.sub(f'fill="{c}"', f'fill="@@LANG{i}@@"', svg, flags=re.IGNORECASE)        # legend
        svg = re.sub(f'fill:\\s*{c}', f'fill: @@LANG{i}@@', svg, flags=re.IGNORECASE)     # pie slices
    named = [c for c in order if c.lower() != OTHER]
    for i, color in enumerate(order):
        if color.lower() == OTHER:
            new = palette[-1]                                   # "other" is always the quiet gray
        else:
            new = palette[min(named.index(color), len(palette) - 2)]
        svg = svg.replace(f"@@LANG{i}@@", new)

    open(path, "w", encoding="utf-8").write(svg)
    print(f"{path}: recolored {len(order)} languages")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or len(args) % 2:
        sys.exit(__doc__)
    for svg_path, theme in zip(args[::2], args[1::2]):
        recolor(svg_path, theme)
