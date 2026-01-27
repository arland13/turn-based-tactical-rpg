# ⚔️ Turn-Based Tactical RPG (Fire Emblem–Inspired)

This project is a **console-based, turn-based tactical RPG prototype** inspired by classic games like *Fire Emblem*.  
It focuses on **game logic, combat systems, and turn/phase management**, rather than graphics or UI.

---

## 📌 Purpose of This Project

This repository exists primarily as a **learning project**.

I am using this project to:
- Learn **game logic programming**
- Understand **turn-based combat systems**
- Practice **state management (phases, turns, actions)**
- Study how **grid-based movement and range checking** works
- Explore **object-oriented design** in games

---

## 🤖 AI-Assisted Development (Important Note)

> **Most of the code in this repository was generated or heavily assisted by AI (ChatGPT).**

This project is **not** intended to claim originality of the implementation.  
Instead, AI is used as a **learning companion and teaching tool**.

My workflow:
1. Ask AI to help design or implement systems
2. Read and study the generated code
3. Modify, break, and extend the logic myself
4. Learn *why* things work the way they do

The goal is **understanding**, not authorship.

---

## 🧠 What I Am Learning From This Project

- Turn-based phase systems (Player / Enemy / Ally)
- Grid-based movement using Manhattan distance
- Weapon range logic (min / max range)
- Faction-based targeting (Player vs Enemy)
- Combat resolution:
  - Hit rate
  - Avoid
  - Damage
  - Critical hits
  - Follow-up attacks
- Inventory and consumable items
- Permanent stat modifiers
- Skill-triggered combat effects (e.g. Vantage)

---

## ▶️ How to Run

```bash
python main.py

The game runs entirely in the terminal and is meant for logic testing, not final gameplay.

## 🚧Current Limitations
- No GUI (terminal only)
- No cursor-based movement yet
- Enemy AI is very simple
- No pathfinding (movement ignores obstacles)
- No save/load system
These limitations are intentional to keep the focus on fundamentals.

🔮 Planned Improvements

## Cursor-based unit selection
- Attack preview (hit / damage / crit)
- Weapon triangle
- Smarter enemy AI
- Status effects
- Terrain bonuses

## 📖 Disclaimer
This project is:
- Educational
- Experimental
- AI-assisted
If you are reviewing this repository, please evaluate it as a learning sandbox, not a finished or original game engine.
