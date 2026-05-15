#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageOps

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

INPUT_DIR = Path(".")
OUTPUT_DIR = Path("optimizadas")
SIZE = (1200, 1200)
QUALITY = 82

def find_image(base_name: str):
    stem = Path(base_name).stem
    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        candidate = INPUT_DIR / f"{stem}{ext}"
        if candidate.exists():
            return candidate
    return None

def optimize_image(input_path: Path, output_path: Path):
    with Image.open(input_path) as img:
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img = ImageOps.fit(img, SIZE, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        img.save(output_path, "JPEG", quality=QUALITY, optimize=True, progressive=True)

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\n🪵 Verificando y optimizando imágenes de productos...\n")

    missing = []
    processed = []

    for filename in PRODUCTOS:
        source = find_image(filename)
        output = OUTPUT_DIR / filename

        if source is None:
            missing.append(filename)
            print(f"❌ Falta: {filename}")
            continue

        try:
            optimize_image(source, output)
            processed.append(filename)
            print(f"✅ OK: {source.name} → optimizadas/{filename}")
        except Exception as e:
            print(f"⚠️ Error procesando {source.name}: {e}")

    print("\n==============================")
    print(f"✅ Procesadas: {len(processed)}")
    print(f"❌ Faltantes: {len(missing)}")
    print("==============================\n")

    if missing:
        print("Imágenes faltantes:")
        for item in missing:
            print(f"- {item}")

    print("\nRuta optimizada:")
    print(OUTPUT_DIR)

if __name__ == "__main__":
    main()
