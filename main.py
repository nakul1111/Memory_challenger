from game import game

gm = game()
try:
    gm.main()
except Exception as e:
    print(f"Error: {e}")