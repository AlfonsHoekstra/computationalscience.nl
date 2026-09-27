# People Profiles Guide

This directory contains individual markdown profiles for all Computational Science Lab members and alumni.

---

## How to Edit Your Profile

1. Locate your file in this folder (e.g. `prof-dr-ir-w-wouter-huberts.md`).
2. Click the pencil icon on GitHub to edit directly, or edit locally with your favorite code editor.
3. Make your changes in the **YAML front matter** block between the `---` delimiters.
4. Commit your changes.

---

## Example Profile

```yaml
---
title: "prof. dr. ir. W. (Wouter) Huberts"
date: 2024-01-01
draft: false
description: "Assistant Professor"
image: "img/people/w-huberts.jpg"
group: "Faculty"
active: true
email: "w.huberts@uva.nl"
website: "https://www.uva.nl/en/profile/h/u/w.huberts/w.huberts.html"
seniority: 3
domain_keywords:
  - "Computational Biomedicine"
  - "Complex Systems"
method_keywords:
  - "Multi-Scale Simulation"
  - "Data-Driven Modeling & AI"
---
```

---

## Fields Reference

- **`title`**: Full academic title and name (e.g., `"prof. dr. ir. W. (Wouter) Huberts"`).
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
