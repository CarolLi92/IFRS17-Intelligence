# 🧠 IFRS17 Semantic & Insight Layer — AI Build Specification

## 🎯 Objective

You are tasked with expanding an existing Python package into a **production-ready Semantic & Insight Layer** for IFRS17 financial data.

The goal is NOT to build an AI model.

The goal is to **structure financial data so that AI can generate high-quality insights reliably**.

---

## 🧱 Core Principle

DO NOT rely on AI intelligence.  
MAKE the data structured enough so that even a simple model can produce meaningful insights.

---

## 📦 Existing Codebase

You will receive a basic Python package with the following modules:

- data_processing
- variance_engine
- semantic_layer
- driver_analysis
- insight_builder

The current implementation is minimal and needs to be **fully redesigned and expanded**.

---

## 🏗️ Target Architecture

/ifrs17_semantic_layer
  /data_processing
  /variance_engine
  /semantic_layer
  /driver_analysis
  /insight_builder
  /config
  /tests
  main.py

---

## ⚙️ Module Requirements

### 1. data_processing (FOUNDATION)

Goal:
Standardize raw IFRS17 outputs into a clean, consistent structure.

Requirements:
- column normalization
- data type enforcement
- missing value handling
- validation (required fields, consistency)

Output schema:
entity | period | metric | value | dimensions

---

### 2. variance_engine (CRITICAL LOGIC)

Goal:
Turn raw numbers into interpretable movements.

Must include:
- period-over-period variance
- actual vs expected
- variance decomposition:
  experience / assumption / new business / economic

Functions:
- calculate_period_variance()
- decompose_variance()
- aggregate_variance()

---

### 3. semantic_layer (KEY DIFFERENTIATOR)

Goal:
Translate finance data into business meaning.

Requirements:
- external mapping config
- add business_label, category, driver_type
- classify metrics (driver / outcome / supporting)

---

### 4. driver_analysis (INSIGHT CORE)

Goal:
Define HOW insights are explained.

Must include:
- driver hierarchy (config-driven)
- contribution calculation (% and absolute)
- ranking logic (top drivers)

Functions:
- calculate_driver_contribution()
- rank_drivers()
- select_top_drivers()

---

### 5. insight_builder (FINAL OUTPUT)

Goal:
Produce AI-ready structured insight objects.

Must output JSON:
- metric
- change
- direction
- top_drivers
- summary

---

### 6. config

Externalize:
- semantic mapping
- driver hierarchy
- thresholds

---

### 7. testing

Include:
- unit tests
- sample dataset
- expected outputs

---

## 🔄 End-to-End Flow

1. Load data
2. Standardize
3. Compute variance
4. Apply semantic mapping
5. Calculate drivers
6. Build insights

---

## 🔐 Constraints

- No external API calls
- No black-box ML
- Fully explainable logic
- Modular code

---

## 🚀 Deliverables

- Working Python package
- Modular structure
- Sample data
- Example run
- JSON output

---

## 🧠 Final Instruction

You are building:

A translation layer between finance data and AI reasoning.

Focus on:
- clarity
- structure
- explainability
