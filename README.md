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

## PW2 --- Lab A

**Mean acceleration:**
-8.58 m/s² (std 28.7 m/s²). This is consistent with -9.81 m/s²
within the sampling uncertainty, because the noise is so large.

**Why the acceleration is noisy:**
each derivative divides the small difference between
neighbouring noisy measurements by the tiny time step (0.1 s), which amplifies the noise,
and I did this twice, while the position itself was never differentiated.

**Integrating back:**
integrating the noisy acceleration twice recovered the position to
within 0.78 m of the original. Integration sums many values, so the random noise largely
cancels. Differentiation amplifies noise; integration suppresses it.

![Motion](PW2/Lab%20A/motion.png)

**Bonus (2D trajectory):** I differentiated x and y separately with `np.gradient` and
combined them into the speed sqrt(vx² + vy²). The path is smooth, but the speed is noisy
because it comes from a derivative of noisy positions.

## PW2 --- Lab B

**What i built:**
    1. I compared gradient descent, Newton's method and SLSQP on an easy function and a harder one (warmup.py).
    2. I fitted the rate constant of a first-order reaction to noisy data (kinetics.py).
    3. I found the equilibrium of H2 + I2 <=> 2 HI in two ways (equilibrium.py).
    4. Bonus: I located a titration's equivalence point from the slope of the pH curve (titration.py).

**Part 2: three methods:**
    -On f(x) = (x-3)^2 + 1, all three methods reach x = 3.
    -On g(x) = x^4 - 3x^2 + x + 5 they disagree. From x0 = 0, gradient descent and SLSQP find the global minimum at x = -1.30, but Newton lands on x = 0.17, which is a maximum (g'' < 0), because Newton only finds stationary points.
    -From x0 = 2, gradient descent and Newton get stuck in the local minimum at x = 1.13 (g'' > 0), while SLSQP reaches the global minimum at x = -1.30.
    -So on a complicated landscape, the starting point and the algorithm both change the result.

**Part 3: reaction rate:**
    -Fitted k = 0.262 (expected about 0.25).
    -The difference comes from measurement noise, including noise in the first point used as C0.

![Kinetics](PW2/Lab%20B/kinetics.png)

**Part 4: equilibrium (K = 15.6):**
    -Newton and SLSQP agree: x = 0.664.
    -H2 = I2 = 0.336 mol and HI = 1.328 mol.

![Equilibrium](PW2/Lab%20B/equilibrium.png)

**Part 5 (bonus): titration:**
    -The equivalence point is at 50.0 mL, where the pH curve jumps and its slope is largest.

![Titration](PW2/Lab%20B/titration.png)

**Conclusion:**

    In this PW i learned that optimization appears all over chemistry: fitting a rate constant, solving for an equilibrium, and finding a titration's equivalence point. I learned that on a simple convex function every method works, but on a complicated one the starting point and the algorithm matter, and that Newton's method can land on a maximum, so I have to check the sign of the second derivative. I also saw that the same equilibrium can be found by root-finding (Newton) or by minimizing the squared imbalance (SLSQP).

    One problem I had was with equilibrium.py: the return line of my function was not indented, which gave an IndentationError, and I fixed it by indenting it. I also first ran the scripts from the wrong folder, and I fixed it by moving into PW2/Lab B before running them.

    