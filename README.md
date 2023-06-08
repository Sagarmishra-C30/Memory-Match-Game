# Memory Match Game

Memory Match Game is a simple game built using Python and the Tkinter library. The objective of the game is to find matching pairs of images by clicking on buttons. This README file provides an overview of the game and explains how to run it.

## Features

- Grid-based layout of buttons
- Randomized placement of images
- Timer to track the elapsed time
- Statistics display showing the number of moves, pairs selected, and pairs remaining
- End-of-game message box displaying the number of moves

## Requirements

To run the Memory Match Game, you need to have the following installed:

- Python (version 3.6 or higher)
- Tkinter library
- PIL (Python Imaging Library)

## How to Run

1. Clone the repository or download the `MemoryMatchGame.py` file.

2. Open a terminal or command prompt and navigate to the directory containing the `MemoryMatchGame.py` file.

3. Install pillow from *requirements.txt* file:
	
	```
	pip install -r requirements.txt 
	```

4. Run the following command to start the game:

   ```
   python MemoryMatchGame.py
   ```

   This will launch the game window.

## How to Play

1. The game window will display a grid of buttons, each representing a tile.

2. Click on a tile to reveal the image hidden beneath it.

3. Click on another tile to reveal its image.

4. If the images on the two tiles match, they will remain visible, and you can proceed to the next pair.

5. If the images on the two tiles do not match, they will be hidden again.

6. Continue revealing tiles and finding matching pairs until all pairs are found.

7. After finding all pairs, a message box will display the number of moves made.

8. Click "OK" in the message box to exit the game.


## Customization

You can customize the game by modifying the following aspects:

- Images: Add or replace the images in the `img` folder. The game supports any size of images (best option includes type: png, ratio: 150x150), and their file names should be added to the `all_images` list in the `MemoryMatchGame.py` file.

- Grid Size: You can modify the grid size by changing the values of the `range()` functions in the for loop. By default, it creates a 6x4 grid.

- Button Appearance: You can customize the button size, border width, relief style, and other properties by modifying the `Button` constructor parameters inside the for loop.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

The Memory Match Game is inspired by various memory matching games and is created for educational purposes.


## Contributing

Contributions to the Memory Match Game project are welcome and encouraged! If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

Please ensure that your code adheres to the existing coding style and conventions used in the project. Also, make sure to include appropriate tests for your changes if applicable.

### Ways to Contribute

You can contribute to the project in various ways, including but not limited to:

- Adding new features or enhancements to the game
- Fixing bugs or issues
- Improving the user interface and experience
- Optimizing the code for better performance
- Writing documentation and examples

Before starting to work on a significant feature or change, it is recommended to open an issue to discuss the proposed changes with the project maintainers and gather feedback.

Thank you for considering contributing to the Memory Match Game project! Your efforts are greatly appreciated.

---
Have fun playing the Memory Match Game! If you have any questions or feedback, please feel free to contact me.