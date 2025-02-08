namespace SpriteKind {
    export const coin = SpriteKind.create()
    export const FLOWER = SpriteKind.create()
    export const fireball = SpriteKind.create()
    export const bee = SpriteKind.create()
    export const shield = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    curret_level += 1
    destroy()
    start_level()
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy += -150
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.FLOWER, function (sprite4, otherSprite2) {
    sprites.destroy(otherSprite2)
    mySprite4 = sprites.create(img`
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
        `, SpriteKind.bee)
    animation.runImageAnimation(
    mySprite4,
    [img`
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
        `,img`
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
        `],
    200,
    true
    )
    mySprite4.setPosition(mySprite.x + 80, mySprite.y - 80)
    mySprite4.follow(mySprite)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.coin, function (sprite3, otherSprite) {
    info.changeScoreBy(1)
    sprites.destroy(otherSprite)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite2, location2) {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.bee, function (sprite7, otherSprite5) {
    if (mySprite.y < mySprite4.y) {
        info.changeScoreBy(3)
    } else {
        info.changeLifeBy(-1)
    }
    sprites.destroy(otherSprite5)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.shield, function (sprite6, otherSprite4) {
    sprites.destroy(otherSprite4)
    mySprite.setImage(img`
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
        `)
})
function start_level () {
    if (curret_level == 0) {
        tiles.setCurrentTilemap(tilemap`level1`)
    } else if (curret_level == 1) {
        tiles.setCurrentTilemap(tilemap`level2`)
        scene.setBackgroundImage(img`
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
            `)
        mySprite = sprites.create(img`
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
            `, SpriteKind.Player)
    } else {
        game.gameOver(true)
    }
    info.setLife(9)
    for (let value of tiles.getTilesByType(assets.tile`coin`)) {
        mySprite2 = sprites.create(img`
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
            `, SpriteKind.coin)
        tiles.placeOnTile(mySprite2, value)
        tiles.setTileAt(value, assets.tile`transparency16`)
        animation.runImageAnimation(
        mySprite2,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    }
    for (let value2 of tiles.getTilesByType(assets.tile`myTile2`)) {
        mySprite3 = sprites.create(img`
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
            `, SpriteKind.FLOWER)
        tiles.placeOnTile(mySprite3, value2)
        tiles.setTileAt(value2, assets.tile`transparency16`)
    }
    for (let value3 of tiles.getTilesByType(assets.tile`myTile4`)) {
        mySprite5 = sprites.create(img`
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
            `, SpriteKind.fireball)
        tiles.placeOnTile(mySprite5, value3)
        tiles.setTileAt(value3, assets.tile`transparency16`)
        animation.runMovementAnimation(
        mySprite5,
        " c 0 -100 0 100 0 0",
        2000,
        true
        )
        mySprite5.startEffect(effects.fire)
    }
    for (let value4 of tiles.getTilesByType(assets.tile`myTile3`)) {
        tiles.placeOnRandomTile(mySprite, assets.tile`myTile3`)
        tiles.setTileAt(value4, assets.tile`transparency16`)
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.fireball, function (sprite5, otherSprite3) {
    info.changeLifeBy(-2)
    otherSprite3.startEffect(effects.disintegrate)
    sprites.destroy(otherSprite3)
})
function destroy () {
    for (let value5 of sprites.allOfKind(SpriteKind.bee)) {
        sprites.destroy(value5)
    }
    for (let value6 of sprites.allOfKind(SpriteKind.fireball)) {
        sprites.destroy(value6)
    }
    for (let value7 of sprites.allOfKind(SpriteKind.FLOWER)) {
        sprites.destroy(value7)
    }
}
let mySprite5: Sprite = null
let mySprite3: Sprite = null
let mySprite2: Sprite = null
let mySprite4: Sprite = null
let curret_level = 0
let mySprite: Sprite = null
scene.setBackgroundColor(9)
scene.setBackgroundImage(img`
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
    `)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 0)
scene.cameraFollowSprite(mySprite)
curret_level = 0
start_level()
game.onUpdate(function () {
    mySprite.setImage(img`
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
        `)
    if (mySprite.vy < 0) {
        mySprite.setImage(img`
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
            `)
    } else if (mySprite.vy > 0) {
        mySprite.setImage(img`
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
            `)
    } else {
    	
    }
    if ((mySprite.isHittingTile(CollisionDirection.Left) || mySprite.isHittingTile(CollisionDirection.Left)) && mySprite.vy >= 0) {
        mySprite.vy = 0
        mySprite.ay = 0
        mySprite.setImage(img`
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
            `)
    } else {
        mySprite.ay = 350
    }
    if (mySprite.vx < 0 || mySprite.isHittingTile(CollisionDirection.Left)) {
        mySprite.image.flipX()
        mySprite.setImage(mySprite.image)
    }
})
