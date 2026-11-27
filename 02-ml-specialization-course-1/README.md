# Machine Learning Specialization — Course 1

This directory contains my learning notes, Jupyter Notebook implementations, experiments, and results for **Course 1 of the Machine Learning Specialization by Andrew Ng**.

The course work is organized into three weekly learning folders and a separate implementation project. The weekly folders contain topic-focused notebooks created while studying the course. The implementation project is where I practice the concepts through independent exercises and experiments.

> **Academic integrity:** The exercises in `course-1-implementation/` are practice questions prepared for my personal learning from the topics covered in my course notebooks. They are not copied from the official DeepLearning.AI graded quizzes or assignments. The implementations and explanations are intended to be my own work.

## Repository Structure

```text
02-ml-specialization-course-1/
│
├── README.md
├── requirements.txt
│
├── Week 1/
│   ├── supervised-learning.ipynb
│   └── regression-model.ipynb
│
├── Week 2/
│   ├── feature-scaling.ipynb
│   ├── multiple-linear-regression.ipynb
│   └── polynomial-regression.ipynb
│
├── Week 3/
│   ├── logistic-regression.ipynb
│   ├── loss-function-in-logistic-regression.ipynb
│   ├── overfitting.ipynb
│   └── regularization.ipynb
│
├── course-1-implementation/
│   ├── README.md
│   ├── numpy-practice.ipynb
│   ├── linear-regression-from-scratch.ipynb
│   ├── multiple-linear-regression-and-feature-scaling.ipynb
│   ├── polynomial-regression.ipynb
│   ├── logistic-regression.ipynb
│   └── regularization-experiments.ipynb (planned)
│
└── results/
```

## Learning Roadmap

### Week 1 — Introduction to Supervised Learning and Linear Regression

- Supervised learning and its main workflow.
- Regression models and predictions.
- Model representation and cost.
- Learning through model parameters.

### Week 2 — Multiple Features and Model Improvements

- Multiple linear regression.
- Feature scaling and normalization.
- Polynomial regression.
- Model complexity and fitting nonlinear patterns.

### Week 3 — Classification and Generalization

- Logistic regression.
- Logistic loss and classification.
- Overfitting.
- Regularization.

## Course 1 Implementation Project

The `course-1-implementation/` directory contains additional practice exercises designed to turn the course concepts into working code.

| Notebook                                                                                                                       | Main Topics                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| [NumPy Practice](course-1-implementation/numpy-practice.ipynb)                                                                 | Arrays, shapes, indexing, vector operations, residuals, and visualization                            |
| [Linear Regression From Scratch](course-1-implementation/linear-regression-from-scratch.ipynb)                                 | Prediction, squared-error cost, gradients, batch gradient descent, and learning-rate experiments     |
| [Multiple Linear Regression and Feature Scaling](course-1-implementation/multiple-linear-regression-and-feature-scaling.ipynb) | Multiple features, vectorized prediction, cost and gradients, normalization, and scaling experiments |
| [Polynomial Regression](course-1-implementation/polynomial-regression.ipynb)                                                   | Polynomial features, model degree, underfitting, overfitting, and evaluation                         |
| [Logistic Regression](course-1-implementation/logistic-regression.ipynb)                                                       | Sigmoid, probability predictions, logistic loss, binary classification, and decision thresholds      |
| Regularization Experiments _(Planned)_                                                                                         | Regularized cost and gradients, Ridge regression, and regularized logistic regression                |

## Tools and Libraries

The project uses:

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

All Python dependencies are managed centrally through the root `pyproject.toml` and `uv.lock` files.

The module-level `requirements.txt` is retained from the earlier setup. It is not required for installing the current shared environment.

## How to Run

This module uses the shared Python environment managed by **uv** at the repository root.

You do not need a separate virtual environment or a separate dependency installation for this course.

For complete setup instructions, refer to the [main repository README — Environment Setup](../README.md#environment-setup).

### 1. Navigate to the Repository Root

```bash
cd ai-foundation-portfolio
```

### 2. Synchronize the Environment

```bash
uv sync
```

This installs the dependencies declared in the root `pyproject.toml` using `uv.lock`.

### 3. Run Jupyter Notebooks Using VS Code

1. Open the repository in VS Code.
2. Navigate to the desired week or implementation folder.
3. Open the `.ipynb` notebook.
4. Click **Select Kernel**.
5. Select the Python environment from the repository's `.venv` directory.
6. Execute the notebook cells.

Make sure the Python and Jupyter extensions are installed in VS Code.

### 4. Run Notebooks Using JupyterLab

If JupyterLab has not already been added to the root project dependencies, install it once from the repository root:

```bash
uv add jupyterlab
```

Launch JupyterLab:

```bash
uv run jupyter lab
```

Navigate to the desired notebook:

- `02-ml-specialization-course-1/Week 1/`
- `02-ml-specialization-course-1/Week 2/`
- `02-ml-specialization-course-1/Week 3/`
- `02-ml-specialization-course-1/course-1-implementation/`

Open the notebook and execute its cells.

### Environment Guidelines

- Use the shared `.venv` from the repository root.
- Do not create another virtual environment inside this course folder.
- Do not use `pip install` to install project dependencies.
- Use `uv add` from the repository root when additional dependencies are required.
- Keep the root `pyproject.toml` and `uv.lock` synchronized.

## Progress

This repository is a work in progress. The weekly learning notebooks and implementation exercises will be updated as I move through the course and complete experiments.

## Attribution

- **Course:** [Machine Learning Specialization — DeepLearning.AI](https://www.deeplearning.ai/courses/machine-learning-specialization/)
- **Instructor:** Andrew Ng
- **Practice exercises:** Personal practice exercises prepared from the topics studied; not official graded course content.
- **Libraries:** NumPy, Pandas, Matplotlib, Scikit-learn, and Jupyter.

Dataset sources and applicable licenses should be credited alongside the relevant notebook when external datasets are used.
