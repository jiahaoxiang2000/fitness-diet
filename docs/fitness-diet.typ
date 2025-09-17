#import "@preview/basic-document-props:0.1.0": simple-page
#show: simple-page.with(
  "isomo",
  "",
  middle-text: "Diet: Heat Input and Diet Allocation",
  date: true,
  numbering: true,
  supress-mail-link: false,
)

#set heading(numbering: "1.1")
#set math.equation(numbering: "(1)")
#set text(lang: "en")
#show ref: it => {
  if it.element != none and it.element.func() == math.equation {
    // Show equation references with parentheses
    "(" + str(counter(math.equation).at(it.element.location()).first()) + ")"
  } else {
    it
  }
}
#show table: it => align(center, it)

= Heat Balance Theory

This document discusses the input heat of the human body, energy consumption, and the relationship between the two. It explores how to control heat input to achieve weight loss or muscle gain goals.

== Heat Balance Equation

The heat input of the human body is mainly from food, and the heat output of the human body is mainly from basal metabolism, physical activity, and diet-induced thermogenesis. The heat balance equation is as follows:

$ Q_"in" = Q_"basal" + Q_"activity" + Q_"diet" $ <eq:1>

Where:

- $Q_"in"$ is the total heat input, dependent on eating food.
- $Q_"basal"$ is the heat from basal metabolism, affected by personal body status.
- $Q_"activity"$ is the heat from physical activity.
- $Q_"diet"$ is the heat from diet-induced thermogenesis, influenced by the type of food.

*Food Heat Input Calculation ($Q_"in"$)*

To calculate the heat input from food, we need to consider the main components: carbohydrates, proteins, and fats. The heat from food is derived from these components, often referred to as *CPF* (carbohydrates, proteins, fats). The heat input from food can be calculated using the following formula:

$ Q_"in" = C times 4.1 + P times 4.1 + F times 9.3 $ <eq:2>

Where:

- $C$ is the amount of carbohydrates (in grams).
- $P$ is the amount of proteins (in grams).
- $F$ is the amount of fats (in grams).

#block(
  fill: rgb("f0f0f0"),
  inset: 8pt,
  radius: 4pt,
)[
  *Note:* The heat values for each component are: Carbohydrates: 4.1 kcal/g, Proteins: 4.1 kcal/g, Fats: 9.3 kcal/g.

  *Warning:* The basal metabolism and the physical activity heat is hard to accurately calculate, sometimes using formulas to estimate. So here we do not discuss the calculation of these two parts.
]

*Diet-induced Thermogenesis Calculation ($Q_"diet"$)*

The heat from diet-induced thermogenesis is influenced by the type of food. Simple calculation is by the *CPF*, the Carbohydrates, Proteins, and Fats. The diet-induced thermogenesis values for each component are: Carbohydrates: 5%, Proteins: 40%, Fats: 5%. So the diet-induced thermogenesis can be calculated using the following formula:

$ Q_"diet" = C times 0.05 + P times 0.4 + F times 0.05 $ <eq:3>

*Reduced Heat Equation*

We put equation @eq:2 and @eq:3 into equation @eq:1, we can get the reduced heat equation based on the food components *CPF*:

$
                                     Q_"in" & = Q_"basal" + Q_"activity" + Q_"diet" \
    C times 4.1 + P times 4.1 + F times 9.3 & = Q_"basal" + Q_"activity" + C times 0.05 + P times 0.4 + F times 0.05 \
  C times 4.05 + P times 3.7 + F times 9.25 & = Q_"basal" + Q_"activity"
$ <eq:4>

In this view, we can see the protein has the lowest heat value.

*Issue for Heat Input*

One issue is that calculating $Q_"basal"$ and $Q_"activity"$ can be challenging. To estimate these values, we can use body weight as a practical approach. Here's how:

1. *Record Food Intake and Body Weight*: Track your daily food intake and body weight over a period of time.
2. *Estimate $Q_"basal"$ and $Q_"activity"$*: Use changes in body weight to estimate these values:
  - If body weight increases, $Q_"basal"$ and $Q_"activity"$ are lower than the food intake.
  - If body weight decreases, $Q_"basal"$ and $Q_"activity"$ are higher than the food intake.

By monitoring these changes, you can better estimate the heat input components related to basal metabolism and physical activity.

= Diet Allocation for Weight Loss and Muscle Gain

Based on the heat balance equation for the *CPF* (Carbohydrates, Proteins, and Fats) components, we can adjust the diet allocation to achieve different goals, such as weight loss or muscle gain.

== Weight Loss

The table below shows the diet allocation for weight loss:

#table(
  columns: 5,
  table.header[*Gender*][*Phase*][*Carbohydrates (g/kg)*][*Proteins (g/kg)*][*Fats (g/kg)*],
  [Man], [head], [2.5-3.0], [1.5], [0.8],
  [Man], [last], [2.0-2.5], [1.5], [0.8],
  [Woman], [head], [2.5-3.0], [1.2-1.5], [0.8],
  [Woman], [last], [2.0-2.5], [1.2-1.5], [0.8],
)

For example, I am a man, and I want to lose weight, I can use the diet allocation in the first row of the table. My weight is 88kg, so I can calculate the diet allocation for me:

$ C = 2.5 times 88 = 220 $
$ P = 1.5 times 88 = 132 $
$ F = 0.8 times 88 = 70.4 $

We use equation @eq:4 to calculate the heat input from food:

$
         C times 4.05 + P times 3.7 + F times 9.25 & = Q_"basal" + Q_"activity" \
  220 times 4.05 + 132 times 3.7 + 70.4 times 9.25 & = Q_"basal" + Q_"activity" \
                               891 + 488.4 + 651.2 & = Q_"basal" + Q_"activity" \
                                            2030.6 & = Q_"basal" + Q_"activity"
$

== Muscle Gain

The table below shows the diet allocation for muscle gain:

#table(
  columns: 4,
  table.header[*Gender*][*Carbohydrates (g/kg)*][*Proteins (g/kg)*][*Fats (g/kg)*],
  [Man], [3.5-4.5], [1.5-2.0], [1.0],
  [Woman], [3.0-3.5], [1.5], [1.0],
)

For example, I am a man, and I want to gain muscle, I can use the diet allocation in the first row of the table. My weight is 88kg, so I can calculate the diet allocation for me:

$
  C & = 4.5 times 88 = 396 \
  P & = 2.0 times 88 = 176 \
  F & = 1.0 times 88 = 88
$

We use equation @eq:4 to calculate the heat input from food:

$
       C times 4.05 + P times 3.7 + F times 9.25 & = Q_"basal" + Q_"activity" \
  396 times 4.05 + 176 times 3.7 + 88 times 9.25 & = Q_"basal" + Q_"activity" \
                            1603.8 + 651.2 + 814 & = Q_"basal" + Q_"activity" \
                                            3069 & = Q_"basal" + Q_"activity"
$

= Practical Diet Allocation

The heat input interval for weight loss and muscle gain is 2030.6 to 3069 kcal/day. Therefore, we need to allocate the diet to meet this interval.

== Weight Loss Target

For weight loss, the target heat input is 2100 kcal/day for a 88 kg individual. Based on this target, the macronutrient requirements are as follows:

- *Carbohydrates*: 220 g/day
- *Protein*: 132 g/day
- *Fat*: 70.4 g/day

These values are calculated using the equation provided in the previous section. To start allocating the diet, we need a database for normal food composed by the *CPF*. One way is to use online tools, another way is to create a database. We found an interesting project that does the job, so we use the data from the project, which has 1800+ food data. We only focus on food in China on the *CPF* metric. Before we start, we first record daily food intake, and then we can calculate the total intake of the day.

== Record Data

Every morning after waking up, record your *weight* in `data/weight.csv`, which contains only two columns: date and weight. This makes it easy to maintain.

Food input recording is more challenging. If you eat simple foods or foods with available CPF data, recording becomes easier. There are two approaches:

1. *Cook your own meals* - This gives precise control over ingredients
2. *Use approximation method* - Estimate portions and use similar foods in the database

For simplicity, we start with the approximation method. Record food intake in `data/food.csv`, which includes:
- Date of consumption
- Food name
- Weight (grams)

To convert food items to CPF values, we use the China Food Composition Database stored in `data/food-cpf.csv`.

== Analysis Data

Here we can use the *weight.csv* to determine if $Q_"in" > Q_"out"$. The $Q_"in"$ can be computed using food.csv & food-cpf.csv with equation @eq:4. We need a simple equation to convert weight changes to heat (Q). For simplicity, we use the following approximation:

$ Delta Q = Delta "weight" times 7700 "kcal/kg" = Q_(\in) - Q_(\o\ut) $ <eq:5>

Where:
- $Delta Q$ is the net heat surplus/deficit in kcal
- $Delta "weight"$ is the weight change in kg
- 7700 kcal/kg is the approximate energy content of body fat

This means:
- Weight gain of 1 kg ≈ 7700 kcal surplus
- Weight loss of 1 kg ≈ 7700 kcal deficit

From the equation, we can derive the daily energy output:

$ Q_"out" = Q_"in" - Delta "weight" times 7700 "kcal/kg" $ <eq:6>

We record this analysis in `heat.csv` with three columns:
- Date
- Input heat (kcal)
- Output heat (kcal)
- Delta weight (kg)

To automate this process, we create an `script/analysis.py` script with the following logic:

1. *Read existing data*: Load `weight.csv`, `food.csv`, `food-cpf.csv`, and `heat.csv`
2. *Identify new dates*: Find dates in weight/food data that haven't been processed yet
3. *Calculate daily $Q_"in"$*: For each new date:
  - Sum all food items consumed
  - Look up CPF values from the composition database
  - Apply equation @eq:4: $Q_"in" = C times 4.05 + P times 3.7 + F times 9.25$
4. *Calculate daily $Q_"out"$*: Using weight changes and equation @eq:6
5. *Update heat.csv*: Append new calculations with date, input heat, and output heat
6. *Generate summary*: Show trends in heat balance and weight changes

= References

- 健身新手的饮食完全手册-B站版: https://www.bilibili.com/video/BV1yX4y1q7LP/
- China Food Composition Data: https://github.com/Sanotsu/china-food-composition-data
