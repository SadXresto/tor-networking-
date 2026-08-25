# Tor-Resources-Hub

This repository serves as a centralized directory for verified `.onion` addresses and essential guides related to the Tor Hidden Service network. 

## 🌐 What You Will Find
- **Verified Search Engines**: Direct links to active instances of Ahmia, DuckDuckGo (Darknet), Torch, and Chive.
- **Market Directories**: Catalogs of historically significant marketplaces with their latest known entry points.
- **Safety Guidelines**: Best practices for verifying addresses, using PGP encryption, and securing transactions via escrow.

## ⚠️ Note on Volatility
Since servers in the Tor network migrate frequently (e.g., from `v2.onion` to `v3.onion`) to evade censorship, this repo acts as a checkpoint list to cross-reference against official surface-web counterparts before visiting any hidden service. Always verify URLs before transacting sensitive data.

---
*Sources are dynamically managed; check the interface or documentation for updates.*

***NEW BLOCK READ IT PLS BEFORE USE 



Here is the "Quick Start" command block you can copy and paste directly into your `README.md`. It assumes your Python script (`update_ahmia.py`) and Bash runner (`run_update.sh`) are already in place.

### Quick Start Guide (Copy & Paste)

```markdown
## 🚀 Quick Start: Get Fresh Links in Seconds

This repository updates automatically via a simple script that fetches the latest `.onion` addresses from official surface-web sources. No manual hunting required!

### 1️⃣ Install Dependencies
Make sure you have Python 3 installed, then run this once to install required libraries:
```bash
pip install -r requirements.txt
# If no requirements file is found yet, use: pip install requests beautifulsoup4 python-dateutil
```

### 2️⃣ Run the Updater Command
Navigate into your project folder and execute the automated updater:
```bash
cd Tor-Resources-Hub      # Adjust if cloned elsewhere
./scripts/run_update.sh   # Or just: python scripts/update_ahmia.py on Mac/Linux/WSL
```

### 3️⃣ Verify Results
Check the generated JSON file containing verified links. For Ahmia specifically (current example):
- **File Location:** `data/ahmia_latest.json`  
- **Sample Output Preview:**
    ```json
    {
        "service": "Ahmia", 
        "surface_domain": "https://ahmia.fi", 
        "url": "https://xjgk4q5z6r7y.onion/", 
        "status": "active"
    }
    ```

> 💡 **Note**: The script will create a new directory named `data/` if it doesn't exist on your first run.

### 4️⃣ Integrate into Your Workflow (Optional)
If you want to automate updates daily or weekly, add the following command to your system crontab:
```bash
# Run every Sunday at 12:00 PM (UTC+3 example for Dagestani timezone context):
0 12 * * 0 cd ~/path/to/Tor-Resources-Hub && ./scripts/run_update.sh >> logs/update.log 2>&1
```

---
*Ready? Just run `./scripts/run_update.sh` and browse!*
```

You can copy this block directly above. The next time you update, just ensure the script covers whatever new source you decide to add! 🚀
