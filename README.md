# Fitness Diet Heat Balance Analysis

A Python-based system for analyzing daily food intake and weight changes to calculate heat balance according to scientific formulas. This project implements the heat balance theory for fitness and diet management as documented in `docs/fitness-diet.typ`.

## 🎯 Overview

This system helps you:

- Track daily food intake and body weight changes
- Calculate heat input from food using macronutrient composition (CPF - Carbohydrates, Proteins, Fats)
- Estimate metabolic heat output based on weight changes
- Analyze heat balance for weight loss or muscle gain goals
- Generate comprehensive dietary reports

## ⚖️ Heat Balance Theory

The system is based on scientific heat balance equations:

### Heat Input Calculation

```text
Q_in = C × 4.05 + P × 3.7 + F × 9.25
```

Where:

- `C` = Carbohydrates (grams)
- `P` = Proteins (grams)
- `F` = Fats (grams)

### Heat Output Estimation

```text
Q_out = Q_in - Δweight × 7700
```

Where:

- `Δweight` = Daily weight change (kg)
- `7700` = Approximate energy content of body fat (kcal/kg)

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd fitness-diet

# Install dependencies with uv
uv sync
```

### Usage

1. **Record your data** in CSV files:

   - `data/weight.csv` - Daily weight measurements
   - `data/food.csv` - Daily food intake records

2. **Run the analysis**:

   ```bash
   uv run python script/analysis.py
   ```

3. **Review results** in `data/heat.csv` and console output

## 📁 Project Structure

```shell
fitness-diet/
├── data/                          # Data files
│   ├── weight.csv                # Daily weight records
│   ├── food.csv                  # Daily food intake
│   └── heat.csv                  # Generated analysis results
├── script/
│   ├── analysis.py               # Main analysis script
│   └── data/
│       └── food.csv              # Chinese food composition database (1800+ items)
├── docs/
│   └── fitness-diet.typ          # Scientific documentation (Typst format)
├── pyproject.toml                # Project dependencies
└── README.md                     # This file
```

## 📊 Data Format

### Weight Data (`data/weight.csv`)

```csv
date,weight
2024-09-01,88.5
2024-09-02,88.3
```

### Food Data (`data/food.csv`)

```csv
date,food_name,weight_grams
2024-09-01,米饭,120
2024-09-01,鸡胸肉,150
2024-09-01,蔬菜沙拉,200
```

### Analysis Results (`data/heat.csv`)

```csv
date,input_heat_kcal,output_heat_kcal,delta_weight_kg
2024-09-01,920.9,2460.9,-0.2
2024-09-02,603.1,2143.1,-0.2
```

## ✨ Features

### Intelligent Food Matching

- **1800+ Chinese food database** with complete nutritional data
- **Fuzzy string matching** for food name lookup
- **Data cleaning** handles malformed entries automatically

### Comprehensive Analysis

- **Daily heat balance calculations**
- **Weight change tracking**
- **Macronutrient breakdown** (carbs, protein, fat)
- **Heat balance validation** using scientific formulas

### Smart Processing

- **Incremental updates** - only processes new dates
- **Error handling** for missing data
- **Backwards compatibility** with existing data files

### Detailed Reporting

- Daily summaries with all metrics
- Average daily values and trends
- Heat balance validation
- Macronutrient analysis

## 📈 Example Output

```shell
==================================================
HEAT BALANCE ANALYSIS SUMMARY
==================================================
Period: 2024-09-01 to 2024-09-02
Days analyzed: 2

AVERAGE DAILY VALUES:
  Heat input:  761.5 kcal
  Heat output: 2301.5 kcal
  Heat balance: -1540.0 kcal
  Weight change: -0.20 kg

MACRONUTRIENT BREAKDOWN:
  Carbohydrates: 56.3g
  Protein:       42.7g
  Fat:           35.7g

HEAT BALANCE VALIDATION:
  Total weight change: -0.40 kg
  Expected heat difference: -3080 kcal
  Actual heat difference: -3080 kcal
  Difference: 0 kcal
```

## 🎯 Diet Goals

The system supports analysis for different fitness goals:

### Weight Loss

- Target heat deficit through controlled intake
- Monitor daily progress
- Validate actual vs. expected weight loss

### Muscle Gain

- Ensure adequate protein intake
- Track surplus for lean mass building
- Balance macronutrients optimally

## ⚙️ Technical Details

### Dependencies

- **pandas** - Data manipulation and analysis
- **numpy** - Numerical calculations
- **difflib** - Fuzzy string matching for food names

### Food Database

- Based on China Food Composition Database
- Covers common Chinese foods and ingredients
- Includes CPF values per 100g
- Handles traditional Chinese food names

### Data Processing

- Robust parsing of malformed nutritional data
- Automatic data type conversion and validation
- Error handling for missing or incomplete records

## ⚙️ Requirements

Create your data files following the format above:

1. **Daily weight tracking** - Record weight every morning
2. **Food logging** - Log food name and weight in grams
3. **Consistent naming** - Use food names that match the database

## Contributing

This project implements scientific dietary analysis methods. Contributions welcome for:

- Additional food databases (international cuisines)
- Enhanced analysis features
- Improved food name matching
- Data visualization components

## ⚙️ License

MIT License - See LICENSE file for details

## ⚙️ References

- Scientific methodology documented in `docs/fitness-diet.typ`
- China Food Composition Database
- Heat balance theory for human metabolism
- Macronutrient energy conversion factors

---

**Note**: This tool provides estimates based on established nutritional science. For medical advice or specific dietary requirements, consult qualified healthcare professionals.
