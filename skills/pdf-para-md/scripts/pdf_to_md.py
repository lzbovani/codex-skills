#!/usr/bin/env python3
"""Convert a PDF file to a Markdown file.

This script extracts text page by page and applies lightweight Markdown cleanup.
It tries PyMuPDF first, then pdfplumber, then pypdf.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in text.split("\n")]

    # Merge hyphenated line breaks: "informa-\ncao" -> "informacao"
    merged: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if i + 1 < len(lines) and line.endswith("-") and lines[i + 1] and not lines[i + 1].startswith("-"):
            merged.append(line[:-1] + lines[i + 1].lstrip())
            i += 2
            continue
        merged.append(line)
        i += 1

    # Convert obvious title-like lines to markdown headers.
    out: list[str] = []
    for ln in merged:
        stripped = ln.strip()
        if not stripped:
            out.append("")
            continue

        if is_heading_candidate(stripped):
            out.append(f"## {stripped}")
        else:
            out.append(stripped)

    # Collapse 3+ blank lines to max 2
    content = "\n".join(out)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip() + "\n"


def is_heading_candidate(line: str) -> bool:
    if len(line) > 80:
        return False
    if line.endswith((".", ",", ";", ":")):
        return False

    letters = sum(ch.isalpha() for ch in line)
    if letters == 0:
        return False

    upper = sum(ch.isupper() for ch in line)
    upper_ratio = upper / max(letters, 1)

    # Uppercase headings or short numbered section labels.
    if upper_ratio > 0.7 and len(line.split()) <= 10:
        return True
    if re.match(r"^\d+(\.\d+)*\s+", line):
        return True

    return False


def extract_with_pymupdf(pdf_path: Path) -> str:
    import fitz  # type: ignore

    parts: list[str] = []
    with fitz.open(pdf_path) as doc:
        for idx, page in enumerate(doc, start=1):
            txt = page.get_text("text")
            parts.append(f"\n\n<!-- page {idx} -->\n\n{txt}")
    return "".join(parts)


def extract_with_pdfplumber(pdf_path: Path) -> str:
    import pdfplumber  # type: ignore

    parts: list[str] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for idx, page in enumerate(pdf.pages, start=1):
            txt = page.extract_text() or ""
            parts.append(f"\n\n<!-- page {idx} -->\n\n{txt}")
    return "".join(parts)


def extract_with_pypdf(pdf_path: Path) -> str:
    from pypdf import PdfReader  # type: ignore

    reader = PdfReader(str(pdf_path))
    parts: list[str] = []
    for idx, page in enumerate(reader.pages, start=1):
        txt = page.extract_text() or ""
        parts.append(f"\n\n<!-- page {idx} -->\n\n{txt}")
    return "".join(parts)


def extract_text(pdf_path: Path) -> str:
    errors: list[str] = []

    for name, fn in (
        ("PyMuPDF (fitz)", extract_with_pymupdf),
        ("pdfplumber", extract_with_pdfplumber),
        ("pypdf", extract_with_pypdf),
    ):
        try:
            return fn(pdf_path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"- {name}: {exc}")

    joined = "\n".join(errors)
    raise RuntimeError(
        "No supported PDF library is available or extraction failed.\n"
        "Install one of: pymupdf, pdfplumber, or pypdf.\n"
        f"Details:\n{joined}"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown.")
    parser.add_argument("input_pdf", help="Path to input PDF")
    parser.add_argument("-o", "--output", help="Path to output .md file")
    args = parser.parse_args()

    input_pdf = Path(args.input_pdf).expanduser().resolve()
    if not input_pdf.exists() or input_pdf.suffix.lower() != ".pdf":
        print(f"Invalid input PDF: {input_pdf}", file=sys.stderr)
        return 2

    output_md = Path(args.output).expanduser().resolve() if args.output else input_pdf.with_suffix(".md")

    raw_text = extract_text(input_pdf)
    md_text = normalize_text(raw_text)

    output_md.write_text(md_text, encoding="utf-8")
    print(f"Markdown file created: {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
