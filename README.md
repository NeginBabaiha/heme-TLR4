# 🧬 Heme–TLR4 Knowledge Graph Expansion

**Expanding the Heme–TLR4 Interaction Network through Semi-Automated Curation and Knowledge Graph Integration**  
*Dhruv C. Rathod, Negin Sadat Babaiha, Elena Kullmann, Martin Hofmann-Apitius, Diana Imhof*

---

## 📖 Overview

This repository contains all code, curated data, and results from our study aimed at expanding the **Heme Knowledge Graph (HemeKG)** with updated information on **heme–TLR4 signaling interactions**. Through manual curation of recent literature and integration using **Biological Expression Language (BEL)**, we enhanced the representation of key pathways relevant to inflammation and porphyria.

This project serves as a reference for anyone interested in **knowledge graph curation**, **TLR4-mediated inflammation**, or **semi-automated biological data integration**.

---

## 🧠 Key Objectives

- Integrate new findings (2021–2024) into the existing HemeKG.
- Curate data using BEL standards with NLP-assisted preprocessing.
- Validate and store the knowledge graph in a **Neo4j** database.
- Perform **pathway enrichment** using **DAVID**, **KEGG**, **Reactome**, and **WikiPathways**.

---

## 📁 Repository Structure

```bash
heme-TLR4-kg/
│
├── README.md               # This file
│
├── data/
│   ├── original-hemeKG/                # Original BEL files, input articles
│   └── cleaned-original-hemKG/          # Cleaned and validated BEL triples, gene lists
│
├── src/
│   └── ebel_upload.ipynb # Neo4j loader script
