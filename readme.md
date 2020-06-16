# Batkill 
This is a WIP game built on pygame with the aim of developing a sufficiently difficult game so that a well trained 
reinforcement learning algo can outperform the average human.

# Set-up
Python 3.7 only I'm afraid, due to incompatibilities between stable-baselines and tensorflow. Other than that, `pip install -r requirements.txt` 
and you're good to go.

## Playing the game
Run `play.py` WASD to move and jump, and space to attack.

## Training the model
Run `model_train.py`, and it should start reporting, you'll just see a black screen, that's expected, don't close it. There are a few variables here that you may want to play with:
```python
model_storage_dir = 'nn_models'
max_bats = 2
allow_jump = False
timestep_checkpoint = 10000
baseline_model = PPO2
baseline_policy = MlpPolicy
verbosity = 1
```
- `model_storage_dir`: Where the models will be stored
- `max_bats`: Maximum number of bats on the screen at any given point
- `allow_jump`: Whether the player is allowed to jump, adds a lot of complexity
- `timestep_checkpoint`: How often to save the model to disk
- `baseline_model`: Stable Baselines Model to use
- `baseline_policy`: Stable Baselines Policy to use
- `verbosity`: Model training verbosity level
## Evaluating the model (Seing the AI play!)
Run `model_evaluate.py` and it should pick up the latest model and start playing. Every time the player dies it'll look 
for a newer model, so you can evaluate whilst you train and see the "progress".

The number of max_bats, allow_jump the baseline_model should be the same as on the trained model, but it'll break hard otherwise, so you'll know.

# Sprite credits
Forest background: [edermunizz](https://edermunizz.itch.io/free-pixel-art-forest), [CC BY-ND](https://creativecommons.org/licenses/by-nd/4.0)  

Adventurer: [rvros](https://rvros.itch.io/), [No resale, no redistribution](https://rvros.itch.io/animated-pixel-hero)

Bat: [OcO](https://oco.itch.io/), [No resale](https://oco.itch.io/medieval-fantasy-character-pack)