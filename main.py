stars: List[Sprite] = []
starsnumber = 0

while starsnumber < 10:
    
    star = sprites.create(img("""
        . . . . . . . b b . . . . . . .
        . . . . . . b d d b . . . . . .
        . . . . . b d 5 5 d b . . . . .
        . . . . b b 5 5 5 5 b b . . . .
        . . . . b 5 5 5 5 5 5 b . . . .
        b b b b b 5 5 5 5 1 1 d b b b b
        b 5 5 5 5 5 5 5 5 1 1 1 5 5 5 b
        b d d 5 5 5 5 5 5 1 1 1 5 d d b
        . b d d 5 5 5 5 5 5 5 5 d d b .
        . . b b 5 5 5 5 5 5 5 5 b b . .
        . . c b 5 5 5 5 5 5 5 5 b c . .
        . . c 5 5 5 5 d d 5 5 5 5 c . .
        . . c 5 5 d b b b b d 5 5 c . .
        . . c 5 d b c c c c b d 5 c . .
        . . c c c c . . . . c c c c . .
        . . . . . . . . . . . . . . . .
        """), SpriteKind.food) 

    star.set_position(randint(0, screen.width), randint(0, screen.height))
    stars.append(star)
    pause(100)
    starsnumber += 1

starsnumber = 0
while starsnumber < len(stars):
    star = stars[starsnumber]
    star.set_flag(SpriteFlag.INVISIBLE, True)
    pause(100)
    starsnumber += 1