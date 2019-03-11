# Create virtual environment to run experiment
conda create --name dotExperiment python=3.6
conda activate dotExperiment

# Install pygame
python -m pip install -U pygame --user

# Run ex
python dotExp.py
