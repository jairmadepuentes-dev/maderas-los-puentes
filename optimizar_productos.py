#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageOps

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "assets/images/productos"
OUTPUT_DIR = INPUT_DIR / "optimizadas"

PRODUCTOS = [
    "tabla-burra-30cm.jpg",
    "tabla-burra-25cm.jpg",
    "tabla-burra-20cm.jpg",
    "tabla-burra-15cm.jpg",
    "tablas-chapas-30cm.jpg",
    "tablas-chapas-25cm.jpg",
    "tablas-chapas-20cm.jpg",
    "tablas-forros-30cm.jpg",
    "tablas-forros-25cm.jpg",
    "cercos-8x8x3.jpg",
    "repizas-8x4x3.jpg",
    "repizas-8x4x3-arregladas.jpg",
    "repizas-8x4x4.jpg",
    "planchon-3m.jpg",
    "planchon-4m.jpg",
    "durmientes-3m.jpg",
    "durmientes-4m.jpg",
    "varas-corredor-6m.jpg",
    "vara-limaton-6m.jpg",
    "guadua-esterilla-4m.jpg",
    "paral-rollizo-3m.jpg",
    "triplex-122x244x4mm.jpg",
    "liston-camilla-8x18x070.jpg",
    "bocel-triangular-2x2x3m.jpg",
    "bocel-triangular-3x3x3m.jpg",
    "repizas-camilla-8x4x140.jpg",
    "formaleta-70x140.jpg",
]

SIZE = (1200, 1200)
QUALITY = 82

def find_image(filename):
    stem = Path(filename).stem
    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        path = INPUT_DIR / f"{stem}{ext}"
        if path.exists():
            return path
    return None

def optimize_image(source, target):
    with Image.open(source) as img:
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img = ImageOps.fit(
            img,
            SIZE,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5)
        )
        img.save(target, "JPEG", quality=QUALITY, optimize=True, progressive=True)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"\nOrigen: {INPUT_DIR}")
    print(f"Destino: {OUTPUT_DIR}\n")

    missing = []
    ok = []

    for filename in PRODUCTOS:
        source = find_image(filename)
        target = OUTPUT_DIR / filename

        if not source:
            print(f"❌ Falta: {filename}")
            missing.append(filename)
            continue

        optimize_image(source, target)
        print(f"✅ {source.name} -> optimizadas/{filename}")
        ok.append(filename)

    print("\nResumen")
    print(f"Procesadas: {len(ok)}")
    print(f"Faltantes: {len(missing)}")

    if missing:
        print("\nFaltantes:")
        for item in missing:
            print(f"- {item}")

if __name__ == "__main__":
    main()
