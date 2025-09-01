# Women’s Health DAO – Digital Endpoints (v0.0.1)

Early, **device-agnostic** and **privacy-first** code + specs for analytically valid, interpretable digital endpoints from de‑identified wearable time‑series.

**This is a pre-release (v0.0.1)** intended to support NIH SBIR Phase I submission. It includes:
- `src/` minimal reference implementation (endpoint + SQI stubs)
- `spec/Endpoint_Spec_v0.0.1.docx` (endpoint definitions & QC/SQI)
- `data/examples/redacted_sample.csv` (synthetic, de-identified)
- `docs/Dataset_Card_v0.0.1.docx`
- `docs/DMS_SOP_Short.md` (sharing plan snippet)
- `CITATION.cff` (replace DOI after Zenodo minting)
- `.zenodo.json` metadata (edit if needed before upload)

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Quick start

```bash
python src/compute_endpoints.py --input data/examples/redacted_sample.csv --out out/endpoints_demo.csv
```

## Reproducibility

- Deterministic transforms where possible; seed control via `--seed`.
- Versioned releases with DOIs via Zenodo (see `.zenodo.json`).
- Redacted sample only; **no real data**.

## License

MIT — see `LICENSE`.

## Licensing

- **Code** (everything under `src/` and supporting scripts): **MIT License** (see `LICENSE`).
- **Specifications & docs** (e.g., `spec/Endpoint_Spec_v0.0.1.docx`, files under `docs/`): **CC BY 4.0** (see `LICENSE_CC-BY-4.0.txt`).
- **Redacted sample data** (`data/examples/`): **CC0 1.0** (see `LICENSE_CC0-1.0.txt`).

When citing, please use `CITATION.cff` and update the DOI after Zenodo minting.
