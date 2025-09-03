---
layout: post
title:  "Diet Allocation"
date:   2024-08-28 08:19:00 +0800
categories: practical 
---

[Input heat](https://jiahaoxiang2000.github.io/fitness-diet/theory/2024/08/27/input-power.html) shows that the interval heat for Weight Loss and Muscle Gain is 1521.95 to 2300.25 kcal/day. Therefore, we need to allocate the diet to meet this interval.

## Weight Loss

For weight loss, the target heat input is 1600 kcal/day for a 66 kg individual. Based on this target, the macronutrient requirements are as follows:

- **Carbohydrates**: 173.33 g/day
- **Protein**: 104.07 g/day
- **Fat**: 55.51 g/day

These values are calculated using the equation provided in the previous post. Start to allocation the diet, we need have a database for the normal food compose by the *CPF*. One way to use the online tool, other way is to create a database. Here we find one [interesting project](https://github.com/Sanotsu/china-food-composition-data) do the job, so we use the [data](https://github.com/jiahaoxiang2000/fitness-diet/blob/main/script/data/food.csv) form the project, which have 1800+ food data, we only focus the food in China on the *CPF* metric. Before we start, we first to record day food intake, and then we can calculate the total intake of the day.
