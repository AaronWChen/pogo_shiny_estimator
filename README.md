# Pokemon Go Shiny Oddity Calculator

This repo contains code for an "oddity" calculator for Pokemon Go (PoGo)! The idea for this project came from my PoGo friend group who commented that I had a very lucky shiny appearance/catch rate. I assumed I was just being lucky with the game's random number generator, but I was extremely curious to do some investigating after I had a streak of 6 days of getting at least one shiny per day.

I figured this would be a fun way to practice some statistics and build a new webapp, so here we are!

## What is Pokemon Go?

More information can be found [here](https://pokemongolive.com/en/) if you've never played or heard of the game. I am a recent player who started in January 2020, although the game debuted in 2016.

I started playing because I liked the idea of walking around and seeing Pokemon! Plus, I was on the job hunt and thought it was something nice to use as a break from applications, networking, and studying.

## What are Shinies?

Each Pokemon species has an originally designed color palette. However, one can occasionally find versions with different colors! One of the most obvious is the duck Pokemon Psyduck. In its normal appearance, it is a yellow duck, but the shiny form is blue!

These [shiny forms](https://bulbapedia.bulbagarden.net/wiki/Shiny_Pok%C3%A9mon) are generally extremely rare: in the mainstream Pokemon games, one had a 1/8192 chance of seeing one originally and then that was increased to 1//4096! In this context, Pokemon Go is nicer to players as the shiny appearance rate is dramatically increased to an estimated 1/500.

## Wait so why make this?

Well, a few of my friends were lamenting their shiny luck. Players with older accounts would say that they could go weeks without seeing a shiny. Or even other new players wondered how I was able to get particularly rare Pokemon as shiny. For example, in my area, Slakoth almost never spawns, yet I got a shiny literally at my house with less than 10 appearances. I have 2 shiny Gible with less than 20 appearances. And I got a shiny Pineco on it's 7th appearance (a hatch). I didn't really think about it too much since I always thought of it as chance. I've also had weeks without a shiny, and my total shiny amount is pretty low. However, I did have a 6 day long streak where I caught a total of 10 shinies and it made me think about how rare that streak could be.

## How to use

The goal is to get this converted to a webapp, but currently, it has to be deployed locally and run with Jupyter Notebook. There are two options:

## Fork and Clone

### Initial Setup

To utilize this repo, first fork the repo. After forking, you can clone your fork to your computer via normal git clone methods. The repo contains a custom environment in both conda and pip flavors

#### Using conda environment

If you have conda already installed, you can run

```
conda env create -f environment.yml
```

from the repo's base directory to use the same environment I have.

#### Using pip

If you are using pip, you can run 

```
pip install requirements.txt
```

from the repo's base directory to use the same environment I have.

### Make this conda environment available as a kernel in jupyter

Once you've gotten the environment set up, you can run the following in your terminal 
```python -m ipykernel install --user --name pogo_shiny --display-name "PoGo_Shiny_Env"```

### Run!

Once all that is set up, you can open a terminal in the repo's notebooks folder, type
``` jupyter notebook``` and opening the ```pogo_shiny_predictor.ipynb``` file