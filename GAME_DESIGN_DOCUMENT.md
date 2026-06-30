# Game Design Document: Echoes of Lily

## 1. Game Overview & Aesthetics

### Title
**Echoes of Lily** – A psychological horror journey through memory and guilt

### Art Style
- **Pixel Resolution**: 16-bit detailed pixel art (512x512 room tiles)
- **Visual Language**: 
  - Dynamic, gloomy lighting system with volumetric shadows
  - Muted color palette: grays, desaturated yellows, faded blues, deep purples
  - Hand-drawn quality despite pixel medium—no primitive geometry
  - Environmental decay: peeling wallpaper, water stains, dust particles
  - Layered parallax backgrounds for depth
- **Character Sprites**: 32x48px base for protagonists, fully animated with idle, walk, run, and emotional states
- **Dialogue Portraits**: 128x128px illustrated faceports with subtle emotional variations
- **Lighting**: Real-time dynamic shadows cast by light sources; fog effects obscure distant areas

### Atmosphere & Tone
- **Primary Genre**: Psychological horror with environmental storytelling
- **Influences**: Ib (emotional narrative), The Witch's House (twisted reality), Yume Nikki (dream logic)
- **Key Pillars**:
  - Tension over jump scares
  - Unsettling ambiance rather than gore
  - Moral complexity and guilt as the true horror
  - Audio design as critical as visuals (ambient drones, unnatural silence, heartbeat SFX)

---

## 2. Character Profiles

### Protagonist: Clara Blackwood
**Age**: 17  
**Visual Description**: Shoulder-length chestnut hair, pale complexion, dark eyes with a haunted look

**Signature Outfit**: Frayed yellow raincoat (tattered at edges, fabric soaked and dripping), white undershirt, dark jeans, worn sneakers

**Sprite Sheet Specifications**:
- **Base Resolution**: 32x48px (animated frame)
- **Color Palette**: 12-16 unique colors per frame
- **Key Animations**:
  1. **Idle** (4 frames, 0.3s each) – Slight breathing motion, hands clutching coat
  2. **Walk** (6 frames, 0.15s each) – Hesitant, careful footsteps, looking around nervously
  3. **Run** (8 frames, 0.1s each) – Panicked galloping, arms pumping, coat flaring
  4. **Flashlight Hold** (1 static frame) – Holding flashlight forward, beam casting light downward
  5. **Panicked Breathing** (5 frames, 0.2s each) – Hunched over, heavy breathing animation, coat heaving
  6. **Interact/Examine** (3 frames, 0.25s each) – Leaning forward, hands reaching out
  7. **Fear Reaction** (1 frame + 0.5s hold) – Wide eyes, mouth open, trembling
  8. **Hiding** (1 frame) – Crouched, barely visible behind furniture

**Personality**: Initially cautious and introspective, gradually becoming aware of the wrongness around her. She questions what she's experiencing and shows emotional depth in her dialogue.

---

### The Antagonist: The Mimic (Entity)

**Nature**: A manifestation of Clara's guilt—not truly alive, but a psychic projection born from trauma

**Visual Design**: Shifting, glitching pixel shadow with impossible geometry
- **Base Form**: 40x64px silhouette, mostly black with purple/dark blue aura
- **Key Features**:
  - Elongated limbs that distort and stretch
  - White, completely empty eyes (no pupils or sclera detail—just white void)
  - Pixelated distortion effect around edges (chromatic aberration, scan lines)
  - Can briefly shift into the faces of Clara's loved ones before glitching back
  - Movement is jerky and unnatural (teleporting short distances, crawling on walls)

**Behavior**:
- Appears in mirrors and reflective surfaces first
- Stalks from a distance, gradually closing in
- Mimics Clara's movements in shadows
- Teleports behind doors or around corners if player is too close
- Moves faster as Clara's Sanity meter depletes

**Audio Signature**: Distorted versions of Clara's breathing, reversed dialogue, static crackle mixed with human voices

---

### Companion: The Porcelain Doll (Lilith)

**Appearance**: Small (12x16px sprite), made of pale porcelain with cracks in its surface, wearing a Victorian dress with small tears and stains

**Personality**: Cryptic, knowing, speaks in riddles and fragmented sentences. Occasionally references events Clara doesn't remember, suggesting the doll has seen more than it should.

**Function**: 
- Provides hints through cryptic dialogue ("The light reveals what the dark conceals")
- Reacts to Clara's emotional state—smile fades if Sanity is low
- Can be found in different rooms, suggesting it's watching or guiding Clara
- Final revelation: The doll represents Clara's younger, innocent self

**Dialogue Style**: Uses poetic, unsettling language mixed with childlike observations

---

## 3. The Full Narrative & Plot Outline

### Act I: Awakening – "The Distorted House" (20-30 minutes)

**The Hook**:
Clara opens her eyes in the familiar bedroom of her childhood home. The furniture is wrong—too large or too small. The wallpaper breathes. Sunlight streams through the window, but outside, there's only an endless black void—not darkness, but *nothing*. The doors don't open. The windows won't break.

**Initial Realization**:
- Clara finds a handwritten note: "You're still asleep, Clara. Don't wake up yet."
- She discovers a flickering flashlight in the bedside drawer with a note: "You'll need this to see the truth."
- She finds a mirror with her reflection, but it doesn't quite match her movements.

**Companion Introduction**:
Clara discovers the porcelain doll in a closet, half-hidden. When examined, the doll's lips appear to move: "Hello again, Clara. I've been waiting."

**Key Revelations**:
- Clara doesn't remember how she got here
- Time feels strange—clocks don't work, or they run backward
- She finds a calendar from 7 years ago (she was 10)

---

### Act II: Descent – "The Infinite School Corridor" (40-50 minutes)

**The Transition**:
A door that wasn't there before opens to a long hallway—the hallway of Clara's elementary school. It stretches impossibly far. Doors line both sides, but some are locked, some open to impossible spaces.

**First Entity Encounter**:
Clara hears footsteps. She sees a familiar silhouette at the far end of the corridor—her mother. But something is wrong. The figure's limbs are too long. Its head tilts at an unnatural angle. As Clara approaches, the figure's face glitches—white noise overlays it—and it mimics her movements perfectly.

Clara must hide (in a classroom, a locker, under a desk) while the Entity searches.

**The Puzzle Sequence**:
Clara finds cryptic notes written in handwriting that matches her own but doesn't remember writing:
- "The way forward is through memory"
- "Three doors hold the past"
- "Choose the one you fear most"

She must open three specific classroom doors, each revealing:
1. **Door 1 (Classroom A)**: A memory of a birthday party where Clara was left behind while her older sister went to the beach
2. **Door 2 (Classroom B)**: A scene where Clara's mother scolds her for breaking something valuable
3. **Door 3 (Classroom C)**: A twisted version of Clara's best friend, Emma, laughing at her

**Emotional Depth**:
The doll appears in a corner and whispers: "Guilt eats at us from the inside, doesn't it? These were the moments that broke you."

---

### Act III: Truth – "The Sunken Asylum / Memory Ward" (50-70 minutes)

**The Discovery**:
Clara descends into a dilapidated hospital/asylum wing. Beds are full of sleeping bodies—all Clara at different ages. Medical charts read "Clara Blackwood - Patient ID 7749 - Status: Comatose."

**The Full Truth Revealed**:
Through a combination of found documents, dialogue with the doll, and fragmented memories, Clara learns:

Seven years ago (when she was 10), Clara was in a car accident. Her older sister Emma was driving. Emma was distracted by Clara fighting with her in the backseat over a toy. The car swerved. They hit a tree. Emma died instantly. Clara survived but fell into a coma.

For seven years, Clara's mind has been trapped in this space, replaying the moment of the accident, unable to forgive herself. The Entity is Clara's guilt manifested—not a monster hunting her, but a reflection of her self-condemnation.

**The Doll's Final Role**:
The doll reveals itself as a manifestation of Clara at age 10—the last moment before the trauma. It whispers: "I've been trying to help you remember so you can let go. But you keep running from the truth."

---

### The Climax: Confrontation

**Two Possible Endings**:

#### Ending A: Acceptance (True Ending)
- Clara allows the Entity to catch her
- Instead of disappearing, the Entity stops and begins to fade
- A voice—Emma's voice—speaks from the darkness: "I forgive you, little sister. Let yourself wake up."
- Clara's eyes open in a hospital bed. She's alive, breathing on her own for the first time in 7 years.
- The screen fades to white.
- **Post-credits**: Clara, now older, receives her first visit from her parents. They smile through tears.

#### Ending B: Rejection (Bad Ending)
- Clara keeps running from the Entity
- She finds a door labeled "Sleep"
- She enters and locks it behind her
- The screen cuts to black
- Text appears: "Clara remains dreaming. In the real world, machines keep her alive. In here, she is still running."
- **Post-credits (optional)**: A flash of a girl's hand flatline on a hospital monitor, or the fading sound of a hospital room

---

## 4. Core Gameplay Mechanics

### 4.1 Exploration & Environmental Puzzles

**Puzzle Types**:

1. **Light-Based Puzzles**
   - Using the flashlight to reveal hidden doorways or messages written in glow-in-the-dark paint
   - Positioning light sources to cast shadows that form shapes (opening locks or revealing paths)
   - Example: In the bedroom, shadows cast by furniture spell out a code when the flashlight is held at the correct angle

2. **Cryptic Note Decoding**
   - Finding fragmented notes written in blood, dust, or crayon
   - Notes contain riddles, reversed text, or encoded messages
   - Example: "The child counts to ten while the mother hides. Where does she look first?" (Answer: The closet)

3. **Memory/Sequence Puzzles**
   - Interacting with objects in a specific sequence triggers an event
   - Example: Light three candles in the order of importance (self, sister, family) to unlock a door

4. **Environmental Manipulation**
   - Pushing/pulling objects to reach higher areas or block paths
   - Using items (books, chairs) to solve logic puzzles
   - Example: Stack boxes to reach a high window with a key

### 4.2 Sanity/Fear Meter

**Mechanics**:
- **Visual Indicator**: A candle icon in the top-right corner of the HUD. As Sanity decreases, the flame flickers and eventually goes out.
- **Sanity Loss Triggers**:
  - Staying in complete darkness for more than 10 seconds
  - Direct sight of the Entity (progressive; the longer you see it, the faster it drops)
  - Reading disturbing journal entries
  - Hearing the Entity's distorted breathing sounds
- **Sanity Recovery**:
  - Using the flashlight in bright areas
  - Reading comforting dialogue from the doll
  - Finding safe rooms (the childhood bedroom, the school library)

**Effects of Low Sanity** (5 stages):
1. **Normal (100-80%)**: Standard gameplay, clear UI
2. **Uneasy (79-60%)**: Screen edges darken slightly, subtle audio distortion, Clara breathes harder
3. **Anxious (59-40%)**: Frequent visual glitches (chromatic aberration, scan lines), audio becomes static-filled, Clara's footsteps sound heavy
4. **Terrified (39-20%)**: Screen inverts colors briefly, random rooms appear flipped or rotated, Entity moves faster
5. **Broken (19-0%)**: Screen heavily distorted, Entity becomes nearly invisible, Clara moves slowly and erratically, game over if reaches 0

---

### 4.3 No-Combat Survival: Stealth & Hiding

**Core Mechanic**: Clara **cannot** attack or defend herself. Survival depends entirely on evasion and stealth.

**Stealth System**:
- **Line of Sight**: The Entity operates on a vision cone. If it doesn't see Clara, it searches nearby areas
- **Sound Detection**: Running makes noise; walking is quieter
- **Light Exposure**: The Entity is attracted to areas where Clara uses her flashlight—she must use it strategically

**Hiding Mechanics**:
- **Closets**: Clara can hide inside closets. The Entity may check them if it searches the room. Each closet can only hide her for 20-30 seconds before the Entity discovers her.
- **Under Beds**: Similarly, Clara can hide under beds. Longer hiding duration (30-45 seconds) but requires a specific room with a bed.
- **Behind Furniture**: Large furniture (wardrobes, curtains) provides temporary cover but not complete concealment.
- **Light Extinguishment**: Clara can blow out nearby candles or turn off lights to plunge areas into darkness—this buys time but increases her Sanity loss.

**Chase Sequences**:
- If the Entity spots Clara, a tense chase begins
- A timer appears: "FLEE" (30 seconds)
- Clara must reach a safe room or hide before the timer expires
- If the Entity catches Clara:
  - **Near-Miss Mechanic**: She's teleported to a random nearby room with her Sanity severely depleted
  - **Repeated Catches**: Three catches trigger the Bad Ending

---

## 5. Level Design & Progression Breakdown

### Area 1: The Distorted House (Introduction - 20-30 minutes)

**Objective**: Find the flashlight and escape the house, learning basic mechanics.

**Layout**:
- **Ground Floor**: Distorted living room (furniture too large), kitchen (clocks run backward), hallway with locked front door
- **Basement**: Flooded, water level rising, contains journal entries
- **Second Floor**: Bedrooms (Clara's, parents', sister's), bathroom (mirror sequences)

**Key Puzzles**:
1. **The Living Room Puzzle**: 
   - Furniture is sized wrong. Player must realize the room itself is distorted.
   - Solution: Interact with furniture in order of size (smallest to largest) to unlock a key hidden in a lamp.

2. **The Basement Sequence**:
   - Water is rising. Clara has limited time to find a journal entry before the exit floods.
   - Uses urgency to teach the player about time pressure.

3. **The Mirror Puzzle**:
   - Clara's reflection in the bathroom mirror isn't synchronized. 
   - Player must match Clara's movements to her reflection to unlock the second floor.

**Entity Encounters**: None yet. The Entity appears as a shadow in the corner of the player's view occasionally, but never directly engages.

**Companion**: The doll is found in the bedroom closet. First real conversation happens here.

**Exit**: Clara escapes through a door in the master bedroom that leads to the school corridor.

---

### Area 2: The Infinite School Corridor (Exploration & First Chase - 40-50 minutes)

**Objective**: Navigate the impossible school, solve memory puzzles, survive the first Entity encounter, and find a way to the asylum.

**Layout**:
- **Central Corridor**: Stretches impossibly far (infinite in one direction, visible end in the other)
- **Classrooms (3 main)**: Represent key moments of guilt (see Narrative section)
- **Library**: Safe room with lore documents
- **Gymnasium**: Large open space with limited hiding spots (dangerous area)
- **Basement Stairs**: Lead down to the next area

**Key Puzzles**:

1. **The Three Doors Puzzle** (Major):
   - Three classroom doors, each labeled with symbols (heart, shadow, mirror)
   - Player must enter each and relive a memory
   - Solution: Open them in order of the trauma's emotional weight (not chronological)
   - Correct sequence reveals a path; wrong sequence triggers a timed chase

2. **The Corridor Extension Puzzle**:
   - The corridor seems to loop infinitely. Player must find subtle environmental clues to understand the true path
   - Solution: Follow the doll's footprints (visible only with the flashlight on specific angles) to the exit

3. **The Gymnasium Balance Puzzle**:
   - A series of floorboards. Some are safe; others trigger an alarm that alerts the Entity
   - Solution: Use shadows cast by a hanging basketball hoop to determine safe paths

**Entity Encounters**:
- **First Sighting**: At the far end of the corridor, Clara sees a figure that looks like her mother but distorts into the Entity
- **First Chase**: Triggers when Clara approaches the figure. She has 30 seconds to hide or flee. If successful, she learns the Entity can be evaded. If she's caught, she's teleported to a random classroom (teaches the catching mechanic)
- **Recurring Stalking**: As Area 2 progresses, the Entity appears more frequently, faster, and closer

**Sanity Decay**: Heavily emphasized here. The longer Clara stays in the dark corridors, the more her Sanity drops, causing visual and audio distortions.

**Exit**: Basement stairs lead downward into the asylum.

---

### Area 3: The Sunken Asylum / Memory Ward (Truth & Climax - 50-70 minutes)

**Objective**: Uncover the full truth, face the Entity in its strongest form, and make the final choice.

**Layout**:
- **Main Ward**: Hospital beds in rows, each containing a sleeping version of Clara
- **Medical Records Room**: Files revealing the accident, coma details, and 7-year history
- **Therapy Room**: Mirrors and chairs; the final confrontation space
- **Shadow Realm** (optional): A twisted dimension entered through mirrors; represents the deepest parts of Clara's trauma

**Key Puzzles**:

1. **The Memory Sequence Puzzle**:
   - Clara must find seven fragments of a fragmented memory (one for each year in the coma)
   - Each fragment is hidden in a hospital record, a personal item, or a journal entry
   - Solution: Collecting all fragments triggers a cinematic showing the accident

2. **The Mirror Maze**:
   - The therapy room contains multiple mirrors. Clara must navigate through them.
   - The Entity is stronger here; it can move through mirrors
   - Solution: Clara must smash specific mirrors (indicated subtly) to trap the Entity temporarily and reach the next area

3. **The Final Confrontation Setup**:
   - Clara discovers the therapy room where she must make her choice
   - A large mirror dominates the room. The Entity's true form is visible within it.

**Entity Encounters**:
- **Escalated Threats**: The Entity moves faster, teleports more frequently, and can briefly manifest multiple copies of itself
- **Sanity Correlation**: If Sanity is critically low, the Entity becomes partially invisible, making evasion harder
- **Pre-Climax Chase**: A intense sequence where Clara must navigate the ward while the Entity hunts her, leading to the final confrontation room

**Companion Role**: The doll appears multiple times, offering hints and emotional support. In the records room, the doll reveals its true nature.

**The Ending**:
- **Acceptance Path** (A): Clara stops running and lets the Entity catch her. The Entity dissolves into light. Emma's voice provides absolution. Clara wakes up.
- **Rejection Path** (B): Clara finds the "Sleep" door and locks herself away. The game ends ambiguously, with Clara remaining in her comatose state.

---

## 6. Detailed Opening Scene: Dialogue

### Scene: "Awakening"
**Location**: Clara's childhood bedroom  
**Time**: Unknown  
**Atmosphere**: Morning-like light streams through the window, but it feels artificial—too perfect. A gentle ambient drone plays.

---

**[FADE IN: Clara's eyes flutter open. She stares at the ceiling, confused. A moment of silence.]**

**CLARA** (V.O., groggy): Where...?

**[She sits up slowly. Her room is exactly as she remembers it—posters of her favorite bands, a shelf of books, a small desk. But something is *off*. The proportions are wrong. The dresser seems too tall. The bed too soft. She rubs her eyes.]**

**CLARA** (V.O., realizing): I'm home? But... how did I get here?

**[She swings her legs out of bed. Her feet touch the carpet. It's damp. She looks down—the carpet is soaked, though there's no source. She stands, unsteady, and walks to the window.]**

**CLARA** (V.O., growing distress): This isn't right.

**[She peers outside. There is no world. Only a void—black, infinite, suffocating. No trees, no sky, no horizon. Her reflection in the glass is perfect, but it blinks a fraction of a second after she does.]**

**CLARA**: No... no, this is a dream. I'll wake up.

**[She pinches her arm. Nothing. She tries the window—it won't open. She tries harder, panic rising.]**

**CLARA** (breathless): This is a dream. This has to be a dream.

**[She turns and rushes to the bedroom door. She pulls. It won't budge. She pulls harder. The door is locked from the outside. Her breathing quickens.]**

**CLARA** (voice breaking): Hello? Mom? Dad? Emma?

**[Silence. Only her own breathing echoes. She sinks to the floor, back against the door. She looks around the room, trying to ground herself. That's when she notices something on her nightstand—a note, written in handwriting that might be her own, or might be someone else's. She crawls over and picks it up with trembling hands.]**

**[She reads it silently, her expression changing from confusion to horror.]**

**CLARA** (reading aloud, whisper): "You're still asleep, Clara. Don't wake up yet."

**[She drops the note. Her hands are shaking. She notices the bedside drawer is slightly open. She hesitates, then opens it fully. Inside is a flashlight, old and slightly rusted. It turns on with a weak, flickering beam. Attached to it is another note.]**

**CLARA** (reading): "You'll need this to see the truth."

**[She turns the flashlight over in her hands. The beam is unsteady, almost like a pulse—or a heartbeat. As the camera pulls back, we see Clara sitting in the center of her bedroom, the void visible through the window, the flashlight's pale beam barely reaching the corners of the room.]**

**CLARA** (V.O., determined but afraid): I need to get out of here. I need to wake up.

**[FADE TO BLACK]**

**[Opening credits roll]**

---

## 7. First Major Puzzle: "The Photograph Lock"

### Puzzle Name: The Living Room Lock (Area 1, Objective)

**Location**: The distorted living room of Clara's childhood home  
**Trigger**: Player attempts to leave through the front door, which is locked  
**Difficulty**: Easy-Medium (teaching puzzle)  
**Time Limit**: None (first puzzle, no pressure)

---

### Visual Setup

The living room is composed of furniture arranged in a circle, all slightly wrong in proportion:
- An oversized grandfather clock (face showing no numbers, hands spinning erratically)
- A sofa that's too wide for the room
- Two armchairs, one too small and one too large
- A coffee table with various items on it: a family photograph, a music box, a toy car, a book
- A locked cabinet with a keyhole shaped like a heart
- Family photographs hang on the walls, but they're distorted—faces are blurred or missing

### The Puzzle Mechanic

**Step 1: The Photograph Observation**
- On the coffee table is a photograph of Clara's family: Mom, Dad, Emma (older sister), and Clara (age 10, before the accident)
- When the player examines the photograph, Clara says: "This was from before everything changed..."
- The doll can be found in the corner and whispers: "There is always a first, isn't there? A beginning before the ending."

**Step 2: The Hidden Numbers**
- The player must examine each piece of furniture carefully:
  1. **The Grandfather Clock**: The hour hand points to 9
  2. **The Sofa**: 4 cushions visible
  3. **The Coffee Table**: 5 items (book, photo, music box, toy car, candle)
  4. **The Armchairs**: 2 chairs (one small = 1, one large = 3, total = 4)
  5. **The Cabinet**: 1 lock (heart-shaped)

**Step 3: The Sequence Logic**
- The numbers represent family importance or the order of the accident:
  - Clara (1, the survivor)
  - Emma (2, the driver, the one who caused it)
  - Dad (3, attempted to protect)
  - Mom (4, discovered them)
  - The Family Unit (5, shattered)

**Step 4: Input the Correct Sequence**
- Interacting with the heart-shaped lock opens a sequence input menu
- The player must input: 9-4-5-2-3 (or similar, depending on designer choice)
- Alternative logic: The player must rearrange the furniture in the room to spell out a number sequence with their positions

**Alternatively (More Complex Version)**:

The player could:
1. Find a key hidden in the music box (triggered by playing a specific melody)
2. Notice that the photographs on the wall are actually dates written in a cipher
3. Combine these clues to understand the lock mechanism requires the birth order of family members: Clara (9), Emma (4), etc.

### Solution

**Correct Input**: 9-4-5-2-3  
**Success Result**:
- The cabinet unlocks with a satisfying click
- The cabinet opens to reveal a **brass key** (ornate, with a bird-shaped head)
- Clara says: "This must be the key to get out of here."
- The doll smiles (visual change in sprite)

**Incorrect Attempts** (3 allowed):
- The lock glows red
- A distorted audio cue plays (discordant note)
- After 3 failures, the lock resets with a hint from the doll: "Look for patterns in what surrounds you. Family, time, loss... they're all connected."

### Use of the Brass Key

- The brass key opens the front door, revealing a hallway that leads to the next area
- Optional: Opening the front door shows the void outside for a moment before it transitions to the next location, reinforcing the surreal nature of the world

---

## 8. Clara's Sprite Sheet: Detailed Animation Specifications

### Base Specifications
- **Resolution**: 32x48 pixels (standing height)
- **Grid**: 8x12 pixels per frame within the sprite sheet
- **Total Frames Needed**: 45+ across all animations
- **Palette**: 14 colors (including transparency)
- **Outline**: 1-pixel black outline for all sprites for clarity in pixel art
- **Shading**: 3-4 shades per color for depth and dimension

---

### Color Palette

| Color | Hex | Purpose |
|-------|-----|---------|
| Transparent | #00FF00 | Background (magenta key) |
| Black | #000000 | Outlines, shadows |
| Skin Tone | #E8B8A8 | Face, hands |
| Dark Brown | #6B4423 | Hair |
| Light Brown | #8B6239 | Hair highlight |
| Yellow (Coat) | #FFE66D | Rain coat primary |
| Dark Yellow | #D4A940 | Rain coat shadow |
| White | #FFFFFF | Eyes, highlights |
| Dark Gray | #3A3A3A | Clothing shadow |
| Medium Gray | #696969 | Pants |
| Light Skin | #F0CBA8 | Skin highlight |
| Cyan (Glow) | #00D4FF | Flashlight effect |
| Purple (Distortion) | #9D4EDD | Fear/Sanity effect |
| Red | #CC0000 | Blood/Warning |

---

### Animation Suite

#### 1. **IDLE (Default State)**
- **Frames**: 4
- **Duration**: 0.3 seconds per frame (1.2s total loop)
- **Description**: Clara stands facing forward, coat hanging, slightly swaying
  
**Frame Breakdown**:
- Frame 1: Neutral standing, both arms at sides
- Frame 2: Slight sway left, right arm moves slightly
- Frame 3: Neutral again (return to center)
- Frame 4: Slight sway right, left arm moves slightly

**Animation Purpose**: Conveys patience and slight anxiety—breathing motion without overtly animating breathing

---

#### 2. **WALK (Movement)**
- **Frames**: 6
- **Duration**: 0.15 seconds per frame (0.9s total loop)
- **Description**: Clara walks cautiously, looking around nervously, feet stepping deliberately

**Frame Breakdown**:
- Frame 1: Left leg forward, arms naturally swinging
- Frame 2: Both legs at neutral stride
- Frame 3: Right leg forward, arms opposite swing
- Frame 4: Both legs neutral (mid-stride)
- Frame 5: Left leg forward again
- Frame 6: Both legs neutral (return to loop start)

**Head Movement**: Tilts slightly left and right between frames (adds nervousness)  
**Coat Movement**: Sways gently with each step

**Animation Purpose**: Shows deliberate, cautious movement—not running, but not calm either

---

#### 3. **RUN (High-Speed Movement)**
- **Frames**: 8
- **Duration**: 0.1 seconds per frame (0.8s total loop)
- **Description**: Clara sprinting in panic, coat flaring behind her, arms pumping, legs moving rapidly

**Frame Breakdown**:
- Frame 1: Left leg up, right leg back, left arm forward
- Frame 2: Right leg up, left leg back, right arm forward
- Frame 3: Left leg forward again (faster than walk cycle)
- Frame 4: Body leaning forward slightly, mid-stride
- Frame 5: Right leg extended far forward
- Frame 6: Recovery frame, arms pumping
- Frame 7: Left leg extends
- Frame 8: Return to near-neutral running pose

**Head Position**: Slightly tilted down (looking where she's running)  
**Coat**: Flares out dramatically behind her, suggesting wind resistance  
**Shoes**: Show motion lines or blur

**Animation Purpose**: Conveys panic and urgency—fast, almost desperate

---

#### 4. **FLASHLIGHT_HOLD (Static Pose)**
- **Frames**: 1 (static, no animation)
- **Description**: Clara holding flashlight forward with both hands, arms extended

**Details**:
- Flashlight sprite extends 8 pixels in front of Clara
- A light cone effect (semi-transparent) projects outward
- Clara's expression is determined but fearful
- Hands are shown gripping the flashlight tightly

**Animation Purpose**: Used when player is actively using the flashlight in dark areas

---

#### 5. **PANICKED_BREATHING (Fear State)**
- **Frames**: 5
- **Duration**: 0.2 seconds per frame (1.0s total loop)
- **Description**: Clara hunched over, heavy breathing, coat heaving

**Frame Breakdown**:
- Frame 1: Standing, normal posture, shallow breath
- Frame 2: Hunched forward slightly, chest expanding
- Frame 3: Deeply hunched, breathing in (maximum air intake)
- Frame 4: Hunching back slightly, breathing out
- Frame 5: Return to near-neutral, but trembling slightly

**Visual Details**:
- Eyes wide open
- Mouth slightly open, breathing heavily
- Coat heaves with each breath
- Hands are clenched
- Optional: Add motion lines radiating from Clara suggesting distress

**Animation Purpose**: Triggers during high Sanity loss or after encounters with the Entity

---

#### 6. **INTERACT / EXAMINE (Puzzle Solving)**
- **Frames**: 3
- **Duration**: 0.25 seconds per frame (0.75s total)
- **Description**: Clara leans forward and reaches toward an object

**Frame Breakdown**:
- Frame 1: Neutral standing position, arms at sides
- Frame 2: Leaning forward (45-degree angle), arms extending forward
- Frame 3: Fully bent forward, hands reaching out, almost touching an object

**Visual Details**:
- Head tilts down to look at object
- Eyes widen slightly in curiosity
- Coat bunches up at the front from the forward lean

**Animation Purpose**: Plays when player interacts with items or puzzles

---

#### 7. **FEAR_REACTION (Trauma Response)**
- **Frames**: 1 (static) + 0.5-second hold
- **Description**: Immediate shock upon seeing the Entity or a major horror moment

**Visual Details**:
- Eyes wide open (nearly fully dilated)
- Mouth open in a silent scream or gasp
- Hands raised up to sides of face
- Body is rigid and trembling
- Coat stands on end (suggesting electricity or extreme fear)

**Animation Purpose**: Single-frame shock reaction, held for dramatic effect

---

#### 8. **HIDING (Stealth Position)**
- **Frames**: 1 (static) per location
- **Description**: Clara crouched or concealed, barely visible

**Variations**:
- **In Closet**: Clara crouched, visible only as a small silhouette, eyes barely visible
- **Under Bed**: Clara curled up, visible between the bed frame and floor
- **Behind Furniture**: Partially obscured by a wardrobe or curtain

**Visual Details**:
- Head lowered
- Body compressed/folded
- Breathing visible but shallow
- Eyes tracking, looking around nervously

**Animation Purpose**: Plays when player initiates hiding in safe locations

---

#### 9. **FALLING / HURT (Damage State)**
- **Frames**: 2 (optional, for extended gameplay)
- **Duration**: 0.3 seconds per frame

**Frame 1**: Clara stumbling backward, arms flailing
**Frame 2**: Clara on ground, sitting/fallen position

**Animation Purpose**: If the Entity catches Clara, shows her being thrown or falling

---

### Direction Variations

**All animations exist in 4 directions**:
1. **Down** (facing camera): Primary perspective
2. **Up** (back to camera): For fleeing or moving away
3. **Left** (profile): Used when moving left
4. **Right** (profile, mirrored): Used when moving right

**Note**: For a top-down game, up/down variants show character facing different directions relative to the camera, while left/right are horizontal perspectives.

---

### Additional Sprite Elements

#### **Flashlight Prop Sprite** (8x16px)
- Metallic body with cylindrical shape
- A glowing circular lens at the front
- When held by Clara, attaches to her hand sprite
- Emits light cone effect

#### **Light Cone Effect** (Dynamic)
- Semi-transparent yellow/white gradient
- Expands as it projects outward from the flashlight
- Affected by walls and obstacles (blocks light realistically)

#### **Distortion Overlay** (For Sanity States)
- Applied over Clara's sprite when Sanity is low
- Chromatic aberration (red/cyan color shift)
- Scan lines (horizontal lines)
- Glitch effect (random line displacement)

---

### Animation Implementation Notes

**Total Sprite Sheet Size**: 
- 8 animations × 4 directions × varying frames
- Approximately 2048x1024 pixels total (assuming efficient grid layout)
- Organized as a single sprite sheet for optimal rendering performance

**Frame Rate**:
- Base frame rate: 60 FPS
- Animations adjusted for visual clarity (slower for dramatic moments, faster for action)

**Optimization**:
- Left and right directions can use the same sprite sheet with horizontal flipping
- Reduces sprite sheet size by ~25%
- Final optimized sheet: ~1536x1024 pixels

---

## 9. Audio Design (Brief Overview)

### Ambient Soundscape
- **Base Layer**: Subtle drone (100Hz sine wave, barely perceptible)
- **Environmental Layer**: Creaking floorboards, wind howling outside void, faint clock ticking
- **Emotional Layer**: Heartbeat (varies with Sanity level)

### Interactive SFX
- **Footsteps**: Soft, careful steps in hallway; echoing in empty rooms
- **Flashlight**: Click when toggled on/off; hum when active
- **Entity**: Distorted breathing, static crackle, reversed human voice

### Music
- **Area 1 (House)**: Soft, nostalgic piano melody corrupted by dissonance
- **Area 2 (School)**: Industrial ambience with distant, echoing bells
- **Area 3 (Asylum)**: Purely atmospheric; minimal melodic content; focus on unease

---

## 10. Development Roadmap

### Phase 1: Vertical Slice (2-3 weeks)
- Implement Area 1: The Distorted House
- Create Clara's full sprite sheet
- Code basic movement, flashlight mechanic, UI
- Design and implement "The Photograph Lock" puzzle

### Phase 2: Core Systems (3-4 weeks)
- Sanity/Fear meter system
- Entity AI and pathfinding
- Stealth and hiding mechanics
- Sound design and audio implementation

### Phase 3: Narrative & Level Design (4-6 weeks)
- Area 2: The Infinite School Corridor
- Area 3: The Sunken Asylum
- Dialogue system and faceport portraits
- Companion doll interactions

### Phase 4: Polish & Testing (2-3 weeks)
- Bug fixes and optimization
- Player feedback integration
- Difficulty balancing
- Visual polish and VFX refinement

---

## 11. Design Principles & Conclusion

### Core Design Philosophy
1. **Psychological Over Physical**: Horror comes from uncertainty and guilt, not gore
2. **Player Agency in Narrative**: Choices matter; two distinct endings reward different playstyles
3. **Atmosphere as Gameplay**: The environment itself is a puzzle to be understood
4. **Emotional Authenticity**: Clara's trauma is universal—loss, guilt, the weight of living after tragedy

### Target Audience
- Players aged 16+ who enjoy psychological horror
- Fans of Ib, The Witch's House, and narrative-driven indie games
- Players seeking meaningful emotional engagement over action

### Unique Selling Points
- Deeply personal narrative wrapped in pixel art aesthetics
- Stealth-based horror without combat
- Two mechanically different endings (not just cosmetic choices)
- Therapist-approved exploration of trauma, coping, and forgiveness

---

**END OF GAME DESIGN DOCUMENT**

*This document is a living design; adjustments should be made during playtesting and development based on player feedback and technical constraints.*
