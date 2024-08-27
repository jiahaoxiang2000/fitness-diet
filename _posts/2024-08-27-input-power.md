---
layout: post
title:  "Input heat"
date:   2024-08-27 08:37:00 +0800
categories: theory 
---

This post is about the input heat of the human body. We will discuss the energy input of the human body, the energy consumption of the human body, and the relationship between the two. How to control the input heat to achieve the goal of weight loss or muscle gain.

## Heat Balance Equation

The heat input of the human body is mainly from food, and the heat output of the human body is mainly from basal metabolism, physical activity, and diet-induced thermogenesis. The heat balance equation is as follows:

$$
Q_{\text{in}} = Q_{\text{basal}} + Q_{\text{activity}} + Q_{\text{diet}} \tag{1}
$$

Where:

- $$ Q_{\text{in}} $$ is the total heat input, dependent on eating food.
- $$ Q_{\text{basal}} $$ is the heat from basal metabolism, affected by personal body status.
- $$ Q_{\text{activity}} $$ is the heat from physical activity.
- $$ Q_{\text{diet}} $$ is the heat from diet-induced thermogenesis, influenced by the type of food.

### Food Heat Input Calculation ($$Q_{\text{in}}$$)

To calculate the heat input from food, we need to consider the main components: carbohydrates, proteins, and fats. The heat from food is derived from these components, often referred to as *CPF* (carbohydrates, proteins, fats). The heat input from food can be calculated using the following formula:

$$
Q_{\text{in}} = C \times 4.1 + P \times 4.1 + F \times 9.3 \tag{2}
$$

Where:

- $$C$$ is the amount of carbohydrates (in grams).
- $$P$$ is the amount of proteins (in grams).
- $$F$$ is the amount of fats (in grams).

> **Note:** The heat values for each component are: Carbohydrates: 4.1 kcal/g, Proteins: 4.1 kcal/g, Fats: 9.3 kcal/g.
>
> **Warning:** The basal metabolism and the physical activity heat is hard to accurate calculate, sometime use some formula to estimate. So here we not discuss the calculation of these two parts.

### Diet-induced Calculation ($$Q_{\text{diet}}$$)

The heat from diet-induced thermogenesis is influenced by the type of food. Simple calculation is by the *CPF*, the Carbohydrates, Proteins, and Fats. The diet-induced thermogenesis values for each component are: Carbohydrates: 5%, Proteins: 40%, Fats: 5%. So the diet-induced thermogenesis can be calculated using the following formula:

$$ Q_{\text{diet}} = C \times 0.05 + P \times 0.4 + F \times 0.05 \tag{3} $$

### Reduce Heat Equation

We put the equation (2) and (3) into the equation (1), we can get the reduce heat equation based on the food components *CPF*:

$$
\begin{split}
Q_{\text{in}} &= Q_{\text{basal}} + Q_{\text{activity}} + Q_{\text{diet}} \\
C \times 4.1 + P \times 4.1 + F \times 9.3&= Q_{\text{basal}} + Q_{\text{activity}} + C \times 0.05 + P \times 0.4 + F \times 0.05 \\
C \times 4.05 + P \times 3.7 + F \times 9.25 &= Q_{\text{basal}} + Q_{\text{activity}} \\

\end{split} \tag{4}
$$

In this view, we can see the protein have the lowest heat value.

### Issue for Heat Input

One issue is that calculating $$Q_{\text{basal}}$$ and $$Q_{\text{activity}}$$ can be challenging. To estimate these values, we can use body weight as a practical approach. Here's how:

1. **Record Food Intake and Body Weight**: Track your daily food intake and body weight over a period of time.
2. **Estimate $$Q_{\text{basal}}$$ and $$Q_{\text{activity}}$$**: Use changes in body weight to estimate these values:
   - If body weight increases, $$Q_{\text{basal}}$$ and $$Q_{\text{activity}}$$ are lower than the food intake.
   - If body weight decreases, $$Q_{\text{basal}}$$ and $$Q_{\text{activity}}$$ are higher than the food intake.

By monitoring these changes, you can better estimate the heat input components related to basal metabolism and physical activity.

## Diet allocation for Weight Loss and Muscle Gain

Based on the heat balance equation for the *CPF* (Carbohydrates, Proteins, and Fats) components, we can adjust the diet allocation to achieve different goals, such as weight loss or muscle gain. Here are some general guidelines for diet allocation based on practical experiences.

### Weight Loss

The Table below shows the diet allocation for weight loss:

| Gender | Phase | Carbohydrates (*g/kg*) | Proteins (*g/kg*) | Fats (*g/kg*) |
| ------ | ----- | ---------------------- | ----------------- |
| Man    | head  | 2.5-3.0                | 1.5               | 0.8           |
| Man    | last  | 2.0-2.5                | 1.5               | 0.8           |
| Woman  | head  | 2.5-3.0                | 1.2-1.5           | 0.8           |
| Woman  | last  | 2.0-2.5                | 1.2-1.5           | 0.8           |

For example, i am man, and i want to lose weight, i can use the diet allocation in the first row of the table. my wight is 66kg, so i can calculate the diet allocation for me:

$$ C = 2.5 \times 66 = 165 $$

$$ P = 1.5 \times 66 = 99 $$

$$ F = 0.8 \times 66 = 52.8 $$

we use the equation (4) to calculate the heat input from food:

$$
\begin{split}
  C \times 4.05 + P \times 3.7 + F \times 9.25 &= Q_{\text{basal}} + Q_{\text{activity}} \\
  165 \times 4.05 + 99 \times 3.7 + 52.8 \times 9.25 &= Q_{\text{basal}} + Q_{\text{activity}} \\
  667.25 + 366.3 + 488.4 &= Q_{\text{basal}} + Q_{\text{activity}} \\
  1521.95 &= Q_{\text{basal}} + Q_{\text{activity}} \\
\end{split}
$$

## Reference

- [健身新手的饮食完全手册-B站版](https://www.bilibili.com/video/BV1yX4y1q7LP/)
