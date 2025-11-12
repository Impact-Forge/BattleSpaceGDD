# BATTLESPACE - LEAN GDD & 12-MONTH ROADMAP
**Version 2.0 - Hyper-Critical Edition**

## BRUTAL REALITY CHECK
Your current scope is **2-3 years of work**. To ship in 12 months, you must cut 70% of features and focus on what makes money and retains players.

---

## THE ONLY VISION THAT MATTERS
**Core Game:** 32v32 tactical FPS with ONE killer feature - grid-based persistent warfare  
**Platform:** PC only (Steam)  
**Engine:** UE 5.3 with existing plugin stack  
**Target:** Stable MVP in 12 months, not feature-complete  

### CUT IMMEDIATELY
âŒ 100+ player battles (technically impossible in 12 months)  
âŒ 14 roles (reduce to 6 core roles)  
âŒ Complex medical system (basic revive only)  
âŒ Vehicle combat (infantry-only for MVP)  
âŒ Multiple maps (ONE polished map)  
âŒ Console support  
âŒ Advanced construction (basic fortifications only)  

---

## LEAN CORE FEATURES (MVP ONLY)

### 1. COMBAT FUNDAMENTALS
- **SKG Framework** integration (already in codebase)
- **Terminal Ballistics** for differentiation
- 6 weapons total (2 rifles, 1 LMG, 1 sniper, 1 SMG, 1 pistol)
- Basic attachment system (scope, grip, barrel)

### 2. SIMPLIFIED ROLE SYSTEM
**Only 6 Roles:**
1. **Squad Leader** - Spawn beacons, tactical map
2. **Rifleman** - Standard infantry 
3. **Support** - LMG, ammo supply
4. **Marksman** - Long-range engagement
5. **Engineer** - Basic fortifications
6. **Medic** - Revive/heal only

### 3. GRID WARFARE (Your Differentiator)
- ONE 4kmÂ² map divided into 9 grids
- Capture-and-hold mechanics
- Persistent territory between matches
- Simple resource system (tickets only)

### 4. MINIMUM VIABLE NETWORKING
- 32v32 maximum (64 players)
- AWS GameLift integration via UMS
- Basic anti-cheat (client-side only for MVP)
- Voice chat (proximity only)

---

## AGGRESSIVE 12-MONTH MILESTONES

### MONTH 1-2: FOUNDATION SPRINT
**Goal:** Playable 8v8 prototype
- SKG Framework integrated (already done)
- Integrate Terminal Ballistics
- Basic movement, shooting, damage
- One test map (greybox)
- **Deliverable:** Internal 8v8 deathmatch

### MONTH 3-4: CORE LOOP
**Goal:** Grid capture mechanics working
- Grid system implementation
- Basic capture points
- Score/ticket system
- UI for grid status
- **Deliverable:** 16v16 grid capture playtest

### MONTH 5-6: ROLE IMPLEMENTATION
**Goal:** All 6 roles functional
- Role selection UI
- Unique loadouts per role
- Squad system (6-player squads)
- Spawn on squad leader
- **Deliverable:** Closed alpha with 50 testers

### MONTH 7-8: NETWORKING SCALE
**Goal:** 32v32 stable matches
- AWS infrastructure setup
- Server optimization
- Lag compensation
- Basic matchmaking
- **Deliverable:** Open beta weekend (32v32)

### MONTH 9-10: MAP & POLISH
**Goal:** One complete map
- Full art pass on single map
- Environmental audio
- Lighting and atmosphere
- Performance optimization
- **Deliverable:** Early Access launch announcement

### MONTH 11: LAUNCH PREP
**Goal:** Store-ready build
- Steam page setup
- Anti-cheat integration
- Tutorial/onboarding
- Bug fixing sprint
- **Deliverable:** Release candidate

### MONTH 12: LAUNCH
**Goal:** Early Access release
- $19.99 price point
- Marketing push
- Streamer keys
- Day-one patch ready
- **Deliverable:** Live on Steam

---

## CRITICAL SUCCESS METRICS

### Technical (Non-Negotiable)
- **Performance:** 60+ FPS with 64 players
- **Latency:** <80ms average
- **Crash rate:** <2% per session
- **Load time:** <90 seconds

### Business (Reality Check)
- **Week 1 Sales:** 5,000 units minimum
- **Month 1 Retention:** 40% playing weekly
- **Peak CCU:** 500+ players
- **Review Score:** 70%+ positive

---

## POST-LAUNCH ROADMAP (Months 13-18)

Only after successful launch:
1. **Month 13-14:** Second map + 2 new weapons
2. **Month 15-16:** Vehicle combat (light vehicles only)
3. **Month 17-18:** 50v50 scaling + advanced roles

---

## RESOURCE REQUIREMENTS

### Minimum Team (for 12-month delivery)
- **1 Technical Director** (you)
- **2 Programmers** (networking, gameplay)
- **1 Level Designer** 
- **2 Environment Artists**
- **1 Character Artist**
- **1 UI/UX Designer**
- **1 Sound Designer**
- **1 QA Lead**
- **Total:** 10 people minimum

### Budget Reality
- **Development:** $800K-1M (10 people Ã— 12 months)
- **Infrastructure:** $50K (servers, tools, testing)
- **Marketing:** $100K minimum
- **Total:** ~$1M to launch

---

## RISK MITIGATION

### Highest Risk: Network Performance
**Mitigation:** Start with 16v16, scale gradually. Have fallback to 24v24 if needed.

### High Risk: Player Retention
**Mitigation:** Weekly updates, rapid response to feedback, competitive season 1 month after launch.

### Medium Risk: Competition
**Mitigation:** Focus on grid persistence (unique feature), price below competitors.

---

## THE HARD TRUTH

**What you're building:** A solid 32v32 tactical shooter with one unique feature  
**What you're NOT building:** The next Battlefield or Squad killer  
**Why this works:** Focused scope, proven tech stack, achievable with small team  
**Why this fails:** Trying to do everything in your original GDD  

## DECISION POINTS

**By Month 3:** If 16v16 isn't stable, reduce to 12v12  
**By Month 6:** If retention <30% in tests, pivot grid system  
**By Month 9:** If performance <60fps, cut visual fidelity  
**By Month 11:** If critical bugs exist, delay 1-2 months maximum  

---

## IMMEDIATE NEXT STEPS

1. **Week 1:** Lock feature set, no additions for 12 months
2. **Week 2:** Hire 2 network programmers immediately  
3. **Week 3:** Begin greybox map production
4. **Week 4:** Set up daily playtests with team

**Remember:** Every feature you add delays launch by 2-4 weeks. Every "nice to have" kills your timeline. Ship lean, iterate after launch based on player data, not assumptions.