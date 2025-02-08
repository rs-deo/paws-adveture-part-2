@namespace
class SpriteKind:
    coin = SpriteKind.create()
    FLOWER = SpriteKind.create()
    fireball = SpriteKind.create()
    bee = SpriteKind.create()
    shield = SpriteKind.create()

def on_overlap_tile(sprite, location):
    global curret_level
    curret_level += 1
    destroy()
    start_level()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile2)

def on_up_pressed():
    if mySprite.vy == 0:
        mySprite.vy += -150
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def start_level():
    global mySprite, mySprite2, mySprite3, mySprite5
    if curret_level == 0:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
    elif curret_level == 1:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffff1ffffffffffffffffffffffffff1fffffffffffffffff222228888fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff2222222888888fffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55222222228888822f5ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5552222222228888222255fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55ff22222222888882222f555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ff2222222288888822222ff55ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55ff2222228888888882222fff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5fff2222888888888882222fff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ff2228888888888822222ff5ffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55555555555555555555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888888888888822222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888888888888822222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888888888888222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888888888882222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888888882222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888888822222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffff888888822222222ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888822222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff882222222fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11fffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
        mySprite = sprites.create(img("""
                . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . 1 1 1 . . . 
                            . . . . . . . . . . . 1 f 1 1 1 . 
                            . . . . . . . . . . . 1 f f f 1 1 
                            . . . 1 1 1 1 1 1 1 1 1 f f 8 f 1 
                            1 1 1 1 f f f f f f f f f f f f 1 
                            1 f f f f f f 1 1 1 1 f f f 1 1 1 
                            1 1 1 1 f f 1 1 1 1 1 f f f 1 . . 
                            . . . 1 f 1 f 1 1 1 1 f 1 f 1 . . 
                            . . . 1 f 1 f 1 . . 1 f 1 f 1 . . 
                            . . . 1 f 1 f 1 . . 1 f 1 f 1 . .
            """),
            SpriteKind.player)
    else:
        game.game_over(True)
    info.set_life(9)
    for value in tiles.get_tiles_by_type(assets.tile("""
        coin
    """)):
        mySprite2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . f 5 5 5 5 5 5 5 f . . . 
                            . . . f 5 4 4 4 4 4 5 5 5 f . . 
                            . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                            . . . f 5 5 4 4 5 5 5 5 5 f . . 
                            . . . . f 5 5 5 5 5 5 5 f . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.coin)
        tiles.place_on_tile(mySprite2, value)
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
        animation.run_image_animation(mySprite2,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 4 4 4 4 4 5 5 f . . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . . f 5 5 4 4 5 5 5 5 5 f . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f f . . . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . f 5 5 4 4 4 5 5 f . . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . . f 5 5 4 5 5 5 5 f . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . . . f f f f f . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . f f f . . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . f 5 5 4 5 5 f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . . f f f . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . f 5 4 5 5 5 f . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . . f 5 f . . . . . . 
                                . . . . . . . . f . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . f f f . . . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . f 5 5 4 5 5 f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . f 5 4 5 5 5 5 5 f . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . . . f 5 5 5 f . . . . . 
                                . . . . . . . f f f . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . f f f f f . . . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . f 5 5 4 4 4 5 5 f . . . 
                                . . . f 5 5 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . f 5 4 5 5 5 5 5 5 5 f . . 
                                . . . . f 5 5 4 5 5 5 5 f . . . 
                                . . . . . f 5 5 5 5 5 f . . . . 
                                . . . . . . f f f f f . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . f 5 5 4 4 4 4 4 5 5 f . . 
                                . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                                . . . f 5 5 4 4 5 5 5 5 5 f . . 
                                . . . . f 5 5 5 5 5 5 5 f . . . 
                                . . . . . f f f f f f f . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            200,
            True)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile2
    """)):
        mySprite3 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 3 a . . a 3 . . . . . 
                            . . . . . a 3 4 4 3 a . . . . . 
                            . . . . . . . 3 3 . . . . . . . 
                            . . . . . 7 7 7 . . . . . . . . 
                            . . . . . . . 7 7 7 . . . . . . 
                            . . . . . . . 7 . . . . . . . . 
                            . . . . . . . 7 . . . . . . . .
            """),
            SpriteKind.FLOWER)
        tiles.place_on_tile(mySprite3, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))
    for value3 in tiles.get_tiles_by_type(assets.tile("""
        myTile4
    """)):
        mySprite5 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . 2 2 2 . . . . . . . 
                            . . . . . 2 2 4 2 2 . . . . . . 
                            . . . . 2 2 4 4 4 2 . . . . . . 
                            . . . . 2 2 4 5 4 2 2 . . . . . 
                            . . . . 2 2 4 5 4 4 2 . . . . . 
                            . . . . 2 4 4 8 5 4 4 2 . . . . 
                            . . . . 2 4 5 8 5 5 4 2 . . . . 
                            . . . . 2 4 5 f 5 5 4 2 . . . . 
                            . . . . 2 4 5 8 5 5 4 2 . . . . 
                            . . . . 2 4 5 5 4 4 2 2 . . . . 
                            . . . . 2 4 4 4 4 2 2 . . . . . 
                            . . . . 2 2 4 4 2 . . . . . . . 
                            . . . . 2 2 4 4 2 . . . . . . . 
                            . . . . . 2 4 2 . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.fireball)
        tiles.place_on_tile(mySprite5, value3)
        tiles.set_tile_at(value3, assets.tile("""
            transparency16
        """))
        animation.run_movement_animation(mySprite5, " c 0 -100 0 100 0 0", 2000, True)
        mySprite5.start_effect(effects.fire)
    for value4 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        tiles.place_on_random_tile(mySprite, assets.tile("""
            myTile3
        """))
        tiles.set_tile_at(value4, assets.tile("""
            transparency16
        """))

def on_on_overlap(sprite3, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap)

def on_on_overlap2(sprite4, otherSprite2):
    global mySprite4
    sprites.destroy(otherSprite2)
    mySprite4 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.bee)
    animation.run_image_animation(mySprite4,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . f f f f f f f f . . . . . 
                        . . f 1 1 1 1 1 1 1 1 f . . . . 
                        . . f f 1 1 1 1 1 1 f f . . . . 
                        . . f 1 1 1 1 1 1 1 1 f . . . . 
                        . . . . 1 1 1 1 1 1 . . . . . . 
                        . . . f f f f f f f f . . . . . 
                        . . f 5 5 5 5 5 5 5 5 f . . . . 
                        . . f f 5 5 5 5 5 5 f f . . . . 
                        . . f 5 5 5 5 5 5 5 5 f . . . . 
                        . . . f f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . f f f f f f f f . . . . . 
                        . . f 5 5 5 5 5 5 5 5 f . . . . 
                        . . f f 5 5 5 5 5 5 f f . . . . 
                        . . f 5 5 5 5 5 5 5 5 f . . . . 
                        . . . f f f f f f f f . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
    mySprite4.set_position(mySprite.x + 80, mySprite.y - 80)
    mySprite4.follow(mySprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.FLOWER, on_on_overlap2)

def on_on_overlap3(sprite5, otherSprite3):
    info.change_life_by(-2)
    otherSprite3.start_effect(effects.disintegrate)
    sprites.destroy(otherSprite3)
sprites.on_overlap(SpriteKind.player, SpriteKind.fireball, on_on_overlap3)

def destroy():
    for value5 in sprites.all_of_kind(SpriteKind.bee):
        sprites.destroy(value5)
    for value6 in sprites.all_of_kind(SpriteKind.fireball):
        sprites.destroy(value6)
    for value7 in sprites.all_of_kind(SpriteKind.FLOWER):
        sprites.destroy(value7)

def on_on_overlap4(sprite6, otherSprite4):
    sprites.destroy(otherSprite4)
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . 9 9 9 . . . 
                . . . . . . . . . . . 9 f 9 9 9 . 
                . . . . . . . . . . . 9 f f f 9 9 
                . . . 9 9 9 9 9 9 9 9 9 f f 8 f 9 
                9 9 9 9 f f f f f f f f f f f f 9 
                9 f f f f f f 1 1 1 1 f f f 9 9 9 
                9 9 9 9 f f 1 1 1 1 1 f f f 9 . . 
                . . . 9 f 9 f 9 9 9 9 f 9 f 9 . . 
                . . . 9 f 9 f 9 . . 9 f 9 f 9 . . 
                . . . 9 f 9 f 9 . . 9 f 9 f 9 . . 
                . . . 9 9 9 9 9 . . 9 9 9 9 9 . .
    """))
sprites.on_overlap(SpriteKind.player, SpriteKind.shield, on_on_overlap4)

def on_on_overlap5(sprite7, otherSprite5):
    if mySprite.y < mySprite4.y:
        info.change_score_by(3)
    else:
        info.change_life_by(-1)
    sprites.destroy(otherSprite5)
sprites.on_overlap(SpriteKind.player, SpriteKind.bee, on_on_overlap5)

mySprite4: Sprite = None
mySprite5: Sprite = None
mySprite3: Sprite = None
mySprite2: Sprite = None
curret_level = 0
mySprite: Sprite = None
scene.set_background_color(9)
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999991111111199999999111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999991111111111111119911111111111111111199999999999119999999999999999999999999999999999991111111111999911111111111111999999999999999999999999999
        9999999999999999999911111111111111111911111111111111111111999991111111199999999999999999999999999999999911111111111119911111111111111199999999999999999999999999
        9999999999999999111111111111111111111111111111111111111111111911111111111999999999999999999999999999999911111111111111911111111111111119999999999999999999999999
        9999999999999991111111111111111111111111111111111111111111111111111111111999999999999999999999999999999111111111111111111111111111111111999999999999999999999999
        9999999999999991111111111111111111111111111111111111111111111111111111111199999999999999999999999999999111111111111111111111111111111111119991111119999999999999
        9999999999999991111111111111111111111111111111111111111111111111111111111199999999999999999999999999999111111111111111111111111111111111111991111111119999999999
        9999999999999991111111111111111111111111111111111111111111111111111111111119999999999999999999999999999911111111111111111111111111111111111911111111111199999999
        9999999999999991111111111111111111111111111111111111111111111111111111111119999999999999999999999999999911111111111111111111111111111111111111111111111111999999
        9999999999999999111111111111111111111111111111111111111111111111111111111111999999999999999999999999999991111111111111111111111111111111111111111111111111119999
        9999999999999999111111111111111111111111111111111111111111111111111111111111999999999999999999999999999991111111111111111111111111111111111111111111111111119999
        9999999999999999911111111111111111111111111111111111111111111111111111111111199999999999999999999999999991111111111111111111111111111111111111111111111111119999
        9999999999999999911111111111111111111111111111111111111111111111111111111111199999999999999999999999999999111111111111111111111111111111111111111111111111119999
        9999999999999999911111111111111111111111111111111111111111111111111111111111199999999999999999999999999999111111111111111111111111111111111111111111111111119999
        9999999999999999911111111111111111111111111111111111111111111111111111111111199999999999999999999999999999911111111111111111111111111111111111111111111111199999
        9999999999999999911111111111111111111111111111111111111111111111111111111111999999999999999999999999999999999999111111111111111111111111111111111111111111199999
        9999999999999999911111111111111111111111111111111111111111111111111111111119999999999999999999999999999999999999999999111111111111111111111111111111111111199999
        9999999999999999999911111111111111199999999999999999999999999991111111111999999999999999999999999999999999999999999999999999999911111111111111111111111111199999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999966699999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999966669999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999966666699999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999966666699999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999966666699999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999666666666999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999666666666999999999999999999999999999999999999999999999999996666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999666666666999999999999999999999999999999999999999999999966666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999996666666666699999999999999999999999999999999999999999666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999996666666666699999999999999999999999999999999999999666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999996666666666699999999999999999999999999999999999666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999996666666666669999999999999999999999999999999996666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999996666666666669999999999999999999999999999999666666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999996666666666666699999999999999999999999999966666666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999966666666666666666999999999999999999999996666666666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999666666666666666666669999999999999999999666666666666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999666666666666666666666699999999999999966666666666666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999996666666666666666666666666666699999999666666666666666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999966666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999999966999999999999999999999999999999999999999999999999999999999666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999999966699999999999999999999999999999999999999999999999999999996666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999999666699999999999999999999999999999999999999999999999999999996666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999999666699999999999999999999999999999999999999999999999999999996666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999996666699999999999999999999999999999999999999999999999999999966666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999966666699999999999999999999999999999999999999999999999999999666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999999666666699999999999999999999999999999999999999999999999999999666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999996666666669999999999999999999999999999999999999999999999999996666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999999966666666666999999999999999999999999999999999999999999999999966666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999996666666666666666699999999999999999999999999999999999999999666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999966666666666666666666669999999999999999999999999999999996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999999666666666666666666666666666999999999999999999999999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999996666666666666666666666666666666699999999999999999666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999966666666666666666666666666666666666666999999966666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999999666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9999999666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        9996666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
"""))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . f . . . . 
            . . . . . . . . . . . f f f . . 
            . . . . . . . . . . . f f 8 f . 
            . . . f f f f f f f f f f f f . 
            f f f f f f 1 1 1 1 f f f . . . 
            . . . f f 1 1 1 1 1 f f f . . . 
            . . . f . f . . . . f . f . . . 
            . . . f . f . . . . f . f . . . 
            . . . f . f . . . . f . f . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 0)
scene.camera_follow_sprite(mySprite)
curret_level = 0
start_level()

def on_on_update():
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . f . . . . 
                . . . . . . . . . . . . f f f . . 
                . . . . . . . . . . . . f f 8 f . 
                f f f f f f f f f f f f f f f f . 
                . . . f f f f 1 1 1 f f f . . . . 
                . . . f f f 1 1 1 1 f f f . . . . 
                . . . f . f . . . . f . f . . . . 
                . . . f . f . . . . f . f . . . . 
                . . . f . f . . . . f . f . . . .
    """))
    if mySprite.vy < 0:
        mySprite.set_image(img("""
            . . . . . . . . . . . . f . . . 
                        . . . . . . . . . . . . f f f . 
                        . . . . . . . . . . . . f f 8 f 
                        . . . . . . . . . . . . f f f f 
                        . . . . . . . . . . . f f . . . 
                        . . . . . . . . . . f f f . . . 
                        . . . . . . . . . f f f f f f f 
                        . . . . . . . . f f f f 1 . . . 
                        . . f f f f f f f f 1 1 . . . . 
                        . f . . . f f f f 1 1 . . . . . 
                        f . . . . f . f 1 1 . . . . . . 
                        . . . . f f . f . . . . . . . . 
                        . . . . f . f f . . . . . . . . 
                        . . . . . . f . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    elif mySprite.vy > 0:
        mySprite.set_image(img("""
            f . . . . . . . . . . . . . . . 
                        f f . . . . . . . . . . . . . . 
                        . f . . . . . . . . . . . . . . 
                        . f . . . . . . . . . . . . . . 
                        . f f . . . . . . . . . . . . . 
                        . . f f f f . . . . . . . . . . 
                        . . . f f f f f f . . . . . . . 
                        . . . f f 1 1 f f f . . f . . . 
                        . . f f f f 1 1 f f f f f f f . 
                        . . f . . f 1 1 1 f f f f f 8 f 
                        . . f . . f . . 1 f f f f f f f 
                        . . . . . f . . . f . . f . . . 
                        . . . . . f . . . f . . f . . . 
                        . . . . . . . . . f f . f f . . 
                        . . . . . . . . . . f . . f . . 
                        . . . . . . . . . . . . . . . .
        """))
    else:
        pass
    if (mySprite.is_hitting_tile(CollisionDirection.LEFT) or mySprite.is_hitting_tile(CollisionDirection.LEFT)) and mySprite.vy >= 0:
        mySprite.vy = 0
        mySprite.ay = 0
        mySprite.set_image(img("""
            . . . . . . . . . . f f . . . . 
                        . . . . . . . . . f 8 f . . . . 
                        . . . . . . . . . f f f . . . . 
                        . . . . . . . . f f f f f f f f 
                        . . . . . . . . . . f f f . . . 
                        . . . . . . . . . . f f f f f f 
                        . . . . . . . . . . f 1 1 . . . 
                        . . . . . . . . . . f 1 1 . . . 
                        . . . f . . . . . . f 1 1 . . . 
                        . . . f . . . . . . f 1 1 . . . 
                        . . . f . . . . . . f f 1 . . . 
                        . . . f . . . . . . f f f f f f 
                        . . . f f . . . . . f f f . . . 
                        . . . . f f f f f f f f f f f f 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    else:
        mySprite.ay = 350
    if mySprite.vx < 0 or mySprite.is_hitting_tile(CollisionDirection.LEFT):
        mySprite.image.flip_x()
        mySprite.set_image(mySprite.image)
game.on_update(on_on_update)
