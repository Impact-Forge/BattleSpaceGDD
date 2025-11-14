---
title: Medical System
layout: default
---

# BattleSpace - Medical System

**Version:** 1.0  
**Last Updated:** November 2025  
**Design Philosophy:** Engaging tactical medical gameplay without excessive complexity

---

## 1. System Overview

The BattleSpace medical system balances tactical depth with accessibility, creating meaningful medic gameplay without overwhelming players. The system focuses on **three core pillars**:

1. **Bandaging** - Stop bleeding and stabilize wounded players
2. **Revival** - Bring incapacitated teammates back to the fight
3. **Healing** - Restore health to damaged body parts

**Design Goals:**
- Medic role is essential and rewarding
- Players understand their medical state intuitively
- Medical actions require tactical decision-making
- System scales from solo play to coordinated squad operations
- Performance-friendly for 32v32 combat

---

## 2. Health System

### 2.1 Hit Zone System

Players have **six distinct body parts**, each with independent health pools:

| Body Part | Health Pool | Death Threshold | Functionality Impact |
|---|---|---|---|
| Head | 100 HP | Instant death at 0 HP | Vision blur below 50 HP |
| Torso | 100 HP | Incapacitation at 0 HP | — |
| Left Arm | 50 HP | — | Weapon sway penalty |
| Right Arm | 50 HP | — | Weapon sway penalty |
| Left Leg | 50 HP | — | Movement speed penalty |
| Right Leg | 50 HP | — | Movement speed penalty |

**Key Mechanics:**
- Head damage is lethal - headshots at 0 HP result in immediate death (no revival)
- Torso damage at 0 HP causes incapacitation (player can be revived)
- Limb damage reduces combat effectiveness but does not cause incapacitation
- Each body part bleeds independently

### 2.2 Player States

**Healthy (All body parts > 0 HP)**
- Full combat capability
- Can sprint, aim accurately, move at full speed
- All actions available

**Wounded (One or more body parts damaged)**
- Visual feedback: Blood effects, screen vignette intensity based on damage
- Audio feedback: Heavy breathing, groaning based on pain level
- Functional penalties based on damaged body part:
  - **Arms:** +25% weapon sway per damaged arm
  - **Legs:** -20% movement speed per damaged leg
  - **Torso:** -10% stamina regeneration

**Bleeding (Active bleed on any body part)**
- HP drains over time from affected body part
- Bleeding rate: 2-10 HP per second (based on wound severity)
- Blood trail visible to other players
- Screen desaturation effect increases with blood loss
- Critical bleeding (>5 HP/s) shows pulsing red screen edge
- Death occurs when torso or head reaches 0 HP

**Incapacitated (Torso reaches 0 HP)**
- Cannot move, shoot, or use items
- Can communicate via voice (reduced volume)
- Can see surroundings (reduced vision radius)
- Bleeds out in 120 seconds without medical intervention
- Bleedout timer visible to nearby teammates
- Can be revived by any player with appropriate medical supplies

**Dead**
- Headshot death: No revival possible
- Bleedout death: Exceeded incapacitation timer
- Must respawn at designated spawn point
- Body ragdolls and remains for 30 seconds (visual confirmation)

---

## 3. Injury & Bleeding System

### 3.1 Wound Types

**Light Wound**
- Caused by: Pistol rounds, shrapnel (distance >20m), grazing hits
- Bleeding rate: 2 HP per second
- Requires: 1 bandage to stop bleeding

**Moderate Wound**
- Caused by: Rifle rounds, close shrapnel (distance 10-20m), fall damage
- Bleeding rate: 5 HP per second
- Requires: 2 bandages to stop bleeding

**Severe Wound**
- Caused by: High-caliber rounds, direct explosion, vehicle collision
- Bleeding rate: 10 HP per second
- Requires: 3 bandages to stop bleeding
- Visual: Heavy blood spurt effect, large blood pool

### 3.2 Multiple Wounds

- Each body part can have multiple active wounds
- Bleeding rates stack (e.g., 2 moderate wounds = 10 HP/s total)
- Bandaging addresses one wound at a time (most severe first)
- Maximum 3 wounds per body part before bleedout is inevitable without immediate treatment

### 3.3 Pain System

**Pain Threshold:**
- Pain accumulates based on damage taken (not current HP)
- Pain level: 0-100 (increases with damage, decreases slowly over time)
- Effects begin at Pain > 30

**Pain Effects:**
- **30-50 Pain:** Slight vision blur, minor aim sway increase (+10%)
- **50-75 Pain:** Moderate vision blur, significant aim sway (+25%), occasional screen flash
- **75-100 Pain:** Severe vision blur, extreme aim sway (+50%), frequent screen flash, movement speed -10%

**Pain Management:**
- Pain naturally decreases at 5 points per minute
- Morphine (medic only) instantly reduces pain by 50 points
- Morphine lasts 5 minutes, provides complete pain suppression

---

## 4. Medical Items & Actions

### 4.1 Bandages

**Field Dressing (Standard Bandage)**
- **Availability:** All players carry 2 bandages
- **Application time:** 5 seconds
- **Effect:** Stops one active bleed on target body part
- **Animation:** A_C_Bandage / A_I_Bandage
- **Usage:** Can self-apply or apply to teammate
- **Resupply:** Ammo caches, medical vehicle, medic supply drop

**How Bandaging Works:**
1. Approach wounded player (or self-treat)
2. Select bandage from inventory
3. Target specific body part showing bleed icon
4. Hold interaction key for 5 seconds
5. Bandage applied - one bleed stopped

**Tactical Considerations:**
- Vulnerable during application (cannot move, weapon lowered)
- Prioritize severe bleeds first (automatically targets worst bleed)
- Can bandage while prone or behind cover
- Squad callouts: "Bandaging!" voice line plays automatically

### 4.2 Medical Kit

**Personal Medical Kit**
- **Availability:** Medic role only (starts with 1, can carry 2 maximum)
- **Application time:** 10 seconds per body part
- **Effect:** Restores 50 HP to selected body part
- **Animation:** A_C_MedicalKit / A_I_MedicalKit
- **Usage:** Teammate only (cannot self-heal with medical kit)
- **Charges:** 6 uses per kit (one per body part for one full heal)
- **Resupply:** Medical vehicle, main base medical facility

**Healing Mechanics:**
- Must stop all bleeding on body part before healing can begin
- Healing is channeled - interruption cancels and wastes charge
- Partial healing not possible (full 10 seconds or nothing)
- Cannot heal dead players
- Can heal incapacitated players to stabilize before revival

**Field Limitations:**
- Maximum field heal: 50 HP per body part
- Full heal (100 HP) requires:
  - Medical facility (permanent structure)
  - Medical vehicle (mobile ambulance)
  - MASH tent (medic deployable)

### 4.3 Revival Items

**Epinephrine Auto-Injector**
- **Availability:** Medic role only (starts with 2)
- **Application time:** 8 seconds
- **Effect:** Revives incapacitated player to 50 HP (torso only)
- **Animation:** A_C_Epinephrine / A_I_Epinephrine
- **Usage:** Incapacitated teammates only
- **Resupply:** Medical vehicle, main base medical facility

**Revival Process:**
1. Approach incapacitated player
2. All critical bleeds must be bandaged first
3. Select epinephrine from inventory
4. Channel for 8 seconds
5. Player revived at 50 HP torso, all limbs at last known HP
6. Revived player has 10 second "grace period" with -50% incoming damage

**Revival Restrictions:**
- Cannot revive headshot deaths (instant death, no incap state)
- Cannot revive if bleedout timer expired
- Must bandage torso bleeds before revival possible
- Revived player cannot sprint for 5 seconds (recovery period)

### 4.4 Pain Management

**Morphine Auto-Injector**
- **Availability:** Medic role only (starts with 3)
- **Application time:** 3 seconds
- **Effect:** Instantly reduces pain by 50 points, prevents pain accumulation for 5 minutes
- **Animation:** A_C_Morphine / A_I_Morphine
- **Usage:** Self or teammate
- **Resupply:** Medical vehicle, main base medical facility

**Morphine Mechanics:**
- Provides immediate combat effectiveness restoration
- Does not heal damage, only suppresses pain effects
- Duration: 5 minutes
- Can be applied preemptively before engagement
- Overdose: Using 3+ morphine within 10 minutes causes 5-second unconsciousness (rare)

---

## 5. Medical Animations

All medical actions feature dedicated character and item animations for visual clarity and immersion.

### 5.1 Medical Item Animations

**Bandaging:**
- `A_C_Bandage` - Character wraps bandage around body part
- `A_I_Bandage` - Bandage item unwrapping and application
- Duration: 5 seconds
- Can be performed prone, crouched, or standing

**Medical Kit:**
- `A_C_MedicalKit` - Character opens medical bag, applies supplies
- `A_I_MedicalKit` - Medical supplies being retrieved and used
- Duration: 10 seconds
- Requires medic to kneel beside patient

**Epinephrine:**
- `A_C_Epinephrine` - Character administers auto-injector to torso
- `A_I_Epinephrine` - Auto-injector device activation
- Duration: 8 seconds
- Dramatic revival animation on success

**Morphine:**
- `A_C_Morphine` - Quick injection to thigh/arm
- `A_I_Morphine` - Auto-injector usage
- Duration: 3 seconds
- Fast application for combat situations

### 5.2 Animation Interruption

- All medical animations can be interrupted by:
  - Taking damage
  - Movement input (intentional cancel)
  - Entering vehicle
  - Player death
- Interrupted actions consume the item but provide no benefit
- Revival interruption is particularly costly (wastes epinephrine)

---

## 6. Medic Role

### 6.1 Medic Loadout

**Starting Equipment:**
- 6x Field Dressings (standard bandages)
- 1x Personal Medical Kit (6 charges)
- 2x Epinephrine Auto-Injectors
- 3x Morphine Auto-Injectors
- 1x Smoke Grenade (for medical cover)

**Weight Considerations:**
- Medical supplies add 8kg to loadout
- Reduced ammunition capacity (3 magazines vs. 6 for rifleman)
- Cannot carry heavy weapons
- Faster sprint speed than other roles (+5%) for medical emergencies

### 6.2 Medic Abilities

**Medical Triage HUD**
- Medic can see wounded player indicators through walls (within 50m)
- Wounded players show:
  - Health bar above nameplate
  - Bleed severity indicator (pulsing red)
  - Incapacitation status (grey icon)
- Allows medic to prioritize critical patients

**Supply Resupply**
- Medic can resupply bandages to teammates
- Transfer action: 3 seconds, gives 2 bandages to teammate
- Medic must have at least 4 bandages to share

**MASH Deployment** (Advanced Feature)
- Medic can deploy Mobile Army Surgical Hospital (MASH)
- Requires: Medical vehicle within 25m
- Deployment time: 45 seconds
- Effect: Creates field hospital with full healing capability
- Capacity: 2 players simultaneously
- Duration: Permanent until destroyed or manually packed
- Destruction: 500 HP, destroyed by explosives or sustained fire

---

## 7. Medical Facilities

### 7.1 Permanent Medical Facilities

**Main Base Hospital**
- Location: Team main spawn base
- Capacity: 8 players simultaneously
- Healing rate: Instant full heal on all body parts
- Free access: No supply cost
- Resupply station for all medical items

**Captured Field Hospital**
- Location: Designated capture points on map
- Capacity: 4 players simultaneously
- Healing rate: 10 HP per second (10 seconds for full heal)
- Requires: Friendly control of capture point
- Limited resupply: Bandages only

### 7.2 Mobile Medical Assets

**Medical Vehicle (Ambulance)**
- Deployed by commander or spawned at motor pool
- Driver + 3 passengers
- Interior healing zone: 50 HP per body part maximum
- Exterior resupply point for all medical items
- HP: 800 (light armor, vulnerable to small arms)
- Speed: Fast (80 km/h), good off-road capability

**MASH Tent (Medic Deployable)**
- Deployed by medic role only
- Requires medical vehicle proximity
- Provides full healing (100 HP per body part)
- Capacity: 2 players simultaneously
- Healing rate: 5 HP per second (20 seconds for full heal)
- Destructible: 500 HP structure
- Visible on tactical map to teammates

---

## 8. Medical Tactics & Strategies

### 8.1 Casualty Priorities

**Triage System (Medic Decision Making):**

1. **Immediate (Red)** - Incapacitated with <30 seconds bleedout remaining
   - Priority: Immediate bandage + revival
   - Risk: High - may lose patient if delayed

2. **Urgent (Yellow)** - Severe bleeding (>5 HP/s), still conscious
   - Priority: Bandage severe bleeds to prevent incapacitation
   - Risk: Medium - will become Immediate if untreated

3. **Delayed (Green)** - Light/moderate wounds, functional
   - Priority: Bandage when safe, low urgency
   - Risk: Low - can wait for lull in combat

4. **Expectant (Black)** - Headshot death, bleedout timer expired
   - Priority: None - cannot be saved
   - Action: Move to next patient

### 8.2 Medical Tactics

**"Combat Medic" Playstyle:**
- Stay 10-15m behind frontline infantry
- Use smoke grenades to create medical cover
- Prioritize squad members over distant teammates
- Call out medical status: "Two down, need cover!"
- Coordinate with Squad Leader for rally point safety

**"Trauma Surgeon" Playstyle:**
- Operate from MASH tent or medical vehicle
- Create backline triage station
- Radio calls for wounded to fall back to medical position
- Maximum healing efficiency, minimum combat exposure
- Defend medical facility as priority target

**Squad Medical Coordination:**
- Buddy system: Pairs watch each other's health
- Self-bandaging reduces medic workload
- Call "Medic!" voice command (automatic on incapacitation)
- Drop smoke for medic approach vectors
- Cover medic during revival channeling

---

## 9. Balance & Tuning

### 9.1 Time-to-Kill vs. Time-to-Heal

**Design Intent:**
- TTK (Time to Kill): 0.5-2 seconds for skilled players
- Time to Stabilize: 5-15 seconds (bandaging)
- Time to Revival: 8 seconds (epinephrine)
- Time to Full Heal: 10 seconds (medical kit in field), 20 seconds (MASH)

**Tuning Philosophy:**
- Fast enough to keep combat flowing
- Slow enough to create tactical vulnerability
- Rewards coordinated squad protection during medical treatment

### 9.2 Medical Supply Economy

**Supply Sources:**
- Starting loadout (sufficient for 1-2 casualties)
- Ammo cache resupply: Bandages only
- Medical vehicle: Full resupply, no cost
- Main base: Full resupply, no cost

**Supply Costs (Capital Warfare Mode):**
- Personal Medical Kit: $50 (medic purchase)
- Epinephrine: $75 (medic purchase)
- Morphine: $25 (medic purchase)
- Bandages: Free (unlimited resupply)
- Medical Vehicle spawn: $2,000 (team capital)

### 9.3 Death Penalties

**Respawn System:**
- Death timer: 15 seconds base
- Spawn location: Rally point, FOB, or main base
- Equipment: Respawn with last selected loadout
- Penalty: Team loses $25 capital per death (Capital Warfare)

**Revival vs. Respawn:**
- Revival saves team capital and maintains squad position
- Revived player returns to combat immediately at reduced HP
- Encourages risk-taking for medic players
- Rewards squads that protect their medic

---

## 10. UI & Feedback

### 10.1 Player HUD Elements

**Health Display:**
- Body part diagram in lower right corner
- Color-coded HP per body part:
  - Green: >75% HP
  - Yellow: 50-75% HP
  - Orange: 25-50% HP
  - Red: <25% HP
  - Grey: 0 HP (incapacitated)
- Bleed indicators: Pulsing red droplet icon on bleeding body parts
- Pain meter: Horizontal bar above health display

**Medical Action Feedback:**
- Progress bar for bandaging/healing/revival actions
- Text notification: "Bandaging left leg..." (2/3 bleeds stopped)
- Audio cues: Bandage tearing, medical kit rustling, injector click
- Teammate notification: "Medic is treating you" (5 seconds remaining)

### 10.2 Medic-Specific HUD

**Triage Overlay:**
- Wounded players highlighted through walls (50m range)
- Health percentage displayed above nameplate
- Color-coded urgency:
  - Red: Incapacitated or critical bleeding
  - Yellow: Wounded, moderate bleeding
  - Green: Minor wounds
- Distance to patient in meters
- Bleedout timer (incapacitated patients only)

**Supply Tracking:**
- Medical inventory always visible in corner of screen
- Numeric count for each item type
- Flashing indicator when supplies low (<2 bandages, <1 epinephrine)

---

## 11. Performance Considerations

### 11.1 Network Optimization

**Health Replication:**
- Body part HP replicated at 5 Hz (every 200ms)
- Bleed status replicated at 2 Hz (every 500ms)
- Medical action events: Reliable RPC calls
- Bandwidth per player: ~0.5 KB/s for medical system

### 11.2 Animation System

**LOD (Level of Detail) for Medical Animations:**
- Full animation: <10m from camera
- Simplified animation: 10-30m from camera
- No animation (instant effect): >30m from camera

**Performance Targets:**
- Medical animations: Max 2ms CPU time per frame
- Blood particle effects: Max 500 active particles
- Health UI updates: Max 1ms CPU time per frame

---

## 12. Future Expansion

**Post-MVP Features (Not in Initial Release):**

### 12.1 Advanced Wound System
- Fractures (limb immobilization, requires splint)
- Internal bleeding (not visible, requires diagnosis)
- Infection mechanic (long-duration wounds without treatment)

### 12.2 Medical Specializations
- Combat Lifesaver (basic medic for non-medic roles)
- Paramedic (advanced revival capabilities)
- Field Surgeon (can perform complex procedures at MASH)

### 12.3 Additional Medical Items
- Splints (fracture treatment)
- IV Saline (blood volume restoration)
- Chest Seals (punctured lung treatment)
- Tourniquets (limb-specific severe bleed control)

### 12.4 Medical Vehicle Variants
- Armored ambulance (better protection, slower)
- Medical UTV (fast extraction, light capacity)
- Medical helicopter (aerial evacuation)

**Design Philosophy for Expansion:**
- Add complexity only after core medical loop is proven fun
- Maintain 60 FPS performance target
- Keep medic role accessible to new players
- Avoid "sim" complexity that slows gameplay

---

## Document Changelog

- **v1.0** (Nov 2025): Initial medical system design
- Core focus: Bandage, revive, heal
- Simplified from ACE Medical references
- Omitted cardiovascular/cardiac arrest complexity
- Aligned with BattleSpace MVP scope

