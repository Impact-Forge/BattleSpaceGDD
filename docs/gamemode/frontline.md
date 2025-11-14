# Frontline

**Game Mode Type:** Pre-Battle Construction with Territory Control  
**Player Count:** 32v32 (64 players)  
**Match Duration:** 60-90 minutes (5-min setup + 55-85 min combat)  
**Difficulty:** Advanced - Requires strategic planning and construction coordination

---

## Overview

Frontline revolutionizes territorial warfare by letting teams design the battlefield itself before combat begins. In a 5-minute setup phase, both teams simultaneously construct their defensive networks, define strategic road systems extending into enemy territory, and place three critical objectives that will determine victory. Once construction completes, teams battle for control of the infrastructure they've collaboratively created, where every road, settlement, and objective placement reflects pre-battle strategic decisions.

Inspired by Source Forts' construction mechanics, Frontline emphasizes strategic foresight over reactive tactics. Teams must balance defensive depth with offensive positioning, infrastructure connectivity with resource efficiency, and fortification strength with construction speed. The battlefield becomes a living testament to both teams' strategic philosophies, creating unique match experiences every time.

---

## Construction Phase

### Setup Period (5 Minutes)

**Simultaneous Construction:**
- Both teams construct independently
- Cannot see enemy construction progress
- Fog of war during setup phase
- Must complete minimum requirements before combat begins

**Construction Teams:**
- All players participate in construction
- No combat during setup phase
- Commander coordinates team efforts
- Squad Leaders manage sector construction

**Failure Conditions:**
- If minimum requirements not met by 5-minute mark:
  - **Auto-generate missing elements** (suboptimal placement)
  - **30-second penalty** added to setup timer
  - Team that fails loses strategic initiative

### Map Structure

**Blank Canvas:**
- Starting State: **Empty neutral territory**
- Map Size: **4km x 4km**
- Team Spawn Zones: **Fixed** (opposite ends of map)
- Separation Distance: **3km** between main bases
- Construction Zone: **80%** of map (neutral space)

**Territorial Divisions:**
- **Friendly Zone:** 15% (own side, fully controlled)
- **Neutral Zone:** 70% (contested space)
- **Enemy Zone:** 15% (enemy side, highly risky)

---

## Construction Requirements

### Road Network (Mandatory)

**Primary Roads (Team Must Build 3):**
- Definition: Major supply routes extending from main base toward enemy
- Purpose: Vehicle movement, supply logistics, objective connections
- Width: **8 meters** (two-lane traffic)
- Extension Requirement: **Must cross into enemy zone** (minimum 500m penetration)
- Interconnection: All 3 roads must **connect to each objective** (directly or via secondary roads)

**Construction Mechanics:**
- Placement: Commander/Squad Leaders mark road paths
- Engineers: Execute construction
- Build Rate: **10 meters/second** (all Engineers working)
- Cost: **Free** (primary strategic infrastructure)
- Vulnerability: Destructible post-combat (can be cratered/blocked)

**Road Types:**

**Primary Roads (Mandatory 3):**
- Width: **8 meters**
- Speed: **100% vehicle speed**
- Durability: **1,000 HP per 10-meter section**
- Purpose: Main offensive/defensive arteries

**Secondary Roads (Optional, Unlimited):**
- Width: **4 meters**
- Speed: **80% vehicle speed**
- Durability: **500 HP per 10-meter section**
- Purpose: Inter-objective connections, flanking routes
- Cost: **200 LP per 50 meters**

**Tactical Roads (Optional, Unlimited):**
- Width: **2 meters** (infantry only)
- Speed: **Infantry normal speed**
- Durability: **250 HP per 10-meter section**
- Purpose: Concealed infantry movement
- Cost: **100 LP per 50 meters**

**Road Placement Rules:**
- Cannot overlap with objectives
- Must maintain **15-meter spacing** from other roads (parallel)
- Cannot cross water bodies (bridges cost extra LP)
- Maximum grade: **15%** slope (avoid steep hills)

### Objectives (Mandatory 3)

**Critical Capture Points:**
- Count: **Exactly 3 per team** (6 total on map)
- Purpose: Victory condition targets, spawn points
- Placement: Team decision within constraints
- Type: Varies by strategic intent

**Objective Placement Constraints:**

**Minimum Distance from Own Base:**
- **500 meters** (prevents defensive clustering)
- Forces projection into neutral/enemy territory

**Maximum Distance from Own Base:**
- **2,000 meters** (prevents unreachable placements)
- Ensures objectives are contestable

**Inter-Objective Spacing:**
- **300 meters minimum** between own team objectives
- **200 meters minimum** between own and enemy objectives
- Prevents objective clustering

**Road Connection Requirement:**
- Each objective **must connect to at least 1 primary road**
- Connection via secondary roads acceptable
- Maximum **100 meters** from nearest road

**Objective Types (Team Chooses):**

**Type A: Town Center**
- Structure: Multi-building urban complex
- Capture Radius: **50 meters**
- Capture Time: **3 minutes** uncontested
- Spawn Function: Yes (after capture)
- Resource Generation: **+150 LP/minute**
- Fortification: Medium (pre-built walls, some cover)

**Type B: Military Outpost**
- Structure: Fortified compound with guard towers
- Capture Radius: **40 meters**
- Capture Time: **4 minutes** uncontested
- Spawn Function: Yes (after capture)
- Resource Generation: **+100 LP/minute**
- Fortification: High (reinforced walls, elevated positions)

**Type C: Supply Depot**
- Structure: Warehouse complex with vehicle access
- Capture Radius: **60 meters**
- Capture Time: **2 minutes** uncontested
- Spawn Function: No (resupply only)
- Resource Generation: **+200 LP/minute**
- Fortification: Low (minimal walls, open layout)

### Settlements (Optional)

**Additional Structures:**
- Definition: Smaller buildings/fortifications near objectives
- Purpose: Provide cover, defensive positions, spawn points
- Placement: **Within 200 meters** of objectives
- Cost: **500-2,000 LP** depending on structure type
- Build Time: **30-120 seconds**

**Settlement Types:**

**Small Garrison:**
- Cost: **500 LP**
- Build Time: **30 seconds**
- Features: Single building, basic cover
- Spawn: Squad spawn point only
- Resource: None

**Fortified Checkpoint:**
- Cost: **1,000 LP**
- Build Time: **60 seconds**
- Features: Walls, gate, 2 buildings
- Spawn: Squad spawn point
- Resource: **+25 LP/minute**

**Forward Base:**
- Cost: **2,000 LP**
- Build Time: **120 seconds**
- Features: Multiple buildings, walls, towers
- Spawn: Team spawn point (after main objective)
- Resource: **+50 LP/minute**

**Placement Rules:**
- Maximum **2 settlements per objective**
- Cannot block road movement
- Must maintain **50-meter spacing** from each other

---

## Combat Phase

### Match Start

**Fog of War Lifted:**
- Both teams see complete battlefield layout
- All roads, objectives, settlements revealed
- 30-second observation period before combat begins
- Teams assess enemy strategic decisions

**Strategic Evaluation:**
- Enemy road positions
- Objective placement patterns
- Settlement fortifications
- Adjust tactics based on enemy layout

### Victory Conditions

**Primary: Objective Control**
- Control **4 of 6 total objectives** for **5 continuous minutes**
- Captures own 3 + 1 enemy objective = Victory
- Most common victory condition

**Secondary: Objective Domination**
- Control **all 6 objectives** simultaneously for **60 seconds**
- Instant victory
- Rare but decisive

**Tertiary: Time Limit**
- 90-minute timer expires
- Team controlling **more objectives** wins
- Tiebreaker: Higher total LP reserves

### Objective Capture Mechanics

**Standard Capture:**
- Presence-based: 2+ players in radius
- Contested: Opposing players halt capture
- Progressive: Capture progress saved if interrupted
- Visual: Flag/indicator shows control status

**Capture Benefits:**
- Spawn Point: Team can respawn at captured objective
- Resource Generation: Continuous LP income
- Strategic Position: Territorial advantage
- Defensive Fortification: Pre-built infrastructure

**Recapture:**
- Enemy can recapture owned objectives
- Same capture time as initial capture
- Losing objective stops resource generation
- Respawn disabled at lost objectives

---

## Strategic Construction Patterns

### Aggressive Forward Deployment

**Road Layout:**
- 3 primary roads extend **deep into enemy territory** (1.5km+)
- Straight, direct routes for rapid advance
- Minimal secondary roads

**Objective Placement:**
- All 3 objectives placed **1,200-1,500m** from own base
- Forward positioning near enemy roads
- Type: 2x Military Outpost, 1x Supply Depot

**Settlements:**
- Limited to 1-2 Forward Bases
- Positioned between objectives for mutual support

**Strategy:**
- Early aggression, rapid territorial expansion
- Risk: Overextension, difficult to defend all objectives
- Reward: Pressure enemy from match start

### Defensive Depth Strategy

**Road Layout:**
- 3 primary roads with **extensive secondary connections**
- Complex road network with multiple routes
- Roads curve, create multiple approach vectors

**Objective Placement:**
- All 3 objectives placed **600-900m** from own base
- Clustered positioning (within connection rules)
- Type: 3x Town Center or 2x Town + 1x Military Outpost

**Settlements:**
- 4-6 Fortified Checkpoints between objectives
- Layered defensive positions
- Overlapping fields of fire

**Strategy:**
- Consolidated defense, difficult for enemy to penetrate
- Risk: Surrender early territorial control
- Reward: Strong defensive positions, easier to hold

### Hybrid Projection Strategy

**Road Layout:**
- 2 primary roads extend forward (offensive)
- 1 primary road defensive (fallback route)
- Secondary roads connect all objectives

**Objective Placement:**
- 2 objectives forward (**1,000-1,200m**)
- 1 objective defensive (**700m**)
- Mixed types: 1x Military Outpost, 1x Town, 1x Supply Depot

**Settlements:**
- 2 Forward Bases (at forward objectives)
- 2 Fortified Checkpoints (defensive objective)

**Strategy:**
- Balanced approach, options for offense and defense
- Risk: Jack of all trades, master of none
- Reward: Adaptable to enemy strategy

---

## Road Warfare Tactics

### Road Control

**Importance:**
- Vehicle Speed: **+100%** on roads vs. off-road
- Supply Lines: LP generation routes
- Predictable Movement: Ambush opportunities

**Offensive Road Use:**
- Rapid vehicle deployment to objectives
- Armored columns via primary roads
- Infantry support via tactical roads

**Defensive Road Denial:**
- Crater roads (explosives create 10m gaps)
- Ambush positions at choke points
- Roadblocks (deployable barriers)

### Road Interdiction

**Denial Tactics:**
- Engineers place explosives on enemy roads
- Destroy 10-meter sections (1,000 HP)
- Repair Time: **2 minutes** (enemy Engineers)
- Strategic: Disrupt enemy supply/reinforcement

**Counter-Interdiction:**
- Patrol road networks
- Engineers on standby for repairs
- Alternative routes via secondary roads

---

## Resource System

### Logistics Points (LP)

**Generation Sources:**

**Base Generation:**
- Main Base: **+100 LP/minute**
- Captured Objectives: **+100-200 LP/minute** (type dependent)
- Settlements: **+25-50 LP/minute** (type dependent)

**Construction Costs (Recap):**
- Secondary Roads: **200 LP per 50m**
- Tactical Roads: **100 LP per 50m**
- Settlements: **500-2,000 LP** (type dependent)
- Defensive Structures: **200-800 LP** (varies)

**Combat Costs:**
- Respawns: **50-200 LP** (escalating)
- Equipment: **40-500 LP** (varies)
- Vehicles: **400-5,000 LP** (type dependent)
- Commander Abilities: **300-1,000 LP** (varies)

---

## Team Roles

### Construction Phase Roles

**Commander:**
- Strategic vision: Road layout planning
- Objective type selection and placement
- Resource allocation for optional structures
- Coordinate team construction efforts

**Squad Leaders:**
- Sector construction management
- Road segment assignments
- Settlement placement
- Engineer coordination

**Engineers (Critical):**
- Execute all construction
- Minimum **8 Engineers** recommended
- Rotate between road and settlement construction
- Post-setup: Transition to repair/fortification

**Infantry:**
- Provide security during setup (minimal threat)
- Scout planned construction zones
- Assist with light construction tasks

### Combat Phase Roles

**Objective Assault Teams:**
- Capture enemy objectives
- Clear defensive positions
- Utilize road networks for rapid deployment

**Objective Defense Teams:**
- Hold captured objectives
- Repel enemy assaults
- Maintain spawn point availability

**Road Interdiction Teams:**
- Engineers + Infantry escort
- Destroy enemy road sections
- Plant ambushes at choke points

**Mobile Reaction Force:**
- Rapid response to enemy breakthroughs
- Reinforce threatened objectives
- Counter-attack enemy weak points

---

## Map Design Requirements

### Terrain Features

**Mostly Flat Construction Space:**
- **70%** of map suitable for road construction
- Flat areas for objective placement
- Minimal elevation changes (under 10m)

**Natural Obstacles (30%):**
- Rivers/lakes: Require bridge construction
- Hills: Limit direct road paths
- Forests: Provide cover but slow construction
- Rocky areas: Cannot build on, must route around

**Aesthetic Environment:**
- Neutral setting (grasslands, plains, light forests)
- Post-setup: Structures appear fully constructed
- Dynamic: Destruction alters battlefield appearance

---

## Advanced Tactics

### Deceptive Objective Placement

**Feint Objective:**
- Place 1 objective exposed and weakly defended
- Concentrate defenses on other 2 objectives
- Enemy wastes resources attacking "bait" objective
- Counter-attack while enemy overcommitted

### Road Network Traps

**Channelization:**
- Design road network to funnel enemy vehicles
- Ambush positions at convergence points
- Mines, AT positions covering predictable routes

### Settlement Surprise

**Hidden Forward Bases:**
- Place Forward Bases in unexpected locations
- Use terrain (forests, hills) to conceal
- Surprise spawn points behind enemy lines

### Adaptive Construction

**Mid-Match Building:**
- Use remaining LP to build new secondary roads
- Construct additional settlements as needed
- Adapt infrastructure to emerging tactical needs

---

## Developer Notes

### Design Pillars

1. **Strategic Foresight:** Pre-planning determines battlefield
2. **Creative Freedom:** Teams design own infrastructure
3. **Asymmetric Battlefields:** No two matches identical
4. **Infrastructure Warfare:** Roads and settlements have value
5. **Combined Arms:** Construction and combat skills both essential

### Balance Testing Focus

**Metrics:**
- Construction completion rates
- Objective capture frequency by placement pattern
- Road usage intensity
- Settlement survival duration
- Victory condition distribution

**Adjustment Vectors:**
- Construction time limits
- LP costs for optional structures
- Road durability values
- Objective spacing requirements
- Capture time balancing

---

## Future Expansion

### Advanced Construction

**Bridges:**
- Cross rivers/gaps
- Cost: **1,000 LP per bridge**
- Build Time: **90 seconds**
- Vulnerable: Can be destroyed, cuts route

**Tunnels:**
- Underground passages
- Cost: **2,000 LP per 50m**
- Build Time: **120 seconds**
- Advantage: Concealed movement, hard to interdict

**Defensive Lines:**
- Pre-built trench systems
- Cost: **1,500 LP per 100m**
- Build Time: **60 seconds**
- Benefit: Strong defensive positions

### Dynamic Weather

**Construction Phase Weather:**
- Rain: **+50% construction time** (muddy ground)
- Clear: Standard construction rates
- Fog: Limited visibility during planning

**Combat Phase Weather:**
- Affects vehicle speed on roads
- Alters visibility for ambushes
- Damage to roads from heavy weather

---

## Conclusion

Frontline transforms players from soldiers into battlefield architects, where strategic vision during the setup phase determines tactical options throughout the combat phase. Teams must think like military engineers, designing infrastructure networks that support their intended strategy while anticipating enemy plans.

The mode's emphasis on pre-battle planning creates a unique blend of creative construction and competitive combat. Every road placement, objective selection, and settlement location reflects strategic intent, rewarding thoughtful design while punishing hasty decisions. The battlefield becomes a physical manifestation of competing strategic philosophies.

**Frontline is architectural warfare:** build the battlefield, then dominate it.

---

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Status:** Post-MVP Expansion - Design Complete  
**Target Implementation:** Month 36+