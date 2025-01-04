import pygame 
from pygame.math import Vector2
import random
from functions import is_point_on_line,rotate_on_point

class Paddle(pygame.sprite.Sprite):
    def __init__(self,x,y,movement_keys,bounding_box):
        super().__init__()
        self.original_image=pygame.image.load("paddle.png").convert_alpha()

        self.image=self.original_image

        self.rect=self.image.get_rect(center=(x,y))
        

        self.mask=pygame.mask.from_surface(self.image)

        self.angle=0


        #The set of keys to control each paddle 
        self.movement_keys=movement_keys

        #The bounding box to limit movement to the game area. Rect
        self.bounding_box=bounding_box

    

   

    def update(self):
    
        keys=pygame.key.get_pressed()
        rotation_angle=0

        if keys[self.movement_keys[0]] and self.rect.left > self.bounding_box.left:
            self.rect.centerx -= 5
            

        elif keys[self.movement_keys[1]] and self.rect.right < self.bounding_box.right:
            self.rect.centerx += 5
            

        if keys[self.movement_keys[2]] and self.rect.top > self.bounding_box.top:
            self.rect.centery -= 5
            

        elif keys[self.movement_keys[3]] and self.rect.bottom < self.bounding_box.bottom:
            self.rect.centery += 5
            

        if keys[self.movement_keys[4]]:
            self.angle+=5
            rotation_angle+=5
        elif keys[self.movement_keys[5]]:
            self.angle-=5
            rotation_angle-=5


        rotated_image=pygame.transform.rotate(self.original_image,self.angle)

        self.mask=pygame.mask.from_surface(rotated_image)

        self.rect=rotated_image.get_rect(center=(self.rect.center))

        
        self.image=rotated_image

        
        

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.image=pygame.image.load("ball.png").convert_alpha()

        random_number = random.choice([random.randint(-4, -2), random.randint(2, 4)])
        random_number2 = random.choice([random.randint(-4, -2), random.randint(2, 4)])

        self.velocity=Vector2(random_number,random_number2)

        self.mask=pygame.mask.from_surface(self.image)

        self.rect=self.image.get_rect(center=(x,y))

    def __update_ball(self):
        self.rect.center=(750,400)

        random_number = random.choice([random.randint(-4, -2), random.randint(2, 4)])
        random_number2 = random.choice([random.randint(-4, -2), random.randint(2, 4)])

        self.velocity=Vector2(random_number,random_number2)
        
    def _collision_detection(self, paddles,player1_score,player2_score):
        if self.rect.right>1495:
            player1_score+=1
            self.__update_ball()
        elif self.rect.left<5:
            player2_score+=1
            self.__update_ball()

        if self.rect.bottom>=800:
            self.velocity.reflect_ip(Vector2(0,1))

        elif self.rect.top<=0:
            self.velocity.reflect_ip(Vector2(0,-1))

        for paddle in paddles:
            collision = pygame.sprite.collide_mask(self, paddle)
            if collision:
                # Collision detected with this paddle!
                # Get the point of collision
                offset = (self.rect.x - paddle.rect.x, self.rect.y - paddle.rect.y)
                intersection = paddle.mask.overlap(self.mask, offset)
                intersection = (intersection[0] + paddle.rect.x, intersection[1] + paddle.rect.y)
                print("Intersection:", intersection)

                # Calculate the overlapping area between the masks
                overlap_area = paddle.mask.overlap_area(self.mask, offset)

                # Calculate the gradient of the overlapping area through finite difference
                epsilon = 1e-6  # Small value to avoid division by zero
                delta_x = paddle.mask.overlap_area(self.mask, (offset[0] + 1, offset[1])) - overlap_area
                delta_y = paddle.mask.overlap_area(self.mask, (offset[0], offset[1] + 1)) - overlap_area

                # Calculate the collision normal using the finite difference
                collision_normal = pygame.Vector2(delta_x, delta_y)
                collision_normal.normalize_ip()

                # Determine the direction of the collision relative to the paddle's orientation
                if collision_normal.x < 0:
                    print("Ball hit from the right")
                elif collision_normal.x > 0:
                    print("Ball hit from the left")
                if collision_normal.y < 0:
                    print("Ball hit from below")
                elif collision_normal.y > 0:
                    print("Ball hit from above")

                self.velocity.reflect_ip(collision_normal)
                self.rect.move_ip(6*-collision_normal)

                

        return player1_score,player2_score




                    
                


               

    def update(self,paddles,player1_score,player2_score):
        self.rect.move_ip(self.velocity)
        player1_score,player2_score=self._collision_detection(paddles,player1_score,player2_score)
        

        return player1_score,player2_score
    
    