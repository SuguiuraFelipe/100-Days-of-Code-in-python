# Modifying Global Scope

enemies = 1

#Pior jeito
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Melhor jeito
def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemy = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


