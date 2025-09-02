# Women’s Health DAO – Digital Endpoints (v0.0.4)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17028417.svg)](https://doi.org/10.5281/zenodo.17038304)

Early, **device-agnostic** and **privacy-first** code + specs for analytically valid, interpretable digital endpoints from de-identified wearable time-series.

> **What’s new (v0.0.3):** added the 3–5 page **Endpoint Specification (PDF)** to the Zenodo record. **Code unchanged** from v0.0.2.

**This is a pre-release (v0.0.3)** intended to support NIH SBIR Phase I submission. It includes:
- `src/` minimal reference implementation (endpoint + SQI stubs) *(same as v0.0.2)*
- `spec/Endpoint_Spec_v0.0.1.docx` (endpoint definitions & QC/SQI) *(doc asset v0.0.1)*
- **`spec/Endpoint_Spec_v0_0_2_ASCII.pdf`** *(added in v0.0.3; PDF spec for reviewers)*
- `data/examples/redacted_sample.csv` (synthetic, de-identified)
- `docs/Dataset_Card_v0.0.1.docx` *(doc asset v0.0.1)*
- `docs/DMS_SOP_Short.md` (sharing plan snippet)
- `CITATION.cff` (contains DOI `10.5281/zenodo.17028417`)
- `.zenodo.json` metadata (used by Zenodo for future releases)

## Install
> Requires Python 3.10+.
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt


mkdir -p out
python src/compute_endpoints.py --input data/examples/redacted_sample.csv --out out/endpoints_demo.csv


```powershell
mkdir out -ErrorAction SilentlyContinue
python src/compute_endpoints.py --input data/examples/redacted_sample.csv --out out/endpoints_demo.csv

## Reproducibility

- Deterministic transforms where possible; seed control via `--seed`.
- Versioned releases with DOIs via Zenodo.
- Redacted sample only; **no real data**.


## Licensing

- **Code** (everything under `src/` and supporting scripts): **MIT License** (see `LICENSE`).
- **Specifications & docs** (e.g., `spec/Endpoint_Spec_v0.0.1.docx`, files under `docs/`): **CC BY 4.0** (see `LICENSE_CC-BY-4.0.txt`).
- **Redacted sample data** (`data/examples/`): **CC0 1.0** (see `LICENSE_CC0-1.0.txt`).

## Release
- GitHub release: [`v0.0.3`](https://github.com/magnitumlabs/womens-health-dao-endpoints/releases/tag/v0.0.3)
- Zenodo (Version DOI): **10.5281/zenodo.17028417**


**Citing:** Kvinto D. *Women’s Health DAO – Digital Endpoints.* v0.0.4. DOI: 10.5281/zenodo.17038304

