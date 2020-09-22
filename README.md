# Linear Particle Chamber Animation Project

## Running the project locally

* Clone this repo and `cd` into the project root
* Run `python animate.py <speed> <initial_positions>`
    * Example: `python animate.py 2 LRLR.LRLR`
    * Note: speed must be `>= 1` and `<= 10`.
    * Notes:
        * speed must be `>= 1` and `<= 10`.
        * `initial_positions` must be between 1 and 50 characters long and contain only `R`, `L`, or `.` characters.
    * Example:

            % python animate.py 2 LRLR.LRLR
            XXXX.XXXX
            X..X.X..X
            .X.X.X.X.
            .X.....X.
            .........

## Running tests

* Run `python -m unittest discover -v tests` in the project root
