# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.


## Setup
Create the environment for a given lab:

conda env create -f PW1/Lab\ A/environment.yml
conda activate cspc


## PW1 - Lab A: Reproducible Foundations

**What i built:**
    1. I built my personal CSPC course repository with conda environment.
    2. Decay simulations.
    3. Pytest for testing simulations.
    4. Speed comparison for Numpy and Loop version.

**Speed comparison results:**
    -Loop time: 2.2309
    -NumPy time: 0.0002
    -NumPy is 13083.0x faster than Loop time.

**Test results:**
    -All three tests passed.


**Conclusion:**

    In this PW i learned how to install conda environment and how to work with it. I published my program on GitHub and I also learned how Git branches work. I made a branch, worked on it, committed my changes, and then merged it back into main.

    One problem I had was with my test_matches_law test. it failed the first time because I only used 50 seeds, and the average was not close to the expected value. I fixed it by using more seeds, and then it passed.

## PW1 - Lab B: Data, Plotting, and Automation

**What i built:**
    1. I read the observed decay data (decay_observed.csv) and plotted it next to the analytical decay law N0*exp(-lambda*t), with lambda = 0.3.
    2. I built a 1x2 figure with shared axes, so the observed points and analytical curve are directly comparable.
    3. I automated the figure generation with a Snakemake pipeline (Snakefile).

**Result:**
    The observed data [closely followed / showed noticeable scatter around] the analytical curve, confirming the data is consistent with exponential decay.

**Snakemake pipeline:**
    The Snakefile defines one rule that runs plot.py to build figure.png from decay_observed.csv. It compares file timestamps, so it only reruns plot.py when the CSV (or missing output) makes the figure out of date, and does nothing when nothing changed.

**Conclusion:**

    In this PW i learned how to read a CSV file into NumPy arrays and plot real data against a theoretical model using shared axes for a fair comparison. I also learned how Snakemake pipelines work: defining rules with input, output and shell, and how it uses timestamps to avoid rerunning steps that are already up to date.

    One problem I had was installing snakemake with conda, since it was not found in the conda-forge channel on its own. I fixed it by installing matplotlib with conda and snakemake with pip instead.

