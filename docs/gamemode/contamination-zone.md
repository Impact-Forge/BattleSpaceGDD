# Contamination Zone

**Game Mode Type:** Dynamic Territory Push with Environmental Hazard  
**Player Count:** 32v32 (64 players)  
**Match Duration:** 45-60 minutes (Best of 3/5 rounds)  
**Difficulty:** Advanced - Requires environmental awareness and coordinated pushes

---

## Overview

Contamination Zone transforms traditional territory control into an asymmetric battle against both the enemy team and a spreading environmental hazard. A hostile Contamination Zone (CZ) constantly expands from the map's center, threatening to engulf both teams. Victory belongs to the team that successfully pushes the CZ into enemy territory while preventing it from consuming their own base.

Unlike static objective modes, the CZ's dynamic nature creates constantly shifting tactical priorities. Teams must capture and hold Containment Nodes to push the zone away while simultaneously preventing enemy captures that would reverse the CZ's direction. The zone itself acts as a third force, punishing teams that lose control and rewarding those who maintain containment infrastructure.

---

## The Contamination Zone

### Environmental Hazard

**Visual Characteristics:**
- Appearance: Green gaseous fog, corrosive mist, or dark energy field
- Visibility: Clearly defined boundary with particle effects
- Audio: Low ominous hum, distorted sounds within
- Starting Position: **Map center**, equidistant from both main bases
- Starting Size: **200-meter radius circle**

**Movement Behavior:**

**Neutral Expansion:**
- No team interference: **+5 meters/minute** in all directions
- Symmetrical growth pattern
- Will eventually consume entire map if unchecked

**Team Influence:**
- Each captured Containment Node: **-8 meters/minute** push
- Direction: Away from capturing team, toward enemy
- Multiple nodes: Effects stack additively
- Net direction determined by node control differential

### Player Effects Within CZ

**Health Degradation:**
- Base Damage: **10 HP/second** continuous
- Depth Scaling: **+2 HP/second per 10 meters** deeper
- Example: 30 meters deep = 16 HP/second damage
- No natural regeneration while inside CZ

**Environmental Debuffs:**

**Visual Impairment:**
- Visibility range reduced to **30 meters**
- Blurred vision effect (cannot use long-range optics)
- HUD interference (minimap flickers, compass unreliable)

**Audio Disruption:**
- All sounds muffled (footsteps, gunfire less audible)
- Directional audio distorted
- Voice comms crackling/static (still functional)

**Physical Debuffs:**
- Stamina regeneration: **-75% rate**
- Sprint speed: **-20%**
- Weapon accuracy: **+15% recoil** (from coughing/shaking)

**Survival Time:**
- Standard player: **60-90 seconds** maximum
- With Medical Kit buff: **90-120 seconds**
- Debuff resistance upgrade: **120-180 seconds**

**Death Within CZ:**
- Normal death rules apply
- Respawn at main base or forward spawn
- No "trapped forever" scenarios

---

## Strategic Objectives

### Containment Nodes (CN)

**Primary Objectives:**
- Count: **12-16 per map** (arranged in grid/line pattern)
- Location: Distributed across neutral territory between bases
- Purpose: Push CZ away from capturing team

**Capture Mechanics:**
- Capture Time: **90 seconds** uncontested
- Capture Radius: **25 meters**
- Minimum Capture Force: **2 players**
- Capture Progress: Saved (50% progress retained if interrupted)

**Containment Effects:**

**CZ Push Force:**
- Each captured CN: **-8 meters/minute** CZ recession
- Direction: Perpendicular away from node toward enemy
- Stacking: 3 nodes = **-24 meters/minute** total push
- Net Effect: Calculated as (Team A nodes - Team B nodes) × 8 meters/min

**Safe Zone Generation:**
- Radius: **15-meter sphere** around CN
- Effect: **-50% health drain** while inside
- Does NOT eliminate damage, only reduces
- Provides brief respite for pushes through CZ

**Node States:**
- **Neutral:** Uncaptured, CZ unaffected
- **Team A Controlled:** Pushing CZ toward Team B
- **Team B Controlled:** Pushing CZ toward Team A
- **Contested:** Both teams present, no CZ effect
- **Overrun:** CZ consumed node (becomes unusable until CZ recedes)

**Vulnerability:**
- Can be recaptured by enemy team
- Standard capture time applies
- Immediately reverses CZ push direction
- Critical to defend captured nodes

### Purification Devices (PD)

**High-Value Landmarks:**
- Count: **1 per team** (2 total)
- Location: **300-500 meters** behind frontline (each team's territory)
- Purpose: Massive CZ pushback when captured

**Capture Mechanics:**
- Capture Time: **5 minutes** uncontested
- Capture Radius: **40 meters**
- Minimum Capture Force: **6 players**
- Heavily Defended: Deep in enemy lines
- No capture progress saving (resets if interrupted)

**Purification Pulse Effects:**

**Massive CZ Pushback:**
- Duration: **60 seconds**
- Push Force: **-100 meters/minute** (multiplicative with CNs)
- Direction: Toward enemy owning the captured PD
- Visual: Bright energy wave effect from PD

**Enemy Debuff:**
- Enemy CN push effects: **Disabled for 60 seconds**
- Enemy respawn timers: **+10 seconds**
- Enemy equipment costs: **+50% CC increase**

**Strategic Value:**
- Game-changing momentum shift
- Requires deep coordinated assault
- High risk, extremely high reward
- Can reverse losing situations

**Defense Priority:**
- Teams should allocate dedicated defenders
- Losing PD often leads to round loss
- Recapture time: **3 minutes** (by original owner)

---

## Resource System

### Containment Credits (CC)

**Primary Currency:**
- Funds respawns and equipment
- Shared team pool
- Similar function to previous mode LP

**CC Generation:**

**Passive Income:**
- Base Rate: **+100 CC/second** (regardless of situation)
- Ensures teams never completely broke

**Containment Node Income:**
- Per Captured CN: **+50 CC/second**
- Stacks: 5 nodes = **+250 CC/second**
- Lost when node recaptured

**CZ Containment Bonus:**
- Formula: Distance CZ center is from map center toward enemy
- Every **10 meters**: **+20 CC/second** bonus
- Maximum: **+300 CC/second** (CZ pushed 150m into enemy side)
- Penalty: If CZ pushed toward your side, **-20 CC/second per 10m**

**Example Calculation:**
```
Base: +100 CC/sec
5 CNs: +250 CC/sec
CZ 80m into enemy side: +160 CC/sec
Total: +510 CC/sec
```

### CC Expenditure

**Respawn Costs:**
- First respawn: **100 CC**
- Second respawn: **150 CC**
- Third respawn: **200 CC**
- Fourth+ respawn: **250 CC**
- Resets each round

**Equipment & Abilities:**
- Frag Grenade: **80 CC**
- Smoke Grenade: **60 CC**
- Medical Kit: **100 CC**
- Decontamination Kit: **200 CC** (limited duration CZ immunity)
- Deployable Cover: **150 CC**

**Team Buffs:**
- Temporary CZ Resistance: **500 CC** (team-wide, 2 minutes, -50% damage)
- Emergency Respawn Wave: **1,000 CC** (all dead players respawn immediately)

**Infrastructure:**
- Reinforce CN: **800 CC** (double capture time for enemy, 5 minutes)
- Deploy Forward Spawn: **1,200 CC** (90-second duration spawn beacon)

---

## Victory Conditions

### Primary: Zone Encroachment

**Enemy Base Engulfment:**
- CZ boundary reaches enemy "Core Objective" (structure at base)
- Core Objective must be **80%+ inside CZ** for **30 seconds**
- Represents catastrophic contamination of enemy base
- Instant round victory for opposite team
- Most common victory condition

**Visual Indicator:**
- Core Objective health bar (represents contamination level)
- 0 HP = Fully contaminated = Round loss
- Core Objective takes **50 damage/second** when inside CZ

### Secondary: Containment Goal

**Time Limit Evaluation:**
- If **20-minute round timer** expires without Zone Encroachment
- Measure: **CZ center position relative to map center**
- Victory: Team whose side has CZ pushed furthest into enemy territory
- Measurement: Distance in meters from map center

**Example:**
- Map Center: 0 meters
- Team A Base: -1,500 meters
- Team B Base: +1,500 meters
- CZ Center at round end: -400 meters (pushed toward Team A)
- **Team B Wins** (successfully pushed CZ into Team A territory)

### Tertiary: Bankruptcy

**CC Depletion:**
- Team reaches **0 CC** and cannot respawn
- Less central than previous modes
- Rare due to passive CC generation
- Requires catastrophic mismanagement

---

## Match Structure

### Round Format

**Best of 3 or Best of 5:**
- Each round: **15-20 minutes**
- Teams switch sides after each round
- CZ resets to center each round
- First team to win majority wins match

### Round Phases

**Opening Phase (0-5 minutes):**
- Initial Containment Node captures
- CZ still small, minimal threat
- Teams establish CN control patterns
- First CZ push effects begin showing

**Mid Phase (5-12 minutes):**
- CZ significantly expanded
- CN captures near CZ boundary become hazardous
- First team likely achieving net CZ push
- PD capture attempts may begin

**Late Phase (12-20 minutes):**
- CZ potentially approaching one team's base
- Desperate CN recapture attempts
- Possible PD capture for comeback
- Victory condition imminent

**Critical Phase (Core Objective Threatened):**
- CZ at one team's base
- Core Objective taking contamination damage
- 30-second countdown to defeat
- All-hands defense required

---

## Team Roles & Strategy

### Frontline Roles

**CN Capture Teams:**
- Offensive squads capturing neutral/enemy CNs
- Coordinate to flip multiple nodes simultaneously
- Accept CZ exposure risk for strategic gains
- Recommended: **3-4 squads** (18-24 players)

**CN Defense Teams:**
- Hold captured CNs against enemy recapture
- Establish defensive positions around nodes
- Call for reinforcements when under attack
- Recommended: **2-3 squads** (12-18 players)

### Special Roles

**CZ Penetration Specialists:**
- Equipped with Decontamination Kits
- Conduct deep raids through CZ
- Capture nodes beyond CZ boundary
- High-risk, high-reward tactics
- Recommended: **1-2 squads** (6-12 players)

**PD Assault Team:**
- Dedicated to capturing enemy Purification Device
- Heavy firepower, sustained assault capability
- Coordinate timing for maximum impact
- Recommended: **2 squads** (12 players) for assault

**PD Defense Force:**
- Guard own Purification Device
- Repel enemy assaults
- Critical to prevent momentum shifts
- Recommended: **1 squad** (6 players) minimum

---

## Tactical Considerations

### CZ Push Strategy

**Aggressive Expansion:**
- Capture maximum CNs early
- Establish strong net CZ push
- Risk: Overextension, hard to defend all nodes
- Reward: Rapid CZ advancement toward enemy

**Defensive Consolidation:**
- Capture fewer CNs, heavily defend them
- Maintain consistent modest CZ push
- Risk: Slower progress toward victory
- Reward: Secure position, hard to reverse

**CZ Penetration:**
- Send specialists through CZ to capture deep nodes
- Flank enemy defensive positions
- Risk: High casualty rate from CZ damage
- Reward: Capture undefended nodes behind enemy lines

### Common Mistakes

**Ignoring CZ Threat:**
- Focusing on combat, neglecting CN captures
- Allowing CZ to expand freely
- Waking up to threat too late

**CN Overextension:**
- Capturing too many nodes to defend effectively
- Enemy recaptures nodes behind lines
- Net CZ push reverses unexpectedly

**PD Neglect:**
- Leaving PD undefended
- Enemy capture causes massive CZ reversal
- Round lost despite previous advantage

**Poor Resource Management:**
- Excessive equipment spending
- Unable to afford respawns during critical moments
- Economic collapse despite tactical success

---

## Advanced Tactics

### Synchronized Node Flips

**Coordinated Captures:**
- Multiple squads capture different CNs simultaneously
- Sudden large shift in CZ push direction
- Enemy cannot respond to all at once
- Requires excellent timing and communication

### PD Timing Attacks

**Strategic Pulse Deployment:**
- Capture enemy PD when CZ is already pushed into their territory
- Compounds CZ pressure, accelerates victory
- Requires scouting enemy PD defense strength

### Decontamination Kit Rotations

**Sustained CZ Operations:**
- Squads take turns pushing through CZ
- Fresh squads with Decon Kits replace depleted squads
- Maintains constant pressure via CZ flanking
- Expensive but effective

### Feint Assaults

**Decoy PD Attacks:**
- Stage false assault on enemy PD
- Draw defenders away from CNs
- Main force captures multiple CNs during diversion
- High-level coordination required

---

## Map Design Requirements

### Spatial Layout

**Map Size:**
- **3km x 3km** to **4km x 4km**
- Main bases **2-2.5km apart**
- CZ starts at exact center

**Containment Node Distribution:**
- **12-16 CNs** arranged in grid or line pattern
- Roughly equal distance from both bases
- Some CNs intentionally in more exposed positions (risk/reward)

**Purification Device Placement:**
- **300-500 meters** from main base (deep in team territory)
- Defensible position (elevated, choke points)
- Requires coordinated assault to reach

**CZ Flow Lanes:**
- Clear "lanes" or "sections" for CZ expansion
- Natural funnels or corridors
- Environmental hazards within future CZ path (broken infrastructure)

### Example Map: "Dead Zone"

**Setting:** Abandoned industrial complex
**Containment Nodes:** 14 total
- Arranged in 3 parallel lanes
- Central lane: 6 CNs (high-traffic, contested)
- North lane: 4 CNs (vehicle-friendly, open)
- South lane: 4 CNs (infantry-focused, urban)

**Purification Devices:**
- Team A: Old power plant (elevated, fortified)
- Team B: Water treatment facility (multiple entry points)

**CZ Starting Position:**
- Central factory complex
- Expands along industrial roads
- Environmental storytelling: Hazmat equipment, warning signs

---

## Environmental Design

### CZ Visual Effects

**Tier 1 (Outer Edge):**
- Light green fog
- **-50%** visibility reduction
- Minimal audio distortion
- Health drain: **10 HP/second**

**Tier 2 (Mid-Zone):**
- Dense green/yellow fog
- **-75%** visibility reduction
- Moderate audio distortion
- Health drain: **15 HP/second**

**Tier 3 (Deep Zone):**
- Thick corrosive mist, electrical surges
- **-90%** visibility reduction
- Heavy audio distortion
- Health drain: **20 HP/second**
- Weapon malfunction chance: **5% per shot**

**Core (CZ Center):**
- Nearly opaque, dark energy
- **-95%** visibility reduction
- Severe audio distortion
- Health drain: **30 HP/second**
- Lethal within seconds, avoid at all costs

### Audio Design

**Ambient Sounds:**
- Low ominous hum (increases with depth)
- Chemical hissing, electrical crackling
- Distorted echoes of distant gunfire

**Player Audio:**
- Coughing, labored breathing
- Muffled footsteps
- Radio static on comms

**Warning Indicators:**
- Geiger counter-style clicking (increases near CZ)
- HUD warning: "CONTAMINATION ZONE - XX METERS"
- Directional audio cue for CZ boundary

---

## Comeback Mechanics

### CZ Reversal Opportunity

**When Core Objective >50% Contaminated:**
- Trailing team respawn costs: **-30%**
- CN capture time: **-20 seconds** (70 seconds instead of 90)
- Decontamination Kit cost: **-50%** (100 CC instead of 200)
- Purpose: Give defending team chance to mount desperate defense

**Emergency Measures:**
- Free CC income boost: **+100 CC/second** for 2 minutes
- One-time free team CZ resistance buff (automatic, no cost)
- Extended PD capture grace period (enemy needs 7 minutes instead of 5)

---

## Developer Notes

### Design Pillars

1. **Environmental Pressure:** Third force creates urgency
2. **Dynamic Territory:** Constantly shifting battlefield
3. **Risk/Reward:** CZ penetration tactics vs. safety
4. **Asymmetric Combat:** Offense and defense against zone
5. **Momentum Swings:** PD captures enable comebacks

### Balance Testing Focus

**Metrics:**
- CZ expansion/recession rates
- Average CN control distribution
- Victory condition frequency (Encroachment vs. Containment)
- Player time spent in CZ
- Decontamination Kit usage rates
- PD capture success rates

**Adjustment Vectors:**
- CZ damage rates
- CN push force values
- PD pulse magnitude and duration
- Decontamination Kit duration/cost
- Core Objective contamination threshold

---

## Future Expansion

### Advanced Features

**Multi-Tiered CZ:**
- Different contamination types (chemical, radiation, biological)
- Each type requires different protection
- Varied visual effects and debuffs

**Mobile Purification Units:**
- Deployable vehicles that create temporary safe zones
- Can push into CZ to support operations
- Vulnerable to destruction

**CZ Mutations:**
- CZ behavior changes mid-round
- Sudden rapid expansion events
- Creates unpredictable tactical situations

**Civilian Rescue Objectives:**
- NPCs trapped in CZ-threatened areas
- Bonus CC for successful evacuations
- Adds PvE element to mode

---

## Spectator Features

### Tactical Overview

**Overhead Map View:**
- Real-time CZ boundary visualization
- Color-coded CN control (Team A blue, Team B red)
- CZ push vectors showing direction of expansion
- Core Objective contamination percentage

**Team Momentum Indicators:**
- Net CZ push rate (meters/minute)
- CN control count
- CC generation rates
- Critical moment alerts (PD captures, Core Objective threats)

---

## Conclusion

Contamination Zone reimagines territorial warfare by adding a hostile environmental force that punishes hesitation and rewards aggressive, coordinated play. The CZ's constant pressure ensures matches never stagnate, forcing teams to continuously adapt their strategies as the zone shifts.

Success requires balancing three competing priorities: capturing Containment Nodes to push the CZ, defending captured nodes from enemy recapture, and preventing catastrophic PD captures. Teams must manage both spatial control and resource economics while operating under the constant threat of environmental contamination.

**Contamination Zone is environmental warfare:** push the poison, or be consumed by it.

---

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Status:** Post-MVP Expansion - Design Complete  
**Target Implementation:** Month 24+