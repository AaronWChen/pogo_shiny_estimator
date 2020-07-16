# Pokemon Go Shiny Oddity Calculator

This repo contains code for an "oddity" calculator for Pokemon Go (PoGo)! The idea for this project came from my PoGo friend group who commented that I had a very lucky shiny appearance/catch rate. I assumed I was just being lucky with the game's random number generator, but I was extremely curious to do some investigating after I had a streak of 6 days of getting at least one shiny per day.

I figured this would be a fun way to practice some statistics and build a new webapp, so here we are!

## What is Pokemon Go?


## Initial Setup

To utilize this repo, first fork the repo. Then go into your forked copy of the repo's settings, and check the box for "Template repository." This will enable you to quickly use this template in the future.

Once you are ready to use the template to create your own data science repo, click "Use this template" on your forked copy of the repo's homepage. It will copy all of the repo structure and files into a new repo. Clone that repo onto your local machine, and then follow the proceeding instructions to finish setup on your local copy.

## Setting up the src code and customizing the conda environment

The conda environment in `environment.yml` is a starter environment, only for setting up the repo. I include instructions for renaming and customizing the conda environment after the initial installation is complete. Use the following steps to complete the installation of the environment and make code stored in src available as a package.

After cloning the repo, navigate into the repo and run:

```
# create the conda environment
conda env create -f environment.yml

# activate the conda environment
conda activate initial-env
```

Then, to make a copy of the initial-env conda environment and rename it to whatever you want to use as your custom environment name, use the following, replacing `custom-env` with your preferred name.

```
# first make a copy of initial-env 
# (can use the flag --offline if you don't want to redownload packages)
conda create --name custom-env --clone initial-env

# second, delete initial-env
conda remove --name initial-env --all
```

Now you have your own custom conda environment. I suggest running the following lines to make your environment available to Jupyter as a kernel and export your new environment to the `environment.yml` file (remember to rerun the latter as you add more libraries to your environment).

```
# make this conda environment available as a kernel in jupyter
python -m ipykernel install --user --name custom-env --display-name "custom-env"

# export environment.yml file
conda env export > environment.yml
```

If you for some reason you already have a conda environment you want to use with this repo, all you'll need to do is navigate into the repo, activate your environment, and then run `pip install -e .` to set up the src folder.