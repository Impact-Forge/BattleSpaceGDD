---
title: Game Overview
layout: default
---

# BattleSpace - Game Overview

**Genre:** Large-Scale Tactical First-Person Shooter  
**Platform:** PC (Steam)  
**Engine:** Unreal Engine 5  
**Target Audience:** 18-35, Core FPS players seeking tactical depth  
**Player Count:** 32v32 (64 players)  

---

## Core Vision

BattleSpace is a tactical FPS that combines realistic combined arms warfare with strategic resource management. Players engage in large-scale 32v32 battles where **monetary management is as critical as combat effectiveness**. 

The game emphasizes:
- **Squad-based coordination** over lone-wolf gameplay
- **Economic warfare** alongside kinetic combat
- **Territory control** with persistent consequences
- **Combined arms tactics** (infantry, vehicles, air support)
- **Realistic ballistics** with accessible controls

---

## Game Mode: Capital Warfare

### Overview

Capital Warfare is an economy-driven team vs team game mode where victory is achieved through either:
1. **Economic Victory:** Accumulate $1,000,000 in team capital
2. **Economic Defeat:** Bankrupt the enemy team (reduce to $0)

### Core Loop

**Capture Territory → Generate Income → Purchase Assets → Destroy Enemy Assets → Weaken Enemy Economy**

Players must balance offensive operations with resource preservation. Every death, destroyed vehicle, and lost capture point directly impacts team capital.

### Match Flow

**Phase 1: Early Game (0-15 minutes)**
- Teams spawn with $10,000 starting capital
- Capture initial territory for resource generation
- Light infantry engagements with basic equipment
- Establish forward operating bases (FOBs)

**Phase 2: Mid Game (15-45 minutes)**
- Economy scaling through territory control
- Vehicle warfare introduction (APCs, light armor)
- Infrastructure building (ammo caches, repair stations)
- Strategic asset denial (destroy enemy supply lines)

**Phase 3: Late Game (45+ minutes)**
- Heavy assets deployed (MBTs, attack helicopters)
- Full combined arms warfare
- High-stakes engagements (asset losses hurt economy)
- Victory conditions within reach for dominant team

---

## Core Gameplay Pillars

### 1. Combined Arms Warfare

**Infantry Combat:**
- Terminal ballistics simulation (bullet drop, penetration, ricochet)
- Locational damage system (head, torso, limbs)
- Squad-based tactics (6-player squads)
- Role specialization (medic, engineer, marksman, etc.)

**Vehicle Combat:**
- Ground vehicles: Jeeps, APCs, IFVs, MBTs
- Aerial support: Helicopters, close air support
- Component damage (tracks, engine, turret)
- Logistics vehicles (supply, repair, medical)

**Support Systems:**
- Commander abilities (UAV recon, artillery strikes)
- Engineer fortifications (sandbags, HESCOs, emplacements)
- Medical system (bandage, revive, heal)
- Supply chain (ammunition, fuel, repairs)

### 2. Strategic Economy

**Income Sources:**
- Territory control: $50/minute per sector
- Enemy kills: $25 per elimination
- Vehicle destruction: $50-$500 (based on value)
- Objective completion: $100-$500

**Expenditures:**
- Equipment upgrades: $100-$500
- Vehicle spawns: $500-$25,000
- Infrastructure: $50-$500 per structure
- Respawn costs: $25 per death

**Economic Strategy:**
- Aggressive expansion generates income but risks losses
- Defensive play preserves assets but limits growth
- Asset denial prevents enemy economy growth
- Risk vs. reward in every engagement

### 3. Territory Control

**Capture Mechanics:**
- 9 capture zones per map (3x3 grid)
- 50m capture radius per zone
- 1% capture progress per second per player (max 5 players)
- Contested zones halt all progress
- Neutralization required before enemy capture

**Territory Benefits:**
- Passive income generation
- Spawn point access (rally points, FOBs)
- Infrastructure building zones
- Strategic map control

**Dynamic Frontlines:**
- Territory changes create shifting battle lines
- Supply lines can be cut off
- Rear areas vulnerable to flanking
- Map control provides tactical advantage

---

## Player Roles

BattleSpace features **6 core infantry roles**, each with distinct responsibilities and equipment:

### Squad Leader
- **Responsibilities:** Command 6-player squad, place rally points, coordinate with commander
- **Equipment:** Assault rifle, smoke grenades, binoculars, radio
- **Abilities:** Deploy rally point (mobile spawn), mark objectives, request support
- **Playstyle:** Tactical leadership, positioning, communication

### Rifleman
- **Responsibilities:** Standard infantry, versatile combatant, backbone of squad
- **Equipment:** Assault rifle, frag grenades, extra ammunition
- **Abilities:** No special abilities (fundamental role)
- **Playstyle:** Frontline combat, objective assault, area denial

### Medic
- **Responsibilities:** Heal wounded, revive incapacitated, maintain squad effectiveness
- **Equipment:** Carbine, medical supplies (bandages, epinephrine, morphine), smoke grenades
- **Abilities:** Heal teammates, revive incapacitated players, deploy MASH tent
- **Playstyle:** Support, backline positioning, triage priorities

### Automatic Rifleman
- **Responsibilities:** Suppressive fire, area denial, covering fire for squad
- **Equipment:** Light machine gun, bipod, reduced ammunition capacity
- **Abilities:** Sustained suppressive fire, bipod deployment for accuracy
- **Playstyle:** Support by fire, defensive positions, suppression

### Breacher
- **Responsibilities:** Close-quarters combat, building clearing, explosive breaching
- **Equipment:** Shotgun/SMG, breaching charges, flashbangs
- **Abilities:** Explosive breaching, CQB specialist
- **Playstyle:** Urban warfare, building clearance, point man

### Marksman
- **Responsibilities:** Long-range precision fire, reconnaissance, target elimination
- **Equipment:** Designated marksman rifle, rangefinder, limited ammunition
- **Abilities:** Long-range engagement (300-600m), reconnaissance spotting
- **Playstyle:** Overwatch, flanking positions, high-value target elimination

---

## Setting & Theaters

### Primary Theater: Ukraine

**Odessa Oblast** (Launch Map)
- Coastal terrain with mixed urban/rural zones
- 4km² playable area divided into 9 sectors
- Strategic port facilities, industrial zones, residential areas
- Varied engagement ranges (CQB to 600m)

**Future Ukrainian Theaters:**
- Crimean Oblast (naval/amphibious operations)
- Kyiv Oblast (urban warfare)
- Donetsk Oblast (industrial combat)
- Kharkiv Oblast (multi-axis operations)

### Post-Launch Theaters

**Maritime Operations:**
- Barents Sea (arctic warfare, naval assets)
- South China Sea (carrier operations, island warfare)
- Falkland Islands (amphibious assault, remote logistics)

**Additional Theaters:**
- Alaska (cold weather operations, extended supply lines)
- Poland (NATO operations, multi-national forces)
- Taiwan (island defense, urban combat)
- Kashmir (mountain warfare, high altitude)

---

## Technical Features

### Graphics & Performance

**Unreal Engine 5 Features:**
- Nanite virtualized geometry (high-detail environments)
- Lumen global illumination (dynamic lighting)
- World Partition streaming (large open worlds)
- Chaos physics & destruction (realistic damage)

**Performance Targets:**
- 60 FPS @ 1080p (minimum spec)
- 100+ FPS @ 1440p (recommended spec)
- 30 tick rate servers (33ms tick)
- <80ms average latency

### Networking

**Server Architecture:**
- Dedicated servers (no peer-to-peer)
- 64-player capacity (32v32)
- Client-side prediction & server reconciliation
- Lag compensation for hit detection
- Anti-cheat integration (Easy Anti-Cheat)

**Replication Optimization:**
- 10 Hz character updates (infantry)
- 15 Hz vehicle updates (fast-moving objects)
- 8-12 KB/s bandwidth per player
- Dynamic LOD based on distance

### Audio

**3D Positional Audio:**
- Realistic weapon sounds (suppression, distance falloff)
- Environmental audio (wind, vehicle engines, explosions)
- VOIP integration (local and squad radio)
- Proximity-based enemy detection (footsteps, voice)

---

## Progression & Monetization

### Progression System

**Player Statistics Tracking:**
- Kill/Death/Assist ratios
- Accuracy metrics (overall, headshot percentage)
- Role-specific stats (revives, repairs, captures)
- Win/loss records per game mode
- Capital earned/spent tracking

**Stat-Based Rewards:**
- Cosmetic unlocks tied to milestones
- Profile customization (banners, badges)
- Leaderboards (global, friends, regional)
- Seasonal rewards

### Monetization Strategy

**Base Game:** $19.99 (Steam Early Access)

**Revenue Streams:**
- **Cosmetic DLC:** Weapon skins, character customization, vehicle camos
- **Battle Pass:** Seasonal content with free and premium tiers
- **Premium Features:** Advanced stat tracking, extended match history
- **Future Expansions:** New theaters, factions, vehicles (post-launch)

**No Pay-to-Win:**
- All gameplay-affecting content free
- Cosmetics only monetization
- No loot boxes or gambling mechanics
- Transparent pricing

---

## Development Roadmap

### Phase 1: MVP Launch (Month 12)
- Single map (Odessa Oblast)
- 6 core roles
- Capital Warfare mode
- Basic vehicles (jeeps, APCs)
- Essential infrastructure

### Phase 2: Content Expansion (Months 13-18)
- Second map
- Additional weapons (2 per role)
- Light vehicle combat
- Enhanced commander abilities

### Phase 3: Combined Arms (Months 19-24)
- Heavy vehicles (MBTs)
- Attack helicopters
- Advanced fortifications
- Additional theaters

---

## Competitive & Community

### Competitive Features

**Ranked Mode (Post-Launch):**
- Skill-based matchmaking (ELO system)
- Seasonal rankings with rewards
- Competitive rulesets (standardized economy)
- Leaderboards and tournaments

**Clan System:**
- Clan creation and management
- Clan vs. clan matches
- Clan statistics tracking
- Private servers for scrimmages

### Community Tools

**Server Browser:**
- Custom server hosting
- Community-run servers
- Modifiable rules (economy multipliers, ticket counts)
- Private password-protected matches

**Replay System (Post-Launch):**
- Match recording and playback
- Free camera spectator mode
- Statistics analysis
- Highlight clip creation

---

## Why BattleSpace?

### Unique Selling Points

**1. Economic Warfare Layer**
- No other tactical FPS ties economy directly to victory conditions
- Every tactical decision has strategic consequences
- High-stakes engagements with meaningful resource costs

**2. Grid-Based Territory System**
- Persistent territory control between engagements
- Dynamic frontlines that shift based on performance
- Strategic depth beyond simple kill/death gameplay

**3. Terminal Ballistics**
- Realistic bullet physics (drop, penetration, fragmentation)
- Differentiates from arcade shooters
- Rewards skill and tactical positioning

**4. Combined Arms at Scale**
- 32v32 player count allows true combined arms
- Infantry, vehicles, air support working together
- Squad coordination and teamwork essential

**5. Accessible Mil-Sim**
- Tactical depth without excessive simulation complexity
- Quick-to-learn, difficult-to-master
- Engaging for casual and hardcore players

---

## Target Audience

**Primary Audience:**
- Age: 18-35
- FPS enthusiasts seeking tactical depth
- Fans of: Squad, Hell Let Loose, Battlefield (hardcore modes)
- PC gamers with mid-to-high-end systems

**Secondary Audience:**
- Mil-sim community (Project Reality, ARMA)
- Strategy gamers interested in FPS/RTS hybrid gameplay
- Competitive FPS players looking for team-based play

**Community Focus:**
- Discord integration for voice and community
- Active developer communication
- Community feedback incorporation
- Modding support (post-launch)

---

## Vision Statement

*"BattleSpace delivers the tactical depth of a military simulator with the accessibility and polish of a modern FPS. Every bullet, every vehicle, and every decision matters in a persistent conflict where economic and military victory are intertwined. This is warfare where your squad's coordination, your team's strategy, and your individual skill determine who controls the battlespace."*

---

## Document Information

**Version:** 2.0  
**Last Updated:** November 2025  
**Status:** MVP Development (12-month roadmap)  
**Target Launch:** Q4 2025 (Steam Early Access)

---

For detailed gameplay mechanics, see [Core Mechanics]({{ site.baseurl }}/docs/gameplay/mechanics).  
For development timeline, see [Lean GDD]({{ site.baseurl }}/docs/battlespace-lean-gdd).  
For marketing strategy, see [Marketing Plan]({{ site.baseurl }}/docs/battlespace-marketing-strategy).

