# 01 — Python, NumPy, Pandas & Git

This module establishes the programming and data-handling foundations required for my journey into Artificial Intelligence and Machine Learning.

It focuses on Python programming, object-oriented programming, numerical computing with NumPy, data manipulation with Pandas, data visualization, and exploratory data analysis (EDA).

## Learning Objectives

- Strengthen Python programming fundamentals.
- Understand functions, loops, conditions, data structures, and object-oriented programming.
- Work with NumPy arrays and perform numerical operations efficiently.
- Use Pandas to load, inspect, filter, transform, and clean datasets.
- Gather data from CSV files, Excel files, APIs, and online sources.
- Perform exploratory data analysis and identify patterns in datasets.
- Create meaningful visualizations using Matplotlib and Seaborn.
- Develop good coding organization and Git version-control habits.

## Repository Structure

```text
01-python-numpy-pandas-git/
│
├── src/
│   ├── Basic Python/
│   │   ├── ecommerce.py
│   │   ├── inventory.py
│   │   ├── password.py
│   │   └── question.py
│   │
│   └── OOP/
│       ├── Abstraction/
│       ├── Aggregation and Composition/
│       ├── Bill Payment Scenario/
│       ├── Collection Objects/
│       ├── Custom_Datatype/
│       ├── Encapsulation/
│       ├── Flexible Dictionary/
│       ├── Inheritance/
│       ├── Pass by Reference/
│       ├── Static Methods and Static Variables/
│       └── Tasks/
│
├── notebooks/
│   ├── numpy-basics.ipynb
│   ├── numpy-practice.ipynb
│   ├── pandas-practice.ipynb
│   ├── matplot-notes.ipynb
│   ├── matplot-practice.ipynb
│   ├── seaborn-notes.ipynb
│   ├── seaborn-practice.ipynb
│   │
│   └── Data Analysis/
│       ├── data cleaning/
│       │   ├── data-gathering.ipynb
│       │   ├── data-cleaning.ipynb
│       │   └── EDA.ipynb
│       │
│       └── eda/
│           └── insurance-claim.ipynb
│
└── README.md
```

## 1. Python Fundamentals

Practiced core Python programming concepts through small applications and exercises.

Implemented examples include:

- E-commerce shopping cart system.
- Inventory management system.
- Password validation.
- Student marks and average calculations.

### Object-Oriented Programming

Explored object-oriented programming through practical examples:

- Classes and objects.
- Constructors and instance attributes.
- Encapsulation.
- Inheritance.
- Abstraction.
- Aggregation and composition.
- Static methods and class variables.
- Custom data types.
- Operator overloading.
- Object references.

## 2. NumPy — Numerical Computing

Practiced numerical computation using NumPy arrays.

Topics covered:

- Creating 1D, 2D, and multidimensional arrays.
- Array attributes, dimensions, shapes, and data types.
- Array indexing and slicing.
- Scalar and element-wise operations.
- Array reshaping and broadcasting.
- Array stacking and splitting.
- Fancy indexing and Boolean indexing.
- Mathematical and statistical operations.
- Normalization and Softmax implementation.
- Handling missing numerical values.

**Practice:** NumPy exercises involving array manipulation, distance calculations, matrix operations, and numerical functions.

## 3. Pandas — Data Manipulation

Practiced working with structured datasets using Pandas Series and DataFrames.

Topics covered:

- Creating and comparing Series.
- Creating and manipulating DataFrames.
- Reading CSV and Excel files.
- Selecting rows and columns.
- Filtering and sorting records.
- Handling missing values.
- Detecting and removing duplicate records.
- Data type conversion.
- GroupBy operations and aggregation.
- Applying functions to grouped data.
- Working with real-world datasets.

**Practice datasets:** IPL, Titanic, FIFA World Cup, items, and bird observation examples.

## 4. Data Gathering and Cleaning

Explored the process of collecting and preparing raw data for analysis.

Topics covered:

- Reading local CSV and Excel files.
- Loading datasets from URLs.
- Working with APIs.
- Understanding web scraping as a data collection method.
- Inspecting data types and missing values.
- Identifying duplicate records.
- Handling inconsistent data.
- Converting data types.
- Creating derived columns and cleaning datasets.

**Clinical Trials Dataset Exercise**

Worked with multiple clinical-trial data files, including patients, treatments, and adverse reactions.

The notebook explores data inspection, manual assessment, missing-value handling, data-type conversion, and feature creation.

## 5. Exploratory Data Analysis (EDA)

Used statistical summaries and visual exploration to understand datasets and identify patterns.

Topics explored:

- Univariate analysis.
- Numerical and categorical variables.
- Distribution analysis.
- Mean, median, quartiles, and standard deviation.
- Detecting potential outliers.
- Understanding skewness and dispersion.
- Feature relationships.
- Preparing data for further analysis.

**Practice datasets include:**

- Titanic dataset.
- Insurance claim dataset.
- Clinical trials data.
- IPL-related datasets.

## 6. Data Visualization

### Matplotlib

Practiced creating visual representations of data:

- 3D scatter plots.
- 3D line plots.
- Surface plots.
- Contour plots.
- Heatmaps.
- Color maps and chart customization.

### Seaborn

Practiced statistical visualization:

- Scatter plots.
- Line plots.
- Histograms and distribution plots.
- KDE plots.
- Violin plots.
- Box plots.
- Regression plots.
- Heatmaps.
- Cluster maps.

## How to Run

Clone the repository:

```bash
git clone https://github.com/muhammad-saad-2006/ai-foundation-portfolio.git
```

Navigate to this module:

```bash
cd ai-foundation-portfolio/01-python-numpy-pandas-git
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Open the notebooks inside the `notebooks/` directory.

For individual Python exercises, run:

```bash
python "src/Basic Python/ecommerce.py"
```

**Note:** Some notebooks currently contain local dataset paths. Update those paths to match your own dataset location before executing the corresponding cells.

## Key Takeaways

Through this module, I have developed a foundation in Python programming, numerical computing, data manipulation, data preparation, and exploratory visualization.

These skills provide the groundwork for the next stages of my AI learning path, particularly machine learning algorithms, model training, and evaluation.

## Acknowledgements

Learning resources, practice exercises, and datasets are used for educational purposes. Original implementations and personal learning notes are maintained as part of this portfolio.
