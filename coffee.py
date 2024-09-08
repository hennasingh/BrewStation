import time

# Define the frames of the coffee mug filling up
frames = [
    """
     .-^-.
    |     |
    |     |
    |     |
    |     |
    |_____|
    """,
    """
     .-^-.
    |     |
    |     |
    |     |
    |  ~  |
    |_____|
    """,
    """
     .-^-.
    |     |
    |     |
    |  ~  |
    |  ~  |
    |_____|
    """,
    """
     .-^-.
    |     |
    |  ~  |
    |  ~  |
    |  ~  |
    |_____|
    """,
    """
     .-^-.
    |  ~  |
    |  ~  |
    |  ~  |
    |  ~  |
    |_____|
    """,
    """
     .-^-.
    | ~~~ |
    |  ~  |
    |  ~  |
    |  ~  |
    |_____|
    """,
    """
     .-^-.
    | ~~~ |
    | ~~~ |
    |  ~  |
    |  ~  |
    |_____|
    """,
    """
     .-^-.
    | ~~~ |
    | ~~~ |
    | ~~~ |
    |  ~  |
    |_____|
    """,
    """
     .-^-.
    | ~~~ |
    | ~~~ |
    | ~~~ |
    | ~~~ |
    |_____|
    """
]


def fill_coffee_mug():
    """
    The function creates a filling coffee animation without
    clearing the console
    """
    # Move down to create space for the mug
    print("\n" * (len(frames[0].splitlines()) - 1))
    for frame in frames:
        # Move the cursor back to the top of the mug
        print("\033[F" * (len(frames[0].splitlines()) - 1), end="")
        print(frame, end="")
        time.sleep(0.5)
