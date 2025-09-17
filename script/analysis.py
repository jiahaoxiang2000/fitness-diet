#!/usr/bin/env python3
"""
Diet Heat Balance Analysis Script

This script analyzes daily food intake and weight changes to calculate heat balance
according to the formulas specified in the fitness-diet documentation.

Heat Balance Equations:
- Q_in = C × 4.05 + P × 3.7 + F × 9.25  (equation 4)
- Q_out = Q_in - Δweight × 7700  (equation 6)

Author: Claude Code Assistant
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime, timedelta
from difflib import get_close_matches
import os
import sys
from pathlib import Path


class FoodCompositionDatabase:
    """Handle food composition data with cleaning and fuzzy matching"""

    def __init__(self, food_cpf_path):
        self.food_cpf_path = food_cpf_path
        self.food_db = self._load_and_clean_database()

    def _clean_numeric_value(self, value):
        """Clean and convert numeric values from the dataset"""
        if pd.isna(value) or value == "" or value == "-" or value == "Tr":
            return 0.0

        # Convert to string and clean
        value_str = str(value).strip()

        # Handle cases where multiple values are in one cell (space separated)
        if (
            " " in value_str
            and not value_str.replace(".", "").replace(" ", "").isdigit()
        ):
            # Try to extract the first valid number
            numbers = re.findall(r"\d+\.?\d*", value_str)
            if numbers:
                return float(numbers[0])

        # Handle cases with Chinese characters or other text
        numbers = re.findall(r"\d+\.?\d*", value_str)
        if numbers:
            return float(numbers[0])

        return 0.0

    def _load_and_clean_database(self):
        """Load and clean the food composition database"""
        try:
            # Read with explicit encoding to handle Chinese characters
            df = pd.read_csv(self.food_cpf_path, encoding="utf-8-sig")

            print(f"Loaded {len(df)} food items from database")

            # Clean column names
            df.columns = df.columns.str.strip()

            # Clean the food names
            df["foodName"] = df["foodName"].astype(str).str.strip()

            # Clean numeric columns
            for col in ["carbohydrates", "protein", "fat"]:
                if col in df.columns:
                    df[col] = df[col].apply(self._clean_numeric_value)

            # Remove rows with empty food names
            df = df[
                df["foodName"].notna()
                & (df["foodName"] != "")
                & (df["foodName"] != "nan")
            ]

            # Create a mapping for quick lookup
            food_dict = {}
            for _, row in df.iterrows():
                food_name = row["foodName"]
                food_dict[food_name] = {
                    "carbohydrates": row.get("carbohydrates", 0.0),
                    "protein": row.get("protein", 0.0),
                    "fat": row.get("fat", 0.0),
                }

            print(f"Successfully processed {len(food_dict)} valid food items")
            return food_dict

        except Exception as e:
            print(f"Error loading food database: {e}")
            return {}

    def find_food(self, food_name, cutoff=0.6):
        """Find food composition with fuzzy matching"""
        food_name = food_name.strip()

        # Exact match first
        if food_name in self.food_db:
            return self.food_db[food_name]

        # Fuzzy matching
        matches = get_close_matches(food_name, self.food_db.keys(), n=1, cutoff=cutoff)
        if matches:
            matched_name = matches[0]
            print(f"Fuzzy matched '{food_name}' to '{matched_name}'")
            return self.food_db[matched_name]

        # If no match found, return default values and warn
        print(
            f"Warning: No match found for '{food_name}', using default values (0,0,0)"
        )
        return {"carbohydrates": 0.0, "protein": 0.0, "fat": 0.0}


class HeatBalanceAnalyzer:
    """Main analysis engine for heat balance calculations"""

    def __init__(self, data_dir="data", food_cpf_path="script/data/food-cpf.csv"):
        self.data_dir = Path(data_dir)
        self.food_db = FoodCompositionDatabase(food_cpf_path)

        # File paths
        self.weight_file = self.data_dir / "weight.csv"
        self.food_file = self.data_dir / "food.csv"
        self.heat_file = self.data_dir / "heat.csv"

    def calculate_heat_input(self, carbs, protein, fat):
        """Calculate heat input using equation 4: Q_in = C × 4.05 + P × 3.7 + F × 9.25"""
        return carbs * 4.05 + protein * 3.7 + fat * 9.25

    def calculate_heat_output(self, heat_input, weight_change):
        """Calculate heat output using equation 6: Q_out = Q_in - Δweight × 7700"""
        return heat_input - weight_change * 7700

    def load_data_files(self):
        """Load all required data files"""
        data = {}

        try:
            # Load weight data
            if self.weight_file.exists():
                weight_df = pd.read_csv(self.weight_file)
                weight_df["date"] = pd.to_datetime(weight_df["date"])
                # Convert datetime index to date for dictionary keys
                weight_dict = {}
                for _, row in weight_df.iterrows():
                    weight_dict[row["date"].date()] = row["weight"]
                data["weight"] = weight_dict
                print(f"Loaded {len(weight_df)} weight records")
            else:
                print("Warning: weight.csv not found")
                data["weight"] = {}

            # Load food data
            if self.food_file.exists():
                food_df = pd.read_csv(self.food_file)
                food_df["date"] = pd.to_datetime(food_df["date"])
                data["food"] = food_df
                print(f"Loaded {len(food_df)} food records")
            else:
                print("Warning: food.csv not found")
                data["food"] = pd.DataFrame()

            # Load existing heat data
            if self.heat_file.exists():
                heat_df = pd.read_csv(self.heat_file)
                if not heat_df.empty:
                    heat_df["date"] = pd.to_datetime(heat_df["date"])
                    data["heat"] = heat_df
                    print(f"Loaded {len(heat_df)} existing heat records")
                else:
                    data["heat"] = pd.DataFrame(
                        columns=[
                            "date",
                            "input_heat_kcal",
                            "output_heat_kcal",
                            "delta_weight_kg",
                        ]
                    )
            else:
                data["heat"] = pd.DataFrame(
                    columns=[
                        "date",
                        "input_heat_kcal",
                        "output_heat_kcal",
                        "delta_weight_kg",
                    ]
                )

            return data

        except Exception as e:
            print(f"Error loading data files: {e}")
            return None

    def identify_new_dates(self, data):
        """Identify dates that need processing"""
        if data["food"].empty:
            return []

        # Get all dates with food records
        food_dates = set(data["food"]["date"].dt.date)

        # Get dates already processed
        if not data["heat"].empty:
            processed_dates = set(data["heat"]["date"].dt.date)
        else:
            processed_dates = set()

        # Find new dates
        new_dates = sorted(food_dates - processed_dates)
        return new_dates

    def calculate_daily_intake(self, food_df_day):
        """Calculate total CPF and heat input for a single day"""
        total_carbs = 0
        total_protein = 0
        total_fat = 0

        for _, row in food_df_day.iterrows():
            food_name = row["food_name"]
            weight_grams = row["weight_grams"]

            # Get food composition (per 100g)
            composition = self.food_db.find_food(food_name)

            # Calculate actual amounts based on weight
            carbs = composition["carbohydrates"] * weight_grams / 100
            protein = composition["protein"] * weight_grams / 100
            fat = composition["fat"] * weight_grams / 100

            total_carbs += carbs
            total_protein += protein
            total_fat += fat

        # Calculate heat input
        heat_input = self.calculate_heat_input(total_carbs, total_protein, total_fat)

        return {
            "carbohydrates": total_carbs,
            "protein": total_protein,
            "fat": total_fat,
            "heat_input": heat_input,
        }

    def get_weight_change(self, date, weight_data):
        """Calculate weight change from previous day"""
        try:
            # Get current weight
            current_weight = weight_data.get(date)
            if current_weight is None:
                print(f"Warning: No weight data for {date}")
                return 0.0

            # Get previous day weight
            prev_date = date - timedelta(days=1)
            prev_weight = weight_data.get(prev_date)

            if prev_weight is None:
                print(f"Warning: No previous weight data for {prev_date}")
                return 0.0

            return current_weight - prev_weight

        except Exception as e:
            print(f"Error calculating weight change for {date}: {e}")
            return 0.0

    def process_new_dates(self, data, new_dates):
        """Process new dates and calculate heat balance"""
        results = []

        for date in new_dates:
            print(f"\nProcessing {date}...")

            # Get food data for this date
            food_day = data["food"][data["food"]["date"].dt.date == date]

            if food_day.empty:
                print(f"No food data for {date}")
                continue

            # Calculate daily intake
            intake = self.calculate_daily_intake(food_day)

            # Get weight change
            weight_change = self.get_weight_change(date, data["weight"])

            # Calculate heat output
            heat_output = self.calculate_heat_output(
                intake["heat_input"], weight_change
            )

            # Store result
            result = {
                "date": date,
                "input_heat_kcal": round(intake["heat_input"], 1),
                "output_heat_kcal": round(heat_output, 1),
                "delta_weight_kg": round(weight_change, 2),
                "carbohydrates_g": round(intake["carbohydrates"], 1),
                "protein_g": round(intake["protein"], 1),
                "fat_g": round(intake["fat"], 1),
            }
            results.append(result)

            print(f"  Food items: {len(food_day)}")
            print(
                f"  CPF: {result['carbohydrates_g']}g, {result['protein_g']}g, {result['fat_g']}g"
            )
            print(f"  Heat input: {result['input_heat_kcal']} kcal")
            print(f"  Weight change: {result['delta_weight_kg']} kg")
            print(f"  Heat output: {result['output_heat_kcal']} kcal")

        return results

    def update_heat_file(self, new_results):
        """Update the heat.csv file with new results"""
        if not new_results:
            print("No new results to save")
            return

        # Create DataFrame from results
        new_df = pd.DataFrame(new_results)

        # Load existing data
        if self.heat_file.exists():
            existing_df = pd.read_csv(self.heat_file)
            if not existing_df.empty:
                # Ensure existing data has delta_weight_kg column for backwards compatibility
                if "delta_weight_kg" not in existing_df.columns:
                    existing_df["delta_weight_kg"] = 0.0

                # Combine and sort
                combined_df = pd.concat(
                    [
                        existing_df[
                            [
                                "date",
                                "input_heat_kcal",
                                "output_heat_kcal",
                                "delta_weight_kg",
                            ]
                        ],
                        new_df[
                            [
                                "date",
                                "input_heat_kcal",
                                "output_heat_kcal",
                                "delta_weight_kg",
                            ]
                        ],
                    ],
                    ignore_index=True,
                )
                combined_df["date"] = pd.to_datetime(combined_df["date"])
                combined_df = combined_df.sort_values("date").drop_duplicates(
                    subset=["date"]
                )
            else:
                combined_df = new_df[
                    ["date", "input_heat_kcal", "output_heat_kcal", "delta_weight_kg"]
                ]
        else:
            combined_df = new_df[
                ["date", "input_heat_kcal", "output_heat_kcal", "delta_weight_kg"]
            ]

        # Save to file
        combined_df.to_csv(self.heat_file, index=False)
        print(f"\nUpdated {self.heat_file} with {len(new_results)} new records")

    def generate_summary(self, results):
        """Generate summary statistics"""
        if not results:
            print("\nNo results to summarize")
            return

        print("\n" + "=" * 50)
        print("HEAT BALANCE ANALYSIS SUMMARY")
        print("=" * 50)

        df = pd.DataFrame(results)

        print(f"Period: {df['date'].min()} to {df['date'].max()}")
        print(f"Days analyzed: {len(df)}")
        print()

        print("AVERAGE DAILY VALUES:")
        print(f"  Heat input:  {df['input_heat_kcal'].mean():.1f} kcal")
        print(f"  Heat output: {df['output_heat_kcal'].mean():.1f} kcal")
        print(
            f"  Heat balance: {(df['input_heat_kcal'] - df['output_heat_kcal']).mean():.1f} kcal"
        )
        print(f"  Weight change: {df['delta_weight_kg'].mean():.2f} kg")
        print()

        print("MACRONUTRIENT BREAKDOWN:")
        print(f"  Carbohydrates: {df['carbohydrates_g'].mean():.1f}g")
        print(f"  Protein:       {df['protein_g'].mean():.1f}g")
        print(f"  Fat:           {df['fat_g'].mean():.1f}g")
        print()

        total_weight_change = df["delta_weight_kg"].sum()
        expected_heat_diff = total_weight_change * 7700
        actual_heat_diff = (df["input_heat_kcal"] - df["output_heat_kcal"]).sum()

        print("HEAT BALANCE VALIDATION:")
        print(f"  Total weight change: {total_weight_change:.2f} kg")
        print(f"  Expected heat difference: {expected_heat_diff:.0f} kcal")
        print(f"  Actual heat difference: {actual_heat_diff:.0f} kcal")
        print(f"  Difference: {abs(expected_heat_diff - actual_heat_diff):.0f} kcal")

    def run_analysis(self):
        """Main analysis workflow"""
        print("Starting Heat Balance Analysis...")
        print("=" * 40)

        # Load data
        data = self.load_data_files()
        if data is None:
            print("Error: Could not load data files")
            return

        # Identify new dates
        new_dates = self.identify_new_dates(data)

        if not new_dates:
            print("No new dates to process")
            return

        print(f"\nFound {len(new_dates)} new dates to process:")
        for date in new_dates:
            print(f"  {date}")

        # Process new dates
        results = self.process_new_dates(data, new_dates)

        # Update heat file
        self.update_heat_file(results)

        # Generate summary
        self.generate_summary(results)


def main():
    """Main entry point"""
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir.parent)  # Go to project root

    # Create analyzer
    analyzer = HeatBalanceAnalyzer()

    # Run analysis
    analyzer.run_analysis()


if __name__ == "__main__":
    main()
