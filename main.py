@namespace
class SpriteKind:
    NPC1 = SpriteKind.create()
    NPC2 = SpriteKind.create()
    NPC3 = SpriteKind.create()
    NPC4 = SpriteKind.create()
    NPC5 = SpriteKind.create()
    NPC6 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            1,
            255,
            0,
            153,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
    game.splash("The Great Wall of China is one of the most famous ancient city walls in the world")
    effects.blizzard.end_screen_effect()
    effects.none.start_screen_effect()
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC5, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    music.play(music.create_sound_effect(WaveShape.TRIANGLE,
            4906,
            1046,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    game.splash("Blue and white porcelain is a famous porcelain in China")
    effects.star_field.end_screen_effect()
    effects.bubbles.start_screen_effect()
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC2, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    music.play(music.create_sound_effect(WaveShape.TRIANGLE,
            4906,
            1046,
            255,
            0,
            150,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    game.splash("Taoism and Buddhism are the two major religions in China")
    effects.bubbles.end_screen_effect()
    effects.clouds.start_screen_effect()
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC3, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    game.splash("China has a history of more than five thousand years")
    effects.clouds.end_screen_effect()
    effects.blizzard.start_screen_effect()
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC4, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    game.splash("The Spring Festival is the most important traditional festival in China")
    effects.star_field.start_screen_effect()
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC1, on_on_overlap5)

def on_on_overlap6(sprite6, otherSprite6):
    mySprite.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC6, on_on_overlap6)

def on_overlap_tile(sprite7, location):
    game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile)

mySprite: Sprite = None
game.show_long_text("Mini-MazeGame produced by Miaomiao", DialogLayout.CENTER)
music.play(music.melody_playable(music.power_up),
    music.PlaybackMode.UNTIL_DONE)
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
tiles.set_tilemap(tilemap("""
    级别1
"""))
tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_red_crystal)
scene.camera_follow_sprite(mySprite)
info.start_countdown(300)
NPC22 = sprites.create(img("""
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
    """),
    SpriteKind.NPC1)
tiles.place_on_random_tile(NPC22, sprites.dungeon.chest_open)
NPC32 = sprites.create(img("""
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
    """),
    SpriteKind.NPC2)
tiles.place_on_random_tile(NPC32, sprites.dungeon.green_outer_south2)
NPC52 = sprites.create(img("""
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
    """),
    SpriteKind.NPC3)
tiles.place_on_random_tile(NPC52, sprites.dungeon.green_outer_east2)
NPC62 = sprites.create(img("""
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
    """),
    SpriteKind.NPC4)
tiles.place_on_random_tile(NPC62, sprites.dungeon.purple_switch_up)
NPC7 = sprites.create(img("""
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
    """),
    SpriteKind.NPC5)
tiles.place_on_random_tile(NPC7, sprites.dungeon.stair_ladder)
NPC8 = sprites.create(img("""
        . . . . . . . . b b b b . . . . 
            . . . . b b b b 3 3 3 3 b . . . 
            . c c b b 1 1 3 3 3 3 3 b b . . 
            c c 3 3 1 1 3 3 3 3 3 1 1 b . . 
            c b 3 3 3 3 3 3 3 3 3 1 1 b . . 
            f b b c c c 3 3 3 3 3 3 3 c . . 
            f b c c c b b b b 3 3 3 3 3 c . 
            f b c c d d d d d b b 3 3 3 3 c 
            . c c d c d d d d d d b c 3 3 c 
            . c b d c d d d c d d c c c 3 f 
            . f d d d d d c d d d c c c b f 
            . f d b b b d d d d d c c c b f 
            . . c d d d d d d d b c b b f f 
            . . f f d d d d c c b f f f f . 
            . f f b b f f c c b d d b f . . 
            . f b b b f f . . b d d d f . .
    """),
    SpriteKind.NPC6)
animation.run_movement_animation(NPC8,
    animation.animation_presets(animation.ease_up),
    2000,
    True)
tiles.place_on_random_tile(NPC8, sprites.castle.tile_grass2)