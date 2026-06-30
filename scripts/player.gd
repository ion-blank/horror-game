extends Node2D

class_name Player

@export var speed = 200
@export var flashlight_range = 300
@onready var sprite = $Sprite2D
@onready var animation_player = $AnimationPlayer
@onready var flashlight = $Flashlight
@onready var sanity_system = get_parent().get_node("SanitySystem")

var velocity = Vector2.ZERO
var is_hiding = false
var can_move = true
var current_direction = "down"

func _ready():
	if animation_player:
		animation_player.play("idle_down")

func _physics_process(delta):
	if not can_move:
		return
	
	# Input handling
	var input_vector = Vector2.ZERO
	if Input.is_action_pressed("ui_right"):
		input_vector.x += 1
		current_direction = "right"
	if Input.is_action_pressed("ui_left"):
		input_vector.x -= 1
		current_direction = "left"
	if Input.is_action_pressed("ui_down"):
		input_vector.y += 1
		current_direction = "down"
	if Input.is_action_pressed("ui_up"):
		input_vector.y -= 1
		current_direction = "up"
	
	# Flashlight toggle
	if Input.is_action_just_pressed("ui_select"):
		toggle_flashlight()
	
	# Hide/Seek
	if Input.is_action_just_pressed("ui_focus_next"):
		attempt_hide()
	
	if input_vector != Vector2.ZERO:
		input_vector = input_vector.normalized()
		velocity = input_vector * speed
		play_walk_animation(current_direction)
	else:
		velocity = Vector2.ZERO
		play_idle_animation(current_direction)
	
	position += velocity * delta
	clamp_position()

func play_walk_animation(direction: String):
	if animation_player:
		animation_player.play("walk_" + direction)

func play_idle_animation(direction: String):
	if animation_player:
		animation_player.play("idle_" + direction)

func play_panic_animation():
	if animation_player:
		animation_player.play("panic_" + current_direction)

func play_fear_animation():
	if animation_player:
		animation_player.play("fear_" + current_direction)

func toggle_flashlight():
	if flashlight:
		flashlight.visible = !flashlight.visible
		if flashlight.visible and sanity_system:
			sanity_system.increase_sanity(5)
		elif not flashlight.visible and sanity_system:
			sanity_system.decrease_sanity(1)

func attempt_hide():
	var areas = get_overlapping_areas()
	for area in areas:
		if area.is_in_group("hide_spot"):
			is_hiding = true
			can_move = false
			if animation_player:
				animation_player.play("hide_" + current_direction)
			await get_tree().create_timer(3.0).timeout
			is_hiding = false
			can_move = true
			break

func get_overlapping_areas():
	var space = get_world_2d().direct_space_state
	var query = PhysicsShapeQueryParameters2D.new()
	var shape = CircleShape2D.new()
	shape.radius = 50
	query.shape = shape
	query.transform = global_transform
	return space.intersect_shape(query)

func decrease_sanity(amount: float):
	if sanity_system:
		sanity_system.decrease_sanity(amount)

func clamp_position():
	var screen_size = get_viewport_rect().size
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)
