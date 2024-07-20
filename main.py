import math
import arcade

# Movement constants
ROTATIONSPEED = 0.02
MOVESPEED = 0.03

# Trigeometric tuples + variables for index
TGM = (math.cos(ROTATIONSPEED), math.sin(ROTATIONSPEED))
ITGM = (math.cos(-ROTATIONSPEED), math.sin(-ROTATIONSPEED))
COS, SIN = (0, 1)

# A map over the world
WORLD_MAP = [
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 3, 0, 0, 2],
    [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 3, 1, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 1, 2, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
    [2, 3, 1, 0, 0, 2, 0, 0, 2, 1, 3, 2, 0, 2, 0, 0, 3, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 0, 1, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]


class App(arcade.Window):
    def __init__(self):
        super().__init__()

        # Defines starting position and direction
        self.position_x = 3.0
        self.position_y = 7.0
        self.direction_x = 1.0
        self.direction_y = 0.0
        self.plane_x = 0.0
        self.plane_y = 0.5

        # Define moves
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

        # Define lines to draw
        self.lines = []

    def on_draw(self):
        self.clear()
        for line in self.lines:
            arcade.draw_line(start_x=line[0], start_y=line[1], end_x=line[2], end_y=line[3], color=line[4], line_width=2)

    def on_update(self, delta_time):

        if self.move_up:
            if not WORLD_MAP[int(self.position_x + self.direction_x * MOVESPEED)][int(self.position_y)]:
                self.position_x += self.direction_x * MOVESPEED
            if not WORLD_MAP[int(self.position_x)][int(self.position_y + self.direction_y * MOVESPEED)]:
                self.position_y += self.direction_y * MOVESPEED
        elif self.move_down:
            if not WORLD_MAP[int(self.position_x - self.direction_x * MOVESPEED)][int(self.position_y)]:
                self.position_x -= self.direction_x * MOVESPEED
            if not WORLD_MAP[int(self.position_x)][int(self.position_y - self.direction_y * MOVESPEED)]:
                self.position_y -= self.direction_y * MOVESPEED
        elif self.move_left:
            old_direction_x = self.direction_x
            self.direction_x = self.direction_x * ITGM[COS] - self.direction_y * ITGM[SIN]
            self.direction_y = old_direction_x * ITGM[SIN] + self.direction_y * ITGM[COS]
            old_plane_x = self.plane_x
            self.plane_x = self.plane_x * ITGM[COS] - self.plane_y * ITGM[SIN]
            self.plane_y = old_plane_x * ITGM[SIN] + self.plane_y * ITGM[COS]
        elif self.move_right:
            old_direction_x = self.direction_x
            self.direction_x = self.direction_x * TGM[COS] - self.direction_y * TGM[SIN]
            self.direction_y = old_direction_x * TGM[SIN] + self.direction_y * TGM[COS]
            old_plane_x = self.plane_x
            self.plane_x = self.plane_x * TGM[COS] - self.plane_y * TGM[SIN]
            self. plane_y = old_plane_x * TGM[SIN] + self.plane_y * TGM[COS]

        if not self.lines or (self.move_up or self.move_down or self.move_left or self.move_right):
            # Starts drawing level from 0 to < self.width
            column = 0
            self.lines = []
            while column < self.width:
                camera_x = 2.0 * column / self.width - 1.0
                ray_position_x = self.position_x
                ray_position_y = self.position_y
                ray_direction_x = self.direction_x + self.plane_x * camera_x
                ray_direction_y = self.direction_y + self.plane_y * camera_x + .000000000000001  # avoiding ZDE

                # In what square is the ray?
                map_x = int(ray_position_x)
                map_y = int(ray_position_y)

                # Delta distance calculation
                # Delta = square ( raydir * raydir) / (raydir * raydir)
                delta_distance_x = math.sqrt(1.0 + (ray_direction_y * ray_direction_y) / (ray_direction_x * ray_direction_x))
                delta_distance_y = math.sqrt(1.0 + (ray_direction_x * ray_direction_x) / (ray_direction_y * ray_direction_y))

                # We need side_distance_x and Y for distance calculation. Checks quadrant
                if ray_direction_x < 0:
                    step_x = -1
                    side_distance_x = (ray_position_x - map_x) * delta_distance_x

                else:
                    step_x = 1
                    side_distance_x = (map_x + 1.0 - ray_position_x) * delta_distance_x

                if ray_direction_y < 0:
                    step_y = -1
                    side_distance_y = (ray_position_y - map_y) * delta_distance_y

                else:
                    step_y = 1
                    side_distance_y = (map_y + 1.0 - ray_position_y) * delta_distance_y

                # Finding distance to a wall
                hit = 0
                side = 0
                while hit == 0:
                    if side_distance_x < side_distance_y:
                        side_distance_x += delta_distance_x
                        map_x += step_x
                        side = 0

                    else:
                        side_distance_y += delta_distance_y
                        map_y += step_y
                        side = 1

                    if WORLD_MAP[map_x][map_y] > 0:
                        hit = 1

                # Correction against fish eye effect
                if side == 0:
                    perp_wall_distance = abs((map_x - ray_position_x + (1.0 - step_x) / 2.0) / ray_direction_x)
                else:
                    perp_wall_distance = abs((map_y - ray_position_y + (1.0 - step_y) / 2.0) / ray_direction_y)

                # Calculating HEIGHT of the line to draw
                line_height = abs(int(self.height / (perp_wall_distance + .0000001)))
                draw_start = -line_height / 2.0 + self.height / 2.0

                # if drawStat < 0 it would draw outside the screen
                if draw_start < 0:
                    draw_start = 0

                draw_end = line_height / 2.0 + self.height / 2.0

                if draw_end >= self.height:
                    draw_end = self.height - 1

                # Wall colors 0 to 3
                wall_colors = [[], [150, 0, 0], [0, 150, 0], [0, 0, 150]]
                color = wall_colors[WORLD_MAP[map_x][map_y]]

                # Drawing the graphics
                self.lines.append([column, draw_start, column, draw_end, color])
                # arcade.draw_line(start_x=column, start_y=draw_start, end_x=column, end_y=draw_end, color=color, line_width=2)
                column += 2

    def on_key_press(self, key, key_modifiers):

        if key in [arcade.key.UP, arcade.key.W]:
            self.move_up = True
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.move_down = True
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.move_left = True
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.move_right = True

    def on_key_release(self, key, key_modifiers):

        if key in [arcade.key.UP, arcade.key.W]:
            self.move_up = False
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.move_down = False
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.move_left = False
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.move_right = False


App()
arcade.run()
