namespace SpriteKind {
    export const NPC1 = SpriteKind.create()
    export const NPC2 = SpriteKind.create()
    export const NPC3 = SpriteKind.create()
    export const NPC4 = SpriteKind.create()
    export const NPC5 = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC5, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Sine, 5000, 1, 255, 0, 153, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
    game.splash("The Great Wall of China is one of the most famous ancient city walls in the world")
    effects.blizzard.endScreenEffect()
    effects.none.startScreenEffect()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC2, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Triangle, 4906, 1046, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    game.splash("Blue and white porcelain is a famous porcelain in China")
    effects.starField.endScreenEffect()
    effects.bubbles.startScreenEffect()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC3, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Triangle, 4906, 1046, 255, 0, 150, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    game.splash("Taoism and Buddhism are the two major religions in China")
    effects.bubbles.endScreenEffect()
    effects.clouds.startScreenEffect()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC4, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    game.splash("China has a history of more than five thousand years")
    effects.clouds.endScreenEffect()
    effects.blizzard.startScreenEffect()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.NPC1, function (sprite, otherSprite) {
    music.play(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    game.splash("The Spring Festival is the most important traditional festival in China")
    effects.starField.startScreenEffect()
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite, location) {
    game.over(true, effects.confetti)
})
music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
let mySprite = sprites.create(img`
    . . . . . . 5 . 5 . . . . . . . 
    . . . . . f 5 5 5 f f . . . . . 
    . . . . f 1 5 2 5 1 6 f . . . . 
    . . . f 1 6 6 6 6 6 1 6 f . . . 
    . . . f 6 6 f f f f 6 1 f . . . 
    . . . f 6 f f d d f f 6 f . . . 
    . . f 6 f d f d d f d f 6 f . . 
    . . f 6 f d 3 d d 3 d f 6 f . . 
    . . f 6 6 f d d d d f 6 6 f . . 
    . f 6 6 f 3 f f f f 3 f 6 6 f . 
    . . f f d 3 5 3 3 5 3 d f f . . 
    . . f d d f 3 5 5 3 f d d f . . 
    . . . f f 3 3 3 3 3 3 f f . . . 
    . . . f 3 3 5 3 3 5 3 3 f . . . 
    . . . f f f f f f f f f f . . . 
    . . . . . f f . . f f . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
tiles.setTilemap(tilemap`级别1`)
tiles.placeOnRandomTile(mySprite, sprites.dungeon.collectibleRedCrystal)
scene.cameraFollowSprite(mySprite)
info.startCountdown(300)
let NPC2 = sprites.create(img`
    ........................
    ........................
    ........................
    ........................
    ..........ffff..........
    ........ff1111ff........
    .......fb111111bf.......
    .......f11111111f.......
    ......fd11111111df......
    ......fd11111111df......
    ......fddd1111dddf......
    ......fbdbfddfbdbf......
    ......fcdcf11fcdcf......
    .....ffff111111bf.......
    ....fc111cdb1bdfff......
    ....f1b1bcbfbfc111cf....
    ....fbfbfbffff1b1b1f....
    .........fffffffbfbf....
    ..........fffff.........
    ...........fff..........
    ........................
    ........................
    ........................
    ........................
    `, SpriteKind.NPC1)
tiles.placeOnRandomTile(NPC2, sprites.dungeon.chestOpen)
let NPC3 = sprites.create(img`
    e e e . . . . e e e . . . . 
    c d d c . . c d d c . . . . 
    c b d d f f d d b c . . . . 
    c 3 b d d b d b 3 c . . . . 
    f b 3 d d d d 3 b f . . . . 
    e d d d d d d d d e . . . . 
    e d f d d d d f d e . b f b 
    f d d f d d f d d f . f d f 
    f b d d b b d d 2 f . f d f 
    . f 2 2 2 2 2 2 b b f f d f 
    . f b d d d d d d b b d b f 
    . f d d d d d b d d f f f . 
    . f d f f f d f f d f . . . 
    . f f . . f f . . f f . . . 
    `, SpriteKind.NPC2)
tiles.placeOnRandomTile(NPC3, sprites.dungeon.greenOuterSouth2)
let NPC5 = sprites.create(img`
    ...bbbbbbbbbb...
    ..b1111111111b..
    .b111111111111b.
    .b111111111111b.
    .bddccccccccddb.
    .bdc66666666cdb.
    .bdc61d66666cdb.
    .bdc6d666666cdb.
    .bdc66666666cdb.
    .bdc66666666cdb.
    .bdc66666666cdb.
    .bddccccccccddb.
    .cbbbbbbbbbbbbc.
    fccccccccccccccf
    fbbbbbbbbbbbbbbf
    fbcdddddddddddbf
    fbcbbbbbbbbbbcbf
    fbcbbbbbbbbbbcbf
    fbccccccccccccbf
    fbbbbbbbbbbbbbbf
    fbffffffffffffbf
    ffffffffffffffff
    `, SpriteKind.NPC3)
tiles.placeOnRandomTile(NPC5, sprites.dungeon.greenOuterEast2)
let NPC6 = sprites.create(img`
    ....................
    ....................
    ....................
    ....................
    ....................
    ...........444......
    ..........4eee4.....
    ..........44444.....
    ...........444......
    .....444....7.......
    ....4eee4...7.......
    ....44444..77.7.....
    .....444...7766.....
    ......7....766......
    .......7...76.......
    .....7777..7........
    ......6667.6........
    .........666........
    ....................
    ....................
    `, SpriteKind.NPC4)
tiles.placeOnRandomTile(NPC6, sprites.dungeon.purpleSwitchUp)
let NPC7 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . c c . . . . 
    . . . . . . c c c c 6 3 c . . . 
    . . . . . c 6 6 3 3 3 6 c . . . 
    . . . . c 6 6 3 3 3 3 3 3 c . . 
    b c c c 6 6 c c 3 3 3 3 3 3 c . 
    b 5 5 c 6 c 5 5 c 3 3 3 3 3 c . 
    f f 5 c 6 c 5 f f 6 3 3 3 c c . 
    f f 5 c c c 5 f f 6 6 6 6 c c . 
    . b 5 5 3 5 5 c 3 3 3 3 3 3 c . 
    . c 5 5 5 5 4 c c c 3 3 3 3 c . 
    . c 4 5 5 4 4 b 5 5 c 3 3 c . . 
    . c 5 b 4 4 b b 5 c b b c . . . 
    . c c 5 4 c 5 5 5 c c 5 c . . . 
    . . . c c 5 5 5 5 c c c c . . . 
    . . . . c c c c c c . . . . . . 
    `, SpriteKind.NPC5)
tiles.placeOnRandomTile(NPC7, sprites.dungeon.stairLadder)
