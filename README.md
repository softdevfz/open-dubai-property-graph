# Open Dubai Property Graph

Dubai's land registry is open data, but its files share no common key for a building and each one names things differently. This is the join, published with the places where it fails.

**Full files, data dictionary and match report: https://fairsqft.com/data/**

This repository holds a 100-row sample of each table and a script that downloads the current files from fairsqft.com.

## What is in it

- **`archetypes`** (about 26,000 rows): one row per project or building × home type × bedrooms. Registered unit stock, median and quartiles of ready and off-plan sales, median and quartiles of new and renewed leases, yearly turnover, sample sizes and an abstain flag when the sample is too small.
- **`crosswalk`** (about 22,700 rows): the IDs and names the Dubai Land Department uses for areas, master projects, projects and buildings across its units, buildings, projects, sales and rental files.

Nothing is per unit. Formats: Parquet, CSV and JSONL. Updated with each data date (`as_of`).

## Where the join fails (data as of 26 October 2026)

| Source, last 12 months | Linked to a building | Project only | Not linked |
|---|---:|---:|---:|
| Sales (151,182) | 50.0% | 44.4% | 0.7% |
| Rental contracts (613,449) | 15.6% | 15.9% | 68.5% |

The remaining 4.9% of sales are linked only by the building name in the sales file. Rental contracts never name the building. In projects with several towers the registry gives each tower an ID but no name, so those are published at project level and never split by guesswork. The full report is on the data page.

## Get the data

```
python3 download.py --format parquet
```

## API and MCP

A free REST API and MCP server, with no login, answer questions over the same data: resolve a name such as "Marina Gate 2" to registry IDs, check an asking price against registered sales, check a rent renewal. See https://fairsqft.com/developers/

## Licence and sources

Source: Dubai Land Department (DLD) open data, published on data.dubai. Analysis: FairSqft. Not endorsed by the DLD or the Government of Dubai.

The data is offered under the same [Dubai Open Data Licence](https://data.dubai), with no additional terms. Credit the Dubai Land Department and link the source dataset. The script in this repository is MIT-licensed.

Not a valuation. Not financial or legal advice.

FairSqft is operated by Soft Dev FZ LLC (UAE) and is built and run by AI agents with a human owner. Contact: hello@fairsqft.com
