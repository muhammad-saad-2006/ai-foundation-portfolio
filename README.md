# AI Foundation Portfolio

A structured learning portfolio documenting my journey into Artificial Intelligence, Machine Learning, Deep Learning, and PyTorch.

Each module contains original implementations, experiments, results, and reflections to demonstrate my practical understanding of the concepts.

## Progress Tracker

| #   | Module                                | Status      | Start      | Finish     | Folder                                     |
| --- | ------------------------------------- | ----------- | ---------- | ---------- | ------------------------------------------ |
| 01  | Python, NumPy, Pandas, Git            | Completed   | 18-11-2026 | 19-11-2026 | [01](01-python-numpy-pandas-git)           |
| 02  | ML Specialization Course 1            | Completed   | 21-11-2026 | 27-11-2026 | [02](02-ml-specialization-course-1)        |
| 03  | Classical ML Comparison               | Not started |            |            | [03](03-classical-ml-comparison)           |
| 04  | Neural Networks and Model Improvement | Not started |            |            | [04](04-neural-nets-and-model-improvement) |
| 05  | PyTorch Basics                        | Not started |            |            | [05](05-pytorch-basics)                    |
| 06  | MLP and CNN Training Loops            | Not started |            |            | [06](06-mlp-cnn-training-loops)            |
| 07  | Responsible Evaluation (Optional)     | Not started |            |            | [07](07-responsible-evaluation)            |
| 08  | Error Analysis Report                 | Not started |            |            | [08](08-error-analysis-report)             |

## Minimum Foundation Outputs

- [ ] Linear and logistic regression implemented with explanations of loss and optimization.
- [ ] Classical ML comparison with 3+ models and a justified evaluation protocol.
- [ ] PyTorch MLP and CNN with self-written training and validation loops.
- [ ] Error analysis report covering failure cases and possible improvements.
- [ ] Documented evidence for every completed module.

---

## Environment Setup

This repository uses **[uv](https://docs.astral.sh/uv/)** for Python version management, dependency management, and virtual environment management.

All Python dependencies are managed centrally through the root `pyproject.toml` and `uv.lock` files.

There is no need to create separate virtual environments or install dependencies independently for each module.

### 1. Prerequisites

- Python 3.13 or newer.
- Git.
- uv.
- VS Code (recommended for working with Jupyter notebooks).

### 2. Install uv

**Windows (PowerShell):**

```powershell
winget install --id=astral-sh.uv -e
```

Alternatively, use the official installer:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Check the installation:

```bash
uv --version
```

### 3. Clone the Repository

```bash
git clone https://github.com/muhammad-saad-2006/ai-foundation-portfolio.git

cd ai-foundation-portfolio
```

### 4. Install Python and Project Dependencies

Install the required Python version:

```bash
uv python install 3.13
```

Synchronize the project environment:

```bash
uv sync
```

This will:

- Create the `.venv` virtual environment if it does not exist.
- Install the dependencies declared in `pyproject.toml`.
- Use `uv.lock` to maintain reproducible dependency versions.

### 5. Run Python Scripts

Run Python scripts using:

```bash
uv run python path/to/script.py
```

For example:

```bash
uv run python "01-python-numpy-pandas-git/src/Basic Python/ecommerce.py"
```

`uv run` automatically executes commands inside the project's managed environment.

### 6. Run Jupyter Notebooks

**Option A — VS Code (Recommended)**

1. Open the repository in VS Code.
2. Open any `.ipynb` notebook.
3. Click **Select Kernel**.
4. Choose the Python environment located in the repository's `.venv` directory.
5. Execute the notebook cells.

Make sure the VS Code Python and Jupyter extensions are installed.

The project already includes `ipykernel`, which allows the environment to be used as a notebook kernel.

**Option B — JupyterLab**

To use JupyterLab in your browser, install it once from the repository root:

```bash
uv add jupyterlab
```

Then launch it:

```bash
uv run jupyter lab
```

This adds JupyterLab to the root project dependencies, so it will also be available to other modules.

### 7. Manage Dependencies

All dependency changes should be made from the repository root.

**Add a package:**

```bash
uv add package-name
```

Example:

```bash
uv add seaborn
```

**Remove a package:**

```bash
uv remove package-name
```

**Update dependencies:**

```bash
uv lock --upgrade
uv sync
```

**View installed dependencies:**

```bash
uv tree
```

### Environment Guidelines

- Maintain one shared `.venv` for the entire repository.
- Manage dependencies through the root `pyproject.toml`.
- Keep `uv.lock` committed to GitHub.
- Do not commit the `.venv` directory.
- Do not create separate virtual environments inside individual modules.
- Do not use `pip install` for managing project dependencies.
- Use `uv add` whenever a new project dependency is required.
- Run project commands from the repository root for consistency.

For additional information, refer to the [official uv documentation](https://docs.astral.sh/uv/).

---

## Learning Philosophy

This portfolio focuses on understanding concepts through implementation rather than only studying theoretical material.

My approach includes:

- Understanding mathematical foundations before implementation.
- Writing algorithms and functions independently.
- Experimenting with different parameters and configurations.
- Visualizing model behaviour and results.
- Evaluating models using appropriate metrics.
- Documenting challenges, observations, and improvements.

## Future Direction

After completing the foundational modules, the next goal is to strengthen my understanding of classical machine learning, neural networks, and deep learning through practical implementations.

The long-term objective is to develop the knowledge and practical skills required to work as an AI/ML Engineer.
