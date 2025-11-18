---
title: Core Gameplay Mechanics
layout: default
---

# BattleSpace - Core Gameplay Mechanics

**Version:** 1.0  
**Last Updated:** November 2025  
**Target:** 32v32 Capital Warfare Mode

---

## 1. Player Movement System

### 1.1 Movement States

| Movement State | Speed | Stamina Drain | Noise Level |
|---|---|---|---|
| Walk | 2.0 m/s | None | Low (10m detection) |
| Jog | 4.0 m/s | 5/s | Medium (25m detection) |
| Sprint | 6.0 m/s | 15/s | High (50m detection) |
| Crouch Walk | 1.5 m/s | None | Very Low (5m detection) |
| Prone Crawl | 1.0 m/s | 2/s | Silent (0m detection) |

**Stamina System:**
- Maximum stamina: 100 points
- Regeneration rate: 10 points/second (when not sprinting)
- Sprint disabled below 10 stamina
- Recovery penalty: 5 second delay after full stamina depletion

### 1.2 Stance System

**Supported Stances:**
- **Standing** - Default combat stance, full movement speed
- **Crouched** - 75% movement speed, 50% reduced profile
- **Prone** - 50% movement speed, 80% reduced profile
- **Supine** (roll from prone) - Defensive position, no movement

**Stance Transitions:**
- Stand → Crouch: 0.3 seconds
- Crouch → Stand: 0.3 seconds
- Crouch → Prone: 0.8 seconds
- Prone → Crouch: 1.0 seconds
- Prone → Supine Roll: 0.5 seconds

**Design Notes:**
- Prone state uses custom physics movement mode
- Vaulting requires clear obstacle height check (maximum 120cm)
- Mantling provides vertical boost to overcome tall obstacles

### 1.3 Advanced Movement

**Vaulting:**
- Height range: 60cm - 120cm
- Forward velocity maintained at 80%
- Animation: 0.6s vault over time
- Cannot vault while ADS or carrying heavy weapons (>8kg)

**Mantling:**
- Height range: 120cm - 250cm
- Player velocity reset to zero during mantle
- Animation: 1.2s climb time
- Weapon lowered automatically

**Swimming:**
- Surface speed: 150 cm/s
- Underwater speed: 100 cm/s
- Breath hold: 45 seconds
- Weapons inoperable while swimming
- Inventory weight penalty: -10 cm/s per 5kg over 15kg

---

## 2. Combat Mechanics

### 2.1 Weapon Handling

**Aim Down Sights (ADS):**
- ADS transition time: 0.35 seconds
- Movement speed while ADS: 50% of base speed
- Cannot sprint while aiming
- ADS accuracy bonus: 75% reduction in weapon sway

**Weapon Sway:**
- Base sway (hip fire): ±2 degrees
- ADS sway: ±0.5 degrees
- Stamina below 30%: +50% sway penalty
- Breath hold (Shift key): -75% sway for 5 seconds, 30 second cooldown

**Recoil System:**
- Vertical recoil: 1.5 degrees per shot (average)
- Horizontal recoil: ±0.8 degrees random
- Recoil recovery: 5 degrees per second
- Sustained fire increases recoil accumulation
- Crouched: -25% recoil, Prone: -50% recoil

### 2.2 Damage System

**Damage Model:** Locational hit detection with armor penetration

| Body Part | Damage Multiplier | Armor Coverage |
|---|---|---|
| Head | 4.0x | Helmet (Lvl 2-4) |
| Neck | 2.5x | None |
| Chest | 1.0x | Plate Carrier |
| Abdomen | 1.2x | Plate Carrier |
| Arms | 0.6x | None |
| Legs | 0.7x | None |

**Armor System:**
- Armor reduces damage by 40% to covered areas
- Helmet protection levels: Lvl 2 (pistol), Lvl 3 (rifle), Lvl 4 (armor-piercing)
- Plate carriers protect chest and abdomen only
- Armor degrades with repeated hits (5 hits to failure)

### 2.3 Ballistics

**Terminal Ballistics Integration:**
- Bullet drop calculated per projectile
- Wind deflection at >500m range
- Penetration values per material type
- Ricochet angles: <15° deflection, >15° penetration attempt

**Zeroing Ranges:** 100m, 200m, 300m, 400m, 500m, 600m
- Press PageUp/PageDown to adjust zero
- Optic reticle adjusts to selected zero

---

## 3. Squad & Team Mechanics

### 3.1 Squad System

**Structure:**
- Squad size: 6 players maximum
- 1 Squad Leader (required)
- 5 Squad Members (flexible roles)

**Squad Leader Abilities:**
- Deploy rally points (mobile spawn beacons)
- Place tactical markers on map
- Request commander support
- Coordinate with other squad leaders
- View enhanced tactical information

**Rally Point Mechanics:**
- Placement cooldown: 120 seconds
- Active duration: 180 seconds
- Minimum distance from enemy: 150m
- Spawn limit: 10 spawns before depleted
- Automatically destroyed if enemy within 25m for 10 seconds
- Only one rally point active per squad

### 3.2 Voice Communication

**VOIP System:**
- **Local Voice:** 50m radius, all players can hear
- **Squad Radio:** Unlimited range, squad members only
- **Command Radio:** Squad Leader to Squad Leader communication
- **Proximity Detection:** Enemy players can hear your local voice at 15m

**Radio Mechanics:**
- Radio equipment required for squad/command channels
- Local voice always available (simulates shouting)
- Voice quality degrades with distance
- Radio interference possible through enemy EW (Electronic Warfare) assets

---

## 4. Territory Control

### 4.1 Capture Points

**Capture Mechanics:**
- Capture radius: 50m sphere from flag
- Capture rate: 1% per second per player (maximum 5 players = 5%/second)
- Capture time: 20-100 seconds (depends on player count)
- Contested state: Both teams present, no capture progress
- Neutralization required: Enemy points must reach 0% before friendly capture begins

**Point States:**
- **Neutral:** Uncontrolled, can be captured by either team
- **Capturing (Friendly):** Your team is capturing, progress bar advancing
- **Capturing (Enemy):** Enemy team is capturing
- **Contested:** Both teams present, no progress made
- **Friendly Controlled:** Your team controls the point
- **Enemy Controlled:** Enemy team controls the point

**Capture Priority:**
- Players inside capture zone contribute to capture progress
- Maximum 5 players counted (additional players provide no benefit)
- Squad Leaders provide 1.5x capture speed bonus

### 4.2 Infrastructure System

**Deployable Structures:**

| Structure | Cost | Build Time | Function |
|---|---|---|---|
| FOB Radio | $500 | 60s | Command/spawn point |
| Ammo Cache | $300 | 30s | Resupply ammunition |
| Repair Station | $400 | 45s | Vehicle repairs |
| MG Emplacement | $250 | 30s | Static defense |
| AT Emplacement | $350 | 45s | Anti-vehicle |
| Sandbag Wall | $50 | 10s | Light cover |
| HESCO Barrier | $150 | 20s | Heavy cover |

**Build Requirements:**
- Engineer role required
- Must be within friendly territory
- Cannot build within 100m of active combat (suppression zone)
- Limited by team resource pool

---

## 5. Vehicle System

### 5.1 Vehicle Categories

**Light Vehicles:**
- Jeeps, trucks, light armored vehicles
- Seating: 2-8 players
- Armor: Small arms resistant
- Speed: 60-100 km/h

**Heavy Vehicles:**
- APCs, IFVs, MBTs
- Seating: 2-4 crew
- Armor: Heavy caliber resistant
- Speed: 40-70 km/h
- Requires Crewman role

**Logistics Vehicles:**
- Supply trucks, fuel tankers
- Capacity: 3000 supply points
- Critical for FOB construction
- Unarmed, lightly armored

### 5.2 Vehicle Damage Model

**Component Damage System:**
- Vehicles have multiple damageable components (engine, tracks, turret, etc.)
- Each component has independent health pool
- Component damage affects vehicle functionality
- Destroyed components cannot be field-repaired

**Damage States:**
- **100-75% HP:** Fully operational, no performance penalty
- **75-50% HP:** Performance degraded (reduced speed/turret traverse)
- **50-25% HP:** Critical damage (smoke effects, weapon accuracy penalty)
- **25-0% HP:** Disabled (immobile, weapons offline)
- **0% HP:** Destroyed (explosion, vehicle is lost, cannot be repaired)

**Repair System:**
- Repair tool (Engineer): 10 HP per second
- Repair vehicle: 25 HP per second
- Cannot repair fully destroyed components in field
- Destroyed vehicles must return to base for full rebuild

---

## 6. Medical System

### 6.1 Health States

**Health Thresholds:**
- Maximum health: 100 HP
- Incapacitated threshold: Below 25 HP (player goes down)
- Bleedout timer: 120 seconds when incapacitated
- Death: After bleedout timer expires or catastrophic damage

**Player States:**
- **Healthy (100-26 HP):** Full combat capability, no penalties
- **Wounded (25-1 HP):** Movement speed reduced 20%, blurred vision, heavy breathing
- **Incapacitated (0 HP):** Cannot move or shoot, requires medic revive, bleeding out
- **Dead:** Must respawn at designated spawn point

### 6.2 Healing Mechanics

**Medic Abilities:**
- **Bandage:** Stops bleeding, restores 25 HP, 5 second application time
- **Medkit:** Full heal over 10 seconds (cannot move during healing)
- **Revive:** Restore incapacitated player to 50 HP, 8 second channeling time
- **Field Surgery:** Advanced healing for critical wounds (Medic only)

**Self-Healing:**
- All players carry 2 bandages in default loadout
- Bandage application: 5 seconds (cannot move while bandaging)
- Restores 25 HP and stops bleeding effects
- Cannot self-revive from incapacitated state
- Additional medical supplies can be purchased or resupplied at ammo caches

---

## 7. Economy System (Capital Warfare)

### 7.1 Resource Generation

**Income Sources (Reward-Focused):**
- Enemy kill: $25
- Kill assist: $15
- Territory capture: $50 per player
- Territory defense: $25 (kill within 50m of friendly point)
- Vehicle destruction: $50-$500 (based on vehicle value)
- Revive teammate: $20
- Resupply teammate: $15
- Repair vehicle: $10 per 25 HP repaired
- Spotting assist: $10 (enemy you spotted gets killed)
- Squad order completion: $50
- Territory control: $50 per minute per sector controlled
- Objective completion: $100-$500 (based on objective importance)
- Resource extraction: Variable income from captured industrial sites

**Performance Bonuses:**
- 3 kill streak: +$25 bonus
- 5 kill streak: +$50 bonus
- 10 kill streak: +$100 bonus + team announcement
- Role performance bonuses (Medic: 5 revives = $100, Engineer: 500 HP repairs = $100, etc.)

**Team Economy:**
- Starting capital: $10,000 per team
- Capital goal (victory): $1,000,000
- Bankruptcy threshold (defeat): $0
- Income is shared across entire team
- Commander manages major expenditures

### 7.2 Expenditures

**Death Cost:**
- Flat respawn cost: $25 (no escalation)
- Equipment persistent until death (purchased loadouts don't need repurchasing unless you die)

**Equipment Costs:**
- Standard loadout: $0 (free)
- Upgraded weapons: $100-$500
- Armor plates: $150
- Grenades: $25 each
- Medical supplies: $50
- Insurance (50% refund on death): $50 (for loadouts $300+)

**Vehicle Costs (Base):**
- Light transport: $500
- Armed jeep: $1,500
- APC: $5,000
- IFV: $8,000
- MBT: $15,000
- Attack helicopter: $25,000

**Vehicle Upgrade Tiers:**
- Tier 1 (Improved): +$2,000 (25% armor, improved optics)
- Tier 2 (Advanced): +$5,000 (50% armor, APS, enhanced weapon)
- Tier 3 (Elite): +$10,000 (75% armor, advanced APS, best weapon, thermals)

**Note:** Vehicle costs may increase based on demand (dynamic pricing) to prevent meta-spam of single vehicle types.

---

## 8. Player Progression System

### 8.1 Experience and Unlocks

**Experience Point (XP) System:**
- Players earn XP through gameplay actions
- XP unlocks weapons, vehicles, and equipment
- All unlocks are cosmetic or horizontal progression (no pay-to-win)

**XP Sources:**
- Kill: 100 XP
- Assist: 50 XP
- Capture Point: 200 XP
- Revive: 75 XP
- Repair Vehicle: 50 XP
- Squad Orders: 100 XP
- Victory: 500 XP

**Unlock Tiers:**

| Level | Total XP | Unlocks |
|---|---|---|
| 1 | 0 | Basic weapons & vehicles |
| 5 | 5,000 | Tier 2 weapons (scopes, DMRs) |
| 8 | 10,000 | Light armor vehicles |
| 10 | 15,000 | Tier 3 weapons (LMGs, launchers) |
| 12 | 20,000 | IFVs, attack helicopters |
| 15 | 30,000 | Tier 4 weapons (advanced optics) |
| 16 | 35,000 | Main battle tanks |
| 20 | 50,000 | Elite weapons & fighter aircraft |

### 8.2 Role Performance Unlocks

**Role Mastery System:**
Players unlock specialized equipment by performing role-specific actions:

**Medic Example:**
- 0 revives: Basic medkit
- 50 revives: Advanced medkit (faster healing)
- 100 revives: Defibrillator (revive from longer distances)
- 250 revives: Field surgery kit (revive with more HP)

**Anti-Tank Example:**
- 0 vehicle kills: RPG-7 (basic launcher)
- 10 vehicle kills: M136 AT4 (faster reload)
- 25 vehicle kills: Javelin (top-attack capability)
- 50 vehicle kills: TOW launcher (wire-guided)

**Note:** Full progression details in [Feedback and Improvements]({{ site.baseurl }}/docs/gameplay/feedback-responses-and-improvements)

### 8.3 Tutorial and Onboarding

**Progressive Tutorial System:**

**Stage 1: Basic Training (Required)**
- Movement, shooting, communication basics
- ~10 minutes
- Required before multiplayer access

**Stage 2-3: Role & Vehicle Training (Optional)**
- Role-specific tutorials (medic, engineer, SL, AT)
- Vehicle operation tutorials (driving, IFV, tank, helicopter)
- Each tutorial rewards +500-1000 XP
- 5-10 minutes each

**Context-Sensitive Help:**
- In-game tooltips for new mechanics
- Video demonstrations (<15 seconds) on hover
- "Don't show again" option for experienced players

**Mentor System:**
- New players (Level <5) marked with [NEW] tag
- Experienced players (Level 15+) can volunteer as mentors
- Mentors earn bonus XP for helping new players succeed
- Automatic squad matching for new players with mentors

**Note:** Full tutorial and learning systems detailed in [Feedback and Improvements]({{ site.baseurl }}/docs/gameplay/feedback-responses-and-improvements)

---

## 9. Input Mapping

### 9.1 Default Keybinds

**Movement:**
- W - Forward
- S - Backward
- A - Strafe Left
- D - Strafe Right
- Shift - Sprint
- C - Crouch/Stand
- X - Prone
- Space - Jump/Vault
- Alt - Walk (speed modifier)

**Combat:**
- LMB - Fire weapon
- RMB - Aim Down Sights
- R - Reload
- T - Toggle Weapon Light/Laser
- G - Throw Grenade
- V - Melee Attack
- B - Fire Mode (Auto/Semi/Burst)

**Interaction:**
- F - Use/Interact
- Q - Lean Left
- E - Lean Right
- Z - Deploy Bipod
- Hold F - Build Menu (Engineer only)

**Communication:**
- Caps Lock - Local Voice (50m radius)
- Left Alt - Squad Radio (unlimited range)
- Hold Tab - Scoreboard
- M - Tactical Map
- Insert - Squad Management

---

## 10. Performance Requirements

### 10.1 Network Optimization

**Replication Settings:**
- Infantry character update rate: 10 Hz (10 updates per second)
- Vehicle update rate: 15 Hz (higher for fast-moving objects)
- Minimum update frequency: 2 Hz (bandwidth conservation)

**Bandwidth Targets:**
- Per player: 8-12 KB/s
- 64-player server total: 768 KB/s maximum
- Packet rate: 30 packets per second
- Lag compensation: Up to 150ms client latency

### 10.2 CPU/GPU Targets

**Client Performance:**
- Target: 60 FPS @ 1080p
- Minimum: 45 FPS @ 1080p
- CPU: 8-core modern processor
- GPU: RTX 2060 / RX 5700 equivalent

**Server Performance:**
- Target: 30 tick rate (33ms)
- CPU: 16-core dedicated server
- RAM: 32GB minimum
- Network: 100 Mbps symmetrical

---

## 11. Future Expansion Notes

**Planned Mechanics (Post-MVP):**

These features are planned for implementation after the initial Capital Warfare mode launch:

- **Artillery Strike System:** Commander ability to call in artillery barrages on marked positions
  - Requires observer or recon unit for targeting
  - 60 second cooldown between strikes
  - High capital cost ($5,000 per strike)
  - Area of effect: 50m radius

- **UAV Reconnaissance:** Aerial spotting and intelligence gathering
  - Reveals enemy positions on tactical map for 30 seconds
  - 120 second flight time before return
  - Can be shot down by enemy anti-air
  - Squad Leader ability (requires upgraded FOB)

- **Electronic Warfare (EW):** Communications jamming capabilities
  - Blocks enemy radio communications in 200m radius
  - 120 second active duration
  - 10 minute cooldown
  - Requires specialized EW vehicle deployment

- **Weather System:** Dynamic environmental conditions affecting gameplay
  - **Rain:** Reduced visibility to 50m, slippery vehicle handling
  - **Fog:** Severely reduced visibility to 25m, muffled weapon sounds
  - **Snow:** 20% movement speed penalty, vehicle traction loss

- **Day/Night Cycle:** Time-based lighting and gameplay changes
  - Night operations require NVG (Night Vision Goggles)
  - Artificial lighting sources (flares, vehicle lights, building lights)
  - Stealth movement advantages during nighttime
  - Reduced detection ranges for enemy spotting

**Design Principles for Future Features:**
- Must maintain 60 FPS performance target
- Cannot exceed current network bandwidth (12 KB/s per player)
- Must integrate with existing Capital Warfare economy
- No pay-to-win mechanics
- All features must enhance tactical depth without adding complexity bloat

---

## Document Changelog

- **v1.0** (Nov 2025): Initial game design specification
- Focus on Capital Warfare mode mechanics
- Aligned with 12-month MVP roadmap
- Project Reality-style documentation format

