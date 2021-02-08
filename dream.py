from big_sleep import Imagine

dream = Imagine(
    text = "put the hand on the metal and feel it",
    lr = 5e-2,
    save_every = 25,
    save_progress = True,
    epochs= 2
)

dream()
