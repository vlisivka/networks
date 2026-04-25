#!/bin/bash
set -ueE -o pipefail

panic() {
  echo "ERROR: $*" >&2
  exit 1
}

info() {
  echo "INFO: $*"
}

SRC_DIR="src"
TGT_DIR="docs"
IMG_DIR="$SRC_DIR/img"

# Створюємо папку doc, якщо її немає
rm -rf "$TGT_DIR" || panic "Cannot remove \"$TGT_DIR\" directory."
mkdir -p "$TGT_DIR" || panic "Cannot create \"$TGT_DIR\" directory."

# Шукаємо всі .md файли в папці src
find src -name "*.md" | while read -r md_file; do
    # Визначаємо шлях до файлу в doc/ (замінюємо src на doc та розширення на .html)
    # Наприклад: src/guide/intro.md -> doc/guide/intro.html
    rel_path="${md_file#src/}"
    html_file="docs/${rel_path%.md}.html"

    # Створюємо підкаталоги в docs/, якщо вони існують в src/
    mkdir -p "$(dirname "$html_file")" || panic "Cannot create \"$(dirname "$html_file")\" directory."

    # Запуск Pandoc
    info "Converting: $md_file -> $html_file"
    pandoc "$md_file" \
      --standalone \
      --from=Markdown \
      --lua-filter=change-links.lua \
      --to=html5 \
      --template "template.html" \
      -o "$html_file" || panic "Cannot generate HTML from \"$md_file\" to \"$html_file\"."
done

# Копіюємо зображення
cp -ra "$IMG_DIR" "$TGT_DIR" || panic "Cannot copy images from \"$IMG_DIR\" to \"$TGT_DIR\" directory."
