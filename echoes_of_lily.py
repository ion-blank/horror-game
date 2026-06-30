import pygame
import sys
import json
from enum import Enum
from dataclasses import dataclass
from typing import List, Tuple
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TILE_SIZE = 32

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (58, 58, 58)
MEDIUM_GRAY = (105, 105, 105)
LIGHT_GRAY = (211, 211, 211)
MUTED_YELLOW = (255, 230, 109)
DARK_YELLOW = (212, 169, 64)
SKIN_TONE = (232, 184, 168)
DARK_BROWN = (107, 68, 35)
LIGHT_CYAN = (0, 212, 255)
DEEP_PURPLE = (157, 78, 221)
VOID_BLACK = (15, 15, 20)

class GameState(Enum):
    MENU = 1
    AREA_1 = 2
    AREA_2 = 3
    AREA_3 = 4
    DIALOGUE = 5
    HIDING = 6
    CHASE = 7
    ENDING = 8

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

@dataclass
class PlayerState:
    """Tracks Clara's current state"""
    position: Tuple[int, int]
    direction: Direction
    sanity: int  # 0-100
    has_flashlight: bool
    flashlight_on: bool
    is_hiding: bool
    caught_count: int
    inventory: List[str]

class SanitySystem:
    """Manages Clara's sanity meter and effects"""
    def __init__(self):
        self.sanity = 100
        self.max_sanity = 100
        self.darkness_timer = 0
        self.darkness_threshold = 300  # 5 seconds
        
    def update(self, delta_time: float, in_darkness: bool, saw_entity: bool):
        if in_darkness:
            self.darkness_timer += delta_time
            if self.darkness_timer > self.darkness_threshold:
                self.decrease(0.5)
        else:
            self.darkness_timer = 0
            
        if saw_entity:
            self.decrease(2)
            
    def decrease(self, amount: float):
        self.sanity = max(0, self.sanity - amount)
        
    def increase(self, amount: float):
        self.sanity = min(self.max_sanity, self.sanity + amount)
        
    def get_sanity_level(self) -> str:
        if self.sanity > 80:
            return "normal"
        elif self.sanity > 60:
            return "uneasy"
        elif self.sanity > 40:
            return "anxious"
        elif self.sanity > 20:
            return "terrified"
        else:
            return "broken"

class Entity:
    """The Mimic - Clara's guilt manifested as an entity"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.speed = 80
        self.chase_speed = 150
        self.vision_range = 300
        self.is_chasing = False
        self.chase_timer = 0
        self.visible = False
        self.glitch_timer = 0
        
    def update(self, delta_time: float, player_pos: Tuple[int, int], sanity: int):
        """Update Entity position and behavior based on player proximity and sanity"""
        player_x, player_y = player_pos
        distance = math.sqrt((self.x - player_x)**2 + (self.y - player_y)**2)
        
        # Entity becomes more aggressive as sanity drops
        adjusted_vision_range = self.vision_range * (sanity / 100)
        
        if distance < adjusted_vision_range:
            self.is_chasing = True
            self.target_x = player_x
            self.target_y = player_y
            self.visible = True
        else:
            if self.chase_timer > 0:
                self.chase_timer -= delta_time
            else:
                self.is_chasing = False
                
        # Move towards target
        speed = self.chase_speed if self.is_chasing else self.speed
        
        if abs(self.x - self.target_x) > 5:
            self.x += (self.target_x - self.x) / abs(self.target_x - self.x) * speed * delta_time
        if abs(self.y - self.target_y) > 5:
            self.y += (self.target_y - self.y) / abs(self.target_y - self.y) * speed * delta_time
            
        # Glitch effect
        self.glitch_timer += delta_time
        if self.glitch_timer > 0.3:
            self.x += random.randint(-5, 5)
            self.y += random.randint(-5, 5)
            self.glitch_timer = 0
            
        return distance < 50  # Return if entity caught player
    
    def draw(self, surface: pygame.Surface, camera_offset: Tuple[int, int]):
        """Draw the entity with glitch effects"""
        if not self.visible:
            return
            
        camera_x, camera_y = camera_offset
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        
        if 0 <= screen_x < SCREEN_WIDTH and 0 <= screen_y < SCREEN_HEIGHT:
            # Draw entity sprite (shadow with white eyes)
            pygame.draw.circle(surface, DEEP_PURPLE, (screen_x, screen_y), 20)
            pygame.draw.circle(surface, WHITE, (screen_x - 8, screen_y - 5), 4)
            pygame.draw.circle(surface, WHITE, (screen_x + 8, screen_y - 5), 4)
            
            # Glitch effect overlay
            if self.glitch_timer > 0.15:
                pygame.draw.line(surface, LIGHT_CYAN, 
                               (screen_x - 20, screen_y), 
                               (screen_x + 20, screen_y), 1)

class Player:
    """Clara - the protagonist"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.speed = 150
        self.direction = Direction.DOWN
        self.is_moving = False
        self.width = 24
        self.height = 32
        self.flashlight_range = 200
        
    def update(self, delta_time: float, keys: pygame.key.ScalarKeyType):
        """Update player position based on input"""
        velocity_x = 0
        velocity_y = 0
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            velocity_y = -self.speed
            self.direction = Direction.UP
            self.is_moving = True
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            velocity_y = self.speed
            self.direction = Direction.DOWN
            self.is_moving = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            velocity_x = -self.speed
            self.direction = Direction.LEFT
            self.is_moving = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            velocity_x = self.speed
            self.direction = Direction.RIGHT
            self.is_moving = True
        else:
            self.is_moving = False
        
        self.x += velocity_x * delta_time
        self.y += velocity_y * delta_time
        
    def draw(self, surface: pygame.Surface, camera_offset: Tuple[int, int], sanity_level: str):
        """Draw Clara sprite"""
        camera_x, camera_y = camera_offset
        screen_x = int(self.x - camera_x)
        screen_y = int(self.y - camera_y)
        
        if -50 < screen_x < SCREEN_WIDTH + 50 and -50 < screen_y < SCREEN_HEIGHT + 50:
            # Draw character body (yellow raincoat)
            pygame.draw.circle(surface, MUTED_YELLOW, (screen_x, screen_y), 12)
            pygame.draw.rect(surface, MUTED_YELLOW, 
                           (screen_x - 10, screen_y - 5, 20, 20))
            
            # Draw head
            pygame.draw.circle(surface, SKIN_TONE, (screen_x, screen_y - 15), 8)
            
            # Draw eyes (scared if low sanity)
            if sanity_level == "broken":
                pygame.draw.circle(surface, WHITE, (screen_x - 3, screen_y - 16), 3)
                pygame.draw.circle(surface, WHITE, (screen_x + 3, screen_y - 16), 3)
            else:
                pygame.draw.circle(surface, BLACK, (screen_x - 3, screen_y - 16), 2)
                pygame.draw.circle(surface, BLACK, (screen_x + 3, screen_y - 16), 2)
    
    def get_position(self) -> Tuple[int, int]:
        return (int(self.x), int(self.y))

class Room:
    """Represents a game room/area"""
    def __init__(self, width: int, height: int, name: str, area: int):
        self.width = width
        self.height = height
        self.name = name
        self.area = area
        self.obstacles: List[pygame.Rect] = []
        self.interactables: List['Interactable'] = []
        self.hide_spots: List[pygame.Rect] = []
        self.safe_zones: List[pygame.Rect] = []
        self.background_color = VOID_BLACK
        self.setup_room()
        
    def setup_room(self):
        """Set up obstacles and interactive elements"""
        if self.area == 1:
            self.setup_area_1()
        elif self.area == 2:
            self.setup_area_2()
        elif self.area == 3:
            self.setup_area_3()
    
    def setup_area_1(self):
        """Distorted House"""
        self.background_color = (80, 70, 90)
        
        # Walls
        self.obstacles.append(pygame.Rect(0, 0, self.width, 50))  # Top
        self.obstacles.append(pygame.Rect(0, self.height - 50, self.width, 50))  # Bottom
        self.obstacles.append(pygame.Rect(0, 0, 50, self.height))  # Left
        self.obstacles.append(pygame.Rect(self.width - 50, 0, 50, self.height))  # Right
        
        # Furniture (obstacles)
        self.obstacles.append(pygame.Rect(200, 150, 150, 100))  # Large dresser
        self.obstacles.append(pygame.Rect(800, 200, 200, 80))   # Sofa
        self.obstacles.append(pygame.Rect(400, 400, 100, 120))  # Armchair
        
        # Hide spots
        self.hide_spots.append(pygame.Rect(150, 100, 80, 80))   # Closet
        self.hide_spots.append(pygame.Rect(100, 400, 150, 100)) # Under bed
        
        # Safe zone
        self.safe_zones.append(pygame.Rect(100, 100, 200, 200)) # Bedroom is safe
        
    def setup_area_2(self):
        """Infinite School Corridor"""
        self.background_color = (60, 60, 75)
        
        # Long corridor walls
        self.obstacles.append(pygame.Rect(0, 200, self.width, 30))   # Top wall
        self.obstacles.append(pygame.Rect(0, self.height - 230, self.width, 30))  # Bottom wall
        
        # Classroom doors (obstacles)
        for i in range(3):
            self.obstacles.append(pygame.Rect(150 + i * 300, 100, 80, 150))
            
        # Library (safe zone)
        self.safe_zones.append(pygame.Rect(self.width - 300, 300, 250, 300))
        
        # Hide spots
        self.hide_spots.append(pygame.Rect(200, 100, 60, 80))
        self.hide_spots.append(pygame.Rect(500, 100, 60, 80))
        self.hide_spots.append(pygame.Rect(800, 100, 60, 80))
        
    def setup_area_3(self):
        """Sunken Asylum"""
        self.background_color = (40, 30, 50)
        
        # Hospital beds (obstacles)
        for i in range(7):
            self.obstacles.append(pygame.Rect(100 + i * 150, 150, 120, 80))
        
        # Therapy room (safe area)
        self.safe_zones.append(pygame.Rect(200, 400, 400, 250))
        
        # Hide spots
        self.hide_spots.append(pygame.Rect(150, 450, 80, 100))
        self.hide_spots.append(pygame.Rect(600, 500, 80, 100))
    
    def draw(self, surface: pygame.Surface, camera_offset: Tuple[int, int]):
        """Draw room background and obstacles"""
        surface.fill(self.background_color)
        
        camera_x, camera_y = camera_offset
        
        # Draw obstacles as dark shapes
        for obstacle in self.obstacles:
            screen_rect = pygame.Rect(
                obstacle.x - camera_x,
                obstacle.y - camera_y,
                obstacle.w,
                obstacle.h
            )
            if screen_rect.colliderect(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)):
                pygame.draw.rect(surface, DARK_GRAY, screen_rect)
                pygame.draw.rect(surface, MEDIUM_GRAY, screen_rect, 2)
    
    def check_collision(self, x: int, y: int, width: int, height: int) -> bool:
        """Check if position collides with obstacles"""
        player_rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle):
                return True
        return False

class DialogueSystem:
    """Manages dialogue and story progression"""
    def __init__(self):
        self.current_dialogue = []
        self.dialogue_index = 0
        self.in_dialogue = False
        self.load_dialogues()
        
    def load_dialogues(self):
        """Load dialogue for different story moments"""
        self.dialogues = {
            "awakening": [
                ("CLARA", "Where...?"),
                ("CLARA", "I'm home? But... how did I get here?"),
                ("CLARA", "This isn't right..."),
                ("DOLL", "Hello again, Clara. I've been waiting."),
            ],
            "area_1_complete": [
                ("DOLL", "You're starting to understand, aren't you?"),
                ("CLARA", "What is this place?"),
                ("DOLL", "A place your mind created to protect itself."),
            ],
            "entity_first_sight": [
                ("CLARA", "No... what is that?"),
                ("CLARA", "It looks like... Mother?"),
                ("CLARA", "No, something's wrong..."),
            ],
            "area_3_truth": [
                ("DOLL", "It's time you remembered, Clara."),
                ("CLARA", "Remembered what?"),
                ("DOLL", "The accident. Seven years ago."),
            ],
            "ending_acceptance": [
                ("CLARA", "I forgive myself. I have to."),
                ("ENTITY", "..."),
                ("EMMA_VOICE", "I forgive you, little sister. Let yourself wake up."),
            ],
        }
    
    def start_dialogue(self, dialogue_key: str):
        """Start a new dialogue sequence"""
        if dialogue_key in self.dialogues:
            self.current_dialogue = self.dialogues[dialogue_key]
            self.dialogue_index = 0
            self.in_dialogue = True
    
    def next_line(self):
        """Advance to next dialogue line"""
        if self.dialogue_index < len(self.current_dialogue) - 1:
            self.dialogue_index += 1
        else:
            self.in_dialogue = False
    
    def get_current_line(self) -> Tuple[str, str]:
        """Get current dialogue speaker and text"""
        if self.dialogue_index < len(self.current_dialogue):
            return self.current_dialogue[self.dialogue_index]
        return ("", "")
    
    def draw(self, surface: pygame.Surface, font_large, font_small):
        """Draw dialogue box on screen"""
        if not self.in_dialogue:
            return
            
        speaker, text = self.get_current_line()
        
        # Draw dialogue box background
        dialog_rect = pygame.Rect(50, SCREEN_HEIGHT - 150, SCREEN_WIDTH - 100, 130)
        pygame.draw.rect(surface, BLACK, dialog_rect)
        pygame.draw.rect(surface, LIGHT_CYAN, dialog_rect, 3)
        
        # Draw speaker name
        speaker_text = font_large.render(speaker, True, LIGHT_CYAN)
        surface.blit(speaker_text, (70, SCREEN_HEIGHT - 130))
        
        # Draw dialogue text
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font_small.size(test_line)[0] > SCREEN_WIDTH - 140:
                if current_line:
                    lines.append(current_line)
                current_line = word + " "
            else:
                current_line = test_line
        lines.append(current_line)
        
        for i, line in enumerate(lines):
            dialogue_text = font_small.render(line, True, WHITE)
            surface.blit(dialogue_text, (70, SCREEN_HEIGHT - 100 + i * 25))
        
        # Draw "Press Space to continue"
        continue_text = font_small.render("[SPACE to continue]", True, MEDIUM_GRAY)
        surface.blit(continue_text, (SCREEN_WIDTH - 250, SCREEN_HEIGHT - 30))

class GameManager:
    """Main game manager"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Echoes of Lily - A Psychological Horror Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game state
        self.game_state = GameState.MENU
        self.current_area = 1
        self.current_room: Room = None
        
        # Game systems
        self.player = Player(640, 360)
        self.entity = Entity(100, 100)
        self.sanity_system = SanitySystem()
        self.dialogue_system = DialogueSystem()
        
        # Fonts
        self.font_large = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        self.font_huge = pygame.font.Font(None, 64)
        
        # Camera
        self.camera_x = 0
        self.camera_y = 0
        
        # Chase timer
        self.chase_timer = 0
        self.caught_count = 0
        
        # Story flags
        self.has_seen_entity = False
        self.has_discovered_truth = False
        self.ending_type = None
        
        # Initialize first room
        self.load_area(1)
        
    def load_area(self, area: int):
        """Load a specific game area"""
        self.current_area = area
        if area == 1:
            self.current_room = Room(2000, 1000, "Distorted House", 1)
            self.player.x = 640
            self.player.y = 360
            self.entity.x = 100
            self.entity.y = 100
        elif area == 2:
            self.current_room = Room(3000, 600, "Infinite School Corridor", 2)
            self.player.x = 200
            self.player.y = 300
            self.entity.x = 2500
            self.entity.y = 300
        elif area == 3:
            self.current_room = Room(2000, 800, "Sunken Asylum", 3)
            self.player.x = 500
            self.player.y = 500
            self.entity.x = 1500
            self.entity.y = 200
    
    def update(self, delta_time: float):
        """Update game state"""
        if self.game_state == GameState.MENU:
            self.update_menu()
        elif self.game_state == GameState.AREA_1:
            self.update_gameplay(delta_time)
        elif self.game_state == GameState.AREA_2:
            self.update_gameplay(delta_time)
        elif self.game_state == GameState.AREA_3:
            self.update_gameplay(delta_time)
        elif self.game_state == GameState.ENDING:
            self.update_ending()
        elif self.game_state == GameState.DIALOGUE:
            self.update_dialogue()
    
    def update_menu(self):
        """Handle menu input"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game_state = GameState.AREA_1
            self.dialogue_system.start_dialogue("awakening")
            self.game_state = GameState.DIALOGUE
    
    def update_gameplay(self, delta_time: float):
        """Update active gameplay"""
        keys = pygame.key.get_pressed()
        
        # Handle flashlight toggle
        if keys[pygame.K_f]:
            # Toggle flashlight (simplified)
            pass
        
        # Handle area transitions
        if self.player.x > self.current_room.width - 100 and self.current_area < 3:
            self.load_area(self.current_area + 1)
            self.game_state = GameState(self.current_area + 1)
        
        # Update player
        self.player.update(delta_time, keys)
        
        # Check collision with obstacles
        if self.current_room.check_collision(int(self.player.x), int(self.player.y), 
                                            self.player.width, self.player.height):
            # Simple collision response - move back
            self.player.x -= 100 * delta_time
        
        # Check if in safe zone
        in_safe_zone = any(zone.collidepoint(int(self.player.x), int(self.player.y)) 
                          for zone in self.current_room.safe_zones)
        
        # Update sanity
        in_darkness = not in_safe_zone
        self.sanity_system.update(delta_time, in_darkness, self.has_seen_entity)
        
        # Update entity
        caught = self.entity.update(delta_time, self.player.get_position(), 
                                   self.sanity_system.sanity)
        
        # Check if entity is visible
        distance_to_entity = math.sqrt((self.player.x - self.entity.x)**2 + 
                                      (self.player.y - self.entity.y)**2)
        if distance_to_entity < 400:
            self.has_seen_entity = True
            self.entity.visible = True
        
        if caught:
            self.caught_count += 1
            if self.caught_count >= 3:
                self.ending_type = "bad"
                self.game_state = GameState.ENDING
            else:
                # Teleport player to random safe spot
                self.player.x = 500 + random.randint(-100, 100)
                self.player.y = 400 + random.randint(-100, 100)
                self.sanity_system.decrease(20)
        
        # Check game over condition (sanity at 0)
        if self.sanity_system.sanity <= 0:
            self.ending_type = "bad"
            self.game_state = GameState.ENDING
        
        # Handle area-specific events
        if self.current_area == 3 and not self.has_discovered_truth:
            self.has_discovered_truth = True
            self.dialogue_system.start_dialogue("area_3_truth")
            self.game_state = GameState.DIALOGUE
        
        # Update camera to follow player
        self.camera_x = self.player.x - SCREEN_WIDTH // 2
        self.camera_y = self.player.y - SCREEN_HEIGHT // 2
        self.camera_x = max(0, min(self.camera_x, self.current_room.width - SCREEN_WIDTH))
        self.camera_y = max(0, min(self.camera_y, self.current_room.height - SCREEN_HEIGHT))
    
    def update_dialogue(self):
        """Handle dialogue progression"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.dialogue_system.next_line()
            if not self.dialogue_system.in_dialogue:
                # Resume gameplay
                if self.current_area == 1:
                    self.game_state = GameState.AREA_1
                elif self.current_area == 2:
                    self.game_state = GameState.AREA_2
                elif self.current_area == 3:
                    self.game_state = GameState.AREA_3
    
    def update_ending(self):
        """Handle ending sequence"""
        pass
    
    def draw(self):
        """Draw entire game frame"""
        if self.game_state == GameState.MENU:
            self.draw_menu()
        elif self.game_state in [GameState.AREA_1, GameState.AREA_2, GameState.AREA_3]:
            self.draw_gameplay()
        elif self.game_state == GameState.DIALOGUE:
            self.draw_gameplay()
            self.dialogue_system.draw(self.screen, self.font_large, self.font_small)
        elif self.game_state == GameState.ENDING:
            self.draw_ending()
    
    def draw_menu(self):
        """Draw main menu"""
        self.screen.fill(BLACK)
        
        title = self.font_huge.render("ECHOES OF LILY", True, LIGHT_CYAN)
        subtitle = self.font_large.render("A Psychological Horror Game", True, MEDIUM_GRAY)
        instructions = self.font_small.render("Press SPACE to Begin", True, WHITE)
        
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        self.screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 300))
        self.screen.blit(instructions, (SCREEN_WIDTH // 2 - instructions.get_width() // 2, 500))
        
        # Story hook
        hook_text = "She wakes up in her childhood home... but something is terribly wrong."
        hook = self.font_small.render(hook_text, True, LIGHT_CYAN)
        self.screen.blit(hook, (SCREEN_WIDTH // 2 - hook.get_width() // 2, 400))
        
        pygame.display.flip()
    
    def draw_gameplay(self):
        """Draw active gameplay"""
        # Draw room
        self.current_room.draw(self.screen, (self.camera_x, self.camera_y))
        
        # Draw hide spots for debugging
        for spot in self.current_room.hide_spots:
            screen_rect = pygame.Rect(
                spot.x - self.camera_x,
                spot.y - self.camera_y,
                spot.width,
                spot.height
            )
            pygame.draw.rect(self.screen, (0, 100, 0), screen_rect, 1)
        
        # Draw player
        sanity_level = self.sanity_system.get_sanity_level()
        self.player.draw(self.screen, (self.camera_x, self.camera_y), sanity_level)
        
        # Draw entity
        self.entity.draw(self.screen, (self.camera_x, self.camera_y))
        
        # Draw UI
        self.draw_ui()
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw UI elements (sanity meter, etc.)"""
        # Sanity meter
        sanity_text = self.font_small.render(f"Sanity: {int(self.sanity_system.sanity)}%", True, WHITE)
        self.screen.blit(sanity_text, (10, 10))
        
        # Sanity bar
        bar_width = 200
        bar_height = 20
        sanity_ratio = self.sanity_system.sanity / self.sanity_system.max_sanity
        
        pygame.draw.rect(self.screen, DARK_GRAY, (10, 35, bar_width, bar_height))
        
        # Color based on sanity
        if sanity_ratio > 0.6:
            color = (0, 200, 0)
        elif sanity_ratio > 0.4:
            color = (200, 200, 0)
        elif sanity_ratio > 0.2:
            color = (200, 100, 0)
        else:
            color = (200, 0, 0)
        
        pygame.draw.rect(self.screen, color, (10, 35, bar_width * sanity_ratio, bar_height))
        pygame.draw.rect(self.screen, WHITE, (10, 35, bar_width, bar_height), 2)
        
        # Area name
        area_text = self.font_small.render(f"Area: {self.current_room.name}", True, WHITE)
        self.screen.blit(area_text, (10, 65))
        
        # Controls
        controls = [
            "WASD/Arrows: Move",
            "F: Flashlight",
            "E: Hide"
        ]
        for i, control in enumerate(controls):
            control_text = self.font_small.render(control, True, MEDIUM_GRAY)
            self.screen.blit(control_text, (SCREEN_WIDTH - 200, 10 + i * 25))
    
    def draw_ending(self):
        """Draw ending sequence"""
        self.screen.fill(BLACK)
        
        if self.ending_type == "good":
            title = self.font_huge.render("ACCEPTANCE", True, LIGHT_CYAN)
            text = [
                "Clara's eyes open.",
                "Machines beep steadily around her.",
                "She breathes on her own for the first time in seven years.",
                "",
                "The real world awaits.",
            ]
        else:
            title = self.font_huge.render("THE DREAM CONTINUES", True, DEEP_PURPLE)
            text = [
                "Clara remains dreaming.",
                "In the real world, machines keep her alive.",
                "But here, she is still running.",
                "",
                "Forever.",
            ]
        
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        
        for i, line in enumerate(text):
            if line:
                line_text = self.font_small.render(line, True, WHITE)
            else:
                line_text = self.font_small.render("", True, WHITE)
            self.screen.blit(line_text, (SCREEN_WIDTH // 2 - line_text.get_width() // 2, 250 + i * 40))
        
        restart_text = self.font_small.render("Press SPACE to Return to Menu", True, MEDIUM_GRAY)
        self.screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 600))
        
        pygame.display.flip()
    
    def handle_events(self):
        """Handle user input and window events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def run(self):
        """Main game loop"""
        while self.running:
            delta_time = self.clock.tick(FPS) / 1000.0
            
            self.handle_events()
            self.update(delta_time)
            self.draw()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = GameManager()
    game.run()
