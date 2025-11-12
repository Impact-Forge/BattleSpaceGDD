#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# Source and destination
src_dir = Path('/mnt/project')
dest_dir = Path('/home/claude/battlespace-gdd-site/docs')

# File mapping: source_file -> destination_path
file_mapping = {
    # Core documents
    'Game_Overview_b31cb07d.md': 'game-overview.md',
    'battlespace-lean-gdd.md': 'battlespace-lean-gdd.md',
    'battlespace-marketing-strategy.md': 'battlespace-marketing-strategy.md',
    
    # Gameplay systems
    '___Gameplay___mechanics_c11788b0.md': 'gameplay/gameplay-mechanics.md',
    'Multi-Domain_Operation__MDO-Warfare__6458246f.md': 'gameplay/multi-domain-operations.md',
    'Economy_System___Stats_System_9e64c3cd.md': 'gameplay/economy-system.md',
    'Medical_System_5335047f.md': 'gameplay/medical-system.md',
    'Construction_Function____ebb83a24.md': 'gameplay/construction-function.md',
    'Gameplay_34297752.md': 'gameplay/gameplay.md',
    
    # Combat
    'Land_Warfare_c1c4caad.md': 'combat/land-warfare.md',
    'Aerial_Warfare_b103c788.md': 'combat/aerial-warfare.md',
    'Maritime_Warfare_cf65234f.md': 'combat/maritime-warfare.md',
    'Extraction__EX__287658be.md': 'combat/extraction.md',
    'Fortification__FO__28e0e8bb.md': 'combat/fortification.md',
    
    # Roles
    'Squad_Leader_4583620d.md': 'roles/squad-leader.md',
    'Team_Leader_ba40251c.md': 'roles/team-leader.md',
    'Rifleman_07399c06.md': 'roles/rifleman.md',
    'Auto_Rifleman_68448619.md': 'roles/auto-rifleman.md',
    'Grenadier_4c13923b.md': 'roles/grenadier.md',
    'Special_Weapons_Man_0b791342.md': 'roles/special-weapons-man.md',
    'Designated_Defensive_Marksman___Sniper_4faefb90.md': 'roles/designated-marksman.md',
    'Combat_Engineer_a1699fe6.md': 'roles/combat-engineer.md',
    'Medic_bbc56fa8.md': 'roles/medic.md',
    'Radio_Man_75c1d577.md': 'roles/radio-man.md',
    'Commander_7c5715a7.md': 'roles/commander.md',
    'Pilot_b58048d4.md': 'roles/pilot.md',
    'CrewMan_e7d4bf43.md': 'roles/crew-man.md',
    'Advisor___PMC_784bedd8.md': 'roles/advisor-pmc.md',
    
    # Vehicles
    'Aircraft_af7f2d70.md': 'vehicles/aircraft.md',
    'Jet_Aircraft_280c5695.md': 'vehicles/jet-aircraft.md',
    'Rotary_Aircraft_43282c4b.md': 'vehicles/rotary-aircraft.md',
    'Armor_and_Vehicles_7234f1ba.md': 'vehicles/armor-and-vehicles.md',
    'Vehicles_4789ea78.md': 'vehicles/vehicles.md',
    'Specialty_Functioning_Vehicles_4a986556.md': 'vehicles/specialty-vehicles.md',
    
    # Equipment
    'Weapons_Systems_7cb64074.md': 'equipment/weapons-systems.md',
    'Props_and_Equipment_32367356.md': 'equipment/props-equipment.md',
    
    # Ukraine levels
    'UKRAINE__UA_-_BattleSpace_00a279e9.md': 'levels/ukraine/ukraine-battlespace.md',
    'Ukraine_Level_1__Odessa_Oblast_03f8c44c.md': 'levels/ukraine/odessa-oblast.md',
    'Ukraine_Level_2__Crimean_Oblast_422fba27.md': 'levels/ukraine/crimean-oblast.md',
    'Ukraine_Level_3__Kyiv_Oblast_3ecbecde.md': 'levels/ukraine/kyiv-oblast.md',
    'Ukraine_Level_4__Donetak_Oblast_343e7b6c.md': 'levels/ukraine/donetsk-oblast.md',
    'Ukraine_Level_5__Kharkiv_Oblast_0e9e5c80.md': 'levels/ukraine/kharkiv-oblast.md',
    
    # Other theaters
    'Barents_Sea_f6deffc7.md': 'levels/barents-sea/barents-sea.md',
    'Barents_Sea__BS__Level_1_Svalbard__Norway_-_d04ec4e2.md': 'levels/barents-sea/svalbard.md',
    'South_China_Sea_470ac763.md': 'levels/south-china-sea/south-china-sea.md',
    'South_China_Sea__SCS__Level_1_Taiwan_-_faeef0f4.md': 'levels/south-china-sea/taiwan.md',
    'Falkland_Islands__Islas_Malvinas___Level_1_Argentina_165d013f.md': 'levels/falklands/falklands.md',
    'Black_Sea_98f30cbc.md': 'levels/black-sea.md',
    'North_Sea_89d1c243.md': 'levels/north-sea.md',
    'Indian_Ocean_bee8bb85.md': 'levels/indian-ocean.md',
    'Alaska_9b74f51a.md': 'levels/alaska.md',
    'Poland_40b7b61b.md': 'levels/poland.md',
    'India_-_Kashmir_0a7b0f6e.md': 'levels/india-kashmir.md',
    'North_Korea_cb7a6282.md': 'levels/north-korea.md',
    
    # Art
    'Art_a4e8d35f.md': 'art/art.md',
    'Concept_art_1f955334.md': 'art/concept-art.md',
    'Models_and_Textures_6e6286b5.md': 'art/models-textures.md',
    
    # Audio
    'Sound_24773598.md': 'audio/sound.md',
    'Sound_effects_ccde860d.md': 'audio/sound-effects.md',
    'Music_5d07e887.md': 'audio/music.md',
    'Voice_e0a65808.md': 'audio/voice.md',
    
    # UI
    'HUD_s_and_UI_s_18b61767.md': 'ui/huds-and-uis.md',
    
    # Technical
    'Unreal_Engine_5_1_1f33137c.md': 'technical/unreal-engine.md',
    'Licenses___Hardware_ba62a221.md': 'technical/licenses-hardware.md',
    
    # Narrative
    'Story_478d0955.md': 'narrative/story.md',
    'The_Team_House__Characters__9b1d21b2.md': 'narrative/characters.md',
    'Factions_fe950f63.md': 'narrative/factions.md',
    
    # Characters
    'ArchRevenant_deffa1b7.md': 'characters/arch-revenant.md',
    'Butcher-Ak_4486256c.md': 'characters/butcher-ak.md',
    'Fourleaf_625259db.md': 'characters/fourleaf.md',
    'Akuma_5b838e5e.md': 'characters/akuma.md',
    'Gemesil_643fe894.md': 'characters/gemesil.md',
    'SMILOX_363a2b6d.md': 'characters/smilox.md',
    'Wupy_8289afb5.md': 'characters/wupy.md',
    'vill_chip_9bae9bf6.md': 'characters/vill-chip.md',
    'EmercomCamper_cb665390.md': 'characters/emercom-camper.md',
    
    # Dev
    'Elevator_Pitches__WIP__0f12ee2b.md': 'dev/elevator-pitches.md',
    'Dev_-_Staffing_e0af12b5.md': 'dev/dev-staffing.md',
    'Ranks_Structure_27f29804.md': 'dev/ranks-structure.md',
    'Easter_Eggs_fa025214.md': 'dev/easter-eggs.md',
    'Inventory_Asset_Master_List__WIP__31e04ff4.md': 'dev/inventory-master-list.md',
    
    # Warfare
    '__Warfare_Level__Alpha__c1354382.md': 'warfare/warfare-level-alpha.md',
    '__Warfare_Level__Whiskey__422517f9.md': 'warfare/warfare-level-whiskey.md',
}

# Copy files
print("Organizing GDD files...")
for src_file, dest_file in file_mapping.items():
    src_path = src_dir / src_file
    dest_path = dest_dir / dest_file
    
    if src_path.exists():
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dest_path)
        print(f"✓ {src_file} -> {dest_file}")
    else:
        print(f"✗ Missing: {src_file}")

print("\nOrganization complete!")
