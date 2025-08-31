from utils import crud

# Add new player
print(crud.add_player("MS Dhoni", "Wicket-keeper", "Right-hand bat", "None"))

# View all players
print("Players:", crud.view_players())

# Update player
print(crud.update_player(1, "Virat Kohli", "Batsman", "Right-hand bat", "Right-arm medium"))

# Delete player
print(crud.delete_player(2))  # deletes Jasprit Bumrah (player_id=2)

# View again
print("Players after update/delete:", crud.view_players())
