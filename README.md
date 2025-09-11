# Asteroids Game

A classic Asteroids game built with Python and Pygame. Navigate your spaceship through an asteroid field, avoid collisions, and survive as long as possible!

## Features

- **Spaceship Control**: Rotate and move your triangular spaceship using keyboard controls
- **Asteroid Field**: Dynamic asteroid spawning from screen edges with random sizes and velocities
- **Collision Detection**: Circle-based collision detection between player and asteroids
- **Smooth Movement**: 60 FPS gameplay with delta time-based movement
- **Shooting System**: Fire shots to destroy asteroids (in development)

## Controls

- **A/D**: Rotate spaceship left/right
- **W/S**: Move forward/backward
- **Space**: Fire shots (in development)

## Installation

### Prerequisites
- Python 3.13 or higher
- pip or uv package manager

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd asteriods
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install pygame==2.6.1
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Game Configuration

The game settings can be modified in `constants.py`:

- **Screen**: 1280x720 resolution
- **Asteroids**: 3 different sizes (20-60 pixel radius)
- **Spawn Rate**: New asteroid every 0.8 seconds
- **Player**: 20 pixel radius, 200 speed, 300 turn speed
- **Shots**: 5 pixel radius, 500 speed

## Project Structure

```
asteriods/
├── main.py              # Main game loop and initialization
├── player.py            # Player spaceship and shot classes
├── asteroid.py          # Asteroid class
├── asteroidfield.py     # Asteroid spawning and management
├── circleshape.py       # Base class for circular game objects
├── constants.py         # Game configuration constants
├── pyproject.toml       # Project dependencies
└── README.md           # This file
```

## Game Architecture

- **CircleShape**: Base class providing common functionality for circular game objects
- **Player**: Spaceship with rotation, movement, and shooting capabilities
- **Asteroid**: Circular obstacles with random movement patterns
- **AsteroidField**: Manages asteroid spawning from screen edges
- **Main Loop**: Handles input, updates game state, and renders graphics

## Development Status

- ✅ Basic spaceship movement and rotation
- ✅ Asteroid spawning and movement
- ✅ Collision detection
- ✅ Game over on collision
- 🚧 Shooting system (in progress)
- 🚧 Score system
- 🚧 Sound effects
- 🚧 Multiple lives

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
