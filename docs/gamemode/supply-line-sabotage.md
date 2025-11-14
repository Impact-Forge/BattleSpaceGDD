# Supply Line Sabotage

**Game Mode Type:** Resource Control with Strategic Infrastructure  
**Player Count:** 32v32 (64 players)  
**Match Duration:** 45-60 minutes (Best of 3/5 rounds)  
**Difficulty:** Advanced - Requires strategic planning and resource management

---

## Overview

Supply Line Sabotage transforms territorial warfare into an economic battle focused on logistics networks rather than pure combat dominance. Teams compete to establish vital supply lines connecting resource nodes to their main base while simultaneously disrupting enemy logistics operations. Victory belongs to teams that balance offensive infrastructure expansion with defensive protection of their own supply networks.

Unlike traditional capture modes where holding territory is the end goal, Supply Line Sabotage makes territorial control a means to an end: maintaining the flow of Logistics Points (LP) through secure supply chains. Breaking enemy supply lines is as valuable as building your own, creating dynamic gameplay where raiders and defenders must coordinate across multiple fronts simultaneously.

---

## Core Resource System

### Logistics Points (LP)

**Primary Currency:**
- All team actions funded by shared LP pool
- Generated passively and through territorial control
- Depleted by respawns, equipment usage, and infrastructure investment
- Victory achieved by reaching LP threshold or line domination

**LP Visibility:**
- Team LP total displayed prominently in HUD
- LP generation rate shown (+XXX LP/second)
- Enemy LP total visible with **30-second delay** (prevents perfect counter-play)

### LP Generation (Income)

**Main Base (Uncapturable):**
- Location: Team starting spawn point
- Generation Rate: **+50 LP/second** (baseline, constant)
- Cannot be captured or destroyed by enemy
- Serves as supply line terminus point

**Resource Nodes (Capturable):**
- Count: **8-12 per map** (depending on map size)
- Generation Rate: **+100-200 LP/second** (varies by node type)
- Types:
  - Oil Wells: **+150 LP/second**
  - Mining Operations: **+120 LP/second**
  - Intel Outposts: **+180 LP/second**
  - Fuel Depots: **+200 LP/second**
- Capture Time: **2 minutes** uncontested
- Capture Radius: **30 meters**
- Minimum Capture Force: **2 players**

**Completed Supply Lines (Strategic Objective):**
- Generation Rate: **+500 LP/second per active line**
- Unlocks special abilities and team bonuses
- Requires full connection from Hub to Main Base
- Most valuable LP source in the game

### LP Expenditure (Costs)

**Respawn Costs:**
- First respawn: **50 LP**
- Second respawn: **100 LP**
- Third respawn: **150 LP**
- Fourth+ respawn: **200 LP**
- Resets each round

**Equipment Usage:**
- Frag Grenade: **75 LP**
- Smoke Grenade: **50 LP**
- Flashbang: **40 LP**
- Medical Kit (Medic): **100 LP**
- Deployable Turret: **300 LP**
- Air Strike: **800 LP**

**Vehicle Operations (Optional):**
- Light Vehicle Spawn: **400 LP**
- APC Spawn: **1,200 LP**
- Tank Spawn: **2,500 LP**
- Vehicle Repair: **200-500 LP** (based on damage)

**Infrastructure Investment:**
- Connection Point Capture: **1,000 LP per point** (one-time cost)
- Base Defense Reinforcement: **500 LP** (temporary sandbags/barriers)
- Auto-Turret Deployment: **800 LP** (90-second duration)

---

## Supply Line System

### Supply Line Hubs

**High-Value Strategic Points:**
- Count: **2-3 per map**
- Location: Distributed across neutral territory
- Capture Time: **4 minutes** uncontested
- Capture Radius: **50 meters**
- Minimum Capture Force: **4 players**
- Generation Rate: **+100 LP/second** (even without completed line)

**Strategic Value:**
- Serves as anchor for supply line construction
- Multiple hubs allow multiple supply line strategies
- Losing a hub breaks all lines connected to it

### Connection Points

**Supply Line Segments:**
- Count: **3-5 connection points per hub** (varies by hub location)
- Sequential Capture: Must capture in order (A→B→C→D→E)
- Capture Time: **90 seconds** per connection point
- Capture Radius: **20 meters**
- Minimum Capture Force: **2 players**
- LP Investment: **1,000 LP per connection point** (deducted upon capture)

**Capture Sequence:**
```
Main Base → Connection Point A → Connection Point B → Connection Point C → Supply Line Hub
```

**Connection Point States:**
- **Neutral:** Uncaptured, available to either team
- **Building:** Currently being captured by a team
- **Active:** Captured, part of functioning supply line
- **Contested:** Enemy present, capture halted
- **Broken:** Enemy captured, line disrupted

### Supply Line Benefits

**Active Line Bonuses (Per Completed Line):**

**LP Generation:**
- **+500 LP/second** continuous income
- Compounds with other lines (2 lines = +1,000 LP/second)
- Most significant LP source in game

**Respawn Cost Reduction:**
- Main Base respawns: **-25 LP** discount
- Forward spawn points on line: **-50 LP** discount
- Incentivizes defending active lines

**Special Abilities (Team-Wide):**
- Faster capture rates: **+25%** for all objectives
- Vehicle armor buff: **+20% damage resistance**
- Equipment cost reduction: **-20%** for all items
- Duration: Active while line remains connected

**Unlock Conditions:**
- 1 Line: Basic bonuses
- 2 Lines: Enhanced bonuses (+50% stronger)
- 3 Lines (All): "Supply Line Domination" victory trigger

---

## Sabotage Mechanics

### Line Disruption

**Capturing Enemy Connection Points:**
- Any connection point on enemy line can be targeted
- Standard capture time: **90 seconds**
- Breaking ANY point instantly disables entire line
- Enemy loses all bonuses from that line immediately
- Enemy must recapture from break point forward sequentially

**Strategic Disruption Targets:**

**Early Connection Points (Near Enemy Base):**
- Harder to reach (deep enemy territory)
- Breaks line closer to source
- Longer recapture sequence for enemy

**Mid Connection Points:**
- Easier to access (neutral territory)
- Quicker raids, less risk
- Enemy can recapture faster

**Hub Points:**
- Capturing enemy hub breaks ALL lines connected to it
- Extremely high value target
- Heavily defended by enemy

### Targeted Destruction (Optional)

**Demolition Actions:**
- Breacher Role: Plant explosive on connection point
- Plant Time: **15 seconds** (vulnerable, interruptible)
- Explosion Timer: **30 seconds** (enemy can defuse)
- Effect: Connection point destroyed, requires rebuild
- Rebuild Cost: **2,000 LP** + **3-minute construction time**
- Cooldown: Cannot destroy same point for **5 minutes**

**Strategic Considerations:**
- Destruction more permanent than capture
- Higher risk (must remain for plant time)
- Useful for critical late-game disruptions
- Enemy can adapt by building alternate routes

---

## Match Structure

### Round Format

**Best of 3 or Best of 5:**
- Each round: **15-20 minutes**
- Teams switch sides after each round
- First to win majority of rounds wins match
- No ties (time limit forces LP comparison)

### Round Phases

**Opening Phase (0-5 minutes):**
- Initial resource node captures
- Hub capture attempts
- First LP investments in connection points
- Establishing baseline income

**Mid Phase (5-12 minutes):**
- Active supply line construction
- Counter-raids on enemy lines
- Resource management becomes critical
- First completed lines emerge

**Late Phase (12-20 minutes):**
- Multiple completed lines (if teams successful)
- Aggressive line disruption tactics
- LP accumulation accelerating
- Victory conditions approaching

---

## Victory Conditions

### Primary: Logistics Goal

**LP Accumulation:**
- Victory Threshold: **1,000,000 LP** total accumulated
- Team that reaches threshold first wins round
- Most common victory condition
- Encourages aggressive supply line construction

### Secondary: Supply Line Domination

**Complete Control:**
- Requirements:
  - All supply line hubs captured
  - All lines fully connected to main base
  - Hold all lines simultaneously for **60 seconds**
- Instant victory if achieved
- Rare but decisive victory condition

### Tertiary: End of Round LP Count

**Time Limit Victory:**
- If 20-minute timer expires without other victory
- Team with higher accumulated LP total wins
- Tiebreaker: Most active supply lines
- Second Tiebreaker: Most resource nodes controlled

---

## Team Roles & Strategy

### Offensive Roles

**Supply Line Builders:**
- Squad dedicated to establishing new lines
- Capture connection points sequentially
- Coordinate LP investments with Commander
- Defend newly established connection points
- Recommended: **2 squads** (12-16 players)

**Raiders:**
- Target enemy supply lines for disruption
- Identify weak points in enemy network
- Execute quick capture raids
- Fade before enemy reinforcements arrive
- Recommended: **2-3 squads** (12-18 players)

### Defensive Roles

**Node Defenders:**
- Secure captured resource nodes
- Prevent enemy captures
- Maintain baseline LP generation
- Recommended: **1 squad per 2-3 nodes**

**Line Security:**
- Patrol active supply lines
- Respond to enemy raid attempts
- Defend critical connection points
- Recommended: **1 squad per active line**

### Commander Role (Optional)

**Commander Responsibilities:**
- Prioritize which hubs to capture
- Allocate LP for connection point captures
- Deploy Commander abilities (UAV, artillery)
- Coordinate defensive and offensive squads
- Track enemy supply line status

**Commander LP Abilities:**
- UAV Reconnaissance: **500 LP** (reveals enemy positions 3 minutes)
- Artillery Strike: **800 LP** (deny area, delay captures)
- Temporary Defense Buff: **600 LP** (reinforce connection point)
- Emergency LP Transfer: **Variable** (allocate reserves to squads)

---

## Map Design Requirements

### Spatial Layout

**Map Size:**
- **4km x 4km** optimal for 64 players
- Main bases on opposite ends (**3km+ separation**)
- Resource nodes distributed evenly
- Supply line hubs in neutral territory

**Supply Line Pathways:**
- Multiple viable routes between hubs and bases
- Connection points create decision trees
- Some routes shorter but more exposed
- Other routes longer but more defensible

**Environmental Features:**
- Elevation changes affect sightlines
- Cover along connection point routes
- Natural choke points for defense
- Open areas force tactical crossings

### Example Map: "Black Gold"

**Setting:** Oil-rich desert region
**Supply Line Hubs:** 3 total
- Central Refinery (5 connection points)
- Northern Pipeline Station (4 connection points)
- Southern Drilling Complex (4 connection points)

**Resource Nodes:** 10 total
- 4x Oil Wells (+150 LP/sec each)
- 3x Mining Operations (+120 LP/sec each)
- 3x Intel Outposts (+180 LP/sec each)

**Key Features:**
- Central refinery highly contested (shortest connections)
- Northern pipeline exposed, fast capture but hard to defend
- Southern drilling complex defensible but longer route

---

## Tactical Considerations

### Supply Line Strategy

**Aggressive Expansion:**
- Capture all hubs quickly
- Invest LP in multiple lines simultaneously
- Risk: Overextension, cannot defend all lines
- Reward: Rapid LP accumulation if successful

**Defensive Consolidation:**
- Capture 1-2 hubs, fully complete lines
- Heavily defend completed lines
- Risk: Slower LP accumulation
- Reward: Secure income, hard for enemy to disrupt

**Raiding Focus:**
- Minimal line construction (1 line maximum)
- Dedicate majority of forces to enemy line disruption
- Risk: Low own LP generation
- Reward: Deny enemy LP, slow their progress

### Common Mistakes

**Over-Investment Early:**
- Spending too much LP on connection points
- Depletes reserve for respawns/equipment
- Vulnerable to enemy disruption after heavy investment

**Ignoring Defense:**
- Focusing purely on building lines
- Enemy raiders easily break undefended lines
- Wasted LP investment

**Poor Connection Point Sequencing:**
- Capturing out of order (impossible)
- Not coordinating capture timing
- Exposing partially built lines to enemy

**Resource Node Neglect:**
- Focusing only on supply lines
- Losing baseline LP generation
- Unable to sustain operations

---

## Comeback Mechanics

### LP Deficit Recovery

**Trailing Team Bonuses:**

**When Behind by 200,000+ LP:**
- Respawn costs reduced by **25%**
- Resource node generation increased by **+50 LP/second**
- Connection point capture costs reduced to **750 LP**
- Duration: Until LP gap closes below 150,000

**When Behind by 400,000+ LP:**
- Respawn costs reduced by **50%**
- Resource node generation increased by **+100 LP/second**
- Connection point capture costs reduced to **500 LP**
- Free UAV reconnaissance every **3 minutes**
- Duration: Until LP gap closes below 200,000

**Purpose:**
- Prevent complete snowballing
- Reward clutch plays by trailing team
- Maintain competitive tension throughout round
- Does NOT guarantee victory, only provides opportunity

---

## Advanced Tactics

### Feint Operations

**Decoy Line Construction:**
- Begin building line toward less valuable hub
- Draw enemy defenders
- Main force builds priority line elsewhere
- Requires excellent coordination and timing

### Economic Warfare

**Resource Node Pressure:**
- Constant raids on enemy resource nodes
- Forces enemy to allocate defenders
- Reduces their baseline LP generation
- Softens enemy for line disruption

### Surgical Strikes

**Hub Flipping:**
- Coordinated assault on enemy hub
- Breaks all lines connected to that hub
- Massive LP swing in single action
- High risk, extremely high reward

### Line Redundancy

**Parallel Lines:**
- Build multiple lines to same hub
- If one line broken, backup line maintains income
- Expensive (double LP investment)
- Extremely secure against disruption

---

## Developer Notes

### Design Pillars

1. **Logistics Focus:** Resource flow more important than pure combat
2. **Strategic Depth:** Multiple valid approaches to victory
3. **Dynamic Battlefield:** Supply lines constantly changing hands
4. **Economic Warfare:** Disruption as valuable as construction
5. **Team Coordination:** Requires synchronized offensive and defensive operations

### Balance Testing Focus

**Metrics:**
- LP generation rates by source type
- Average time to complete supply line
- Supply line survival duration
- Victory condition distribution (Logistics Goal vs. Domination vs. Time)
- Comeback mechanic activation frequency

**Adjustment Vectors:**
- LP generation rates (passive, nodes, lines)
- Connection point capture costs
- Supply line bonus magnitudes
- Disruption capture times
- Comeback mechanic thresholds

---

## Future Expansion

### Advanced Features

**Supply Convoy System:**
- Physical vehicles transport LP along lines
- Vulnerable to ambush
- Higher risk, higher reward
- Adds PvE escort element

**Line Upgrades:**
- Spend LP to upgrade connection points
- Armored connections harder to disrupt
- Increased LP generation per line
- More resistant to destruction

**Black Market Trading:**
- Neutral faction offers equipment for LP
- Special items not normally available
- Risk: Depletes LP pool
- Reward: Tactical advantages

**Dynamic Weather:**
- Sandstorms/rain affect visibility along lines
- Easier for raiders to approach undetected
- Defenders must adapt patrol patterns

---

## Conclusion

Supply Line Sabotage revolutionizes territorial warfare by making logistics the primary objective rather than a supporting mechanic. Teams must think like military strategists, balancing infrastructure investment, territorial expansion, defensive allocation, and offensive disruption. Pure combat skill is insufficient; teams require economic awareness, strategic planning, and adaptive tactics.

The constant tension between building your own supply network and disrupting the enemy's creates dynamic gameplay where momentum can shift rapidly. Every captured connection point, every successful raid, every defended line compounds over time, rewarding long-term strategic thinking while maintaining moment-to-moment intensity.

**Supply Line Sabotage is economic warfare:** build, defend, disrupt, dominate.

---

**Document Version:** 1.0  
**Last Updated:** November 2025  
**Status:** Post-MVP Expansion - Design Complete  
**Target Implementation:** Month 20+