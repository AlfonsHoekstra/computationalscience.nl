# People Profiles Guide

This directory contains individual markdown profiles for all Computational Science Lab members and alumni.

---

## How to Edit Your Profile

1. Locate your file in this folder (e.g. `dr-m-h-mike-lees.md`).
2. Click the pencil icon on GitHub to edit directly, or edit locally with your favorite code editor.
3. Make your changes in the **YAML front matter** block between the `---` delimiters.
4. Commit your changes.

---

## Example Profile

```yaml
---
title: "dr. M.H. (Mike) Lees"
date: 2024-01-01
draft: false
description: "Group Leader & Associate Professor"
image: "img/people/dr-m-h-mike-lees.jpg"
group: "Faculty"
active: true
email: "m.h.lees@uva.nl"
website: "http://mhlees.com/"
seniority: 1
domain_keywords:
  - "Computational Social Science"
  - "Complex Systems"
method_keywords:
  - "Agent-Based Modeling (ABM)"
  - "Multi-Scale Simulation"
---
```

---

## Fields Reference

- **`title`**: Full academic title and name (e.g., `"dr. M.H. (Mike) Lees"`).
- **`description`**: Your role (e.g., `"Assistant Professor"`, `"PhD student"`, `"Postdoctoral Researcher"`).
- **`image`**: Photo path. Photos are located in [`../../assets/people/`](../../assets/people/). Reference format: `"img/people/<filename>.jpg"`.
- **`group`**: Group section: `"Faculty"`, `"PhDs & Postdocs"`, or `"Other"`.
- **`active`**: 
  - `true`: Active member (displayed on `/people`).
  - `false`: Alumnus (automatically displayed on `/alumni`).
- **`seniority`**: Faculty ordering level (lowest number displayed first):
  - `1`: Full Professor / Group Leader
  - `2`: Associate Professor / Professor Emeritus
  - `3`: Assistant Professor
  - `4`: Other Faculty, Postdocs, PhD Students, Support Staff
- **`email`**: Contact email.
- **`website`**: Link to your personal website, UvA profile, or LinkedIn.
- **`domain_keywords`**: 1–3 domain keywords from [`../../domain-keywords.txt`](../../domain-keywords.txt).
- **`method_keywords`**: 1–3 method keywords from [`../../method-keywords.txt`](../../method-keywords.txt).

---

## Available Keywords

Please choose your keywords from the official reference files:

### Domain Keywords ([`domain-keywords.txt`](../../domain-keywords.txt))
- `Computational Biomedicine`
- `Computational Social Science`
- `Sustainability & Ecology`
- `Urban Dynamics`
- `Computational Chemistry`
- `Economics`
- `Quantitative Finance`
- `Materials Science`
- `Computational Physics`
- `Complex Systems`
- `Computational Psychology`

### Method Keywords ([`method-keywords.txt`](../../method-keywords.txt))
- `Complex Systems Modeling`
- `Multi-Scale Simulation`
- `Network Science`
- `Agent-Based Modeling (ABM)`
- `Digital Twins`
- `Data-Driven Modeling & AI`
- `Information Theory`
- `System Dynamics & Causal Modeling`
- `High-Performance Computing (HPC)`
- `Scientific Machine Learning (SciML)`
- `Quantum Computing`
- `Game Theory`
